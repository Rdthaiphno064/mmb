module.exports.config = {
    name: "reset",
    version: "2.0.2",
    hasPermssion: 3,
    credits: "Mirai Team mod by Jukie",
    description: "Khởi động lai bot",
    commandCategory: "Admin",
    usages: "restart",
    cooldowns: 5,
    dependencies: { }
}
 
module.exports.run = async function({ api, args, Users, event, permssion}) {
const { threadID, messageID } = event;
const axios = global.nodemodule["axios"];

const moment = require("moment-timezone");
    var gio = moment.tz("Asia/Ho_Chi_Minh").format("HH");
    var phut = moment.tz("Asia/Ho_Chi_Minh").format("mm");
    var giay = moment.tz("Asia/Ho_Chi_Minh").format("ss");
const fs = require("fs");
    let name = await Users.getNameUser(event.senderID)
  if (permssion != 3) return api.sendMessage( `[ DONATE ]`, event.threadID, event.messageID)
if(args.length == 0) api.sendMessage(`Tiến hành khởi động lại bot ☑️`,event.threadID, () =>process.exit(1))
else{    
let time = args.join(" ");
setTimeout(() =>
api.sendMessage(`Bot sẽ khởi động lại sau ${args}s\nBây giờ là: ${gio}:${phut}:${giay} ☑️`, threadID), 0)
setTimeout(() =>
api.sendMessage(`Đã hết ${args}s bắt đầu quá trình khởi động lại ☑️`,event.threadID, () =>process.exit(1)), 1000*`${time}`);
}
}