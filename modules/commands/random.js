module.exports.config = {
	name: "random",
	version: "1.0.0",
	hasPermssion: 0,
	credits: "D-Jukie",
	description: "Chọn ngẫu nhiên thành viên trong box",
	commandCategory: "Game",
	cooldowns: 0
};
module.exports.run = async ({ api, event, args, Users, Currencies }) => {
	try { const { threadID, messageID, participantIDs, isGroup } = event;
	const num = parseInt(args[0]) || 1;
	if(isGroup == false) return api.sendMessage('Vui lòng thực hiện lệnh này ở nhóm!', threadID, messageID);
	const random = participantIDs.sort(function() {
        return .5 - Math.random();
    });
  let data = (await Currencies.getData(event.senderID)).data || {};
    const members = [];
    for( let i = 0; i <= num - 1; i++) {
    	var name = (await Users.getData(random[i])).name;
    	members.push(name)
    }
  await Currencies.increaseMoney(event.senderID, args[1]);
	return api.sendMessage(`Người được chọn là: ${members.join(', ')}
Đã cộng thêm ${args[1]}$`, threadID, messageID);
      } catch (e) {
    console.log(e)
      }
}
