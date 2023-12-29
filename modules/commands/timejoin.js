exports.config = {
  name: 'timejoin',
  version: '0.0.1',
  hasPermssion: 0,
  credits: 'DC-Nam',
  description: 'Tạo & xem thời gian',
  commandCategory: 'Nhóm',
  usages: '[.../list]',
  cooldowns: 3
};
let now = ()  =>  Date.now()  +  25200000;
let link_avatar_fb = id  =>  `https://graph.facebook.com/${id}/picture?height=2000&width=2000&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662`;
let stream_url = (url, ext)  =>  require('axios').get(url, {
  responseType: 'stream',
}).then(res  =>  {
    if (!!ext)  res.data.path = 'tmp.'  +  ext;

    return res.data;
});
let _0 = x  =>  x  <  10  ?  '0'  +  x  :  x;
let days_s = (_1, _2)  =>  (_1  -  _2)  /  (1000  *  60  *  60  *  24)  <<  0;
let time_str = time  =>  (d  =>  `${_0(d.getHours())}:${_0(d.getMinutes())}:${_0(d.getSeconds())} - ${_0(d.getDate())}/${_0(d.getMonth()  +  1)}/${d.getFullYear()} (Thứ ${d.getDay()  ==  0  ?  'Chủ Nhật'  :  d.getDay()  +  1})`)(new Date(time));
let name = uid  =>  global.data.userName.get(uid);
let __ = l  =>  ''.repeat(l  ||  15);

exports.run = async  (o)  => {
  let {
    threadID: tid,
    senderID: sid,
    messageID: mid,
    mentions,
    messageReply: msgr = {},
    participantIDs = [],
  } = o.event;
  let target_id = msgr.senderID || Object.keys(mentions)[0] || sid;
  let send = msg => o.api.sendMessage(msg, tid, mid);  if (!o.event.isGroup)  return send(`Chỉ Hoạt Động Trong Nhóm.`);
  let thread = await o.Threads.getData(tid);
  let data = thread.data;

  if (!data.timejoin)  return send(`Database chưa có dữ liệu về thời gian all user tham gia nhóm, vui lòng thử lại`);
  if (o.args[0] == 'list')  {
    let avatar_box = thread.threadInfo.imageSrc;
    let form_msg = {};

    if (!!avatar_box)  form_msg.attachment = await stream_url(avatar_box, 'jpg');

    form_msg.body = `[ Danh Sách Tham Gia Nhóm ]\n──────────────────\n${(o.args[1]  ?  participantIDs.slice((o.args[1]  -  1)  *  10,  10  *  o.args[1])  :  participantIDs).map((id, ix, o, time_join_ = data.timejoin[id]  ||  now())  =>  `${ix  +  1}. ${name(id)}\n⏰ Time Join: ${time_str(time_join_)}\n→ Đã Tham Gia Được ${days_s(now(), time_join_)} Ngày\n${__()}`).join('\n')}\n${o.args[1]  ?  `• Page [${o.args[1]}/${participantIDs.length  /  10}]`  :  ''}`;

    return send(form_msg);
  };

  let time_join_ = data.timejoin[target_id];

  if (!time_join_)  return send(`Hiện tại chưa có dữ liệu về user này.`);

  send({
    body: `[ Thời Gian Tham Gia Nhóm ]\n──────────────────\n👤 Tên: ${name(target_id)}\n👨‍💻 Nhóm: ${thread.threadInfo.threadName}\n⏰ Time Join: ${time_str(time_join_)}\n⏳ Tính Đến Hiện Tại Là Đã Qua ${days_s(now(), time_join_)} Ngày.\n\n📌 Dùng "/timejoin list" để thời gian tham gia của tất cả thành viên.`,
    attachment: await stream_url(link_avatar_fb(target_id), 'jpg'),
    });
};
exports.handleEvent = async o  => {
  if (!o.event.isGroup)  return;

  let {
    threadID: tid,
    participantIDs = [],
  } = o.event;
  let thread = await o.Threads.getData(tid);
  let data = thread.data;

  if (!data.timejoin)  data.timejoin = {};

  for (let id of participantIDs)  if (!data.timejoin[id])  data.timejoin[id] = now();

  o.Threads.setData(tid, thread);
};