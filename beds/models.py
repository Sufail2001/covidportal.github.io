from django.db import models

# Create your models here.
# after adding all models here, execute the below commands
# python manage.py makemigrations
# python manage.py migrate
dt = (
('AL', 'Alappuzha'),
('ER', 'Ernakulam'),
('ID', 'Idukki'),
('KN', 'Kannur'),
('KS', 'Kasaragod'),
('KL', 'Kollam'),
('KT', 'Kottayam'),
('KZ', 'Kozhikode'),
('MA', 'Malappuram'),
('PL', 'Palakkad'),
('PT', 'Pathanamthitta'),
('TV', 'Thiruvananthapuram'),
('TS', 'Thrissur'),
('WA', 'Wayanad')
)
class Hospital(models.Model):
    sc = (
    ('gov', 'Government'),
    ('prv', 'Private')
    )
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=2, choices=dt)
    phone = models.CharField(max_length=12)
    sector = models.CharField(max_length=3, choices=sc)
    covid_beds = models.IntegerField()
    normal_beds = models.IntegerField()
    icu_beds = models.IntegerField()
    ventilator = models.IntegerField()

    def __str__(self):
        return self.name+" "+self.location

class Patient(models.Model):
    ct = (
    ('cv', 'Covid'),
    ('nc', 'Non-Covid')
    )
    st = (
    ('W', 'Waiting'),
    ('A', 'Admitted'),
    ('D', 'Discharged')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    aadharno = models.IntegerField()
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=2, choices=dt)
    category = models.CharField(max_length=2, choices=ct)
    status = models.CharField(max_length=2, choices=st, blank=True, default='W')

    def __str__(self):
        return self.name

class BedAllocation(models.Model):
    ct = (
    ('C', 'Covid'),
    ('N', 'Normal'),
    ('I', 'ICU'),
    ('V', 'Ventilator')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=ct)

    def __str__(self):
        return self.patient.name +" admitted on "+self.hospital.name
