let logo=document.getElementById('logo')
logo.addEventListener('click', ()=>{
    window.location.href='http://127.0.0.1:4545/home'
})
function Search(e){
    const search=e.target.value.toUpperCase();
    const items=document.getElementById('mini-main')
    const product=document.querySelectorAll(".main-container")
    const pname=items.getElementsByTagName("h2");
    for(var i=0;i<pname.length;i++){
        let match=pname[i];
        if(match){
            let textValue=match.innerHTML
            if(textValue.toUpperCase().indexOf(search)>-1){
                product[i].style.display=""
                document.getElementById('main-container').style.display="none"
            }
            else{
                product[i].style.display="none"
                document.getElementById('main-container').style.display="none"
            }
            if(search===""){
                document.getElementById('main-container').style.display=""
            }
        }
    }
}