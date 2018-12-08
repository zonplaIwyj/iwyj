$(function () {

    // 设置回到屏幕宽度
    $('.home').width(innerWidth)

    var swiper = new Swiper('#top-swiper', {
        // pagination: '.swiper-pagination',
        // paginationClickable: true,
        loop: true,
        autoplay: 2147,
    })
    var swiper = new Swiper('#mustbuySwiper', {
        // pagination: '.swiper-pagination',
        // paginationClickable: true,
        loop: true,
        autoplay: 512,
        slidesPerView:3,
        spaceBetween:9,
    })
})