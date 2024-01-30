function checkAlpha(string){
    for(let i=0;i<string.length;i++){
        if(!((string.charAt(i)>='A' && string.charAt(i)<='Z') || (string.charAt(i)>='a' && string.charAt(i)<='z'))){
            alert('The Firstname and Last should only contain letters');
            return false;
        }
    }   
    return true;
}

function checkUsername(string){
    for(let i=0;i<email.length-10;i++){
        if(!((string.charAt(i)>='A' && string.charAt(i)<='Z') || 
        (string.charAt(i)>='a' && string.charAt(i)<='z') || 
        (string.charAt(i)>='0' && string.charAt(i)<='9') ||
        (string.charAt(i)=='_') ||
        (string.charAt(i)==' ')))
            return true
    }
    return true;
}

function checkPassword(string){
    if(string.length<8){
        alert('The password must contain 8 charaters minimum');
        return false;
    }
    else{
        var charsp=0;
        var charcap=0;
        var charsmall=0;
        var charnum=0
        for(let i=0;i<string.length;i++){
            if(string.charAt(i)>='A' && string.charAt(i)<='Z')
                charcap=charcap+1;
            else if(string.charAt(i)>='a' && string.charAt(i)<='z')
                charsmall=charsmall+1;
            else if(string.charAt(i)>='0' && string.charAt(i)<='9') 
                charnum=charnum+1;
            else 
                charsp=charsp+1;
        }

        if(charcap === 0){
            alert('Password must contain minimum 1 Capital letter');
            return false;
        }
        else if(charsmall === 0){
            alert('Password must contain minimum 1 small letter');
            return false;
        }
        else if(charsp === 0){
            alert('Password must contain minimum 1 special charater(@,#,$,%,^,&,....');
            return false;
        }
        else if(charnum === 0){
            alert('Password must contain minimum 1 number(0,1,2,3....');
            return false;
        }
        else
            return true;
    }
}
function authentication(){
    const firstname= document.getElementById('firstname').value;
    const lastname= document.getElementById('lastname').value;
    const username= document.getElementById('username').value;
    const password= document.getElementById('password').value;

    const fullname=firstname+lastname

    const checnked_fullname=checkAlpha(fullname);
    const checked_username=checkUsername(username);
    const checked_password=checkPassword(password)

    const ans=(checnked_fullname && checked_username && checked_password)

    return ans;
}
