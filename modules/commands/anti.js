module.exports.config = {
  name: "anti",
  version: "4.1.5",
  hasPermssion: 1,
  credits: "BraSL",
  description: "ANTI BOX",
  commandCategory: "Qtv",
  usages: "anti dùng để bật tắt",
  cooldowns: 0,
  dependencies: {
    "fs-extra": "",
  },
};

const {
  readdirSync,
  readFileSync,
  writeFileSync,
  existsSync,
  unlinkSync,
} = require("fs");
const axios = require('axios')

module.exports.handleReply = async function ({
  api,
  event,
  args,
  handleReply,
}) {
  const { senderID, threadID, messageID, messageReply } = event;
  const { author, permssion } = handleReply;
  
  const pathData = global.anti;
  const dataAnti = JSON.parse(readFileSync(pathData, "utf8"));

  if(author !== senderID ) return api.sendMessage(`❎ Bạn không phải người dùng lệnh`,threadID)

  var number = event.args.filter(i=> !isNaN(i))
 for (const num of number){
  switch (num) {
    case "1": {
      //---> CODE ADMIN ONLY<---//
      if (permssion < 1)
        return api.sendMessage(
          "⚠️ Bạn không đủ quyền hạn để sử dụng lệnh này",
          threadID,
          messageID
        );
      var NameBox = dataAnti.boxname;
      const antiImage = NameBox.find(
        (item) => item.threadID === threadID
      );
      if (antiImage) {
        dataAnti.boxname = dataAnti.boxname.filter((item) => item.threadID !== threadID);
        api.sendMessage(
          "✅ Tắt thành công chế độ anti đổi tên box ",
          threadID,
          messageID
        );
      } else {
        var threadName = (await api.getThreadInfo(event.threadID)).threadName;
        dataAnti.boxname.push({
          threadID,
          name: threadName
        })
        api.sendMessage(
          "✅ Bật thành công chế độ anti đổi tên box",
          threadID,
          messageID
        );
      }
      writeFileSync(pathData, JSON.stringify(dataAnti, null, 4));
      break;
    }
    case "2": {
      if (permssion < 1)
        return api.sendMessage(
          "⚠️ Bạn không đủ quyền hạn để sử dụng lệnh này",
          threadID,
          messageID
        );
      const antiImage = dataAnti.boximage.find(
        (item) => item.threadID === threadID
      );
      if (antiImage) {
        dataAnti.boximage = dataAnti.boximage.filter((item) => item.threadID !== threadID);
        api.sendMessage(
          "✅ Tắt thành công chế độ anti đổi ảnh box",
          threadID,
          messageID
        );
      } else {
        var threadInfo = await api.getThreadInfo(event.threadID);
        var options = {
          method: "POST",
          url: "https://api.imgur.com/3/image",
          headers: {
            Authorization: "Client-ID fc9369e9aea767c",
          },
          data: {
            image: threadInfo.imageSrc,
          },
        };
        const res = await axios(options);

        var data = res.data.data;
        var img = data.link;
        dataAnti.boximage.push({
          threadID,
          url: img,
        });
        api.sendMessage(
          "✅ Bật thành công chế độ anti đổi ảnh box",
          threadID,
          messageID
        );
      }
      writeFileSync(pathData, JSON.stringify(dataAnti, null, 4));
      break;
    }
    case "3": {
      if (permssion < 1)
        return api.sendMessage(
          "⚠️ Bạn không đủ quyền hạn để sử dụng lệnh này",
          threadID,
          messageID
        );
      const NickName = dataAnti.antiNickname.find(
        (item) => item.threadID === threadID
      );
      
      if (NickName) {
        dataAnti.antiNickname = dataAnti.antiNickname.filter((item) => item.threadID !== threadID);
        api.sendMessage(
          "✅ Tắt thành công chế độ anti đổi biệt danh",
          threadID,
          messageID
        );
      } else {
        const nickName = (await api.getThreadInfo(event.threadID)).nicknames
        dataAnti.antiNickname.push({
          threadID,
          data: nickName
        });
        api.sendMessage(
          "✅ Bật thành công chế độ anti đổi biệt danh",
          threadID,
          messageID
        );
      }
      writeFileSync(pathData, JSON.stringify(dataAnti, null, 4));
      break;
    }
    /*case "4": {
      if (permssion < 1)
        return api.sendMessage(
          "⚠️ Bạn không đủ quyền hạn để sử dụng lệnh này",
          threadID,
          messageID
        );
      const antiout = dataAnti.antiout;
      if (antiout[threadID] == true) {
        antiout[threadID] = false;
        api.sendMessage(
          "✅ Tắt thành công chế độ anti out",
          threadID,
          messageID
        );
      } else {
        antiout[threadID] = true;
        api.sendMessage(
          "✅ Bật thành công chế độ anti out",
          threadID,
          messageID
        );
      }
      writeFileSync(pathData, JSON.stringify(dataAnti, null, 4));
      break;
    }*/
    case "4": {
      const antiImage = dataAnti.boximage.find(
        (item) => item.threadID === threadID
      );
      const antiBoxname = dataAnti.boxname.find(
        (item) => item.threadID === threadID
      );
      const antiNickname = dataAnti.antiNickname.find(
        (item) => item.threadID === threadID
      );
      return api.sendMessage(
        `[ CHECK ANTI ]\n\nAnti name box -> ${antiBoxname ? "true" : "false"}\nAnti avt box -> ${
          antiImage ? "true" : "false"
        }\nAnti nick name -> ${antiNickname ? "true" : "false"}`,/*\nAnti out -> ${dataAnti.antiout[threadID] ? "true" : "false"}*/
        threadID
      );
      break;
    }

    default: {
      return api.sendMessage(
        `Số bạn chọn không có trong lệnh`,
        threadID
      );
    }
  }
 }
};

module.exports.run = async ({ api, event, args, permssion, Threads }) => {
  const { threadID, messageID, senderID } = event;
  const threadSetting = (await Threads.getData(String(threadID))).data || {};
  const prefix = threadSetting.hasOwnProperty("PREFIX")
    ? threadSetting.PREFIX
    : global.config.PREFIX;

  return api.sendMessage(
        `[ ANTI CONFIG SETTING ]\n────────────────\n1. Cấm đổi tên nhóm\n2. Cấm đổi ảnh nhóm\n3. Cấm đổi biệt danh\n4. Check anti của box\n────────────────\n-> Reply (phản hồi) theo stt để chọn`,
        threadID, (error, info) => {
            if (error) {
              return api.sendMessage("Đã xảy ra lỗi!", threadID);
            } else {
              global.client.handleReply.push({
                name: this.config.name,
                messageID: info.messageID,
                author: senderID,
                permssion
              });
            }
          });
};
