const pic = document.querySelector(".pic")
// 图像鼠标跟随
console.log(pic)
document.onmousemove=function(e){
    const that = this
    var x = e.clientX
    var y = e.clientY
    pic.style.left=x+5+"px"
    pic.style.top=y-50+"px"
}
try{
    const loginsec = document.querySelector('.login-section')
    const loginlink = document.querySelector('.login-link')
    const registerlink = document.querySelector('.register-link')
    registerlink.addEventListener('click',()=>{
        loginsec.classList.add('active')
    })
    loginlink.addEventListener('click',()=>{
        loginsec.classList.remove('active')
    })
}catch(error){
    console.error(error);
};