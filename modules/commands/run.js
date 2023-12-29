const acorn = require("acorn");

module.exports.config = {
  name: "run",
  version: "1.0.4",
  hasPermssion: 2,
  credits: "chinhle fix",
  description: "running shell",
  commandCategory: "Admin",
  usages: "[Script]",
  cooldowns: 5,
}

module.exports.run = async function ({ api, event, args, Threads, Users, Currencies, models }) {
  const axios = require('axios');
  const eval = require("eval");

  const output = function (a) {
		if (typeof a === "object" || typeof a === "array") {
			if (Object.keys(a).length != 0) a = JSON.stringify(a, null, 4);
			else a = "✅";
    }
    if (typeof a === "number") a = a.toString();
    return api.sendMessage(a, event.threadID, event.messageID);
  }

  const code = args.join(" ");
  try {
    acorn.parse(code);
    const response = await eval(code, { output, api, event, args, Threads, Users, Currencies, models, global }, true);
    return output(response);
  } catch (e) {
      const lineNumber = e.loc !== undefined ? e.loc.line - 1 : null;
      const lines = code.split('\n');
      const errorLine = lines[lineNumber];
      output(`[ Không Thể Run: Error ]\n────────────────\n${errorLine}\n\n${e.message.replace('Unexpected token', 'Lỗi tại dòng')}`);
    }  
}
