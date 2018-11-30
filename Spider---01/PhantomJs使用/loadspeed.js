/* Create by Liang
   Date:2018-09-30*/


var page = require("webpage").create(),
    system = require("system"),
    t,address;

if(system.args.length === 1){
    console.log("Usage:loadspeed.js<some URL>");
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address,function (status) {
   if(status !== "success"){
       console.log("Fail to load the address");
   } else{
       t = Data.now() - t;
       console.log("Loading"+system.args[1]);
       console.log("Loading time" + t + "msec");
   }
   phantom.exit();
});
