$(function () {
    // docuemnt >> font-size: 16px
    // 320px屏幕下: 1rem  >> 16px

    // 400px屏幕下: 1rem  >> ?

    document.documentElement.style.fontSize = innerWidth / 320 * 16 + 'px'
})