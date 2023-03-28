
 function pass_check(){
     if(document.getElementById("pass").value==document.getElementById("confirmpass").value){
         return true;
     }
     else{
         document.getElementById("wrong-otp").style.display="flex";
         document.getElementById("wrong-otp").innerHTML="Password doesnt match!!!";
         return false
     }
 }
 function pass_show(){
     document.getElementById("pass").type="text";
     document.getElementById("hide_pass").style.display="block"
     document.getElementById("show_pass").style.display="none"
 }
 function pass_hide(){
     document.getElementById("pass").type="password";
     document.getElementById("hide_pass").style.display="none"
     document.getElementById("show_pass").style.display="block"
 }