function change(id){
    //changing comment
        temp_comment=document.getElementById("testimonials_data_para_comment").innerHTML;
        document.getElementById("testimonials_data_para_comment").innerHTML=document.getElementById("other_comment_testimonial_"+id).innerHTML;
        document.getElementById("other_comment_testimonial_"+id).innerHTML=temp_comment;
    //changing name
        temp_name=document.getElementById("name_of_person_name").innerHTML;
        document.getElementById("name_of_person_name").innerHTML=document.getElementById("other_names_testimonial_"+id).innerHTML;
        document.getElementById("other_names_testimonial_"+id).innerHTML=temp_name;
    //changing location
        temp_location=document.getElementById("name_of_person_location").innerHTML;
        document.getElementById("name_of_person_location").innerHTML=document.getElementById("other_location_testimonial_"+id).innerHTML;
        document.getElementById("other_location_testimonial_"+id).innerHTML=temp_location;
    //changing image 
        temp=(document.getElementById("other_pics_testimonial_"+id).src).replace("\"","");
        document.getElementById("other_pics_testimonial_"+id).src=(document.getElementById("main_pic_testimonial_img").src).replace("\"","");
        document.getElementById("main_pic_testimonial_img").src=temp;

}