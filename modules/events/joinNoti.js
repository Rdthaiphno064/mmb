module.exports.config = {
	name: "joinNoti",
	eventType: ["log:subscribe"],
	version: "1.0.1",
	credits: "CatalizCS",
	description: "Thông báo bot hoặc người vào nhóm có random gif/ảnh/video",
	dependencies: {
		"fs-extra": "",
		"path": ""
	}
};

module.exports.onLoad = function () {
    const { existsSync, mkdirSync } = global.nodemodule["fs-extra"];
    const { join } = global.nodemodule["path"];

	const path = join(__dirname, "cache", "joinGif");
	if (existsSync(path)) mkdirSync(path, { recursive: true });	

	const path2 = join(__dirname, "cache", "joinGif", "randomgif");
    if (!existsSync(path2)) mkdirSync(path2, { recursive: true });

    return;
}


module.exports.run = async function({ api, event, Users, Threads }) {
    const { join } = global.nodemodule["path"];
	const { threadID } = event;
	if (event.logMessageData.addedParticipants.some(i => i.userFbId == api.getCurrentUserID())) {
		api.changeNickname(`[ ${global.config.PREFIX} ] • ${(!global.config.BOTNAME) ? "BotMiraiv2" : global.config.BOTNAME}`, threadID, api.getCurrentUserID());
		return api.sendMessage(`\n━━━━━━━━━━━━━━━━━━\n𝗞𝗘̂́𝗧 𝗡𝗢̂́𝗜 𝗧𝗛𝗔̂́𝗧 𝗕𝗔̣𝗜\n━━━━━━━━━━━━━━━━━━\n➝ Nhóm bạn chưa được duyệt để gửi yêu cầu ` + global.config.PREFIX + `request\n➝ Hiện tại mình đang có ${client.commands.size} lệnh có thể sử dụng được.\n➝ Prefix hiện tại khả dụng là: ` + global.config.PREFIX + `\n➝ Liên hệ admin qua\n➝ Fb : https://www.facebook.com/profile.php?id=593577006`, threadID);
	}
  else {
		try {
			const { createReadStream, existsSync, mkdirSync, readdirSync } = global.nodemodule["fs-extra"];
        const moment = require("moment-timezone");
  const time = moment.tz("Asia/Ho_Chi_Minh").format("DD/MM/YYYY || HH:mm:s");
  const hours = moment.tz("Asia/Ho_Chi_Minh").format("HH");
			let { threadName, participantIDs } = await api.getThreadInfo(threadID);
			const threadData = global.data.threadData.get(parseInt(threadID)) || {};
			const path = join(__dirname, "cache", "joinGif");
			const pathGif = join(path, `${threadID}.mp4`);

			var mentions = [], nameArray = [], memLength = [], i = 0;
			
			for (id in event.logMessageData.addedParticipants) {
				const userName = event.logMessageData.addedParticipants[id].fullName;
				nameArray.push(userName);
				mentions.push({ tag: userName, id });
				memLength.push(participantIDs.length - i++);
			}
			memLength.sort((a, b) => a - b);
			
			(typeof threadData.customJoin == "undefined") ? msg = "Welcome thread {type} {name}❗️.\nChào mừng đã đến với {threadName}🥳.\nBạn là thành viên thứ {soThanhVien} của nhóm🌆.🦋\nChúc bạn có một buổi {session} || {time} vui vẻ🌸": msg = threadData.customJoin;
			msg = msg
                .replace(/\{name}/g, nameArray.join(', '))
                .replace(/\{type}/g, (memLength.length > 1) ? 'các bạn' : 'bạn')
                .replace(/\{soThanhVien}/g, memLength.join(', '))
                .replace(/\{threadName}/g, threadName)
                .replace(/\{session}/g, hours <= 10 ? "sáng" : 
    hours > 10 && hours <= 12 ? "trưa" :
    hours > 12 && hours <= 18 ? "chiều" : "tối")
                .replace(/\{time}/g, time);

			if (existsSync(path)) mkdirSync(path, { recursive: true });

			const randomPath = readdirSync(join(__dirname, "cache", "joinGif", "randomgif"));

			if (existsSync(pathGif)) formPush = { body: msg, attachment: (await global.nodemodule["axios"]({
			url: (await global.nodemodule["axios"](`http://apis-01.trankhuong20723.repl.co/video/girl`)).data.data,
			method: "GET",
			responseType: "stream"
		})).data, mentions }
			else if (randomPath.length != 0) {
				const pathRandom = join(__dirname, "cache", "joinGif", "randomgif", `${randomPath[Math.floor(Math.random() * randomPath.length)]}`);
				formPush = { body: msg, attachment: (await global.nodemodule["axios"]({
			url: (await global.nodemodule["axios"](`http://apis-01.trankhuong20723.repl.co/video/girl`)).data.data,
			method: "GET",
			responseType: "stream"
		})).data, mentions }
			}
			else formPush = { body: msg, attachment: (await global.nodemodule["axios"]({
			url: (await global.nodemodule["axios"](`http://apis-01.trankhuong20723.repl.co/video/girl`)).data.data,
			method: "GET",
			responseType: "stream"
		})).data, mentions }

			return api.sendMessage(formPush, threadID);
      
		} catch (e) { return console.log(e) };
	}
        }