module.exports.config = {
 name: "gái",
 version: "1.0.3",
 hasPermssion: 0,
 credits: "Trankhuong",
 description: "Tổng hợp ảnh 18+!",
 usages: "phản hồi 1/2/3",
 commandCategory: "Ảnh",
 cooldowns: 5,
 dependencies: {
  axios: ""
 }
}, module.exports.run = async function({
 event: e,
 api: a,
 args: n
}) {
 if (!n[0]) return a.sendMessage("[ Danh Sách Hình Ảnh Của Bot ]\n────────────────\n1. Ảnh bikini\n2. Ảnh dú\n3. Ảnh gái đít bự\n4. Ảnh mông\n5. Ảnh sexy\n────────────────\n-> Reply (phản hồi) theo stt để xem\n-> Phí xem mỗi hình ảnh là 700$", e.threadID, ((a, n) => {
  global.client.handleReply.push({
   name: this.config.name,
   messageID: n.messageID,
   author: e.senderID,
   type: "create"
  })
 }), e.messageID)
}, module.exports.handleReply = async ({
 api: e,
 event: a,
 client: n,
 handleReply: t,
 Currencies: s,
 Users: i,
 Threads: o,Currencies,
}) => {
    let $ = 700;
    let money = (await Currencies.getData(a.senderID)).money;
    if(money < $)return e.sendMessage(`❎ Cần ${$}$ để xem ảnh!`, a.threadID);
    Currencies.decreaseMoney(a.senderID, $);
 var { p, h } = linkanh();

 if ("create" === t.type) {
  const n = (await p.get(h)).data.data;
  let t = (await p.get(n, {
   responseType: "stream"
  })).data;
  return e.sendMessage({
   body: `✅ Bạn đã bị trừ ${$}$`,
   attachment: t
  }, a.threadID, a.messageID)
 }

    function linkanh() {
        const p = require("axios");
        if ("1" == a.body)
          var h = "https://apis-01.trankhuong20723.repl.co/images/bikini";
      else if ("2" == a.body)
         var h = "https://apis-01.trankhuong20723.repl.co/images/du";
      else if ("3" == a.body)
         var h = "https://apis-01.trankhuong20723.repl.co/images/gaiditbu";
      else if ("4" == a.body)
          var h = "https://apis-01.trankhuong20723.repl.co/images/gaiditbu";
      else if ("5" == a.body)
          var h = "https://apis-01.trankhuong20723.repl.co/images/mong";
      else if ("6" == a.body)
          var h = "https://apis-01.trankhuong20723.repl.co/images/sexy";
        return { p, h };
    }
};
