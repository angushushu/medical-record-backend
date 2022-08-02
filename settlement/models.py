from datetime import date
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from typing import List
from django.db import models
from django_mysql.models import ListCharField
from django.contrib.postgres.fields import ArrayField
from homepage.models import Homepage
import settlement

class Settlement(models.Model):
    homepage = models.OneToOneField(Homepage, primary_key=True, related_name='settlement', on_delete=models.CASCADE, default=None, blank=True)
    list_sn = models.CharField(max_length=20, blank=True)
    org_name = models.CharField(max_length=20, blank=True)
    org_code = models.CharField(max_length=20, blank=True)
    settlement_lvl = models.CharField(max_length=20, blank=True) # 表示不从homepage同步
    settlement_num = models.CharField(max_length=20, blank=True) #
    case_num = models.CharField(max_length=20, blank=True)
    report_time = models.CharField(max_length=20, blank=True) #
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    birthday = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    age_in_day = models.IntegerField(default=0, blank=True) #
    ethnicity = models.CharField(max_length=20, blank=True)
    id_type = models.CharField(max_length=20, blank=True)
    id_card_num = models.CharField(max_length=20, blank=True)
    passport_num = models.CharField(max_length=20, blank=True)
    officer_num = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=20, blank=True)
    present_addr1 = ListCharField( ##
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    present_addr2 = models.CharField(max_length=20, blank=True)
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
    contact_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    contact_addr2 = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    settlement_type = models.CharField(max_length=20, blank=True) #
    special_person_type = models.CharField(max_length=20, blank=True) #
    settlement_loc = models.CharField(max_length=20, blank=True) #
    newborn_check = models.BooleanField(default=False, blank=True)
    newborn_admit_type = models.JSONField(null=True, default=dict, blank=True) #
    newborn_birth_weight = models.FloatField(default=0.0, blank=True)
    newborn_admit_weight = models.FloatField(default=0.0, blank=True)
    diag_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3*21),
        default=None
    ) #
    diag_date = models.CharField(max_length=20, blank=True) #
    # diag_info - DiagInfos
    hosp_reason = models.CharField(max_length=20, blank=True) #
    admit_path = models.CharField(max_length=20, blank=True)
    heal_type = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    admit_time = models.CharField(max_length=20, blank=True) #
    admit_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    trans_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    release_time = models.CharField(max_length=20, blank=True)
    release_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    hosp_duration = models.IntegerField(default=0, blank=True)
    w_emergency_diag = ListCharField(
        base_field=models.CharField(max_length=64, blank=True, default=None),
        max_length=(50 * 65), # 是否应用listcharfield，将有数量限制
        default=None,
    )
    t_emergency_diag = ListCharField(
        base_field=models.CharField(max_length=64, blank=True, default=None),
        max_length=(50 * 65), # 是否应用listcharfield，将有数量限制
        default=None,
    )
    w_disease_code = models.CharField(max_length=20, blank=True)
    t_disease_code = models.CharField(max_length=20, blank=True)
    # western release
    # traditional release
    diag_cnt = models.IntegerField(default=0, blank=True)
    # main_ops
    # other_ops
    op_cnt = models.IntegerField(default=0, blank=True)
    # ventilator_duration
    head_injury_check = models.BooleanField(default=False, blank=True)
    # pre_admit_coma
    # post_admit_coma
    # CU_usage
    # transfusion
    special_care_days = models.IntegerField(default=0, blank=True)
    l1_care_days = models.IntegerField(default=0, blank=True)
    l2_care_days = models.IntegerField(default=0, blank=True)
    l3_care_days = models.IntegerField(default=0, blank=True)
    release_type = models.CharField(max_length=20, blank=True)
    accept_hosp_2 = models.CharField(max_length=20, blank=True)
    accept_hosp_3 = models.CharField(max_length=20, blank=True)
    cont_hosp_check = models.BooleanField(default=False, blank=True)
    cont_hosp_plan = models.CharField(max_length=20, blank=True)
    
    physician_name = models.CharField(max_length=20, blank=True)
    physician_code = models.CharField(max_length=20, blank=True)
    nurse_ic_name = models.CharField(max_length=20, blank=True)
    nurse_ic_code = models.CharField(max_length=20, blank=True)
    biz_sn = models.CharField(max_length=20, blank=True)
    bill_code = models.CharField(max_length=20, blank=True)
    bill_num = models.CharField(max_length=20, blank=True)
    settle_duration = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    # bed_fee
    # diag_fee
    # exam_fee
    # lab_test_fee
    # treat_fee
    # op_fee
    # nursing_fee
    # med_material_fee
    # western_med_fee
    # traditional_tablet_fee
    # traditional_patent_fee
    # general_diag_fee
    # registration_fee
    # other_fee
    # special_fee
    # total_fee
    insurance_pay = models.FloatField(default=0.0, blank=True)
    staff_subsidy = models.FloatField(default=0.0, blank=True)
    residence_insurance = models.FloatField(default=0.0, blank=True)
    public_servant_subsidy = models.FloatField(default=0.0, blank=True)
    health_aid_pay = models.FloatField(default=0.0, blank=True)
    enterprise_supp = models.FloatField(default=0.0, blank=True)
    biz_insurance = models.FloatField(default=0.0, blank=True)
    partial_self_purchase = models.FloatField(default=0.0, blank=True)
    self_purchase = models.FloatField(default=0.0, blank=True)
    account_pay = models.FloatField(default=0.0, blank=True)
    cash_pay = models.FloatField(default=0.0, blank=True)
    payment_type = models.CharField(max_length=20, default='', blank=True)
    designated_med_report_unit = models.CharField(max_length=20, default='', blank=True)
    designated_med_report_person = models.CharField(max_length=20, default='', blank=True)
    health_insurance_org = models.CharField(max_length=20, default='', blank=True)
    health_insurance_org_code = models.CharField(max_length=20, default='', blank=True)
    health_insurance_person = models.CharField(max_length=20, default='', blank=True)
    health_insurance_person_code = models.CharField(max_length=20, default='', blank=True)
    class Meta:
        ordering = ('org_code',)
    def __str__(self):
        return self.org_name

# class NewBornAdmitType(models.Model): # 考虑到选项数量不定，用这种方式
#     value = models.CharField(max_length=20, blank=True)
#     settlement = models.ForeignKey(Settlement, related_name='newborn_admit_type', on_delete=models.CASCADE, default=None)

class VentilatorDuration(models.Model):
    days = models.IntegerField(default=0, blank=True)
    hrs = models.IntegerField(default=0, blank=True)
    mins = models.IntegerField(default=0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='ventilator_duration', on_delete=models.CASCADE, default=None)

class PreAdmitComa(models.Model):
    days = models.IntegerField(default=0, blank=True)
    hrs = models.IntegerField(default=0, blank=True)
    mins = models.IntegerField(default=0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='pre_admit_coma', on_delete=models.CASCADE, default=None)

class PostAdmitComa(models.Model):
    days = models.IntegerField(default=0, blank=True)
    hrs = models.IntegerField(default=0, blank=True)
    mins = models.IntegerField(default=0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='post_admit_coma', on_delete=models.CASCADE, default=None)

class MainOp(models.Model):
    name = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=20, blank=True)
    anaesthesia_type = models.CharField(max_length=20, blank=True)
    operator_name = models.CharField(max_length=20, blank=True)
    operator_code = models.CharField(max_length=20, blank=True)
    anaesthetist_name = models.CharField(max_length=20, blank=True)
    anaesthetist_code = models.CharField(max_length=20, blank=True)
    # op_time = models.CharField(max_length=20, blank=True)
    op_time = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    # anaesthesia_time = models.CharField(max_length=20, blank=True)
    anaesthesia_time = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )

    settlement = models.ForeignKey(Settlement, related_name='main_ops', on_delete=models.CASCADE)

class OtherOp(models.Model):
    name = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=20, blank=True)
    anaesthesia_type = models.CharField(max_length=20, blank=True)
    operator_name = models.CharField(max_length=20, blank=True)
    operator_code = models.CharField(max_length=20, blank=True)
    anaesthetist_name = models.CharField(max_length=20, blank=True)
    anaesthetist_code = models.CharField(max_length=20, blank=True)
    # op_time = models.CharField(max_length=20, blank=True)
    op_time = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    # anaesthesia_time = models.CharField(max_length=20, blank=True)
    anaesthesia_time = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    settlement = models.ForeignKey(Settlement, related_name='other_ops', on_delete=models.CASCADE)

class DiagInfo(models.Model):
    disease_name = models.CharField(max_length=20, blank=True)
    disease_code = models.CharField(max_length=20, blank=True)
    op_name = models.CharField(max_length=20, blank=True)
    op_code = models.CharField(max_length=20, blank=True)
    settlement = models.ForeignKey(Settlement, related_name='diag_info', on_delete=models.CASCADE)
    @classmethod
    def create(cls, settlement, **validated_data):
        print('@DiagInfo.create()')
        diag_info = cls(settlement = settlement,\
            disease_name = validated_data['disease_name'],\
            disease_code = validated_data['disease_code'],\
            op_name = validated_data['op_name'],\
            op_code = validated_data['op_code'])
        # do something with the book
        return diag_info

class WesternRelease(models.Model):
    settlement = models.OneToOneField(Settlement, related_name='western_release', on_delete=models.CASCADE)
class TraditionalRelease(models.Model):
    settlement = models.OneToOneField(Settlement, related_name='traditional_release', on_delete=models.CASCADE)

class MainDiag(models.Model): # 赋予WesternRelease
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    # western_release = models.ForeignKey(WesternRelease, related_name='main_diag', on_delete=models.CASCADE)
    western_release = models.OneToOneField(WesternRelease, related_name='main_diag', on_delete=models.CASCADE)
class OtherDiag(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    western_release = models.ForeignKey(WesternRelease, related_name='other_diags', on_delete=models.CASCADE)

class MainDisease(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    # traditional_release = models.ForeignKey(TraditionalRelease, related_name='main_disease', on_delete=models.CASCADE)
    traditional_release = models.OneToOneField(TraditionalRelease, related_name='main_disease', on_delete=models.CASCADE)
class MainSymp(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    traditional_release = models.ForeignKey(TraditionalRelease, related_name='main_symps', on_delete=models.CASCADE)

class CUUsage(models.Model):
    CU_type = models.CharField(max_length=20, default='', blank=True)
    time = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    total_hr = models.IntegerField(default = 0, blank=True)
    total_min = models.IntegerField(default = 0, blank=True)
    settlement = models.ForeignKey(Settlement, related_name='CU_usage', on_delete=models.CASCADE)

class Transfusion(models.Model):
    blood_type = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=2,
        max_length=(2 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
    blood_volume = models.IntegerField(default = 0, blank=True)
    volume_unit = models.CharField(max_length=20, default='', blank=True)
    settlement = models.ForeignKey(Settlement, related_name='transfusion', on_delete=models.CASCADE)

class BedFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='bed_fee', on_delete=models.CASCADE)
class DiagFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='diag_fee', on_delete=models.CASCADE)
class ExamFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='exam_fee', on_delete=models.CASCADE)
class LabTestFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='lab_test_fee', on_delete=models.CASCADE)
class TreatFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='treat_fee', on_delete=models.CASCADE)
class OpFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='op_fee', on_delete=models.CASCADE)
class NursingFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='nursing_fee', on_delete=models.CASCADE)
class MedMaterialFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='med_material_fee', on_delete=models.CASCADE)
class WesternMedFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='western_med_fee', on_delete=models.CASCADE)
class TraditionalTabletFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='traditional_tablet_fee', on_delete=models.CASCADE)
class TraditionalPatentFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='traditional_patent_fee', on_delete=models.CASCADE)
class GeneralDiagFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='general_diag_fee', on_delete=models.CASCADE)
class RegistrationFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='registration_fee', on_delete=models.CASCADE)
class OtherFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='other_fee', on_delete=models.CASCADE)
class SpecialFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='special_fee', on_delete=models.CASCADE)
class TotalFee(models.Model):
    amount = models.FloatField(default=0.0, blank=True)
    A = models.FloatField(default=0.0, blank=True)
    B = models.FloatField(default=0.0, blank=True)
    self_pay = models.FloatField(default=0.0, blank=True)
    other = models.FloatField(default=0.0, blank=True)
    settlement = models.OneToOneField(Settlement, related_name='total_fee', on_delete=models.CASCADE)