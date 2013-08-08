/*
(function() {
 	var $backToTopEle = $('<!--back to the top--><div href="#" class="back_to_top"></div>').
			appendTo($("body")).
			click(function() {
	 			$("html, body").animate({ scrollTop: 0 }, 120);
	 	}),
		$backToTopFun = function() {
 			var st = $(document).scrollTop(),
			winh = $(window).height();
 			(st > 0)? $backToTopEle.show(): $backToTopEle.hide();    
			 //IE6下的定位
			 if (!window.XMLHttpRequest) {
	 				$backToTopEle.css("top", st + winh - 166);    
	 		}
	 	};
	 	$(window).bind("scroll", $backToTopFun);
 		$(function() { $backToTopFun(); });
 })();
 */
(function() {
 var $backToTopTxt = "返回顶部", $backToTopEle = $('<div class="backToTop"></div>').appendTo($("body"))
 .text($backToTopTxt).attr("title", $backToTopTxt).click(function() {
	 $("html, body").animate({ scrollTop: 0 }, 120);
	 }), $backToTopFun = function() {
 var st = $(document).scrollTop(), winh = $(window).height();
 (st > 0)? $backToTopEle.show(): $backToTopEle.hide();    
 //IE6下的定位
 if (!window.XMLHttpRequest) {
 $backToTopEle.css("top", st + winh - 166);    
 }
 };
 $(window).bind("scroll", $backToTopFun);
 $(function() { $backToTopFun(); });
 })();
