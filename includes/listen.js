module.exports = function({ api, models }) {

  const Users = require("./controllers/users")({ models, api }),
        Threads = require("./controllers/threads")({ models, api }),
        Currencies = require("./controllers/currencies")({ models });
  const logger = require("../utils/log.js");
  const fs = require("fs");
  const moment = require('moment-timezone');
  const axios = require("axios");
  var day = moment.tz("Asia/Ho_Chi_Minh").day();


  const checkttDataPath = __dirname + '/../modules/commands/tt/';
  setInterval(async() => {
    const day_now = moment.tz("Asia/Ho_Chi_Minh").day();
    if (day != day_now) {
      day = day_now;
      const checkttData = fs.readdirSync(checkttDataPath);
      console.log('-> CHECKTT: Ngày Mới');
      checkttData.forEach(async(checkttFile) => {
        const checktt = JSON.parse(fs.readFileSync(checkttDataPath + checkttFile));
        let storage = [], count = 1;
        for (const item of checktt.day) {
            const userName = await Users.getNameUser(item.id) || 'Facebook User';
            const itemToPush = item;
            itemToPush.name = userName;
            storage.push(itemToPush);
        };
        storage.sort((a, b) => {
            if (a.count > b.count) {
                return -1;
            }
            else if (a.count < b.count) {
                return 1;
            } else {
                return a.name.localeCompare(b.name);
            }
        });
        let checkttBody = '[ Top 15 Tương Tác Ngày ]\n────────────────\n';
        checkttBody += storage.slice(0, 15).map(item => {
          return `👑 Top: ${count++}\n👤 Tên: ${item.name}\n💬 Tin Nhắn: ${item.count}\n────────────────`;
      }).join('\n');
//api.sendMessage(`${checkttBody}\n📝 Tương tác để giành top nhé`, checkttFile.replace('.json', ''), (err) => err ? console.log(err) : '');

        checktt.day.forEach(e => {
            e.count = 0;
        });
        checktt.time = day_now;

        fs.writeFileSync(checkttDataPath + checkttFile, JSON.stringify(checktt, null, 4));
      });
      if (day_now == 1) {
        console.log('-> CHECKTT: Tuần Mới');
        checkttData.forEach(async(checkttFile) => {
          const checktt = JSON.parse(fs.readFileSync(checkttDataPath + checkttFile));
          let storage = [], count = 1;
          for (const item of checktt.week) {
              const userName = await Users.getNameUser(item.id) || 'Facebook User';
              const itemToPush = item;
              itemToPush.name = userName;
              storage.push(itemToPush);
          };
          storage.sort((a, b) => {
              if (a.count > b.count) {
                  return -1;
              }
              else if (a.count < b.count) {
                  return 1;
              } else {
                  return a.name.localeCompare(b.name);
              }
          });
          let checkttBody = '[ Top 15 Tương Tác Tuần ]\n────────────────\n';
          checkttBody += storage.slice(0, 15).map(item => {
            return `🏆 Top: ${count++}\n👤 Tên: ${item.name}\n💬 Tin Nhắn: ${item.count}\n────────────────`;
        }).join('\n');
         api.sendMessage(`${checkttBody}\n📝 Tương tác để giành top nhé`, checkttFile.replace('.json', ''), (err) => err ? console.log(err) : '');
          checktt.week.forEach(e => {
              e.count = 0;
          });

          fs.writeFileSync(checkttDataPath + checkttFile, JSON.stringify(checktt, null, 4));
        })
      }
      global.client.sending_top = false;
    }
  }, 1000 * 10);


  //////////////////////////////////////////////////////////////////////
  //========= Push all variable from database to environment =========//
  //////////////////////////////////////////////////////////////////////

(async function () {

    try {
        logger(global.getText('listen', 'startLoadEnvironment'), '[ DATABASE ]');
        let threads = await Threads.getAll(),
            users = await Users.getAll(['userID', 'name', 'data']),
            currencies = await Currencies.getAll(['userID']);
        for (const data of threads) {
            const idThread = String(data.threadID);
            global.data.allThreadID.push(idThread), 
            global.data.threadData.set(idThread, data['data'] || {}), 
            global.data.threadInfo.set(idThread, data.threadInfo || {});
            if (data['data'] && data['data']['banned'] == !![]) 
              global.data.threadBanned.set(idThread, 
              {
                'reason': data['data']['reason'] || '',
                'dateAdded': data['data']['dateAdded'] || ''
            });
            if (data['data'] && data['data']['commandBanned'] && data['data']['commandBanned']['length'] != 0) 
            global['data']['commandBanned']['set'](idThread, data['data']['commandBanned']);
            if (data['data'] && data['data']['NSFW']) global['data']['threadAllowNSFW']['push'](idThread);
        }
        logger.loader(global.getText('listen', 'loadedEnvironmentThread'));
        for (const dataU of users) {
            const idUsers = String(dataU['userID']);
            global.data['allUserID']['push'](idUsers);
            if (dataU.name && dataU.name['length'] != 0) global.data.userName['set'](idUsers, dataU.name);
            if (dataU.data && dataU.data.banned == 1) global.data['userBanned']['set'](idUsers, {
                'reason': dataU['data']['reason'] || '',
                'dateAdded': dataU['data']['dateAdded'] || ''
            });
            if (dataU['data'] && dataU.data['commandBanned'] && dataU['data']['commandBanned']['length'] != 0) 
            global['data']['commandBanned']['set'](idUsers, dataU['data']['commandBanned']);
        }
        for (const dataC of currencies) global.data.allCurrenciesID.push(String(dataC['userID']));
        logger.loader(global.getText('listen', 'loadedEnvironmentUser')), logger(global.getText('listen','successLoadEnvironment'),'[ DATABASE ]');
    } catch (error) {
        return logger.loader(global.getText('listen', 'failLoadEnvironment', error), 'error');
    }
}());
  logger(`${api.getCurrentUserID()} - [ ${global.config.PREFIX} ] • ${(!global.config.BOTNAME) ? "Niiozic" : global.config.BOTNAME}`, "[ BOT INFO ]");

  ///////////////////////////////////////////////
  //========= Require all handle need =========//
  //////////////////////////////////////////////

  const handleCommand = require("./handle/handleCommand")({ api, models, Users, Threads, Currencies });
  const handleCommandEvent = require("./handle/handleCommandEvent")({ api, models, Users, Threads, Currencies });
  const handleReply = require("./handle/handleReply")({ api, models, Users, Threads, Currencies });
  const handleReaction = require("./handle/handleReaction")({ api, models, Users, Threads, Currencies });
  const handleEvent = require("./handle/handleEvent")({ api, models, Users, Threads, Currencies });
  const handleCreateDatabase = require("./handle/handleCreateDatabase")({  api, Threads, Users, Currencies, models });
  const handleUnsend = require("./handle/handleUnsend")({  api, Threads, Users, Currencies, models });
  //DEFINE DATLICH PATH
  const datlichPath = __dirname + '/../modules/commands/data/datlich.json';
  //FUNCTION HOẠT ĐỘNG NHƯ CÁI TÊN CỦA NÓ, CRE: DUNGUWU
  const monthToMSObj = {
    1: 31 * 24 * 60 * 60 * 1000,
    2: 28 * 24 * 60 * 60 * 1000,
    3: 31 * 24 * 60 * 60 * 1000,
    4: 30 * 24 * 60 * 60 * 1000,
    5: 31 * 24 * 60 * 60 * 1000,
    6: 30 * 24 * 60 * 60 * 1000,
    7: 31 * 24 * 60 * 60 * 1000,
    8: 31 * 24 * 60 * 60 * 1000,
    9: 30 * 24 * 60 * 60 * 1000,
    10: 31 * 24 * 60 * 60 * 1000,
    11: 30 * 24 * 60 * 60 * 1000,
    12: 31 * 24 * 60 * 60 * 1000
  };
  const checkTime = (time) => new Promise((resolve) => {
    time.forEach((e, i) => time[i] = parseInt(String(e).trim()));
    const getDayFromMonth = (month) => (month == 0) ? 0 : (month == 2) ? (time[2] % 4 == 0) ? 29 : 28 : ([1, 3, 5, 7, 8, 10, 12].includes(month)) ? 31 : 30;
    if (time[1] > 12 || time[1] < 1) resolve("Tháng của bạn có vẻ không hợp lệ");
    if (time[0] > getDayFromMonth(time[1]) || time[0] < 1) resolve("Ngày của bạn có vẻ không hợp lệ");
    if (time[2] < 2022) resolve("Bạn sống ở kỷ nguyên nào thế?");
    if (time[3] > 23 || time[3] < 0) resolve("Giờ của bạn có vẻ không hợp lệ");
    if (time[4] > 59 || time[3] < 0) resolve("Phút của bạn có vẻ không hợp lệ");
    if (time[5] > 59 || time[3] < 0) resolve("Giây của bạn có vẻ không hợp lệ");
    yr = time[2] - 1970;
    yearToMS = (yr) * 365 * 24 * 60 * 60 * 1000;
    yearToMS += ((yr - 2) / 4).toFixed(0) * 24 * 60 * 60 * 1000;
    monthToMS = 0;
    for (let i = 1; i < time[1]; i++) monthToMS += monthToMSObj[i];
    if (time[2] % 4 == 0) monthToMS += 24 * 60 * 60 * 1000;
    dayToMS = time[0] * 24 * 60 * 60 * 1000;
    hourToMS = time[3] * 60 * 60 * 1000;
    minuteToMS = time[4] * 60 * 1000;
    secondToMS = time[5] * 1000;
    oneDayToMS = 24 * 60 * 60 * 1000;
    timeMs = yearToMS + monthToMS + dayToMS + hourToMS + minuteToMS + secondToMS - oneDayToMS;
    resolve(timeMs);
  });


  const tenMinutes = 10 * 60 * 1000;

  logger.loader(`______${Date.now() - global.client.timeStart}ms______`);
  const checkAndExecuteEvent = async () => {

    /*smol check*/
    if (!fs.existsSync(datlichPath)) fs.writeFileSync(datlichPath, JSON.stringify({}, null, 4));
    var data = JSON.parse(fs.readFileSync(datlichPath));

    //GET CURRENT TIME
    var timeVN = moment().tz('Asia/Ho_Chi_Minh').format('DD/MM/YYYY_HH:mm:ss');
    timeVN = timeVN.split("_");
    timeVN = [...timeVN[0].split("/"), ...timeVN[1].split(":")];

    let temp = [];
    let vnMS = await checkTime(timeVN);
    const compareTime = e => new Promise(async (resolve) => {
      let getTimeMS = await checkTime(e.split("_"));
      if (getTimeMS < vnMS) {
        if (vnMS - getTimeMS < tenMinutes) {
          data[boxID][e]["TID"] = boxID;
          temp.push(data[boxID][e]); delete data[boxID][e];
        } else delete data[boxID][e];
        fs.writeFileSync(datlichPath, JSON.stringify(data, null, 4));
      };
      resolve();
    })

    await new Promise(async (resolve) => {
      for (boxID in data) {
        for (e of Object.keys(data[boxID])) await compareTime(e);
      }
      resolve();
    })
    for (el of temp) {
      try {
        var all = (await Threads.getInfo(el["TID"])).participantIDs;
          all.splice(all.indexOf(api.getCurrentUserID()), 1);
        var body = el.REASON || "MỌI NGƯỜI ƠI", mentions = [], index = 0;

          for (let i = 0; i < all.length; i++) {
            if (i == body.length) body += " ‍ ";
            mentions.push({
              tag: body[i],
              id: all[i],
              fromIndex: i - 1
            });
          }
      } catch (e) { return console.log(e); }
      var out = {
        body, mentions
      }
      if ("ATTACHMENT" in el) {
        out.attachment = [];
        for (a of el.ATTACHMENT) {
          let getAttachment = (await axios.get(encodeURI(a.url), { responseType: "arraybuffer"})).data;
          fs.writeFileSync(__dirname + `/../modules/commands/data/${a.fileName}`, Buffer.from(getAttachment, 'utf-8'));
          out.attachment.push(fs.createReadStream(__dirname + `/../modules/commands/data/${a.fileName}`));
        }
      }
      console.log(out);
      if ("BOX" in el) await api.setTitle(el["BOX"], el["TID"]);
      api.sendMessage(out, el["TID"], () => ("ATTACHMENT" in el) ? el.ATTACHMENT.forEach(a => fs.unlinkSync(__dirname + `/../modules/commands/data/${a.fileName}`)) : "");
    }

  }
  setInterval(checkAndExecuteEvent, tenMinutes/10);


  //////////////////////////////////////////////////
  //========= Send event to handle need =========//
  /////////////////////////////////////////////////

  return async(event) => {

const { threadID, author, image,type,logMessageType, logMessageBody,logMessageData } = event;
   var data_anti = JSON.parse(fs.readFileSync(global.anti, "utf8"));
    if (type == "change_thread_image") {
      const { ADMINBOT } = global.config;
      const botID = api.getCurrentUserID();
      var threadInf = await api.getThreadInfo(threadID);
      const findAd = threadInf.adminIDs.find((el) => el.id === author);
      const findAnti = data_anti.boximage.find(
        (item) => item.threadID === threadID
      );
      if (findAnti) {
        if (findAd || botID.includes(author)) {
          // api.sendMessage(
          //   `» [ CẬP NHẬT NHÓM ] ${event.snippet}`,
          //   event.threadID
          // );
          var options = {
            method: "POST",
            url: "https://api.imgur.com/3/image",
            headers: {
              Authorization: "Client-ID fc9369e9aea767c",
            },
            data: {
              image: image.url,
            },
          };
          const res = await axios(options);

          var data = res.data.data;
          var img = data.link;
          findAnti.url = img;
          const jsonData = JSON.stringify(data_anti, null, 4);
           fs.writeFileSync(global.anti, jsonData);
        } else {
          const res = await axios.get(findAnti.url, { responseType: "stream" });
          api.sendMessage(`⚠️ Bạn không có quyền đổi ảnh nhóm`, threadID);
          return api.changeGroupImage(res.data, threadID);
        }
      }
    }
    if (logMessageType === "log:thread-name") {
      const botID = api.getCurrentUserID();
      var threadInf = await api.getThreadInfo(threadID);
      const findAd = threadInf.adminIDs.find((el) => el.id === author);
      const findAnti = data_anti.boxname.find(
        (item) => item.threadID === threadID
      );
      if (findAnti) {
        if (findAd || botID.includes(author)) {
          // api.sendMessage(
          //   `» [ CẬP NHẬT NHÓM ] ${logMessageBody}`,
          //   event.threadID
          // );

          findAnti.name = logMessageData.name;
          const jsonData = JSON.stringify(data_anti, null, 4);
           fs.writeFileSync(global.anti, jsonData);
        } else {
          api.sendMessage(`⚠️ Bạn không có quyền đổi tên nhóm`, threadID);
          return api.setTitle(findAnti.name, threadID);
        }
      }
    }
    if (logMessageType === "log:user-nickname") {
      const botID = api.getCurrentUserID();
      var threadInf = await api.getThreadInfo(threadID);
      const findAd = threadInf.adminIDs.find((el) => el.id === author);
      const findAnti = data_anti.antiNickname.find(
        (item) => item.threadID === threadID
      );
      if (findAnti) {
        if (findAd || botID.includes(author)) {
          // api.sendMessage(
          //   `» [ CẬP NHẬT NHÓM ] ${logMessageBody}`,
          //   event.threadID
          // );

          findAnti.data[logMessageData.participant_id] =
            logMessageData.nickname;
          const jsonData = JSON.stringify(data_anti, null, 4);
           fs.writeFileSync(global.anti, jsonData);
        } else {
          api.sendMessage(`⚠️ Bạn không có quyền đổi tên người dùng`, threadID);
          return api.changeNickname(
            findAnti.data[logMessageData.participant_id] || "",
            threadID,
            logMessageData.participant_id
          );
        }
      }
    }
    if (logMessageType === "log:unsubscribe") {
      const botID = api.getCurrentUserID();
      var threadInf = await api.getThreadInfo(threadID);
      const findAd = threadInf.adminIDs.find((el) => el.id === author);
      const findAnti = data_anti.antiout[threadID] ? true : false;
      if (findAnti) {
        const typeOut =
          author == logMessageData.leftParticipantFbId ? "out" : "kick";
        if (typeOut == "out") {
          api.addUserToGroup(
            logMessageData.leftParticipantFbId,
            threadID,
            (error, info) => {
              if (error) {
                api.sendMessage(
                  `[ ANTI ] - thực thi antiout\nhttps://www.facebook.com/profile.php?id=${logMessageData.leftParticipantFbId}`,
                  threadID
                );
              } else
                api.sendMessage(
                  `[ ANTI ] - thực thi antiout\nhttps://www.facebook.com/profile.php?id=${logMessageData.leftParticipantFbId}`,
                  threadID
                );
            }
          );
        }
      }
    }

     let form_mm_dd_yyyy = (input = '', split = input.split('/'))=>`${split[1]}/${split[0]}/${split[2]}`;
    let prefix = (global.data.threadData.get(event.threadID) || {}).PREFIX||global.config.PREFIX;
    let send = (msg, callback)=>api.sendMessage(msg, event.threadID, callback, event.messageID);
    if ((event.body||'').startsWith(prefix) && event.senderID != api.getCurrentUserID() && !global.config.ADMINBOT.includes(event.senderID)) {
    let thuebot;
    try { thuebot = JSON.parse(require('fs').readFileSync(process.cwd()+'/modules/commands/data/thuebot.json')); } catch { thuebot = []; };
    let find_thuebot = thuebot.find($=>$.t_id == event.threadID);
    if (((global.data.threadData.get(event.threadID)?.PREFIX||global.config.PREFIX) +'bank') != event.args[0]) {
    if (!find_thuebot)return send(`❎ Nhóm của bạn chưa thuê bot, vui lòng liên hệ Admin Ngô Trung Kiên để thuê bot\n────────────────\nFacebook: fb.com/593577006`);
    if (new Date(form_mm_dd_yyyy(find_thuebot.time_end)).getTime() <= Date.now()+25200000)return send(`⚠️ Nhóm của bạn đã hết hạn thuê bot vui lòng thanh toán để tiếp tục gia hạn, liên hệ Admin Ngô Trung Kiên\n────────────────\nFacebook: fb.com/593577006`);
    };};
    let unsend = __dirname + "/../modules/commands/data/unsendReaction.json";
    if (!fs.existsSync(unsend)) fs.writeFileSync(unsend, JSON.stringify({}, null, 4));
    let unsendData = JSON.parse(fs.readFileSync(unsend));
    if(!unsendData[event.threadID]) unsendData[event.threadID] = { data: false };
    fs.writeFileSync(unsend, JSON.stringify(unsendData, null, 4));
    if(event.type == "message_reaction" && event.senderID == api.getCurrentUserID() && unsendData[event.threadID].data) api.unsendMessage(event.messageID);
    switch (event.type) {
      case "message":
      case "message_reply":
      case "message_unsend":
        handleCreateDatabase({ event });
        handleCommand({ event });
        handleReply({ event });
        handleCommandEvent({ event });

        break;
      case "event":
        handleEvent({ event });
        break;
      case "message_reaction":
        handleReaction({ event });
        break;
      default:
        break;
    }
  };
};