module.exports.config = {
    "name": "mon",
    "version": "1.0.2",
    "hasPermssion": 0,
    "credits": "Trịnh Quốc Đại",
    "description": "Kiểm tra số tiền của bản thân hoặc người được tag",
    "commandCategory": "Bank",
    "usages": "[Tag]",
    "cooldowns": 0
};

module.exports.languages = {
  "vi": {
    "sotienbanthan": "Số tiền bạn đang có: %1$",
    "sotiennguoikhac": "Số tiền của %1 hiện đang có là: %2$"
  },
  "en": {
    "sotienbanthan": "Your current balance: %1$",
    "sotiennguoikhac": "%1's current balance: %2$"
  }
}

module.exports.run = async function({ api, event, args, Currencies, getText }) {
  try{
  const { threadID, messageID, senderID, mentions } = event;

  if (!args[0]) {
    const money = (await Currencies.getData(senderID)).money;
    const b = money.toLocaleString();
    return api.sendMessage(getText("sotienbanthan", b), threadID);
  }

  else if (Object.keys(event.mentions).length == 1) {
    var mention = Object.keys(mentions)[0];
    var money = (await Currencies.getData(mention)).money;
     const b = money.toLocaleString();
    if (!b) money = 0;
    return api.sendMessage({
      body: getText("sotiennguoikhac", mentions[mention].replace(/\@/g, ""), b),
      mentions: [{
        tag: mentions[mention].replace(/\@/g, ""),
        id: mention
      }]
    }, threadID, messageID);

  }

  else return global.utils.throwError(this.config.name, threadID, messageID);
    }catch(e){
    console.log(e)
  }
}
