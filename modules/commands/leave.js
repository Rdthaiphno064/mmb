module.exports.config = {
  name: "leave",
  version: "1.0.0",
  hasPermssion: 2,
  credits: "ManhG",
  description: "Bật tắt thông báo rời nhóm cho nhóm hiện tại",
  commandCategory: "Qtv",
  usages: "",
  cooldowns: 2
};

module.exports.languages = {
  "vi": { "on": "✅ Bật", "off": "✅ Tắt", "successText": "gửi tin nhắn thông báo khi có thành viên rời nhóm chat", },
  "en": { "on": "on", "off": "off", "successText": "send a notification message when a member leaves your chat group", }
}
const fs = require('fs')
const path = __dirname + '/data/dataEvent.json';
exports.onLoad = o=>{
  if (!fs.existsSync(path))fs.writeFileSync(path, '{}')
}
module.exports.run = async function ({ api, event, Threads, getText }) {
  let data = JSON.parse(fs.readFileSync(path))
  const { threadID, messageID } = event;
  if (!data.leave)data.leave = []
  let findDataLeave = data.leave.find(i => i.threadID ==threadID);
  
  if(findDataLeave) findDataLeave.status = !findDataLeave.status?true:false;else findDataLeave = data.leave.push({
         threadID,
         status: true
       });
   fs.writeFileSync(path, JSON.stringify(data,null,4),'utf8')
  return api.sendMessage(`${!findDataLeave.status ? getText("off") : getText("on")} ${getText("successText")}`, threadID, messageID);
}