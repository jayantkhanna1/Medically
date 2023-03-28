from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from dotenv import load_dotenv
load_dotenv()
from django.core.mail import send_mail
from .models import Doctor, staff,patient
from random import randint, randrange
# import crypt
import json
from datetime import datetime
# Create your views here.
#this opens index.html with json data for comments
def index(request):
    try:
        data=open("hospital_app/static/json/comment.json")
        json_data=json.load(data)
        data.close()
        return render(request,'index.html',{"data":json_data})
    except Exception as e:
        return render(request,'error.html')
#this opens aboutus.html page
def aboutus(request):
    try:
        return render(request,'aboutus.html')
    except Exception as e:
        return render(request,'error.html')
#this opens contact us page
def contactus(request):
    try:
        return render(request,'contactus.html')
    except Exception as e:
        print(e)
        #return render(request,'error.html')
#this opens default page i.e for pages that havent yet been created
def default(request):
    try:
        return render(request,'default.html')
    except Exception as e:
        return render(request,'error.html')
#this opens login page
def login(request):
    try:
        return render(request,'login.html')
    except Exception as e:
        return render(request,'error.html')
#this adds comment from modal in index.html to json file data id=4
def commentadd(request):
    try:
        name=request.POST["name"]
        location=request.POST["location"]
        comment=request.POST['comment1']
        image=request.FILES["user_pic_comment"]
        file_name = FileSystemStorage().save("hospital_app/static/person_comments/"+image.name, image)
        team_image = FileSystemStorage().url(file_name)
        team_image = "person_comments/"+image.name
        data=open("hospital_app/static/json/comment.json")
        json_data=json.load(data)
        json_data.pop()
        dictt=[{
            "id":4,
            "name":name,
            "location":location,
            "comment":comment,
            "img":team_image
        }]
        json_data=json_data+(dictt)
        tempvar=json.dumps(json_data)
        with open ("hospital_app/static/json/comment.json","w") as outfile:
            outfile.write(tempvar)
        return redirect('index')
    except Exception as e:
        return render(request,'error.html')
#Sends mail form contact us:
def sendmail(request):
    try:
        message_name=request.POST['name']
        message_mail=request.POST['email']
        message_subject=request.POST['subject']
        message=request.POST['message']
        message="Name: "+message_name+"\n"+"Sender Email: "+message_mail+"\n"+"Subject: "+message_subject+"\n"+message
        reciever=[os.environ.get('EMAIL')]
        send_mail(message_subject,message,message_mail,reciever)
        return redirect('contactus')
    except Exception as e:
       return render(request,'error.html')
#Checks if staff member is present or not
def loginstaff(request):
    Staff_info=staff.objects.all()
    id=request.POST['staffid']
    password=request.POST['staffpass']
    for x in Staff_info:
        if(x.email==id and (password == x.password)):
            request.session['id']=x.email
            return redirect('staffpage')
    messages.info(request,'Username or Password doesnt match')
    return redirect('login')
# Loads staffpage
def staffpage(request):
    data=request.session.get('id',False)
    Staff_info=staff.objects.all()
    Patientinfo=patient.objects.all()
    for x in Staff_info:
        if x.email==data:
            return render(request,'staffpage.html',{'staffdata':x,'patientdata':Patientinfo})
    if(data) : del(request.session['id'])
    return render(request,'error.html')
#Loads forgot password for staff 
def forgotpass_staff(request):
    otp=randrange(111111,999999)
    id=request.POST["emailforgot"]
    Staff_info=staff.objects.all()
    for x in Staff_info:
        if x.email==id:
            send_mail("OTP","Your otp is= "+str(otp),os.environ.get('EMAIL'),[id])
            return render(request,"changepass_staff.html",{"staffdata":x,"otp":otp})
    return render(request,'error.html')
#Changes password for staff
def changepass_staff(request):
    try:
        id=request.POST["email"]
        password=request.POST["password"]
        fin_pass=password
        staff_pass=staff.objects.get(email=id)
        staff_pass.password=fin_pass
        staff_pass.save()
        return redirect("login")
    except Exception as e:
        return render(request,'error.html')
#book appintment
def bookappointment(request):
    try:
        sex=request.POST["sex"]
        department=request.POST["department"]
        name=request.POST["name"]
        email=request.POST["email"]
        num=request.POST["number"]
        doc_seen=False
        ailment="To be entered by doctor"
        prescription="To be entered by doctor"
        patient_info=patient.objects.create(name=name,sex=sex,email=email,phone=num,department=department,doc_seen=doc_seen,ailment=ailment,prescription=prescription)
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html')
#logs out staff
def logoutstaff(request):
    try:
        del(request.session['id'])
        return redirect('login')
    except Exception as e:
        return render(request,'error.html')
#removes patient
def remove(request):
    try:
        id=request.POST['text']
        patient.objects.filter(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html')
#edits appointment
def editappointment(request):
    try:
        id=int(request.POST['patientid'])
        patient_info=patient.objects.get(id=id)
        patient_info.name=request.POST['name']
        patient_info.sex=request.POST['sex']
        patient_info.email=request.POST['email']
        patient_info.phone=request.POST['number']
        patient_info.department=request.POST['department']
        patient_info.save()
        return redirect("staffpage")
    except Exception as e:
        return render(request,'error.html')  
#cecks if doctor exists or not
def logindoc(request):
    doctor_info=Doctor.objects.all()
    id=request.POST["docid"]
    password=request.POST["docpas"]
    for x in doctor_info:
        if(x.email==id and (password == x.password)):
            request.session['id']=x.email
            return redirect('docpage')
    messages.info(request,'Username or Password doesnt match')
    return redirect('login')
#return docpage with all data
def docpage(request):
    data=request.session.get('id',False)
    doctor_info=Doctor.objects.all()
    Staff_info=staff.objects.all()
    Patientinfo=patient.objects.all()
    for x in doctor_info:
        if x.email==data:
            return render(request,'docpage.html',{'docdata':x,'patientdata':Patientinfo,'staffdata':Staff_info})
    if(data) : del(request.session['id'])
    return render(request,'error.html')
#forgot pass doc generates otp 
def forgotpass_doc(request):
    otp=randrange(111111,999999)
    id=request.POST["emailforgot"]
    doc_info=Doctor.objects.all()
    for x in doc_info:
        if x.email==id:
            send_mail("OTP","Your otp is= "+str(otp),os.environ.get('EMAIL'),[id])
            return render(request,"changepass_doc.html",{"staffdata":x,"otp":otp})
    return render(request,'error.html')
#Changes password for staff
def changepass_doc(request):
    try:
        id=request.POST["email"]
        password=request.POST["password"]
        fin_pass=password
        doc_pass=Doctor.objects.get(email=id)
        doc_pass.password=fin_pass
        doc_pass.save()
        return redirect("login")
    except Exception as e:
        return render(request,'error.html')

def logoutdoc(request):
    try:
        del(request.session['id'])
        return redirect('login')
    except Exception as e:
        return render(request,'error.html')
def editappointment_doc(request):
    try:
        id=int(request.POST['patientid'])
        patient_info=patient.objects.get(id=id)
        patient_info.name=request.POST['name']
        patient_info.sex=request.POST['sex']
        patient_info.email=request.POST['email']
        patient_info.phone=request.POST['number']
        patient_info.department=request.POST['department']
        docseen=request.POST.get('docseen',False)
        patient_info.doc_seen=False
        if docseen =="on":
            patient_info.doc_seen=True
        patient_info.ailment=request.POST['ailment']
        patient_info.prescription=request.POST['prescription']
        patient_info.save()
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html') 
def addpatient(request):
    try:
        sex=request.POST["sex"]
        name=request.POST["name"]
        email=request.POST["email"]
        number=request.POST["number"]
        candel=False
        password=os.environ.get('PASSWORD_VIEWS')
        staff_info=staff.objects.create(name=name,sex=sex,email=email,phone=number,can_delete=candel,password=password)
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html')
def remove_staff(request):
    try:
        id=request.POST['text']
        staff.objects.filter(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html')
def edit_staff(request):
    try:
        id=int(request.POST['staffid'])
        staff_info=staff.objects.get(id=id)
        staff_info.name=request.POST['name']
        staff_info.sex=request.POST['sex']
        staff_info.email=request.POST['email']
        staff_info.phone=request.POST['number']
        staff_info.save()
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        return render(request,'error.html')  
def patientinfo(request, id, docid):
    try:
        doctor_info=Doctor.objects.get(id=int(docid))
        patient_info1=patient.objects.get(id=int(id))
        patient_info=patient.objects.filter(name=patient_info1.name)
        n=len(patient_info)
        data=open("hospital_app/static/json/patient.json")
        json_data=json.load(data)
        dictt=[]
        for x in patient_info:
            dictt=dictt+[{
                "id":x.id
            }]
        json_data=(dictt)
        tempvar=json.dumps(json_data)
        with open ("hospital_app/static/json/patient.json","w") as outfile:
            outfile.write(tempvar)
        return render(request,'patientinfo.html',{'patientinfo':patient_info,'docname':doctor_info,'patientname':patient_info1.name,'len':n})
    except Exception as e:
        return render(request,'error.html')  