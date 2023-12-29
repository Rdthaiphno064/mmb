module.exports.config = {
  name: 'antiout',
  eventType: ['log:unsubscribe'],
  version: '1.0.9',
  credits: 'ProCoderMew fix by Niiozic',
  description: 'Listen events',
  dependencies: {path: '' },
}
module.exports.run = async function ({ api, event, Users }) {
  const { resolve } = global.nodemodule.path
  const path = resolve(__dirname, '../commands', 'data', 'antiout.json')
  const { antiout } = require(path)
  const { logMessageData, author, threadID } = event
  const id = logMessageData.leftParticipantFbId
  const moment = require('moment-timezone')
  var timeNow = moment.tz('Asia/Ho_Chi_Minh').format('HH:mm:ss')
  var fullYear = global.client.getTime('fullYear')
  if (author == id && id != api.getCurrentUserID()) {
    const name = (await Users.getNameUser(id)) || 'Người dùng Facebook'
    if (antiout.hasOwnProperty(threadID) && antiout[threadID] == true) {
      try {
        await new Promise((r,j)=>api.addUserToGroup(id, threadID,e=>e?j():r()))
        return api.sendMessage(`Vào lúc ${timeNow} - ${fullYear} người dùng '${name}' định rời đi nhưng không được đâu nhé 🙂`,
          event.threadID,
          event.messageID
        )
      } catch (e) {
        return api.sendMessage(`Vào lúc ${timeNow} - ${fullYear} người dùng '${name}' định rời đi, rất tiếc không thể thêm lại vào nhóm 💔`,
          event.threadID,
          event.messageID
        )
      }
    }
  }
  return
}
