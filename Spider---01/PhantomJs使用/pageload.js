/* Create by Liang 
   Date:2018-09-30*/

var page = require("webpage").create();
page.open("http://www.cnblogs.com/qiyeboy/",function (status) {
   console.log("Status:"+status);
   if(status === "success"){
       page.render("qiye.png");
   }
   phantom.exit();
});
