$(function(){

    //greensock basic setting
    gsap.registerPlugin(ScrollTrigger);

    var delay=0;
    var dur=1.5;
    var tp ="100%";
    
    // green_sock
    function green_sock(){

        // transform set because.. css not..
        gsap.set(".ani_tb",{y:-100,opacity:0})
        gsap.set(".ani_tb2",{y:-50,opacity:0})
        gsap.set(".ani_rl",{x:100,opacity:0})
        gsap.set(".ani_rl2",{x:50,opacity:0})
        gsap.set(".ani_bt",{y:100,opacity:0})
        gsap.set(".ani_bt2",{y:50,opacity:0})
        gsap.set(".ani_lr",{x:-100,opacity:0})
        gsap.set(".ani_lr2",{x:-50,opacity:0})
        
        gsap.set(".ani_opa",{opacity:0})

        // ani_tb ~ ani_opa set
        gsap.utils.toArray(".ani_tb").forEach(function(entry) {    
            delay = $(entry).attr('data-delay');
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            } 
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }         
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, y: 0 });
        });

        gsap.utils.toArray(".ani_rl").forEach(function(entry) {
            delay = $(entry).attr('data-delay');   
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }      
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }     
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, x: 0 });
        });

        gsap.utils.toArray(".ani_bt").forEach(function(entry) {
            delay = $(entry).attr('data-delay');            
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }  
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,                    
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay, duration: dur, opacity: 1, y: 0 });
        });

        gsap.utils.toArray(".ani_lr").forEach(function(entry) {
            delay = $(entry).attr('data-delay');   
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }  
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }         
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }            
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, x: 0 });
        });

        // ani_tb ~ ani_opa set
        gsap.utils.toArray(".ani_tb2").forEach(function(entry) {    
            delay = $(entry).attr('data-delay');
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            } 
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }         
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, y: 0 });
        });

        gsap.utils.toArray(".ani_rl2").forEach(function(entry) {
            delay = $(entry).attr('data-delay');   
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }      
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }     
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, x: 0 });
        });

        gsap.utils.toArray(".ani_bt2").forEach(function(entry) {
            delay = $(entry).attr('data-delay');            
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }  
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,                    
                    start: "top "+tp
                }
            });
            tl.to(entry, { delay:delay, duration: dur, opacity: 1, y: 0 });
        });

        gsap.utils.toArray(".ani_lr2").forEach(function(entry) {
            delay = $(entry).attr('data-delay');   
            if($(entry).attr('data-dur')){
                dur = $(entry).attr('data-dur');
            }  
            if($(entry).attr('data-tp')){
                tp = $(entry).attr('data-tp');
            }         
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }            
            });
            tl.to(entry, { delay:delay,duration: dur, opacity: 1, x: 0 });
        });
    
            
        //height 0~100
        var height1 = gsap.utils.toArray(".ani_height1"); 

        height1.forEach(function(entry) {
            var tl = gsap.timeline({
                scrollTrigger: {
                    trigger: entry,
                    start: "top "+tp
                }
            });
            tl.to(entry, {
                duration: 1.5,
                height: 0
            });
        });        
    }
    // green_sock
    



    green_sock();

});
