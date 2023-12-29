module.exports.config = {
  name: "events",
  version: "1.1.1",
  hasPermssion: 1,
  credits: "BraSL",
  description: "đụ lồn sánh cặc",
  commandCategory: "Qtv",
  usages: "[]",
  cooldowns: 3,
};

const fs = require('fs')
const path = __dirname + '/data/dataEvent.json'
module.exports.run = async function({api, event, args, Users }) {
   const data = require('./data/dataEvent.json')
   const findDataJoin = data.join.find(i => i.threadID === event.threadID)
  const findDataLeave = data.leave.find(i => i.threadID === event.threadID)
  if(args[0] === 'join'){
      if(findDataJoin){
     if(findDataJoin.status){
       findDataJoin.status = false
        api.sendMessage('Đã tắt join nhóm này thành công', event.threadID)
     }else {
       data.join.push({
         threadID,
         status: true
       })
       api.sendMessage('Đã bật join nhóm này thành công', event.threadID)
     }
      return fs.writeFileSync(path, JSON.stringify(data,null,4),'utf8')
   }
  }else if(args[0] === 'leave'){
    if(findDataLeave){
     if(findDataLeave.status){
       findDataLeave.status = false
        api.sendMessage('Đã tắt leave nhóm này thành công', event.threadID)
     }else {
       data.leave.push({
         threadID,
         status: true
       })
       api.sendMessage('Đã bật leave nhóm này thành công', event.threadID)
     }
      return fs.writeFileSync(path, JSON.stringify(data,null,4),'utf8')
   }
  }
   
}
