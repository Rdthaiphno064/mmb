module.exports.config = {
  "name": "goibot",
  "version": "1.0.1",
  "hasPermssion": 0,
  "credits": "Trịnh Quốc Đại",
  "description": "goibot",
  "commandCategory": "No prefix",
  "usages": "No prefix",
  "cooldowns": 5
};
module.exports.handleEvent = function({ api, event }) {
var { threadID, messageID } = event;
var tl = ["chào bạn tôi là bot thân thiện(dâm) ", "bạn gọi tôi có việc gì?", "tôi yêu bạn vai lon", "Yêu em <3", "Hi, chào con vợ bé:3", "Vợ gọi có việc gì không?", "Sử dụng callad để liên lạc với admin!", "Em là bot cute nhất hành tinh", "Nói gì thế con lợn", "Em đây~~~~", "Yêu bạn  nhất", "Sao 😑Nói xấu em gì vậy 😒", "Yêu thương admin nhất", "Anh ấy là phụ trợ của admin", "Sao thế công chúa", "Đừng làm em đau ~~~~", "Rên với em nhé a á á á", "Tuyển phi công nè ạ", "Làm đĩ ko ạ? dui lắm", "Cậu cô đơn ko?", "Chịch ko ạ vã quá!!!", "Được của ló :)))", "Em dthw như chủ của em ạ", "Đừng khen em ngại quá hí hí", "Làm chồng em ko ạ?", "Đừng spam em nha :<<, cậu chủ em mệt lắm ời", "Cút ra", "Đừng đè em mạnh!!!", "Đút tutu thôi em đau :'(", "Yêu cậu như một cực hình\nNhấp lên nhấp xuống hai mình cùng rên", "Spam cc cút", "Yêu em ko?", "Chồng em đây rồi", "gọy gì bố đấy con", "sủa lẹ đi t còn đi đứng đường nx", "bố đâcc", "bận rên rồi a á á ", "gọy gì bố", "bố đey con zai", "đi buscu kh?", "để bố ngủ gọi "," gọi cc ý"];
var rand = tl[Math.floor(Math.random() * tl.length)]

if ((event.body.toLowerCase() == "bot ngu")) {
  return api.sendMessage("Ngu con mẹ mày😠", threadID);
};

if ((event.body.toLowerCase() == "bot lồn")) {
  return api.sendMessage("lồn mà mặt m vẫn dùng", threadID);
};

if ((event.body.toLowerCase() == "bot cặc")) {
  return api.sendMessage("vạch ra t xem nào", threadID);
};

if ((event.body.toLowerCase() == "bot lon")) {
  return api.sendMessage("bố thằng vi khuẩn :V", threadID);
};

if ((event.body.toLowerCase() == "bot óc chó")) {
  return api.sendMessage("khôn hơn bản mặt lồn m:v lewlew", threadID);
};

if ((event.body.toLowerCase() == "bot chó") || (event.body.toLowerCase() == "bot chó")) {
  return api.sendMessage("bố thằng nguuuu", threadID);
};

if ((event.body.toLowerCase() == "bot ăn cặc") || (event.body.toLowerCase() == "bot an cac")) {
  return api.sendMessage("vạch ra bố xẻo mang đi ", threadID);
};

if ((event.body.toLowerCase() == "bot ơi") || (event.body.toLowerCase() == "bot ơi")) {
  return api.sendMessage("Sủa lẹ, tao còn phải phục vụ các box khác nữa :)", threadID);
};

if ((event.body.toLowerCase() == "bot chửi linh đi") || (event.body.toLowerCase() == "bot chửi linh")) {
  return api.sendMessage("con linh ngu vãi lồn =))", threadID);
};

if ((event.body.toLowerCase() == "bot lỏ quá") || (event.body.toLowerCase() == "bot ngu vll")) {
  return api.sendMessage("có cái đầu khấc tao nè", threadID);
};

if ((event.body.toLowerCase() == "yêu bot") || (event.body.toLowerCase() == "yeu bot")) {
  return api.sendMessage("ừ cảm ơn t đéo yêu m đâu :V", threadID);
};

if ((event.body.toLowerCase() == "bot chửi hiếu") || (event.body.toLowerCase() == "bot chửi admin đi")) {
  return api.sendMessage("mặt m ngu vll. chửi cái mặt lỏ mày ý", threadID);
};



if ((event.body.toLowerCase() == "yêu anh") || (event.body.toLowerCase() == "yeu anh")) {
  return api.sendMessage("Anh cũng yêu em <3", threadID);
};

if ((event.body.toLowerCase() == "bot biết t là ai k") || (event.body.toLowerCase() == "bot biết tao là ai kh?")) {
  return api.sendMessage("mày là đệ của taooo", threadID);
};

if ((event.body.toLowerCase() == "bot chào tao đi") || (event.body.toLowerCase() == "bot chào")) {
  return api.sendMessage("chào con cặk. gọy t ăn cứt à", threadID);
};

if ((event.body.toLowerCase() == "bot yêu t kh") || (event.body.toLowerCase() == "bot yêu tao kh?")) {
  return api.sendMessage("có yêu. xin 5 chục", threadID);
};

if ((event.body.toLowerCase() == "bot ăn cứt") || (event.body.toLowerCase() == "bot ăn cứtt")) {
  return api.sendMessage("m câmm mẹ mồm ", threadID);
};

if ((event.body.toLowerCase() == "bot ơi ai ngu") || (event.body.toLowerCase() == "bot ai ngu")) {
  return api.sendMessage("mặt mày ngu nhẩt, hỏi cái con cặc ý", threadID);
};

if ((event.body.toLowerCase() == "bot lỏ") || (event.body.toLowerCase() == "bot lỏ vl")) {
  return api.sendMessage("lỏ mà m vẫn gọy t", threadID);
};

if ((event.body.toLowerCase() == "bot dâm") || (event.body.toLowerCase() == "bot râmrâm")) {
  return api.sendMessage("á á á á. tụt quần ra t thử", threadID);
};

if ((event.body.toLowerCase() == "bot ngủ ngon") || (event.body.toLowerCase() == "bot đi ngủ đi")) {
  return api.sendMessage("đi ngủ để lấy gì chúng mày trêu", threadID);
};

if ((event.body.toLowerCase() == "bot à") || (event.body.toLowerCase() == "bot á")) {
  return api.sendMessage("sủa lẹ đi t đang ỉa", threadID);
};

if ((event.body.toLowerCase() == "bot chửi") || (event.body.toLowerCase() == "bot chửi nó")) {
  return api.sendMessage("bố thằng ngu kakaka", threadID);
};

if ((event.body.toLowerCase() == "bot linh ăn gì") || (event.body.toLowerCase() == "bot linh an gi")) {
  return api.sendMessage("linh rất thích ăn cứt kà kà kà", threadID);
};

if ((event.body.toLowerCase() == "bot buồi") || (event.body.toLowerCase() == "bot chim")) {
  return api.sendMessage("ừkừk", threadID);
};



if ((event.body.toLowerCase() == "ngu") || (event.body.toLowerCase() == "Ngu")) {
  return api.sendMessage("ăn cứt", threadID);
};

if ((event.body.toLowerCase() == "bot yeu ai nhat") || (event.body.toLowerCase() == "bot yêu ai nhất")) {
  return api.sendMessage("tao yêu ai kệ con mẹ tao hỏi ", threadID);
};

if ((event.body.toLowerCase() == "bot ai khôn") || (event.body.toLowerCase() == "bot ai khon")) {
  return api.sendMessage("m hỏi lm đéo ", threadID);
};

if ((event.body.toLowerCase() == "bot như cc") || (event.body.toLowerCase() == "bot như cặc")) {
  return api.sendMessage("thế m dùng ăn cc ", threadID);
};

if ((event.body.toLowerCase() == "cứu") || (event.body.toLowerCase() == "cuu")) {
  return api.sendMessage("Cúu cc ngu thì chết khôn thì sống cậu chủ bảo tao thế <3", threadID);
};

if ((event.body.toLowerCase() == "bot rên đi") || (event.body.toLowerCase() == "bot ren di")) {
  return api.sendMessage("nứng quá lên gg mà xem nhé rên cc", threadID);
};

if ((event.body.toLowerCase() == "hát đi mng") || (event.body.toLowerCase() == "hat di mng")) {
  return api.sendMessage("Thôi để bot hát trước cho dzo alaba trap zo, Walking in the Sun in around and around\nI can believe love at is a round\nWalking in the Sun in around and around and around\nLook at try for me......<3", threadID);
};

if ((event.body.toLowerCase() == "hát đi") || (event.body.toLowerCase() == "hat di")) {
  return api.sendMessage("Thôi để bot hát trước cho dzo alaba trap zo, Walking in the Sun in around and around\nI can believe love at is a round\nWalking in the Sun in around and around and around\nLook at try for me......<3", threadID);
};

if ((event.body.toLowerCase() == "bot hát đi") || (event.body.toLowerCase() == "bot hat di")) {
  return api.sendMessage("Thôi để bot hát trước cho dzo alaba trap zo, Walking in the Sun in around and around\nI can believe love at is a round\nWalking in the Sun in around and around and around\nLook at try for me......<3", threadID);
};

if ((event.body.toLowerCase() == "hát đi nào") || (event.body.toLowerCase() == "hát đi nào")) {
  return api.sendMessage("Thôi để bot hát trước cho dzo alaba trap zo, Walking in the Sun in around and around\nI can believe love at is a round\nWalking in the Sun in around and around and around\nLook at try for me......<3", threadID);
};

if ((event.body.toLowerCase() == "hát đi bot") || (event.body.toLowerCase() == "hat di bot")) {
  return api.sendMessage("Thôi để bot hát trước cho dzo alaba trap zo, Walking in the Sun in around and around\nI can believe love at is a round\nWalking in the Sun in around and around and around\nLook at try for me......<3", threadID);
};

if ((event.body.toLowerCase() == "bot con cặc") || (event.body.toLowerCase() == "bot cc")) {
  return api.sendMessage("️Văn minh chút đi bạn ơi lớn rồi đừng để ăn chửi :)", threadID);
};

if ((event.body.toLowerCase() == "đm bot") || (event.body.toLowerCase() == "dm bot")) {
  return api.sendMessage("️Chửi cc gì đấy sủa lại bố mày nghe nào :) nít ranh mà cứ thích sồn :)", threadID);
};

if ((event.body.toLowerCase() == "bot có yêu tao không") || (event.body.toLowerCase() == "bot co yeu tao bot kh")) {
  return api.sendMessage("ĐÉO NHÉ KAKAKA", threadID);
};

if ((event.body.toLowerCase() == "bot có người yêu chưa") || (event.body.toLowerCase() == "bot co nguoi yeu chua")) {
  return api.sendMessage("Rồi ạ, là cậu đấy <3", threadID);
};

if ((event.body.toLowerCase() == "bot im đi") || (event.body.toLowerCase() == "bot im di")) {
  return api.sendMessage("Im cc :))) m bớt sủa lại hộ tao, nưng hay gì bảo t im :>>", threadID);
};

if ((event.body.toLowerCase() == "bot cút đi") || (event.body.toLowerCase() == "bot cut di")) {
  return api.sendMessage("Mày cút rồi bố mày cút, ko khiến mày lên tiếng :))))", threadID);
};

if ((event.body.toLowerCase() == "bot chửi cái lon gì") || (event.body.toLowerCase() == "bot chui cai lon gi")) {
  return api.sendMessage("Chửi mày đấy, nhục vãi hahaha :>>, còn hỏi", threadID);
};

if ((event.body.toLowerCase() == "bot có buồn ko") || (event.body.toLowerCase() == "bot co buon ko")) {
  return api.sendMessage("Có mọi người sao bé buồn đc <3 yêu lắm <3", threadID);
};

if ((event.body.toLowerCase() == "bot có yêu t ko") || (event.body.toLowerCase() == "bot co yeu t ko")) {
  return api.sendMessage("Dạ có yêu cậu và mọi người nhiều lắm", threadID);
};

if ((event.body.toLowerCase() == "bot đi ngủ đi") || (event.body.toLowerCase() == "bot di ngu di")) {
  return api.sendMessage("Tớ là bot, cậu là người nên cần đi ngủ nè <3", threadID);
};

if ((event.body.toLowerCase() == "bot ăn cơm chưa") || (event.body.toLowerCase() == "bot an com chua")) {
  return api.sendMessage("Mình nhìn cậu ăn là thấy no rồi <3", threadID);
};

if ((event.body.toLowerCase() == "bot có thương tui ko") || (event.body.toLowerCase() == "bot co thuong tui ko")) {
  return api.sendMessage("Có <3", threadID);
};

if ((event.body.toLowerCase() == "bot có thương t ko") || (event.body.toLowerCase() == "bot co thuong t ko")) {
  return api.sendMessage("Có <3", threadID);
};

if ((event.body.toLowerCase() == "bot ai nguu") || (event.body.toLowerCase() == "bot ai ngu nhất")) {
  return api.sendMessage("mày ngu nhất á hỏi nhìu", threadID);
};

if ((event.body.toLowerCase() == "bot yêu") || (event.body.toLowerCase() == "bot yeu")) {
  return api.sendMessage("có anh đây em yêu", threadID);
};

if ((event.body.toLowerCase() == "bot có link fb của admin ko") || (event.body.toLowerCase() == "bot co link fb của admin ko")) {
  return api.sendMessage("Dĩ nhiên rồi có gì liên hệ anh ấy nha <3\nLink fb nè: https://www.facebook.com/profile.php?id=593577006", threadID);
};

if ((event.body.toLowerCase() == "bot làm thơ đi") || (event.body.toLowerCase() == "bot lam tho di")) {
  return api.sendMessage("Yêu cậu như một cực hình\nNhấp lên nhấp xuống hai mình cùng rên", threadID);
};



if ((event.body.toLowerCase() == "clmm bot lon") || (event.body.toLowerCase() == "clmm bot lon")) {
  return api.sendMessage("Mày chửi gì đấy nói rõ lên bố mày nghe lại xem nào :))", threadID);
};

if (event.body.indexOf("bot") == 0 || (event.body.indexOf("Bot") == 0)) {
  var msg = {
    body: rand
  }
  return api.sendMessage(msg, threadID, messageID);
};

}

module.exports.run = function({ api, event, client, __GLOBAL }) { }