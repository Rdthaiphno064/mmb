var configCommand = {
    name: 'autodown',
    version: '1.1.1',
    hasPermssion: 0,
    credits: 'DC-Nam', 
    description: 'Tự động tải xuống khi phát hiện liên kết!',
    commandCategory: 'No prefix',
    usages: 'bật/tắt',
    cooldowns: 3
},
axios = require('axios'),
fse = require('fs-extra'),
path = __dirname+'/data/autodown.json';

let streamURL = (url, ext = 'jpg')=>require('axios').get(url, {
    responseType: 'stream',
}).then(res=>(res.data.path = `tmp.${ext}`, res.data)).catch(e=>null);

function onLoad() {
    if (!fse.existsSync(path)) fse.writeFileSync(path, '{}');
};

async function noprefix(arg) {
    const s = JSON.parse(fse.readFileSync(path));
    if (arg.event.senderID == (global.botID || arg.api.getCurrentUserID())) return;
    if ((typeof s[arg.event.threadID] == 'boolean' && !s[arg.event.threadID])) return;
    const moment = require("moment-timezone");
    const time = moment.tz("Asia/Ho_Chi_Minh").format("HH:mm:ss");
    const out = (a, b, c, d) => arg.api.sendMessage(a, b?b: arg.event.threadID, c?c: null, d?d: arg.event.messageID),
    arr = arg.event.args,
    regEx_tiktok = /(^https:\/\/)((vm|vt|www|v)\.)?(tiktok|douyin)\.com\//,
    regEx_youtube = /(^https:\/\/)((www)\.)?(youtube|youtu)(PP)*\.(com|be)\//,
    regEx_facebook = /(^https:\/\/)(\w+\.)?(facebook|fb)\.(com|watch)\/\w+\/\w?(\/)?/

    //if (arg.event.type == 'message_reply') arr.push(...arg.event.messageReply.args);
    for (const el of arr) {
        /* TỰ ĐỘNG TẢI VIDEO TIKTOK */
        if (regEx_tiktok.test(el)) {
            const data = (await axios.post(`https://www.tikwm.com/api/`, {
                url: el
            })).data.data;
            out({
                body: `[ ${data.images?'Photo':'Video'} Từ Liên Kết Tiktok ]\n──────────────────\n📺 Kênh: ${data.author.nickname}\n📎 URL: https://www.tiktok.com/@${data.author.unique_id}\n📍 Tiêu Đề: ${data.title}\n⛳ Quốc Gia: ${data.region}\n⏱️ Thời Lượng: ${data.music_info.duration}\n👍 Lượt Thích: ${data.digg_count}\n💬 Lượt Bình Luận: ${data.comment_count}\n🔀 Lượt Chia Sẻ: ${data.share_count}\n⬇️ Lượt Tải: ${data.download_count}\n🎧 Nhạc Gốc: ${data.music_info.album}\n📌 Thả cảm xúc để tải nhạc or nhạc gốc`, attachment: (data.images?await Promise.all(data.images.map($=>streamURL($))):await streamURL(data.play, 'mp4')),}, '', (err, dataMsg) => global.client.handleReaction.push({
                    name: configCommand.name, messageID: dataMsg.messageID, url_audio: data.music
                })); // Video không logo thì sửa "wmplay" -> "play";
        };
        /* END */

        /* TỰ DỘNG TẢI VIDEO YOUTUBE */
        if (regEx_youtube.test(el)) {
            const data = (await axios.get(`https://apis-02.trankhuong20723.repl.co/autodownurl/downloader?url=${el}`)).data.data,
            info = (a, b) => `📺 Tiêu Đề: ${a.title}\n⏱️ Thời Lượng: ${a.duration}`;
            if (data.video.size < 26214400)out({
                body: (info(data, data.video.size))+'\n📌 Thả cảm xúc để tải nhạc'+`\n⏰ Time: ${time}`, attachment: await streamURL(data.video.url, 'mp4')}, '', (err, datMsg) => global.client.handleReaction.push({
                    name: configCommand.name, messageID: datMsg.messageID, url_audio: data.music.url
                })); else if (data.music.size < 26214400)out({
                body: (info(data))+`\n⏰ Time: ${time}`, attachment: await streamURL(data.music.url, 'mp3')});
        };
        /* END */

        /* TỰ ĐỘNG TẢI VIDEO FACEBOOK */
        if (regEx_facebook.test(el)) {
            let res = (await axios.get('https://duongkum999.codes/fb/info-post?url='+el)).data;
            let vd = res.attachment.filter($=>$.__typename=='Video');
            let pt = res.attachment.filter($=>$.__typename=='Photo');
            let s = attachment=>out({ body: `Tiêu đề: ${res.message}`+'', attachment,}, '', (err, dataMsg) => global.client.handleReaction.push({
                name: configCommand.name, messageID: dataMsg.messageID, url_audio: null
            }));
            Promise.all(vd.map($=>streamURL($.browser_native_sd_url, 'mp4'))).then(r=>r.filter($=>!!$).length > 0?s(r):'');
            Promise.all(pt.map($=>streamURL(($.image||$.photo_image).uri, 'jpg'))).then(r=>r.filter($=>!!$).length > 0?s(r):'');
        };
        /* END */
    };
};
async function reactionMsg(arg) {
    const out = (a, b, c, d) => arg.api.sendMessage(a, b?b: arg.event.threadID, c?c: null, d),
    _ = arg.handleReaction;
    if ('url_audio'in _) out({
        body: `💿 Music 💿`, attachment: await streamURL(_.url_audio, 'mp3')}, '', '', _.messageID);
};
function runCommand(arg) {
    const out = (a, b, c, d) => arg.api.sendMessage(a, b?b: arg.event.threadID, c?c: null, d?d: arg.event.messageID);
    const data = JSON.parse(fse.readFileSync(path));
    s = data[arg.event.threadID] = typeof data[arg.event.threadID] != 'boolean'||!!data[arg.event.threadID]?false: true;
    fse.writeFileSync(path, JSON.stringify(data, 0, 4));
    out((s?'Bật': 'Tắt')+' '+configCommand.name);
};

module.exports = {
    config: configCommand,
    onLoad,
    run: runCommand,
    handleEvent: noprefix,
    handleReaction: reactionMsg
};
