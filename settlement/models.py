from datetime import date
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from typing import List
from django.db import models
from django_mysql.models import ListCharField
from django.contrib.postgres.fields import ArrayField
from homepage.models import Homepage

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
    age = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    age_in_day = models.IntegerField(default=0, blank=True) #
    ethnicity = models.CharField(max_length=20, blank=True)
    id_type = models.CharField(max_length=20, blank=True)
    id_card_num = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=20, blank=True)
    present_addr1 = ListCharField(
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
    newborn_admit_type = models.CharField(max_length=20, blank=True) #
    newborn_birth_weight = models.FloatField(default=0.0, blank=True)
    newborn_admit_weight = models.FloatField(default=0.0, blank=True)
    diag_specialty = models.ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3*21),
        default=None
    ) #
    diag_date = models.CharField(max_length=20, blank=True) #
    # diag_info - Diags
    hosp_reason = models.CharField(max_length=20, blank=True) #
    admit_path = models.CharField(max_length=20, blank=True)
    heal_type = models.CharField(max_length=20, blank=True) #
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
    hosp_duration = models.CharField(max_length=20, blank=True)
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
    diag_cnt = models.IntegerField(default = 0, blank=True)
    # main_ops
    # other_ops
    op_cnt = models.IntegerField(default=0, blank=True)
    # ventilator_duration
    head_injury_check = models.BooleanField(default=False, blank=True)
    # pre_admit_coma
    # post_admit_coma
    # CU_usage
    release_type = models.CharField(max_length=20, blank=True)
    cont_hosp_check = models.BooleanField(default=False, blank=True)
    cont_hosp_plan = models.CharField(max_length=20, blank=True)
    
    physician_name = models.CharField(max_length=20, blank=True)
    nurse_ic_name = models.CharField(max_length=20, blank=True)
    class Meta:
        ordering = ('org_code',)
    def __str__(self):
        return self.org_name

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
    disease_name = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    op_name = models.CharField(max_length=20, default='', blank=True)
    op_code = models.CharField(max_length=20, default='', blank=True)
    settlement = models.ForeignKey(Settlement, related_name='diag_info', on_delete=models.CASCADE)

class WesterRelease(models.Model):
    settlement = models.OneToOneField(Settlement, related_name='western_release', on_delete=models.CASCADE)
class TraditionalRelease(models.Model):
    settlement = models.OneToOneField(Settlement, related_name='traditional_release', on_delete=models.CASCADE)

class MainDiag(models.Model): # 赋予WesternRelease
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    western_release = models.ForeignKey(WesterRelease, related_name='main_diag', on_delete=models.CASCADE)
class OtherDiag(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    western_release = models.ForeignKey(WesterRelease, related_name='other_diag', on_delete=models.CASCADE)

class MainDisease(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    traditional_release = models.ForeignKey(TraditionalRelease, related_name='main_disease', on_delete=models.CASCADE)
class OtherSymp(models.Model):
    diag = models.CharField(max_length=20, default='', blank=True)
    disease_code = models.CharField(max_length=20, default='', blank=True)
    admit_condition = models.CharField(max_length=20, default='', blank=True)
    traditional_release = models.ForeignKey(TraditionalRelease, related_name='other_symp', on_delete=models.CASCADE)

class CUUsage(models.Model):
    CU_type = models.CharField(max_length=20, default='', blank=True)
    time = models.CharField(max_length=20, default='', blank=True)
    total_hr = models.IntegerField(default = 0, blank=True)
    total_min = models.IntegerField(default = 0, blank=True)