var clickType = "click";
if ("ontouchstart" in document.documentElement) {
    clickType = "touchstart";
}
// $(function () {
//     $(window).bind("resize",function(){
//       var w=$(this).width();
//       if(w<1600){
//         var ratio=w /1600;
//       }else{
//         var ratio=1;
//       }
//       console.log(w);
//       $('body>section').css({'transform':'scale('+ratio+')'})
//     }).trigger("resize");
// })
