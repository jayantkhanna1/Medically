$(document).ready(function(){
    $("#input-searchbar").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#table-body tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  $(document).ready(function(){
    $("#input-searchbar-remove").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#table-body-remove tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  $(document).ready(function(){
    $("#input-searchbar-remove-staff").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#table-body-remove-staff tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  $(document).ready(function(){
    $("#searchbar_staff").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#table-body-staff tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
function edit(id,name,sex,email,phone,department,docseen){
      document.getElementById("appointment_id_edit").value=id;
      document.getElementById("appointment_name_edit").value=name;
      document.getElementById("appointment_department_edit").value=sex;
      document.getElementById("appointment_email_edit").value=email;
      document.getElementById("appointment_number_edit").value=phone;
      document.getElementById("appointment_doctor_edit").value=department;
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
function edit_staff(id,name,sex,email,phone){
    document.getElementById("edit_staff_id").value=id;
    document.getElementById("edit_staff_name").value=name;
    document.getElementById("edit_staff_sex").value=sex;
    document.getElementById("edit_staff_email").value=email;
    document.getElementById("edit_staff_number").value=phone;  
}
function show_patient(){
    $(document).ready(function(){
      $("#staff_mid_data").fadeOut(1);
      $("#mid_data").fadeIn(500);
  })
}
function show_staff(){
  $(document).ready(function(){
    $("#mid_data").fadeOut(1);
    $("#staff_mid_data").fadeIn(500);
})
}