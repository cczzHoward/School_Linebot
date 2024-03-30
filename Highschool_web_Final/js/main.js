var isOpened=true;

$(function(){
    //-----------------
    // 如果圖示被點擊
    //-----------------
    $('.header .pic').mousedown(function(){
        if(isOpened){
            //將導覽列收回
            $(this).parent().stop().animate({marginTop:-130}, {duration:400, easing:'easeOutBounce'});
            $(this).stop().animate({top:70}, {duration:400, easing:'easeOutBounce'});	
            $(this).rotate({
                angle: 0,
                animateTo:180,
                duration:1000
            });	
            	
            isOpened=false;
        }else{
            //將導覽列打開
            $(this).parent().stop().animate({marginTop:0}, {duration:400, easing:'easeOutBounce'});
            $(this).stop().animate({top:70}, {duration:400, easing:'easeOutBounce'});
            $(this).rotate({
                angle: -180,
                animateTo:0
            });				
            isOpened=true;
        }
    });
    //-----------------

    

});

