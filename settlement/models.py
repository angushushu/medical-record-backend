from datetime import date
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django_mysql.models import ListCharField
from homepage.models import Homepage

class Settlement(models.Model):
    homepage = models.OneToOneField(Homepage, primary_key=True, related_name='settlement', on_delete=models.CASCADE, default=None, blank=True)
    list_sn = models.CharField(max_length=20, blank=True)
    org_name = models.CharField(max_length=20, blank=True)
    org_code = models.CharField(max_length=20, blank=True)

    case_num = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    ethnicity = models.CharField(max_length=20, blank=True)
    id_type = models.CharField(max_length=20, blank=True)
    id_card_num = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=20, blank=True)
    # present_addr1 = models.CharField(max_length=20, blank=True)
    present_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    present_addr2 = models.CharField(max_length=20, blank=True)
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
    # contact_addr1 = models.CharField(max_length=20, blank=True)
    contact_addr1 = ListCharField(
        base_field=models.CharField(max_length=20, blank=True, default=None),
        size=3,
        max_length=(3 * 21),
        default=None,
    )
    contact_addr2 = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    newborn_birth_weight = models.FloatField(default=0.0, blank=True)
    newborn_admit_weight = models.FloatField(default=0.0, blank=True)
    admit_path = models.CharField(max_length=20, blank=True)
    # admit_specialty = models.CharField(max_length=20, blank=True)
    admit_specialty = ListCharField(
        base_field=models.CharField(max_length=20, blank=True),
        size=3,
        max_length=(3 * 21),  # 3 * 20 character nominals, plus commas
        default=None,
    )
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
    hosp_duration = models.CharField(max_length=20, blank=True)
    head_injury_check = models.BooleanField(default=False, blank=True)
    release_type = models.CharField(max_length=20, blank=True)
    cont_hosp_check = models.BooleanField(default=False, blank=True)
    cont_hosp_plan = models.CharField(max_length=20, blank=True)
    
    physician_name = models.CharField(max_length=20, blank=True)
    nurse_ic_name = models.CharField(max_length=20, blank=True)
    class Meta:
        ordering = ('org_code',)
    def __str__(self):
        return self.org_name

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