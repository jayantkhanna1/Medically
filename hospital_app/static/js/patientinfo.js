function change_view(id){
    var myArr
    var xmlhttp = new XMLHttpRequest();
    var url = "static/json/patient.json";
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myArr = JSON.parse(this.responseText);
            for(var i=0;i<myArr.length;i++)
            {
                if(parseInt(myArr[i].id)!=parseInt(id)){
                    document.getElementById(myArr[i].id).style.backgroundImage="none";
                    document.getElementById(myArr[i].id).style.color="rgb(64, 64, 64)";
                    document.getElementById("main-"+myArr[i].id).style.display="none";
                }
                else{
                    document.getElementById(myArr[i].id).style.backgroundImage="linear-gradient(270deg, rgb(50, 200, 250) 0%, rgb(88, 125, 228) 100%)";
                    document.getElementById(myArr[i].id).style.color="white";
                    document.getElementById("main-"+myArr[i].id).style.display="block";
                
                }
            }
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
    
}
function edit(id,name,sex,email,phone,department,docseen){
    document.getElementById("appointment_id_edit").value=id;
    document.getElementById("appointment_name_edit").value=name;
    document.getElementById("appointment_department_edit").value=sex;
    document.getElementById("appointment_email_edit").value=email;
    document.getElementById("appointment_number_edit").value=phone;
    document.getElementById("appointment_doctor_edit").value=department;
    console.log(docseen)
    if(docseen=="True")
    {
        document.getElementById("docseen").style.display="none";
        document.getElementById("docseen_label").style.display="none";
    }
    if(docseen=="False")
    {
        document.getElementById("docseen").style.display="inline-block";
        document.getElementById("docseen_label").style.display="inline-block";
    }
}
$(document).ready(function(){
    $("#searchbar").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $(".dates_a").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });