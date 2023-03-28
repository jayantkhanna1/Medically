from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="index"),
    path('aboutus', views.aboutus,name="aboutus"),
    path('home', views.index,name="home"),
    path('commentadd', views.commentadd,name="commentadd"),
    path('default', views.default,name="default"),
    path('contactus', views.contactus,name="contactus"),
    path('sendmail', views.sendmail,name="sendmail"),
    path('login', views.login,name="login"),
    path('loginstaff', views.loginstaff,name="loginstaff"),
    path('forgotpass_staff', views.forgotpass_staff,name="forgotpass_staff"),
    path('changepass_staff', views.changepass_staff,name="changepass_staff"),
    path('staffpage', views.staffpage,name="staffpage"),
    path('bookappointment', views.bookappointment,name="bookappointment"),
    path('logoutstaff', views.logoutstaff,name="logoutstaff"),
    path('logoutdoc', views.logoutdoc,name="logoutdoc"),
    path('remove', views.remove, name='remove'),
    path('editappointment', views.editappointment, name='editappointment'),
    path('editappointment_doc', views.editappointment_doc, name='editappointment_doc'),
    path('logindoc', views.logindoc, name='logindoc'),
    path('docpage', views.docpage,name="docpage"),
    path('forgotpass_doc', views.forgotpass_doc,name="forgotpass_doc"),
    path('changepass_doc', views.changepass_doc,name="changepass_doc"),
    path('addpatient', views.addpatient,name="addpatient"),
    path('remove_staff', views.remove_staff,name="remove_staff"),
    path('edit_staff', views.edit_staff,name="edit_staff"),
    path('<id> <docid>', views.patientinfo,name="patientinfo"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)