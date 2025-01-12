from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Admission.views import display_student, display_all_student, add_student, delete_student, add_form, \
    update_form, update_student, home, feePayForm, feePay, transportMode, search

urlpatterns = [
    path('',home),
    path('allRecords/',display_all_student,name='allRecords'),
    path('search/', search),
    path('addForm/', add_form),
    path('add/',add_student),
    path('display/',display_student),
    path('delete/', delete_student),
    path('updateForm/', update_form),
    path('update/', update_student),
    path('feePayForm/', feePayForm),
    path('feePay/', feePay),
    path('transport/',transportMode),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)