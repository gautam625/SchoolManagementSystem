from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class Students(models.Model):
    admissionNumber=models.CharField(max_length=50,primary_key=True)
    studentName=models.CharField(max_length=50)
    studentClass=models.CharField(max_length=10,blank=True, null=True)
    studentDOB = models.DateField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    aadharNumber=models.CharField(max_length=50,blank=True, null=True,default=None)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50,blank=True, null=True)
    currentDateTime=models.DateTimeField(auto_now_add=True)
    studentAddress=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=10)
    previousSchool=models.CharField(max_length=50,blank=True, null=True)
    previousClass=models.CharField(max_length=20,blank=True, null=True)

    def getAdmissionNumber(self):
        year = datetime.now().year
        year=year%100
        try :
            admissionNumber = Students.objects.all().order_by('-admissionNumber').first().admissionNumber
            return f'BPM-{year}-{str(int(admissionNumber[7:])+1).zfill(4)}'
        except AttributeError:
            return f'BPM-{year}-{str(1).zfill(4)}'


    def check_date_format(self):
        try:
            datetime.strptime(self.studentDOB,"%Y-%m-%d")
        except ValueError:
            self.studentDOB=datetime.strptime(self.studentDOB,"%d-%m-%Y").strftime('%Y-%m-%d')


    def check_validation(self):
        if 10 < len(self.mobileNumber) > 10:
            raise ValidationError("Mobile number must be 10 digit")

        if self.studentName == '':
            raise ValidationError("Student name can not be Empty")

        if 0 != len(self.aadharNumber) and len(self.aadharNumber) != 12:
            raise ValidationError("Aadhar number must contain 12 Digit")


    def check_aadhar_exists(self):
        if self.aadharNumber=='':pass
        elif Students.objects.filter(aadharNumber=self.aadharNumber).exists():
            raise ValidationError("Aadhar number is already there")



class Fee(models.Model):
    admissionNumber = models.ForeignKey(Students, on_delete=models.CASCADE)
    annualFee=models.IntegerField(default=0)
    januaryFee=models.IntegerField(default=0)
    februaryFee = models.IntegerField(default=0)
    marchFee = models.IntegerField(default=0)
    aprilFee = models.IntegerField(default=0)
    mayFee = models.IntegerField(default=0)
    juneFee = models.IntegerField(default=0)
    julyFee = models.IntegerField(default=0)
    augustFee = models.IntegerField(default=0)
    septemberFee = models.IntegerField(default=0)
    octoberFee = models.IntegerField(default=0)
    novemberFee = models.IntegerField(default=0)
    decemberFee = models.IntegerField(default=0)

class Bus(models.Model):
    admissionNumber = models.ForeignKey(Students, on_delete=models.CASCADE)
    transport = models.BooleanField(default=False)
    januaryFee=models.IntegerField(default=0)
    februaryFee = models.IntegerField(default=0)
    marchFee = models.IntegerField(default=0)
    aprilFee = models.IntegerField(default=0)
    mayFee = models.IntegerField(default=0)
    juneFee = models.IntegerField(default=0)
    julyFee = models.IntegerField(default=0)
    augustFee = models.IntegerField(default=0)
    septemberFee = models.IntegerField(default=0)
    octoberFee = models.IntegerField(default=0)
    novemberFee = models.IntegerField(default=0)
    decemberFee = models.IntegerField(default=0)
