from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from Admission.models import Students, Fee, Bus


def home(request):
    return render(request,'index.html')

def display_all_student(request):
    qs=Students.objects.all().order_by('-admissionNumber')
    return render(request, 'Admission/table.html',context={'qs':qs})

def search(request):
    print(request.POST)
    studentClass = request.POST['Class']
    studentName = request.POST['studentName']
    fatherName = request.POST['fatherName']
    mobileNumber = request.POST['Mobile']
    if mobileNumber !='':
        qs = Students.objects.filter(mobileNumber=mobileNumber)
    elif studentName !='':
        qs = Students.objects.filter(studentName=studentName)
    elif fatherName !='':
        qs = Students.objects.filter(fatherName=fatherName)
    elif  studentClass !='':
        qs = Students.objects.filter(studentClass= studentClass)
    return render(request, 'Admission/table.html', context={'qs': qs})

def add_form(request):
    return render(request, 'Admission/saveForm.html')


def add_student(request):
    form=request.POST
    student = Students()
    student.studentName=form['studentName']
    student.studentClass=form['studentClass']
    student.studentDOB=form['studentDOB']
    student.aadharNumber=form['aadharNumber']
    student.fatherName=form['fatherName']
    student.motherName=form['motherName']
    student.mobileNumber=form['mobileNumber']
    student.studentAddress=form['studentAddress']
    student.previousSchool=form['previousSchool']
    student.previousClass=form['previousClass']
    student.image= request.FILES['image'] if request.FILES.get('image')!= None else None
    student.admissionNumber = student.getAdmissionNumber()
    try:
        student.check_aadhar_exists()
        student.check_date_format()
        student.check_validation()
        student.save()
        fee=Fee(admissionNumber=student).save()
        bus=Bus(admissionNumber=student).save()
        return redirect('allRecords')
    except ValidationError as em:
        return render(request, 'Admission/saveForm.html', context={'em':em,'s':student})

def display_student(request):
    admissionNumber = request.GET['admissionNumber']
    student = Students.objects.get(admissionNumber=admissionNumber)
    fee = Fee.objects.get(admissionNumber=admissionNumber)
    bus = Bus.objects.get(admissionNumber=admissionNumber)
    return render(request, 'Admission/display.html', context={'s': student,'f':fee,'b':bus})


def update_form(request):
    admissionNumber = request.GET['admissionNumber']
    student = Students.objects.get(admissionNumber=admissionNumber)
    fee = Fee.objects.get(admissionNumber=admissionNumber)
    bus = Bus.objects.get(admissionNumber=admissionNumber)
    return render(request,'Admission/updateForm.html',context={'s':student,'f':fee,'b':bus})

def update_student(request):
    form=request.POST
    admissionNumber=form['admissionNumber']
    student = Students.objects.get(admissionNumber=admissionNumber)
    student.studentName=form['studentName']
    student.studentClass=form['studentClass']
    student.studentDOB=form['studentDOB']
    student.aadharNumber=form['aadharNumber']
    student.fatherName=form['fatherName']
    student.motherName=form['motherName']
    student.mobileNumber=form['mobileNumber']
    student.studentAddress=form['studentAddress']
    student.previousSchool=form['previousSchool']
    student.previousClass=form['previousClass']
    if request.FILES.get('image') != None :
        student.image = request.FILES['image']
    fee = Fee.objects.get(admissionNumber=admissionNumber)
    bus = Bus.objects.get(admissionNumber=admissionNumber)
    try:
        student.check_date_format()
        student.check_validation()
        student.save()
        student = Students.objects.get(admissionNumber=admissionNumber)
        return render(request, 'Admission/display.html', context={'sm':'Student updated successfully','s':student,'f':fee,'b':bus})
    except ValidationError as em:
        return render(request, 'Admission/updateForm.html', context={'em':em,'s':student,'f':fee,'b':bus})


def delete_student(request):
    admissionNumber=request.GET['admissionNumber']
    student=Students.objects.get(admissionNumber=admissionNumber)
    student.delete()
    return redirect('allRecords')

def feePayForm(request):
    admissionNumber = request.GET['admissionNumber']
    fee = Fee.objects.get(admissionNumber=admissionNumber)
    bus = Bus.objects.get(admissionNumber=admissionNumber)
    student = Students.objects.get(admissionNumber=admissionNumber)
    return render(request, 'Admission/updateAllFee.html', context={'f':fee,'b':bus,'s':student})

def feePay(request):
    form = request.POST
    fee = Fee.objects.get(id=form['fee_id'])
    fee.annualFee=int(form['annualFee']) if  form['annualFee'] != '' else 0
    fee.januaryFee=int(form['januaryFee']) if form['januaryFee']  != '' else 0
    fee.februaryFee=int(form['februaryFee']) if form['februaryFee']  != '' else 0
    fee.marchFee = int(form['marchFee']) if form['marchFee']  != '' else 0
    fee.aprilFee = int(form['aprilFee']) if form['aprilFee']  != '' else 0
    fee.mayFee = int(form['mayFee']) if  form['mayFee'] != '' else 0
    fee.juneFee = int(form['juneFee']) if  form['juneFee'] != '' else 0
    fee.julyFee = int(form['julyFee']) if  form['julyFee'] != '' else 0
    fee.augustFee = int(form['augustFee']) if  form['augustFee'] != '' else 0
    fee.septemberFee = int(form['septemberFee']) if  form['septemberFee'] != '' else 0
    fee.octoberFee = int(form['octoberFee']) if  form['octoberFee'] != '' else 0
    fee.novemberFee = int(form['novemberFee']) if form['novemberFee']  != '' else 0
    fee.decemberFee = int(form['decemberFee']) if form['decemberFee']  != '' else 0
    fee.save()
    bus = Bus.objects.get(id=form['bus_id'])
    if form['btransport']=='True':
        bus.januaryFee = int(form['bjanuaryFee']) if form['bjanuaryFee']  != '' else 0
        bus.februaryFee = int(form['bfebruaryFee']) if  form['bfebruaryFee'] != '' else 0
        bus.marchFee = int(form['bmarchFee']) if  form['bmarchFee'] != '' else 0
        bus.aprilFee = int(form['baprilFee']) if  form['baprilFee'] != '' else 0
        bus.mayFee = int(form['bmayFee']) if  form['bmayFee'] != '' else 0
        bus.juneFee = int(form['bjuneFee']) if form['bjuneFee']  != '' else 0
        bus.julyFee = int(form['bjulyFee']) if  form['bjulyFee'] != '' else 0
        bus.augustFee = int(form['baugustFee']) if form['baugustFee']  != '' else 0
        bus.septemberFee = int(form['bseptemberFee']) if form['bseptemberFee']  != '' else 0
        bus.octoberFee = int(form['boctoberFee']) if  form['boctoberFee'] != '' else 0
        bus.novemberFee = int(form['bnovemberFee']) if  form['bnovemberFee'] != '' else 0
        bus.decemberFee = int(form['bdecemberFee']) if form['bdecemberFee']  != '' else 0
        bus.save()
    student = Students.objects.get(admissionNumber=bus.admissionNumber_id)
    return render(request, 'Admission/display.html', context={'s': student, 'f': fee, 'b': bus})

def transportMode(request):
    admissionNumber = request.GET['admissionNumber']
    id = request.GET['id']
    fee = Fee.objects.get(id=id)
    bus = Bus.objects.get(id=id)
    bus.transport = False if request.GET['transport'] == 'True' else True
    bus.save()
    student = Students.objects.get(admissionNumber=admissionNumber)
    return render(request, 'Admission/display.html', context={'s': student, 'f': fee, 'b': bus})


