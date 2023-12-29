module.exports.config = {
    name: "ship",
    version: "1.0.0",
    hasPermssion: 2,
    credits: "Niiozic",
    description: "share 1 mdl nào đó cho 1 tv trog group",
    commandCategory: "Admin",
    usages: "/share [reply or tag or để trống] + tên mdl muốn share",
    cooldowns: 0,
    dependencies: {
        "pastebin-api": "",
        "cheerio": "",
        "request": ""
    }
};

module.exports.run = async function ({ api, event, args }) {
  const permission = [`${global.config.ADMINBOT[0]}`];
    if (!permission.includes(event.senderID)) return api.sendMessage("⚠️ Bạn không được phép sử dụng lệnh này", event.threadID, event.messageID);
    const axios = require('axios');
    const fs = require('fs');
    const request = require('request');
    const cheerio = require('cheerio');
    const moment = require("moment-timezone");
    const hmm = moment.tz("Asia/Ho_Chi_Minh").format("DD/MM/YYYY | HH:mm:ss");
    const { join, resolve } = require("path");
    const { senderID, threadID, messageID, messageReply, type } = event;
    var name = args[0];
    if (type == "message_reply") {
        var text = messageReply.body;
         var uid = event.messageReply.senderID 
    }
        else uid = event.senderID;
    if(!text && !name) return api.sendMessage(`⏰ Bây giờ là: ${hmm} 
Hãy reply hoặc tag người muốn share`, event.threadID, event.messageID);
    //(!text && name) {
        var data = fs.readFile(
          `./modules/commands/${args[0]}.js`,
          "utf-8",
          async (err, data) => {
            if (err) return api.sendMessage(`⏰ Bây giờ là: ${hmm} \nRất tiếc mdl ${args[0]} mà bạn cần hiện không có trên hệ thống của bot ${global.config.BOTNAME}`, event.threadID, event.messageID);
            const { PasteClient } = require('pastebin-api')
            const client = new PasteClient("R02n6-lNPJqKQCd5VtL4bKPjuK6ARhHb");
            async function pastepin(name) {
              const url = await client.createPaste({
                code: data,
                expireDate: 'N',
                format: "javascript",
                name: name,
                publicity: 1
              });
              var id = url.split('/')[3]
              return 'https://pastebin.com/raw/' + id
            }
            var link = await pastepin(args[1] || 'noname')
        api.sendMessage(`Nhóm: ${global.data.threadInfo.get(event.threadID).threadName}
⏰ Vào lúc: ${hmm} 
💼 Tên lệnh: ${args.join("")}\nĐã gửi module ☑️`, threadID, messageID);
            api.sendMessage(`⏰ Vào lúc: ${hmm}
🔗 Link: ${link} 
🔰 Tên lệnh: ${args[0]}\nỞ nhóm: ${global.data.threadInfo.get(event.threadID).threadName}
Bạn được admin share riêng một module`, uid)
          }
        );
        return
}