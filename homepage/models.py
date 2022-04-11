from datetime import date
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django_mysql.models import ListCharField

class Homepage(models.Model):
    org_name = models.CharField(max_length=20, blank=True)
    org_code = models.CharField(max_length=20, blank=True)

    purchase_method = models.CharField(max_length=20, blank=True)
    health_card = models.CharField(max_length=20, blank=True)
    admit_cnt = models.IntegerField(default = 0, blank=True) # int
    case_num = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    birthday = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    newborn_check = models.BooleanField(default = False, blank=True) # boolean
    newborn_birth_weight = models.CharField(max_length=20, blank=True)
    newborn_admit_weight = models.CharField(max_length=20, blank=True)
    # birthplace = models.CharField(max_length=20, blank=True)
    birthplace = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    # parent_birthplace = models.CharField(max_length=20, blank=True)
    parent_birthplace = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    ethnicity = models.CharField(max_length=20, blank=True)
    id_type = models.CharField(max_length=20, blank=True)
    id_num = models.CharField(max_length=20, blank=True)

    id_card_num = models.CharField(max_length=20, blank=True)
    passport_num = models.CharField(max_length=20, blank=True)
    officer_num = models.CharField(max_length=20, blank=True)

    profession = models.CharField(max_length=20, blank=True)
    marriage_stat = models.CharField(max_length=20, blank=True)
    # present_addr1 = models.CharField(max_length=20, blank=True)
    present_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    present_addr2 = models.CharField(max_length=20, blank=True)
    present_phone = models.CharField(max_length=20, blank=True)
    present_zip = models.CharField(max_length=20, blank=True)
    registered_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    registered_addr2 = models.CharField(max_length=20, blank=True)
    registered_zip = models.CharField(max_length=20, blank=True)
    # work_addr1 = models.CharField(max_length=20, blank=True)
    work_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    work_addr2 = models.CharField(max_length=20, blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    work_zip = models.CharField(max_length=20, blank=True)
    contact_name = models.CharField(max_length=20, blank=True)
    contact_relation = models.CharField(max_length=20, blank=True)
    contact_other_description = models.CharField(max_length=20, blank=True)
    # contact_addr1 = models.CharField(max_length=20, blank=True)
    contact_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    contact_addr2 = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    admit_path = models.CharField(max_length=20, blank=True)
    admit_time = models.CharField(max_length=20, blank=True)
    # admit_specialty = models.CharField(max_length=20, blank=True)
    admit_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    admit_sickroom = models.CharField(max_length=20, blank=True)
    # trans_specialty = models.CharField(max_length=20, blank=True)
    trans_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    release_time = models.CharField(max_length=20, blank=True)
    # release_specialty = models.CharField(max_length=63, blank=True)
    release_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    release_sickroom = models.CharField(max_length=20, blank=True)
    hosp_duration = models.IntegerField(default = 0, blank=True) # int
    diagnosis = models.CharField(max_length=20, blank=True)
    disease_code = models.CharField(max_length=20, blank=True)
    # main_diagnosis 单独 model 或在serializer里用 create？

    od_release = models.CharField(max_length=20, blank=True)
    od_code = models.CharField(max_length=20, blank=True)
    od_condition = models.CharField(max_length=20, blank=True)
    # lesion_reason 单独 model 或在serializer里用 create？
    # pathology

    drug_allergy_check = models.BooleanField(default = False, blank=True) # boolean
    drug_allergy = models.CharField(max_length=20, blank=True)
    necropsy_check = models.BooleanField(default = False, blank=True) # boolean
    blood_group = models.CharField(max_length=20, blank=True)
    rh = models.CharField(max_length=20, blank=True)
    director = models.CharField(max_length=20, blank=True)
    chief = models.CharField(max_length=20, blank=True)
    physician_ic = models.CharField(max_length=20, blank=True)
    resident = models.CharField(max_length=20, blank=True)
    nurse_ic = models.CharField(max_length=20, blank=True)
    refresher = models.CharField(max_length=20, blank=True)
    trainee = models.CharField(max_length=20, blank=True)
    coder = models.CharField(max_length=20, blank=True)
    record_quality = models.CharField(max_length=20, blank=True)
    qc_doctor = models.CharField(max_length=20, blank=True)
    qc_nurse = models.CharField(max_length=20, blank=True)
    qc_date = models.CharField(max_length=20, blank=True)
    release_type = models.CharField(max_length=20, blank=True)
    accept_hosp_2 = models.CharField(max_length=20, blank=True)
    accept_hosp_3 = models.CharField(max_length=20, blank=True)
    cont_hosp_check = models.BooleanField(default = False, blank=True) #boolean
    cont_hosp_plan = models.CharField(max_length=20, blank=True)
    head_injury_check = models.BooleanField(default = False, blank=True) #boolean
 
    class Meta:
        ordering = ('org_code',)
    
    def __str__(self):
        return self.org_name

class MainDiag(models.Model):
    release = models.TextField(max_length=256, default='', blank=True)
    code = models.CharField(max_length=20, default='', blank=True)
    condition = models.CharField(max_length=20, default='', blank=True)
    homepage = models.OneToOneField(Homepage, related_name='main_diag', on_delete=models.CASCADE, default=None)

class LesionReason(models.Model):
    description = models.CharField(max_length=256, default='', blank=True)
    code = models.CharField(max_length=20, default='', blank=True)
    homepage = models.OneToOneField(Homepage, related_name='lesion_reason', on_delete=models.CASCADE, default=None)

class Pathology(models.Model):
    description = models.TextField(max_length=256, default='', blank=True)
    code = models.CharField(max_length=20, default='', blank=True)
    number = models.CharField(max_length=20, default='', blank=True)
    homepage = models.OneToOneField(Homepage, related_name='pathology', on_delete=models.CASCADE, default=None)

class PreAdmitComa(models.Model):
    days = models.IntegerField(default=0, blank=True)
    hrs = models.IntegerField(default=0, blank=True)
    mins = models.IntegerField(default=0, blank=True)
    homepage = models.OneToOneField(Homepage, related_name='pre_admit_coma', on_delete=models.CASCADE, default=None)

class PostAdmitComa(models.Model):
    days = models.IntegerField(default=0, blank=True)
    hrs = models.IntegerField(default=0, blank=True)
    mins = models.IntegerField(default=0, blank=True)
    homepage = models.OneToOneField(Homepage, related_name='post_admit_coma', on_delete=models.CASCADE, default=None)

class OtherDiag(models.Model):
    release = models.TextField(max_length=256, blank=True)
    code = models.CharField(max_length=20, blank=True)
    condition = models.CharField(max_length=20, blank=True)
    homepage = models.ForeignKey(Homepage, related_name='other_diags', on_delete=models.CASCADE)

class Op(models.Model):
    code = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=20, blank=True)
    level = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    operator = models.CharField(max_length=20, blank=True)
    assis1 = models.CharField(max_length=20, blank=True)
    assis2 = models.CharField(max_length=20, blank=True)
    # wound_healing_lvl = models.CharField(max_length=20, blank=True)
    wound_healing_lvl = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    anaesthesia_type = models.CharField(max_length=20, blank=True)
    anaesthetist = models.CharField(max_length=20, blank=True)
    homepage = models.ForeignKey(Homepage, related_name='ops', on_delete=models.CASCADE)

class Charge(models.Model):
    total = models.FloatField(default=0, blank=True)
    self_pay = models.FloatField(default=0, blank=True)
    general_service = models.FloatField(default=0, blank=True)
    general_operation = models.FloatField(default=0, blank=True)
    general_nursing = models.FloatField(default=0, blank=True)
    general_other = models.FloatField(default=0, blank=True)
    pathologic_diag = models.FloatField(default=0, blank=True)
    lab_diag = models.FloatField(default=0, blank=True)
    scan_diag = models.FloatField(default=0, blank=True)
    clinic_diag = models.FloatField(default=0, blank=True)
    non_operational = models.FloatField(default=0, blank=True)
    operational = models.FloatField(default=0, blank=True)
    clinic_physic = models.FloatField(default=0, blank=True)
    anaesthesia = models.FloatField(default=0, blank=True)
    operation = models.FloatField(default=0, blank=True)
    recover = models.FloatField(default=0, blank=True)
    traditional_treat = models.FloatField(default=0, blank=True)
    western_med = models.FloatField(default=0, blank=True)
    antibio_med = models.FloatField(default=0, blank=True)
    traditional_patent_drug = models.FloatField(default=0, blank=True)
    traditional_herb = models.FloatField(default=0, blank=True)
    blood = models.FloatField(default=0, blank=True)
    proteins = models.FloatField(default=0, blank=True)
    globulins = models.FloatField(default=0, blank=True)
    coagulation = models.FloatField(default=0, blank=True)
    cytokine = models.FloatField(default=0, blank=True)
    examine_supplies = models.FloatField(default=0, blank=True)
    treat_supplies = models.FloatField(default=0, blank=True)
    operation_supplies = models.FloatField(default=0, blank=True)
    other = models.FloatField(default=0, blank=True)

    homepage = models.OneToOneField(Homepage, related_name='charge', on_delete=models.CASCADE, default=None)

