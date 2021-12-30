const Discord = require("discord.js");
const fs = require('fs');
const readline = require("readline");
const { Client, WebhookClient, RichEmbed } = require('discord.js');
const { exec } = require("child_process");
const Axios = require('axios')
const akaneko = require('akaneko');
const request = require('request');
let price = require('crypto-price')
const { getHWID } = require('hwid');
var crypto = require('crypto');
var soosenbindermsg = "afk";
const { createCanvas, loadImage } = require('canvas')
const { NekoBot } = require("nekobot-api");
const api = new NekoBot();
var os = require('os');
const snekfetch = require('snekfetch');
const { head } = require("request");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
var reboot = "no"
process.title = "EinTim Selfbot | Login";
FgGreen = "\x1b[32m"
console.log(FgGreen,"[RPC] Initializing discord RPC...")
const rpcappl = require('discord-rich-presence')('780451040889798686');
process.on('unhandledRejection', (err, p) => {
});
const client = new Discord.Client();
var username = null;
var prefix = null;
var rpcenabl = null;
var footer = null;
var configcolor = null;
var thumb = null;
var otherusers = "no"
var wisheduser = null;
var wishedpass = null;
var dcpass = null;
var nitrosniper = null;
var tempuser = null;
var temppass = null;
var afkmsg = "no";
var footerimg = null;
var msgdelay = null;
var nitroemojispoof = "no";
var gsnipe = null;
var config = null;
var sbkey = null;
var hwid = null;
Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"

async function auth(){
  if (!fs.existsSync("./auth.json")) {
    console.log(FgBlue,`
  ████████╗██╗███╗   ███╗███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
  ╚══██╔══╝██║████╗ ████║██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
     ██║   ██║██╔████╔██║███████╗    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
     ██║   ██║██║╚██╔╝██║╚════██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
     ██║   ██║██║ ╚═╝ ██║███████║    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
     ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                        
  `)
      console.log(FgRed,"[AUTH] Please Login or Register!\n")
      console.log(" [1]Login [2]Redeem Key [3]Exit\n")
      rl.question(" :", function(auswahl) {
        if(auswahl == "1"){
          console.log(FgGreen, "[AUTH] Now Enter your Username and password");
          rl.question(" Username:", function(userlol) {
            tempuser = userlol;
            rl.question(" Password:", function(passlol) {
                temppass = passlol;
                heads = {"user-agent":"Mozilla/5.0"}
                var authurl = "https://eintim.ga/authserver.php?user=" + tempuser + "&pass=" + temppass + "&hwid=" + hwid;
                request({ url: authurl, headers: heads}, function (error, response, body) {
                  if(body == "Wrong password"){
                    console.log(FgRed,"\n [AUTH] Wrong Username or password. Press Any Key to exit");
                    process.stdin.setRawMode(true);
                    process.stdin.resume();
                    process.stdin.on('data', process.exit.bind(process, 0));
                  }
                  if(body == "Wrong HWID"){
                    console.log(FgRed,"\n [AUTH] HWID does not match. Contact the support for help. Press Any Key to exit");
                    process.stdin.setRawMode(true);
                    process.stdin.resume();
                    process.stdin.on('data', process.exit.bind(process, 0));
                  }
                  if(body == "All Right"){
                    console.log(FgGreen,"\n [AUTH] Login completed succesfully. Have Fun!");
                    let authjson = { 
                      selfbotuser: tempuser,
                      selfbotpass: temppass
                  };
                  let data = JSON.stringify(authjson);
                  fs.writeFileSync('auth.json', data);
                    loadconfig();
                  }
                });
            })
          })

        }
        if (auswahl == "2"){
          console.log(FgGreen, "[AUTH] Enter your Key\n");
          rl.question(" :", function(key) {
            sbkey = key;
            console.log(FgGreen, "[AUTH] Now enter your wished username and password\n")
            rl.question(" Username:", function(wisheduserlol) {
              wisheduser = wisheduserlol;
              rl.question(" Password:", function(wishedpasslol) {
                  wishedpass = wishedpasslol;
                  heads = {"user-agent":"Mozilla/5.0"}
                  var keyurl = "https://eintim.ga/keyredeem.php?key=" + sbkey + "&user=" + wisheduser + "&pass=" + wishedpass;
                  request({ url: keyurl, headers: heads}, function (error, response, body) {
                    if (body == "Invalid Key"){
                     console.log(FgRed, "\n [AUTH] Invalid key. Feel free to contact our support for help. Press any key to exit.");
                     process.stdin.setRawMode(true);
                     process.stdin.resume();
                     process.stdin.on('data', process.exit.bind(process, 0));
                    }
                    if (body == "already redeemed"){
                      console.log(FgRed, "\n [AUTH] Key is already redeemed. Feel free to contact our support for help. Press any key to exit.");
                      process.stdin.setRawMode(true);
                      process.stdin.resume();
                      process.stdin.on('data', process.exit.bind(process, 0));
                    }
                    if(body == "kk"){
                      console.log(FgGreen, "[AUTH] Registered sucessfully. Have Fun!");
                    
                      let keyjson = { 
                        selfbotuser: wisheduser,
                        selfbotpass: wishedpass
                    };
                    let data = JSON.stringify(keyjson);
                    fs.writeFileSync('auth.json', data);
                    loadconfig();
                    }
                  });
              })

            })

          })
        }
        if (auswahl == "3"){
          process.exit(0);
        }
      })
  }else{
      const authjsonfile = require(process.cwd() + "/auth.json");
      heads = {"user-agent":"Mozilla/5.0"}
      var authurl = "https://eintim.ga/authserver.php?user=" + authjsonfile.selfbotuser + "&pass=" + authjsonfile.selfbotpass + "&hwid=" + hwid;
      request({ url: authurl, headers: heads}, function (error, response, body) {
      if(body == "Wrong password"){
        console.log(FgRed,"[AUTH] Wrong Username or password. Press Any Key to exit");
        process.stdin.setRawMode(true);
        process.stdin.resume();
        process.stdin.on('data', process.exit.bind(process, 0));
      }
      if(body == "Wrong HWID"){
        console.log(FgRed,"[AUTH] HWID does not match. Contact the support for help. Press Any Key to exit");
        process.stdin.setRawMode(true);
        process.stdin.resume();
        process.stdin.on('data', process.exit.bind(process, 0));
      }
      if(body == "All Right"){
        console.log(FgGreen,"[AUTH] Login completed succesfully. Have Fun!");
        loadconfig()
      }
                  
      });
      
  }
}
getHWID().then(id => {
  hwid = id;
  updater();
})
async function close(){
  process.exit(0);
}
async function updater(){
  if (fs.existsSync("./updated")){
    fs.unlinkSync("./updated");
    fs.unlinkSync("./updater.exe");
  };
  var version = 0.2;
  heads = {"user-agent":"Mozilla/5.0"};
  await request({url: "https://eintim.ga/version.txt", headers: heads}, function (error, response, body) {
      if(version != body){
        (async () => {
        console.log(FgGreen, "[UPDATER] A new update is available. It will download automatically. Please be patient. The bot will restart several times.");
        if(os.platform() == "win32"){
          const file = fs.createWriteStream("updater.exe");
          const sendReq =await Axios({
            url: "https://eintim.ga/winupdater.exe",
            method: 'GET',
            headers: {"user-agent":"Mozilla/5.0"},
            responseType: 'stream'
          });
          sendReq.data.pipe(file)
          
          
        file.on('finish', () => {
          file.close();
          sleep(2000).then(value => {
            exec("start updater.exe", (error, stdout, stderr) => {
            

            });
            setTimeout(close, 500);
          });
         
          
        });
        }
        if(os.platform() == "linux"){
          const file = fs.createWriteStream("updater");
          const sendReq = await Axios({
            url: "https://eintim.ga/linupdater",
            method: 'GET',
            headers: {"user-agent":"Mozilla/5.0"},
            responseType: 'stream'
          });
          sendReq.data.pipe(file)
        file.on('finish', () => {
          file.close();
          sleep(2000).then(value => {
            exec("chmod +x updater && ./updater", (error, stdout, stderr) => {
            

            });
            setTimeout(close, 500);
            });
         
        });
        }
        if(os.platform() == "darwin"){
          const file = fs.createWriteStream("updater");
          const sendReq = await Axios({
            urL: "https://eintim.ga/macupdater",
            headers:{"user-agent":"Mozilla/5.0"},
            method: 'GET',
            responseType: 'stream'
          });
          sendReq.data.pipe(file)
        file.on('finish', () => {
          file.close();
          sleep(2000).then(value => {
            exec("chmod +x updater && ./updater", (error, stdout, stderr) => {
            

            });
            setTimeout(close, 500);
            });
        });
      
        }
      })();
      }else{
        console.log(FgGreen, "[UPDATER] The Bot is up to date. Have Fun!");
        auth();
      }
  });
  
}
async function loadconfig(){
  process.title = "EinTim Selfbot | Configuration";
  if (fs.existsSync("./config.json")) {
    config = require(process.cwd() + "/config.json");
    prefix = config.prefix;
    rpcenabl = config.rpc;
    footer = config.footer;
    gsnipe = config.giveawaysniper;
    configcolor = config.embedcolor;
    footerimg = config.footerimage;
    thumb = config.thumbnail;
    dcpass = config.dcpass;
    msgdelay = config.deletedelay;
    token = config.token;
    rectoken = config.receivetoken;
    nitrosniper = config.nitrosniper;
   
    getusername();
	
  }else{
    console.log(FgBlue, `
 ████████╗██╗███╗   ███╗███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
 ╚══██╔══╝██║████╗ ████║██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
    ██║   ██║██╔████╔██║███████╗    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
    ██║   ██║██║╚██╔╝██║╚════██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
    ██║   ██║██║ ╚═╝ ██║███████║    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                       
`);
 console.log(FgRed, "[DISCLAIMER] I am not responsible for banned discord accounts!\n A selfbot is not allowed!\n You will probably be banned if someone reports you.\n");
  var dcconfigtoken = null;
  var dcconfigprefix = null;
  var dcconfigrpc = null;
  var dcconfigfooter = null;
  var dcconfigthumb = null;
  var dcconfignitrosniper = null;
  var dcconfiggsnipe = null;
  var dcconfigwebhook = null;
  var dcconfigtwitch = null;
  var dcconfigcolor = null;
  var dcconfigpass = null;
  var dcconfigdeletedelay = null;
  var dcconfigfooterpic = null;
  var dcconfignssnipereceiveacc = null;
  rl.question(FgCyan + "[CONFIG] Enter your discord account token:", function(tok) {
    dcconfigtoken = tok;
    rl.question(FgCyan + "[CONFIG] Enter a nitro sniper receive discord account token:", function(tokns) {
      dcconfignssnipereceiveacc = tokns;
      rl.question(FgCyan + "[CONFIG] Enter your selfbot prefix:", function(pre) {
        dcconfigprefix = pre;
        rl.question(FgCyan + "[CONFIG] Enter a delay for the deletion of selfbot messages (in seconds):", function(sec) {
          dcconfigdeletedelay = sec;
        rl.question(FgCyan + "[CONFIG] Enter your discord account password:", function(pas) {
          dcconfigpass = pas;
          rl.question(FgCyan + "[CONFIG] Enter a custom embed footer:", function(foo) {
            dcconfigfooter = foo;
            rl.question(FgCyan + "[CONFIG] Enter a embed color (In hex or html format):", function(col) {
              dcconfigcolor = col;
            rl.question(FgCyan + "[CONFIG] Enter a custom thumbnail picture link:", function(thu) {
              dcconfigthumb = thu;
              rl.question(FgCyan + "[CONFIG] Enter a webhook link:", function(web) {
                dcconfigwebhook = web;
              rl.question(FgCyan + "[CONFIG] Enter a custom footer picture link:", function(foop) {
                dcconfigfooterpic = foop;
              rl.question(FgCyan + "[CONFIG] Enter a twitch url for the twitch status:", function(twi) {
                dcconfigtwitch = twi;
               rl.question(FgCyan + "[CONFIG] Should the nitrosniper be enabled by default? (yes/no):", function(nit) {
                dcconfignitrosniper = nit;
              rl.question(FgCyan + "[CONFIG] Should the giveawaysniper be enabled by default? (yes/no):", function(gsn) {
                dcconfiggsnipe = gsn;
              rl.question(FgCyan + "[CONFIG] Should the selfbot rich presence be enabled by default? (yes/no):", function(srpc) {
                dcconfigrpc = srpc;
                let configjson = { 
                token: dcconfigtoken,
                deletedelay: dcconfigdeletedelay,
                receivetoken: dcconfignssnipereceiveacc,
                prefix: dcconfigprefix,
                rpc: dcconfigrpc,
                footer: dcconfigfooter,
                thumbnail: dcconfigthumb,
                webhook: dcconfigwebhook,
                nitrosniper: dcconfignitrosniper,
                giveawaysniper: dcconfiggsnipe,
                twitchurl: dcconfigtwitch,
                dcpass: dcconfigpass,
                embedcolor: dcconfigcolor,
                footerimage: dcconfigfooterpic
                };
                let data = JSON.stringify(configjson);
                fs.writeFileSync('config.json', data)
                  config = require(process.cwd() + "/config.json");
                  prefix = config.prefix;
                  rpcenabl = config.rpc;
                  gsnipe = config.giveawaysniper;
                  footer = config.footer;
                  configcolor = config.embedcolor;
                  footerimg = config.footerimage;
                  thumb = config.thumbnail;
                  dcpass = config.dcpass;
                  msgdelay = config.deletedelay;
                  token = config.token;
                  rectoken = config.receivetoken;
                  nitrosniper = config.nitrosniper;
                  
                  getusername();
              });
            });
          });
        });
      });
    });
  });
          });
         });
        });
        });
      });
    });
  });
 
 
  
  
  
 
 
  }
}
const randomChannel = (guild) => {
  var channel = guild.channels.random()
  if (channel.type === 'text') return channel;
  else return randomChannel(guild);
}
async function getusername(){
  heads = {"authorization":config.token, "user-agent":"Mozilla/5.0",json:true}
  url = 'https://discordapp.com/api/v8/users/@me'
  await request({url,headers: heads}, function (error, response, body) {
    const soosenbinder = JSON.parse(body);
    username = soosenbinder.username;
    init();
    launchbot();
    return soosenbinder.username;
   });
}
function between(min, max) {  
  return Math.floor(
    Math.random() * (max - min + 1) + min
  )
}
function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}   
String.prototype.allReplace = function(obj) {
  var retStr = this;
  for (var x in obj) {
      retStr = retStr.replace(new RegExp(x, 'g'), obj[x]);
  }
  return retStr;
};
function sleepseconds(s) {
  return new Promise((resolve) => {
    setTimeout(resolve,s * 1000);
  });
}   
function makeid(length) {
  var result           = '';
  var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for ( var i = 0; i < length; i++ ) {
     result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}
async function init(){
  process.title = "EinTim Selfbot  | Logged in as " + username;
  if (config.rpc == "yes"){
      rpcappl.updatePresence({
        state: 'Using EinTims selfbot',
        startTimestamp: Date.now(),
        largeImageKey: 'pb',
        largeImageText: 'EinTim Selfbot',
        instance: true,
      });
     
    
  }
   console.log(FgBlue + `
  ████████╗██╗███╗   ███╗███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
  ╚══██╔══╝██║████╗ ████║██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
     ██║   ██║██╔████╔██║███████╗    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
     ██║   ██║██║╚██╔╝██║╚════██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
     ██║   ██║██║ ╚═╝ ██║███████║    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
     ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                        
  `)
  console.log(FgCyan + ' [INFO] Bot started sucesfully')
  console.log(' [INFO] Version 0.2 Recode')
  console.log(' [INFO] Logged in as: ', username)
  console.log(' [SETTING] Your Prefix is: ', config.prefix)
  if(nitrosniper == "yes"){
    console.log(" [SETTING] Nitrosniper:", FgGreen, "Enabled", FgCyan)
  }else{
    console.log(" [SETTING] Nitrosniper: ", FgRed, "Disabled", FgCyan)
  }
  if(gsnipe == "yes"){
    console.log(" [SETTING] Giveaway Sniper:", FgGreen, "Enabled", FgCyan)
  }else{
    console.log(" [SETTING] Giveaway Sniper: ", FgRed, "Disabled", FgCyan)
  }
  console.log(" [MOTD] Were on Version 0.2 Recode Guys! Recode goes brrr")
  console.log(FgRed + "\n————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
  console.log(FgCyan)
}
client.on("messageReactionAdd", function(messageReaction, user){
  if(gsnipe == "yes"){
    if(messageReaction.emoji == "🎉"){
      if(user.id == client.user.id) return;
      console.log("[GSNIPE] Found Giveaway on Server", messageReaction.message.guild.name, "Reacting...");
      sleep(5000).then(value =>{
        messageReaction.message.react("🎉");

      });
    }
  }
  
});
client.on("message", async function(message) {
 if(afkmsg == "yes"){
   if(message.channel instanceof Discord.DMChannel){
     if(message.author.id != client.user.id) {
      const Embed = new  Discord.RichEmbed()
     .setColor(configcolor)
     .addField('\u200B', soosenbindermsg, true)
     message.channel.send(Embed).then(msg =>{
       sleepseconds(msgdelay).then(value =>{
         msg.delete();
       })
      })
     }
     
   }
 }
  if(nitrosniper == "yes"){
    if(message.content.includes('discord.gift') || message.content.includes('discordapp.com/gifts/') || message.content.includes('discord.com/gifts/')) {
      const webhooktoken = /[^/]*$/.exec(config.webhook)[0];
      const webhookid = config.webhook.replace(/^.*\/(?=[^\/]*\/[^\/]*$)|\/[^\/]*$/g, '');
      const webhookclient = new WebhookClient(webhookid, webhooktoken);
      var NitroCode = null;
      var Nitro = /(discord\.gift\/|discord\.com\/gifts\/|discordapp\.com\/gifts\/)[^\s]+/gim
      heads = {"user-agent":"Mozilla/5.0", 'authorization': config.receivetoken}
      var NitroUrl = Nitro.exec(message.content);
     if(NitroUrl.toString().includes("discordapp.com") || NitroUrl.toString().includes("discord.com")){
      NitroCode = NitroUrl[0].split('/')[2];
     }else{
      NitroCode = NitroUrl[0].split('/')[1];
     }
      
     var start = new Date()
      request.post({ url: `https://discordapp.com/api/v8/entitlements/gift-codes/${NitroCode}/redeem`, headers: heads}, function (error, response, body) {
        var oldtime = new Date() - start;
        var time = oldtime.toString().slice(0 ,-1);
       const responsejson = JSON.parse(body);
       
       if(responsejson.message == "Unknown Gift Code"){
         try{
          let embed = new RichEmbed()
          .setColor(configcolor)
          .setTitle('Nitro Code Sniped')
          .addField('Time Taken', time + "ms", true)
          .addField('Result', "Fakecode", true)
          .addField('Code', NitroCode, true)
          .addField('Author', `${message.author.username}`, true)
          .setThumbnail(config.thumbnail)
          .setTimestamp()
           embed.addField('Location', `${message.guild.name} `, true)
           webhookclient.send('', {
            embeds: [embed]
         })
          console.log(FgRed, `[NITROSNIPER] The Nitro code "${NitroCode}" found in "${message.guild.name}" sniped in 0.0${time}s was fake.`, FgCyan)
         }catch{
          let embed = new RichEmbed()
          .setColor(configcolor)
          .setTitle('Nitro Code Sniped')
          .addField('Time Taken', time + "ms", true)
          .addField('Result', "Fakecode", true)
          .addField('Code', NitroCode, true)
          .setTimestamp()
          .setThumbnail(config.thumbnail)
          .addField('Author', `${message.author.username}`, true)
           embed.addField('Location', `DMs `, true)
           webhookclient.send('', {
            embeds: [embed]
         })
          console.log(FgRed, `[NITROSNIPER] The Nitro code "${NitroCode}" found in your DMs sniped in 0.0${time}s was fake.`, FgCyan)
         }
        
       }
       if(responsejson.message == "This gift has been redeemed already."){
         try{
          let embed = new RichEmbed()
          .setColor(configcolor)
          .setTitle('Nitro Code Sniped')
          .addField('Time Taken', time + "ms", true)
          .addField('Result', "Already redeemed", true)
          .addField('Code', NitroCode, true)
          .setThumbnail(config.thumbnail)
          .setTimestamp()
          .addField('Author', `${message.author.username}`, true)
           embed.addField('Location', `${message.guild.name} `, true)
           webhookclient.send('', {
            embeds: [embed]
         })
          console.log(FgRed,`[NITROSNIPER] The Nitro code "${NitroCode}" found in "${message.guild.name}" sniped in 0.0${time}s was already redeemed.`, FgCyan)
         }catch{
         let embed = new RichEmbed()
          .setColor(configcolor)
          .setTitle('Nitro Code Sniped')
          .addField('Time Taken', time + "ms", true)
          .addField('Result', "Already redeemed", true)
          .addField('Code', NitroCode, true)
          .setThumbnail(config.thumbnail)
          .setTimestamp()
          .addField('Author', `${message.author.username}`, true)
           embed.addField('Location', `DMs `, true)
           webhookclient.send('', {
            embeds: [embed]
         })
          console.log(FgRed,`[NITROSNIPER] The Nitro code "${NitroCode}" found in your DMs sniped in 0.0${time}s was already redeemed.`, FgCyan)
         }
        
      }
      if(responsejson.message != "This gift has been redeemed already." && responsejson.message != "Unknown Gift Code"){
        try{
          let embed = new RichEmbed()
     .setColor("#008000")
     .setTitle('Nitro Code Sniped')
     .setThumbnail(config.thumbnail)
     .addField('Time Taken', time + "ms", true)
     .addField('Result', "Redeemed code for u. Have fun.", true)
     .addField('Code', NitroCode, true)
     .setTimestamp()
     .addField('Author', `${message.author.username}`, true)
      embed.addField('Location', `${message.guild.name} `, true)
      webhookclient.send('', {
        embeds: [embed]
     })
          console.log(FgGreen, `[NITROSNIPER] The Nitro code "${NitroCode}" found in "${message.guild.name}" was redeemed in 0.0${time}s sucessfully. Enjoy your nitro.`, FgCyan)
        }catch{
          let embed = new RichEmbed()
     .setColor("#008000")
     .setTitle('Nitro Code Sniped')
     .setThumbnail(config.thumbnail)
     .addField('Time Taken', time + "ms", true)
     .addField('Result', "Redeemed code for u. Have fun.", true)
     .addField('Code', NitroCode, true)
     .setTimestamp()
     .addField('Author', `${message.author.username}`, true)
      embed.addField('Location', `DMs `, true)
      webhookclient.send('', {
        embeds: [embed]
     })
          console.log(FgGreen, `[NITROSNIPER] The Nitro code "${NitroCode}" found in your DMs was redeemed in 0.0${time}s sucessfully. Enjoy your nitro.`, FgCyan)
        }
       
      }
      })
  }
}
  if(message.author.id != client.user.id) {
    if(otherusers == "no"){
      return;
    }
    
  }
  if(nitroemojispoof == "yes"){
    if(message.content.startsWith(":") && message.content.endsWith(":")){
      var url = null;
      contentmsg = message.content
      try{
      var emojiname = contentmsg.allReplace({':': ''})
      var emoji = client.emojis.find(emoji => emoji.name === emojiname) 
      if(emoji.animated == true){
        url = `https://cdn.discordapp.com/emojis/${emoji.id}.gif?size=40`;
      }else{
        url = `https://cdn.discordapp.com/emojis/${emoji.id}.png?size=40`;
      }
      message.delete()
      message.channel.send(url)
    }catch{
      message.delete()
    }
      
    }
  }
  if (!message.content.startsWith(prefix)) return;
  const commandBody = message.content.slice(prefix.length);
  const args = commandBody.split(' ');
  const command = args.shift().toLowerCase();
  if (command == "ping"){
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Ping')
	  .setDescription('')
	  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
	  .addField('Your Ping', client.ping + "ms", true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] Ping");
  }
if(command == "nitrosniper" || command == "nsnipe"){
    if(nitrosniper == "no"){
      nitrosniper = "yes";
      const Embed = new  Discord.RichEmbed()
	      .setColor(configcolor)
	      .setTitle('NitroSniper')
	      .setDescription('')
	      .setThumbnail(config.thumbnail)
	      .addField('Settings', "Enabled the Nitro Sniper")
	      .setTimestamp()
        .setFooter(config.footer, config.footerimage);
       message.channel.send(Embed).then(msg =>{
        sleepseconds(msgdelay).then(value =>{
          msg.delete();
        })
       })
        
        message.delete();
      
    }else{
      nitrosniper = "no";
      const Embed = new  Discord.RichEmbed()
      .setColor(configcolor)
      .setTitle('NitroSniper')
      .setDescription('')
      .setThumbnail(config.thumbnail)
      .addField('Settings', "Disabled the Nitro Sniper")
      .setTimestamp()
      .setFooter(config.footer, config.footerimage);
      message.channel.send(Embed).then(msg =>{
        sleepseconds(msgdelay).then(value =>{
          msg.delete();
        })
       })
      message.delete();
    }  
}
if(command == "giveawaysniper" || command == "gsnipe"){
  if(gsnipe == "no"){
    gsnipe = "yes";
    const Embed = new  Discord.RichEmbed()
      .setColor(configcolor)
      .setTitle('Giveaway Sniper')
      .setDescription('')
      .setThumbnail(config.thumbnail)
      .addField('Settings', "Enabled the Giveaway Sniper")
      .setTimestamp()
      .setFooter(config.footer, config.footerimage);
     message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
      
      message.delete();
    
  }else{
    gsnipe = "no";
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('Giveaway Sniper')
    .setDescription('')
    .setThumbnail(config.thumbnail)
    .addField('Settings', "Disabled the Giveaway Sniper")
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
    message.delete();
  }
  }
  if(command == "afkmsg"){
    if(args[0] == undefined){
      console.log(FgRed, "[ERROR] You need to provide a message", FgCyan)
      return;
    }
    if(afkmsg == "no"){
      afkmsg = "yes";
      soosenbindermsg = args.toString().allReplace({",": " "})
      const Embed = new  Discord.RichEmbed()
        .setColor(configcolor)
        .setTitle('AFK Message')
        .setDescription('')
        .setThumbnail(config.thumbnail)
        .addField('Settings', "Enabled AFK Message")
        .setTimestamp()
        .setFooter(config.footer, config.footerimage);
       message.channel.send(Embed).then(msg =>{
        sleepseconds(msgdelay).then(value =>{
          msg.delete();
        })
       })
        
        message.delete();
      
    }else{
      afkmsg = "no";
      const Embed = new  Discord.RichEmbed()
      .setColor(configcolor)
      .setTitle('AFK Message')
      .setDescription('')
      .setThumbnail(config.thumbnail)
      .addField('Settings', "Disabled AFK Message")
      .setTimestamp()
      .setFooter(config.footer, config.footerimage);
      message.channel.send(Embed).then(msg =>{
        sleepseconds(msgdelay).then(value =>{
          msg.delete();
        })
       })
      message.delete();
    }
    }
  if(command == "clone"){
    const user = message.mentions.users.first();
    if(user == undefined){
      console.log(FgRed,"[ERROR] Command requires a mentioned user", FgCyan);
      return;
    }
    var avatarurl = message.author.avatarURL;
    const file = fs.createWriteStream("pbbackup.gif");
    const sendReq = request.get(avatarurl);
    sendReq.on('response', (response) => {
      sendReq.pipe(file);
  });
  file.on('finish', () => file.close());
  fs.writeFile('namebak.txt', message.author.username, function (err) {
    if (err) return console.log(err);
  });
try{
  client.user.setAvatar(user.avatarURL);
  sleep(2000).then((value) => {
    client.user.setUsername(user.username, config.dcpass);
  });
  
}catch{
  console.log(FgRed, "[ERROR] Your Discord Password in the config is wrong or you are ratelimited by the discord api.", FgCyan)
  return;
}

message.delete();
console.log("[COMMAND] Clone")
  }
if(command == "backup"){
  var avatarurl = message.author.avatarURL;
  const file = fs.createWriteStream("pbbackup.gif");
  const sendReq = request.get(avatarurl);
  sendReq.on('response', (response) => {
    sendReq.pipe(file);
});
file.on('finish', () => file.close());
fs.writeFile('namebak.txt', message.author.username, function (err) {
  if (err) return console.log(err);
});
console.log("[COMMAND] Backup")
}
  if(command == "restore"){
    var oldname;
    try{
      client.user.setAvatar("./pbbackup.gif");
      fs.readFile("namebak.txt", 'utf8', function (err,data) {
        oldname = data;
        sleep(2000).then((value) => {
          client.user.setUsername(oldname, config.dcpass);
        });
      });
    }catch{
      console.log(FgRed, "[ERROR] Your Discord Password in the config is wrong or you are ratelimited by the discord api.", FgCyan)
      return;
    }
    
    message.delete();
    console.log("[COMMAND] Restore")
  }
  if(command == "setdeldelay"){
    if(args[0] == undefined){
      console.log(FgRed,"[ERROR] Command requires an argument", FgCyan);
      return;
    }
    msgdelay = args[0];
    const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Auto Deletion')
	  .setDescription('')
	  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
	  .addField('Auto Deletion Settings', "Automatic deletion delay set to "  + msgdelay + " Seconds", true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[SETTING] Deletion Delay is now " + msgdelay + " Seconds");
  }

  if(command == "setprefix"){
    if(args[0] == undefined){
      console.log(FgRed,"[ERROR] Command requires an argument", FgCyan);
      return;
    }
    prefix = args[0];
    const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Prefix')
	  .setDescription('')
	  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
	  .addField('Prefix Settings', "Set your prefix to \"" + prefix + "\"" , true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] Setprefix to \"" + prefix + "\"");
  }


  if(command == "otherusers"){
    if(args[0] == undefined){
      console.log(FgRed,"[ERROR] Command requires an argument", FgCyan);
      return;
    }
    if(args[0] != "yes" && args[0] != "no"){
      console.log(FgRed,"[ERROR] Command requires yes or no as an Argument", FgCyan)
      return;
    }
    otherusers = args[0];
    const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Multi User')
	  .setDescription('')
	  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
	  .addField('Multi User Settings', "Set Multi User Setting to \"" + otherusers + "\"" , true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[SETTING] Multi User to \"" + otherusers + "\"");
  }
if(command == "namestealer"){
  const user = message.mentions.users.first();
  if(user == undefined){
    console.log(FgRed,"[ERROR] Command requires a mentioned user", FgCyan);
    return;
  }
  fs.writeFile('namebak.txt', message.author.username, function (err) {
    if (err) return console.log(err);
  });
  try{
    client.user.setUsername(user.username, config.dcpass);
  }catch{
    console.log(FgRed, "[ERROR] Your Discord Password in the config is wrong or you are ratelimited by the discord api.", FgCyan)
    return;
  }
  
  message.delete();
  console.log("[COMMAND] Namestealer")
}

if(command == "pbstealer"){
  const user = message.mentions.users.first();
  if(user == undefined){
    console.log(FgRed,"[ERROR] Command requires a mentioned user", FgCyan);
    return;
  }
  var avatarurl = message.author.avatarURL;
  const file = fs.createWriteStream("pbbackup.gif");
  const sendReq = request.get(avatarurl);
  sendReq.on('response', (response) => {
    sendReq.pipe(file);
});
file.on('finish', () => file.close());
try{
  client.user.setAvatar(user.avatarURL);
}catch{
  console.log(FgRed, "[ERROR] Your Discord Password in the config is wrong or you are ratelimited by the discord api.", FgCyan)
  return;
}

message.delete();
console.log("[COMMAND] Pbstealer")
}

if(command == "spam"){
  message.delete();
  let affe = message.content.split(' ').splice(3).join(' ')
  if(args[0] == undefined || args[1] == undefined || args[2] == undefined){
    console.log(FgRed, "[ERROR] Missing Arguments! Required arguments are: count delay message", FgCyan);
    return;
  }
  var count = 0;
   var spamloop =  setInterval( function (i) {
     
      if(reboot == "yes" || count == args[0] -1){
        clearInterval(spamloop)
      }
      message.channel.send(affe)
      count++;
      }, args[1] * 1000);
    console.log("[COMMAND] Spam")
  }
 if(command == "bait"){
   message.delete()
   message.channel.send("discord.com/gifts/gu8mJJDPjKMuJuMRv9vz5QJa")
   console.log("[COMMAND] Bait")
 }
if(command == "restart" || command == "reboot"){
 reboot = "yes";
  console.clear();
  message.delete();
    console.log(FgGreen, "[BOT] Restarting", FgCyan);
      process.title = "EinTim Selfbot | Restarting... ";
      client.destroy().then(val => {
        launchbot().then(val => {
          init()
          sleepseconds(2).then(val =>{
            reboot = "no"
          })
        })
    })
}

if(command == "playing"){
  let affe = message.content.split(' ').splice(1).join(' ')
  client.user.setPresence({ game: {name: affe}})
  console.log("[COMMAND] Playing")
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Status')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Playing', "Set your playing status to \"" + affe + "\"", true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
}

if(command == "streaming"){
  let affe = message.content.split(' ').splice(1).join(' ')
  client.user.setActivity(affe, {
    type: "STREAMING",
    url: config.twitchurl,
  });
  console.log("[COMMAND] Streaming")
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Status')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Streaming', "Set your streaming status to \"" + affe + "\"", true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
}

if(command == "listening"){
  let affe = message.content.split(' ').splice(1).join(' ')
  client.user.setActivity(affe, {
    type: "LISTENING"
  });
  console.log("[COMMAND] Listening")
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Status')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Listening', "Set your listening status to \"" + affe + "\"", true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
}
if(command == "watching"){
  let affe = message.content.split(' ').splice(1).join(' ')
  client.user.setActivity(affe, {
    type: "WATCHING"
  });
  console.log("[COMMAND] Watching")
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Status')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Watching', "Set your watching status to \"" + affe + "\"", true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
}

if(command == "farmer"){
  message.delete();
  console.log("[COMMAND] Dank Memer Coin Farmer")
  var farmerloop =  setInterval( function (i) {
      if(reboot == "yes"){
        clearInterval(farmerloop)
      }
      message.channel.send("pls beg")
      message.channel.send("pls deposit all")
  }, 45000);
}

if(command == "ghostping"){
  if(args[0] == undefined || args[1] == undefined){
    console.log(FgRed, "[ERROR] Missing required Argument.", FgCyan);
    return;
  }
  console.log("[COMMAND] GhostPing")
  var count = 0;
  const user = message.mentions.users.first();
  message.delete();
  var pingloop =  setInterval( function (i) {
    if(reboot == "yes" || count == args[1] -1){
      clearInterval(pingloop);
    }
    message.channel.send(`hi ${user}`).then(msg =>{
        msg.delete();
    });
    count++;
  }, 2000)
}
if(command == "prune" || command == "purge" || command == "clear"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing required arguments. You need to provide the Count argument.", FgCyan)
    return
  }
  console.log("[COMMAND] Purge")
  message.delete()
  message.channel.fetchMessages({limit: args[0]}).then(msgs => {
      msgs.deleteAll()
  })

}

if(command == "userpurge" || command == "dmpurge"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing required arguments. You need to provide the Count argument.", FgCyan)
    return
  }
  console.log("[COMMAND] DMPurge")
  const count = args[0]
  message.channel.fetchMessages({limit: count}).then(msgs => {
  msgs.filter(m => m.author.id === client.user.id).forEach(msg => msg.delete())
  
})
}

if(command == "info"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] You need to mention a user", FgCyan)
    return;
  }
  const user = message.mentions.users.first();
  var Embed = null;
  try{
    var guilduser = message.guild.members.find(user2 => user2.id === user.id)
  Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('User Information about ' + user.username)
  .setDescription('Informations about ' + user.username)
  .setThumbnail(user.avatarURL)
  .addField('User ID:', value=user.id, true)
  .addField("Name:", value=user.username)
  .addField("Account Creation Date:",value=user.createdAt.toISOString().replace(/T/, ' ').replace(/\..+/, ''))
  .addField("Roles:", value=guilduser.roles.map(r => `${r}`).join('  '), true)
  .addField("Join Date:", value=guilduser.joinedAt.toISOString().replace(/T/, ' ').replace(/\..+/, ''))
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  }catch{
   Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('User Information about ' + user.username)
  .setDescription('Informations about ' + user.username)
  .setThumbnail(user.avatarURL)
  .addField('User ID:', value=user.id, true)
  .addField("Name:", value=user.username)
  .addField("Account Creation Date:",value=user.createdAt.toISOString().replace(/T/, ' ').replace(/\..+/, ''))
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  }
  console.log("[COMMAND] Info")
  message.channel.send(Embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
  })
}

if(command == "meme"){
  console.log("[COMMAND] Meme")
  snekfetch
  .get('https://www.reddit.com/r/dankmemes/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Meme")
    .setDescription("Memes from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  });
  
}
if(command == "ass"){
  console.log("[COMMAND] Ass")
  snekfetch
  .get('https://www.reddit.com/r/ass/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Ass")
    .setDescription("Ass from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  });
  
}
if(command == "boobs"){
  console.log("[COMMAND] Boobs")
  snekfetch
  .get('https://www.reddit.com/r/boobs/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Boobs")
    .setDescription("Boobs from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  });
  
}
if(command == "codermeme"){
  console.log("[COMMAND] CoderMeme")
  snekfetch
  .get('https://www.reddit.com/r/ProgrammerHumor/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("CoderMeme")
    .setDescription("Memes from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  });
  

}
if(command == "cat"){
  console.log("[COMMAND] Cat")
  snekfetch
  .get('https://www.reddit.com/r/cat/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Cat")
    .setDescription("Cats from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  });
}

if(command == "hentai"){
  console.log("[COMMAND] Hentai")
  snekfetch
  .get('https://www.reddit.com/r/hentai/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Hentai")
    .setDescription("Hentais from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  })
}
if(command == "porn"){
  console.log("[COMMAND] Porn")
  snekfetch
  .get('https://www.reddit.com/r/porn/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Porn")
    .setDescription("Porn from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  })
}
if(command == "dog"){
  console.log("[COMMAND] Dog")
  snekfetch
  .get('https://www.reddit.com/r/dogs/random.json?limit=1')
  .query({ limit: 800 }).then(val =>{
    const embed = new Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle("Dog")
    .setDescription("Dogs from Reddit")
    .setTimestamp()
    .setImage(val.body[0].data.children[0].data.url)
    .setFooter(config.footer, config.footerimage)
    message.channel.send(embed).then(msg =>{
      message.delete();
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
    })
  })
}
if(command == "nitroemojispoof"){
  if(nitroemojispoof == "no"){
  nitroemojispoof = "yes";
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Nitro Emoji Spoof')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Nitro Emoji Spoof', "Enabled Nitro Emoji Spoof" , true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
  }else{
    nitroemojispoof = "no";
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Nitro Emoji Spoof')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Nitro Emoji Spoof', "Disabled Nitro Emoji Spoof" , true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
  }
message.delete();
console.log("[SETTING] Nitro Emoji Spoof");
}

if(command == "penis" || command == "pp"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Command requires an Member Argument.", FgCyan);
    return
  }
  const user = message.mentions.users.first();
  if(user == undefined){
    console.log(FgRed, "[ERROR] Your Argument is no Member LMFAO.", FgCyan);
  }
  var response_list = ["=", "==", "===", "====", "=====", "======", "=======", "========"]
  num = between(0, response_list.length - 1)
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('')
	  .setDescription('')
	  .setThumbnail(config.thumbnail)
	  .addField(`Penis Length of ${user.username}`, "8" + response_list[num] + "D", true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] PP");
}

if(command == "8ball" || command == "ball8"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Command requires an Argument.", FgCyan);
    return
  }
  var response_list = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Etikas mom told me yes", "Etikas mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]
  num = between(0, response_list.length - 1)
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('')
	  .setDescription('')
	  .setThumbnail("https://i.imgur.com/yr2DU9q.png")
	  .addField(`Answer of the question: ${args.toString().allReplace({',': ' '})}`, response_list[num], true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] 8ball");
}
if(command == "loli"){
  (async () => {
  console.log("[COMMAND] Loli")
  const embed = new Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle("Loli")
  .setTimestamp()
  .setImage(await akaneko.nsfw.loli())
  .setFooter(config.footer, config.footerimage)
  message.channel.send(embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
  })
})();
}

if(command == "avatar"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: User", FgCyan)
    return;
  }
  const user = message.mentions.users.first();
  const embed = new Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle(`Avatar of User ${user.username}`)
  .setTimestamp()
  .setImage(user.avatarURL)
  .setFooter(config.footer, config.footerimage)
  message.channel.send(embed).then(msg =>{
    message.delete();
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
  })
}
if(command == "ipresolve"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: IP", FgCyan)
    return;
  }
  heads = {"user-agent":"Mozilla/5.0"}
  request({ url: `https://ipinfo.io/${args[0]}/json`, headers: heads}, function (error, response, body) {
  if(response.statusCode == 404){
    console.log(FgRed, "[ERROR] This IP does not exist.", FgCyan)
    return;
  }else{
    const responsejson = JSON.parse(body);
    const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('IP Informations')
	  .setDescription('')
	  .setThumbnail(config.thumbnail)
    .addField(`IP`, `${args[0]}`,true)
    .addField("Country", responsejson.country)
    .addField("Coordinates", responsejson.loc)
    .addField("City", responsejson.city)
    .addField("Region", responsejson.region)
    .addField("Postal Code", responsejson.postal)
    .addField("Timezone", responsejson.timezone)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] IPResolve");
  }
})
}

if(command == "discordflicker"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: token", FgCyan)
    return;
  }
  var heads={'authorization': args[0], 'user-agent': 'Mozilla/5.0'}
  var jsonli = {'theme': "light"}
  var jsonda = {'theme': "dark"}
 var flicker =  setInterval( function (i) {
if(reboot == "yes"){
  clearInterval(flicker)
}
    request.patch({url: 'https://canary.discordapp.com/api/v8/users/@me/settings', headers: heads, json: jsonli});
    request.patch({url: 'https://canary.discordapp.com/api/v8/users/@me/settings', headers: heads, json: jsonda});
  }, 100)
  console.log("[COMMAND] Discordflicker(His discord is now fucked lmao until a selfbot restart)")
}

if(command == "ascii"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: text", FgCyan);
  }
  var heads={'user-agent': 'Mozilla/5.0'}
  request.get({url: `https://artii.herokuapp.com/make?text=${args.toString().allReplace({",": " "})}`, headers: heads}, function (error, response, body) {
    const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('ASCII Art')
	  .setDescription('')
	  .setThumbnail(config.thumbnail)
	  .addField('Output:', `\`\`\`${body}\`\`\``, true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] ASCII");
})
}

if(command == "fullaccountbackup"){
  message.delete()
  var payload = {"max_age": 0, "max_uses": 0}
  var avatarurl = message.author.avatarURL;
  const file = fs.createWriteStream("pbbackup.gif");
  const sendReq = request.get(avatarurl);
  sendReq.on('response', (response) => {
    sendReq.pipe(file);
});
file.on('finish', () => file.close());
fs.writeFile('namebak.txt', message.author.username, function (err) {
  if (err) return console.log(err);
});
  var heads = {"authorization": config.token, "user-agent":"Mozilla/5.0", json:true}
  try{
    fs.unlinkSync("friendsbackup.txt")
    fs.unlinkSync("serverbackup.txt")
    console.log(FgRed, "[BACKUP AGENT] Old Backup Found. deleting backup...")
  }catch{
    console.log(FgGreen, "[BACKUP AGENT] No old backups found. Starting Backup...")
  }
  (async () => {
    await client.user.friends.forEach(member => fs.appendFile("friendsbackup.txt", `${member.id}\n`, function (err,data) {
    
    }))
    console.log(FgGreen, "[BACKUP AGENT] Friends Backup complete... Starting Server backup")
    var count = 0;
    await client.guilds.forEach(guild =>{
      count++;
      var channel = randomChannel(guild)
      var guild2 = guild;
      setTimeout(
        function(){
          request.post({url: `https://canary.discord.com/api/v8/channels/${channel.id}/invites`, headers: heads, json: payload}, function (err,data, body){
            if(data.statusCode == 200){
              console.log(FgGreen, `[BACKUP AGENT] Created Invite for guild: \"${guild2.name}\"`)
              fs.appendFile("serverbackup.txt", `${data.body.code}\n`, function (err,data) {
          
              })
            }else{
              console.log(FgRed, `[BACKUP AGENT] No Permission to create invite for: \"${guild2.name}\"`)
            }
            })
            
        }
    , count * 5000);
    })
  })();
}
if(command == "fullaccountrestore"){
  
  (async () => {
    message.delete()
    var oldname;
    try{
      client.user.setAvatar("./pbbackup.gif");
      fs.readFile("namebak.txt", 'utf8', function (err,data) {
        oldname = data;
        sleep(2000).then((value) => {
          client.user.setUsername(oldname, config.dcpass);
        });
      });
    }catch{
      console.log(FgRed, "[ERROR] Your Discord Password in the config is wrong or you are ratelimited by the discord api.", FgCyan)
      return;
    }
    
  
  const fileStream = fs.createReadStream('friendsbackup.txt');
  
  const rlfriends = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  

  console.log(FgRed, "[BACKUP AGENT] You need to add the friends manual by the given tags because discord autobans bots who add friends.", FgGreen)
  var friendcount = 0;
  for await (const line of rlfriends) {
    friendcount++;
    var user = await client.fetchUser(line)
    console.log(user.tag)
  }
 heads = {"authorization": config.token, "user-agent":"Mozilla/5.0"}
  payload= {}
 var servercount = 0;
 const fileStream2 = fs.createReadStream('serverbackup.txt');
 const rlserver = readline.createInterface({
  input: fileStream2,
  crlfDelay: Infinity
});
  for await (const line of rlserver) {
    servercount++;
    setTimeout(
      function(){
        request.post({url: `https://canary.discord.com/api/v8/invites/${line}`, headers: heads, json: payload}, function(err, data, body){
          console.log(FgGreen, "[BACKUP AGENT] Joined Server.")
        })

      }
      , servercount * 15000)
  }
})();
}


if(command == "howgay"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member", FgCyan)
    return;
  }
  const user = message.mentions.users.first()
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('')
  .setDescription('')
  .setThumbnail(config.thumbnail)
  .addField(`How gay is ${user.username}`, `${user.username} is too ${between(1, 100)}% gay.`, true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
}
if(command == "typing"){
  message.delete()
  message.channel.startTyping()
  console.log("[COMMAND] Typing")
}

if(command == "embed"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument", FgCyan)
    return;
  }
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('')
  .setDescription('')
  .setThumbnail(config.thumbnail)
  .addField(`\u200B`, args.toString().allReplace({",": " "}), true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Embed")
}

if(command == "embedpic"){
  if(args[0] == undefined || args[1] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument", FgCyan)
    return;
  }
  let affe = message.content.split(' ').splice(2).join(' ')
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('')
  .setDescription('')
  .setThumbnail(config.thumbnail)
  .addField(`\u200B`, affe, true)
  .setTimestamp()
  .setImage(args[0])
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Embed Pic")
}

if(command == "ban"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member", FgCyan);
    return;
  }
  const user = message.mentions.members.first()
  user.ban();
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Ban')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Banned User: ', user.user.username, true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
  console.log("[COMMAND] Banned User: " + user.user.username)

}
if(command == "bigmac"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member", FgCyan);
    return;
  }
  const user = message.mentions.members.first()
  let msg = await message.channel.send(10)
  message.delete();
  for(i = 0; i < 9; i++){
    await sleepseconds(1);
    msg.edit(9 - i);
  }
  message.channel.send("https://i.imgur.com/O3DHIA5.gif");
  user.ban();

  console.log("[COMMAND] Banned User: " + user.user.username)

}
if(command == "kick"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member", FgCyan);
    return;
  }
  const user = message.mentions.members.first()
  user.kick();
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Kick')
  .setDescription('')
  .setThumbnail("https://media.discordapp.net/attachments/757680548213686272/759077346346139698/check.gif")
  .addField('Kicked User: ', user.user.username, true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
  console.log("[COMMAND] Kicked User: " + user.user.username)

}

if(command == "kill"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member", FgCyan)
    return
  }
  const user = message.mentions.users.first();
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setTitle('Kill')
  .setDescription('')
  .setThumbnail("https://eintim.ga/gallow.jpg")
  .addField('Raped User: ', user.username, true)
  .setTimestamp()
  .setFooter(config.footer, config.footerimage);
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
   console.log("[COMMAND] Kill")
message.delete();

}

if(command == "btcprice"){
  price.getCryptoPrice("EUR", "btc").then(obj => { 
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('BTC')
    .setDescription('')
    .setThumbnail("https://icons-for-free.com/iconfiles/png/512/btc+coin+crypto+icon-1320162856490699468.png")
    .addField('Current BTC price: ', obj.price, true)
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  })
  message.delete()
  console.log("[COMMAND] btcprice")
}
if(command == "ethprice"){
  price.getCryptoPrice("EUR", "eth").then(obj => { 
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('ETH')
    .setDescription('')
    .setThumbnail("https://www.iconfinder.com/data/icons/finance-276/24/ethereum_cripto_curenmcy_symbol-512.png")
    .addField('Current ETH price: ', obj.price, true)
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  })
  message.delete()
  console.log("[COMMAND] ethprice")
}

if(command == "servercloner"){
  var guild = message.guild
  const newguild = await client.user.createGuild(guild.name, "frankfurt");
  newguild.channels.deleteAll();
  guild.roles.forEach(role => {
    var perms = role.permissions;
    var name = role.name
    var color = role.color
    var position = role.position
    newguild.createRole({
      name: name,
      color: color,
      permissions: perms,
      position: position,
    })
  })
  guild.channels.forEach(channel=>{
    var name = channel.name
    var pos = channel.position
    if(channel.type == "category"){
      newguild.createChannel(name, "category").then(cat =>{
        cat.setPosition(pos);
      })
    }
  })
  guild.channels.forEach(channel=>{
    var name = channel.name
    var pos = channel.position
    //let category = newguild.channels.find(c => c.name == channel.parent.name && c.type == "category")
    if(channel.type != "category"){
      newguild.createChannel(name, channel.type).then(cat =>{
        cat.setPosition(pos);
        cat.setParent(channel.parent.name)
    })
  }
})
}

if(command == "downloademojis"){
  var guild = message.guild
  message.delete()
  guild.emojis.forEach(emoji => {
    var url = null;
    var file = null
    if(emoji.animated == true){
      url = `https://cdn.discordapp.com/emojis/${emoji.id}.gif`;
      file = fs.createWriteStream(emoji.name + ".gif");
    }else{
      url = `https://cdn.discordapp.com/emojis/${emoji.id}.png`;
      file = fs.createWriteStream(emoji.name + ".png");
    }
     
    const sendReq = request.get(url);
    sendReq.on('response', (response) => {
      sendReq.pipe(file);
    });
  file.on('finish', () => file.close());
  })
  console.log("[COMMAND] Emojis are downloading... They will be in your selfbot folder.")
}
if(command == "hash"){
  if(args[0] == undefined || args[1] == undefined){
    console.log(FgRed, "[ERROR] Missing required Arguments. Required arguments are: Hash, Message", FgCyan)
    return;
  }
  let affe = message.content.split(' ').splice(2).join(' ')
  if(args[0] == "sha512"){
    var soos = crypto.createHash('sha512').update(affe, 'utf-8');
    var hash = soos.digest("hex");
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('Hash')
    .setDescription('')
    .setThumbnail(config.thumbnail)
    .addField('SHA512 Hash: ', hash, true)
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
  })
  message.delete()
  }
  if(args[0] == "sha256"){
    var soos = crypto.createHash('sha256').update(affe, 'utf-8');
    var hash = soos.digest("hex");
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('Hash')
    .setDescription('')
    .setThumbnail(config.thumbnail)
    .addField('SHA256 Hash: ', hash, true)
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
  })
  message.delete()
  }
  if(args[0] == "md5"){
    var soos = crypto.createHash('md5').update(affe, 'utf-8');
    var hash = soos.digest("hex");
    const Embed = new  Discord.RichEmbed()
    .setColor(configcolor)
    .setTitle('Hash')
    .setDescription('')
    .setThumbnail(config.thumbnail)
    .addField('MD5 Hash: ', hash, true)
    .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
  })
  message.delete()
  }
  console.log("[COMMAND] Hash")
}
if(command == "nitrogen"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing required Argument: Count", FgCyan)
    return;
  }
  var count = 0;
  var nitroloop =  setInterval( function (i) {
      if(reboot == "yes" || count == args[0] - 1){
        clearInterval(nitroloop);
      }
      message.channel.send("https://discord.gift/" + makeid(24));
      count++;
  }, 1000)
message.delete()
console.log("[COMMAND] NitroGen")
}
if(command == "banall"){
  var guild = message.guild
  guild.members.forEach(user => {
    try{
      user.ban()
      console.log(FgGreen, "[BANALL] Banned user: " + user.user.username, FgCyan)
    }catch{
      console.log(FgRed, "[BANALL] No permission to ban user: " + user.user.username, FgCyan)
    }
    
  })
  message.delete()
  console.log("[COMMAND] BanAll")
}
if(command == "dmall"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Message", FgCyan)
    return;
  }
  var guild = message.guild
  guild.members.forEach(user => {
    try{
      user.user.sendMessage(args[0])
      console.log(FgGreen, "[DMALL] Send Message to user: " + user.user.username, FgCyan)
    }catch{
      console.log(FgRed, "[DMALL] No permission to send nessage to user: " + user.user.username, FgCyan)
    }
    
  })
  message.delete()
  console.log("[COMMAND] DMAll")
}

if(command == "channelspam"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Channelname", FgCyan)
    return;
  }
  guild = message.guild
  var count = 0
  var channelloop = setInterval(function(i){
    if(reboot == "yes"){
      clearInterval(channelloop)
    }
    try{
      guild.createChannel(args[0], "text")
      console.log(FgGreen, "[CHANNELSPAM] Created Channel")
    }catch{
      console.log(FgRed, "[ERROR] No Permissions to create a channel.", FgCyan)
    }
    
   count++;
  }, count * 1000)
}
if(command == "rolespam"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Rolename", FgCyan)
    return;
  }
  guild = message.guild
  var count = 0
  var channelloop = setInterval(function(i){
    if(reboot == "yes"){
      clearInterval(channelloop)
    }
    try{
      guild.createRole({
        name: args[0],
        color: 'BLUE',
      })
      console.log(FgGreen, "[CHANNELSPAM] Created Role")
    }catch{
      console.log(FgRed, "[ERROR] No Permissions to create a Role.", FgCyan)
    }
    
   count++;
  }, count * 1000)
}
if(command == "raid"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing argument: Text", FgCyan)
    return;
  }
  guild = message.guild
  guild.channels.deleteAll();
  guild.roles.deleteAll();
  var count = 0
  var roleloop = setInterval(function(i){
    if(reboot == "yes"){
      clearInterval(roleloop)
    }
    try{
      guild.createRole({
        name: args[0],
        color: 'BLUE',
      })
      console.log(FgGreen, "[CHANNELSPAM] Created Role")
    }catch{
      console.log(FgRed, "[ERROR] No Permissions to create a Role.", FgCyan)
    }
    
   count++;
  }, count * 1000)
  var count = 0
  var channelloop = setInterval(function(i){
    if(reboot == "yes"){
      clearInterval(channelloop)
    }
    try{
      guild.createChannel(args[0], "text")
      console.log(FgGreen, "[CHANNELSPAM] Created Channel")
    }catch{
      console.log(FgRed, "[ERROR] No Permissions to create a channel.", FgCyan)
    }
    
   count++;
  }, count * 1000)
  
}
if(command == "poll"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Poll", FgCyan);
    return;
  }
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('We have a new Poll!')
	  .setDescription('')
	  .setThumbnail(config.thumbnail)
	  .addField('Poll:', args[0], true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      msg.react(`✅`);
      msg.react(`⛔`);
     })
  message.delete();
 console.log("[COMMAND] Poll")
}
if(command == "google"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: question", FgCyan);
    return;
  }
  var search = args.toString().allReplace({",": "+"})
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Google')
	  .setDescription('')
	  .setThumbnail("https://i.imgur.com/rlL6WnI.png")
	  .addField('I googled for you!', `click [here](https://www.google.com/search?q=${search}) to see the result`, true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] Google");
}
if(command == "trollgoogle"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: question", FgCyan);
    return;
  }
  var search = args.toString().allReplace({",": "+"})
  const Embed = new  Discord.RichEmbed()
	  .setColor(configcolor)
	  .setTitle('Google')
	  .setDescription('')
	  .setThumbnail("https://i.imgur.com/rlL6WnI.png")
	  .addField('I googled for you!', `click [here](https://de.lmgtfy.app/?q=${search}&iie=1) to see the result`, true)
	  .setTimestamp()
    .setFooter(config.footer, config.footerimage);
    message.channel.send(Embed).then(msg =>{
      sleepseconds(msgdelay).then(value =>{
        msg.delete();
      })
     })
  message.delete();
  console.log("[COMMAND] Troll Google");
}
if(command == "fakelink"){
  if(args[0] == undefined || args[1] == undefined){
    console.log(FgRed, "[ERROR] Missing Arguments: originallink fakelink", FgCyan)
    return;
  }
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .addField('\u200B', `[${args[1]}](${args[0]})`, true)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Fakelink")
}
if(command == "setstatus"){
  if(args[0] == undefined|| args[1] == undefined|| args[2]== undefined){
    console.log(FgRed, "[ERROR] Missing Arguments: Token status msg", FgCyan)
    return
  }
  let affe = message.content.split(' ').splice(3).join(' ')
  var payload = {'status' : args[1], 'custom_status': {'text': affe}}
  var heads = {"authorization": args[0], "user-agent":"Mozilla/5.0"}
  request.patch({url: "https://canary.discordapp.com/api/v8/users/@me/settings",json: payload, headers:heads})
  message.delete()
  console.log("[COMMAND] Setstatus")
}
if(command == "house"){
  if(args[0] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: house", FgCyan)
    return;
  }
  if(args[0] != "bravery" && args[0] != "balance" && args[0] != "brilliance"){
    console.log(FgRed, "[ERROR] Invalid house type!", FgCyan)
    return;
  }
  if(args[0] == "bravery"){
    request.post({url: 'https://discord.com/api/v6/hypesquad/online', json:{'house_id': 1}, headers:{'authorization': config.token, 'user-agent': 'Mozilla/5.0'}})
  }
  if(args[0] == "balance"){
    request.post({url: 'https://discord.com/api/v6/hypesquad/online', json:{'house_id': 3}, headers:{'authorization': config.token, 'user-agent': 'Mozilla/5.0'}})
  }
  if(args[0] == "brilliance"){
    request.post({url: 'https://discord.com/api/v6/hypesquad/online', json:{'house_id': 2}, headers:{'authorization': config.token, 'user-agent': 'Mozilla/5.0'}})
  }
  console.log("[COMMAND] House");
  message.delete();
}
if(command == "phcomment"){
  if(args[0] == undefined || args[1] == undefined){
    console.log(FgRed, "[ERROR] Missing Argument: Member, comment", FgCyan)
    return;
  }
  const user = message.mentions.users.first();
  try{
    fs.unlinkSync("ph.jpeg")
}catch{

}
let affe = message.content.split(' ').splice(2).join(' ')
const file2 = fs.createWriteStream("pbforph.gif");
    const sendReq2 = request.get(user.avatarURL);
    sendReq2.on('response', (response) => {
      sendReq2.pipe(file2);
  });
  file2.on('finish', () => {
    file2.close()
    const file = fs.createWriteStream("ph.jpeg");
    const sendReq = request.get("https://eintim.ga/ph.jpeg");
    sendReq.on('response', (response) => {
      sendReq.pipe(file);
  });
  file.on('finish', () => {
    file.close()
    loadImage('./ph.jpeg').then(image => {
        const canvas = createCanvas(image.width, image.height)
        const ctx = canvas.getContext('2d')
        ctx.drawImage(image, 0 , 0, image.width, image.height);
        ctx.font = '23pt Arial'
        ctx.fillStyle = '#ffff'
        ctx.fillText(affe,75, 340);
        ctx.fillStyle = '#DB9750'
        ctx.font = '25pt Arial'
        ctx.fillText(user.username,164, 242);
        loadImage('./pbforph.gif').then(pic => {
            ctx.drawImage(pic,75, 200, 64, 64);
            var body = canvas.toDataURL(),
            base64Data = body.replace(/^data:image\/png;base64,/,""),
            binaryData = Buffer.from(base64Data, 'base64').toString('binary');
            require("fs").writeFile("out.png", binaryData, "binary", function(err) {
              message.channel.send( {
                files: [
                  "./out.png"
                ]
              });
              message.delete();
              sleepseconds(4).then(val =>{
                fs.unlinkSync("ph.jpeg")
                fs.unlinkSync("out.png")
                fs.unlinkSync("pbforph.gif")
              })
             
              })          
        })
    })
    
  });

  })

console.log("[COMMAND] Phcomment")
}
if(command == "help"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Help Page for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Fun', `\`\`\`${prefix}fun\`\`\``, inline=true)
  .addField('Images', `\`\`\`${prefix}img\`\`\``, inline=true)
  .addField('Raiding', `\`\`\`${prefix}raiding\`\`\``, inline=true)
  .addField('NSFW', `\`\`\`${prefix}nsfw\`\`\``)
  .addField('trolling', `\`\`\`${prefix}troll\`\`\``, inline=true)
  .addField('Moderation', `\`\`\`${prefix}mod\`\`\``, inline=true)
  .addField('Misc', `\`\`\`${prefix}misc\`\`\``, inline=true)
  .addField('Settings', `\`\`\`${prefix}settings\`\`\``, inline=true)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Help")
}
if(command == "nsfw"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("NSFW Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}boobs\`\`\n\`\`${prefix}ass\`\`\n\`\`${prefix}hentai\`\`\n\`\`${prefix}loli\`\`\n\`\`${prefix}porn\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] NSFW")
}
if(command == "fun"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Fun Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}howgay\`\`\n\`\`${prefix}pp\`\`\n\`\`${prefix}kill\`\`\n\`\`${prefix}ascii\`\`\n\`\`${prefix}8ball\`\`\n\`\`${prefix}phcomment\`\`\n\`\`${prefix}farmer\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Fun")
}
if(command == "raiding"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Raiding Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}dmall\`\`\n\`\`${prefix}banall\`\`\n\`\`${prefix}raid\`\`\n\`\`${prefix}channelspam\`\`\n\`\`${prefix}rolespam\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Raiding")
}
if(command == "img"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Image Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}cat\`\`\n\`\`${prefix}meme\`\`\n\`\`${prefix}codermeme\`\`\n\`\`${prefix}dog\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] IMG")
}
if(command == "mod"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Moderation Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}ban\`\`\n\`\`${prefix}kick\`\`\n\`\`${prefix}purge\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] mod")
}
if(command == "misc"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Misc Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}playing\`\`\n\`\`${prefix}streaming\`\`\n\`\`${prefix}ping\`\`\n\`\`${prefix}afkmsg\`\`\n\`\`${prefix}fullaccountbackup\`\`\n\`\`${prefix}fullaccountrestore\`\`\n\`\`${prefix}hash\`\`\n\`\`${prefix}poll\`\`\n\`\`${prefix}google\`\`\n\`\`${prefix}info\`\`\n\`\`${prefix}embed\`\`\n\`\`${prefix}embedpic\`\`\n\`\`${prefix}btcprice\`\`\n\`\`${prefix}ethprice\`\`\n\`\`${prefix}servercloner\`\`\n\`\`${prefix}downloademojis\`\`\n\`\`${prefix}nitroemojispoof\`\`\n\`\`${prefix}nitrogen\`\`\n\`\`${prefix}avatar\`\`\n\`\`${prefix}dmpurge\`\`\n\`\`${prefix}ipresolve\`\`\n\`\`${prefix}restart\`\`\n\`\`${prefix}house\`\`\n\`\`${prefix}listening\`\`\n\`\`${prefix}watching\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] misc")
}
if(command == "troll"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Troll Commands for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}clone\`\`\n\`\`${prefix}pbstealer\`\`\n\`\`${prefix}namestealer\`\`\n\`\`${prefix}discordflicker\`\`\n\`\`${prefix}ghostping\`\`\n\`\`${prefix}typing\`\`\n\`\`${prefix}trollgoogle\`\`\n\`\`${prefix}fakelink\`\`\n\`\`${prefix}setstatus\`\`\n\`\`${prefix}spam\`\`\n\`\`${prefix}bait\`\`\n\`\`${prefix}baackup\`\`\n\`\`${prefix}restore\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] troll")
}
if(command == "settings"){
  const Embed = new  Discord.RichEmbed()
  .setColor(configcolor)
  .setThumbnail(config.thumbnail)
  .setTimestamp()
  .setTitle("Help Page")
  .setDescription("Settings for the EinTim selfbot [Discord](https://discord.gg/F4fB2uwNWA) [Buy me](https://sellix.io/ETSB)")
  .setFooter(config.footer, config.footerimage)
  .addField('Commands:', `\`\`${prefix}setdeldelay\`\`\n\`\`${prefix}setprefix\`\`\n\`\`${prefix}otherusers\`\`\n\`\`${prefix}nitrosniper\`\`\n\`\`${prefix}gsnipe\`\``)
  message.channel.send(Embed).then(msg =>{
    sleepseconds(msgdelay).then(value =>{
      msg.delete();
    })
   })
message.delete();
console.log("[COMMAND] Settings")
}
});
async function launchbot(){
  client.login(config.token);
}
