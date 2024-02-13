function Click(event, name){
    // document.body.style.filter='blur(10px)'
    // event.className='animation-container'
    event.target.className='animation-container'
    document.getElementById(name).className='show'
}

function Close(event, name){
    document.getElementById(name).className='hidden'
    document.getElementById(event.target.name).className='main-container'
}