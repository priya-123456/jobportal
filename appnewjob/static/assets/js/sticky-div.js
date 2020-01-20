function sticky_relocate() {
			    var window_top = $(window).scrollTop() ;
			    var footer_top = $(".footer").offset().top - 30;
			    var div_top = $('#sticky-anchor').offset().top;
			    var div_height = $(".sidenavbar").height();
			    var leftHeight = $('.left-container').height(); 
  
			    if (window_top + div_height > footer_top){
			        $('.sidenavbar').removeClass('stick');
			    	$('.sidenavbar').addClass('abs');
			    	 $('.right-conatainer').css('min-height', leftHeight + 'px');
			    	}
			    else if (window_top > div_top) {
			        $('.sidenavbar').addClass('stick');
			        $('.sidenavbar').removeClass('abs');
			    } else {
			        $('.sidenavbar').removeClass('stick');
			        $('.sidenavbar').removeClass('abs');
			    }
			}

			$(function () {
			    $(window).scroll(sticky_relocate);
			    sticky_relocate();
			});