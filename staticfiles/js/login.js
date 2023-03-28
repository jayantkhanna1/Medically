function fill_doc(){
    document.getElementById("docid").value="demo@doctor.com"
    document.getElementById("docpass").value="demodoc123"
}
function fill_staff(){
    document.getElementById("staffid").value="demo@staff.com"
    document.getElementById("staffpass").value="demostaff123"
}
function show_staff(){
    $(document).ready(function(){
        $("#login-staff").fadeIn(500);
        $("#login-doc").fadeOut(1);
    })
}
function show_doc(){
    $(document).ready(function(){
        $("#login-staff").fadeOut(1);
        $("#login-doc").fadeIn(500);
    })
}
function change_tab(id){
    for(var i=1;i<=5;i+=1){
        if(i!=id){
            document.getElementById("link-tab-"+i).style.color="#404040";
            // document.getElementById("link-tab-"+i).style.backgroundColor="#eaf1f3";
            document.getElementById("link-tab-"+i).style.backgroundImage="none"
            $("#tab-info-"+i).fadeOut(2)
        }
        else{
            document.getElementById("link-tab-"+i).style.color="white";
            document.getElementById("link-tab-"+i).style.backgroundImage="linear-gradient(270deg, rgb(50, 200, 250) 0%, rgb(88, 125, 228) 100%)";
            $("#tab-info-"+i).fadeIn(400);
            document.getElementById("tab-info-"+i).style.display="flex";
        }
    }
    
}
function pass_show_doc(){
    document.getElementById("docpass").type="text";
    document.getElementById("hide_pass_doc").style.display="block"
    document.getElementById("show_pass_doc").style.display="none"
}
function pass_hide_doc(){
    document.getElementById("docpass").type="password";
    document.getElementById("hide_pass_doc").style.display="none"
    document.getElementById("show_pass_doc").style.display="block"
}

function pass_show_staff(){
    document.getElementById("staffpass").type="text";
    document.getElementById("hide_pass_staff").style.display="block"
    document.getElementById("show_pass_staff").style.display="none"
}
function pass_hide_staff(){
    document.getElementById("staffpass").type="password";
    document.getElementById("hide_pass_staff").style.display="none"
    document.getElementById("show_pass_staff").style.display="block"
}