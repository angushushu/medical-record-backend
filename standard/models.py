from xml.dom import ValidationErr
from django.db import models

import os
from django.dispatch import receiver

class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads')

    class Meta:
        db_table = 'files'
        ordering = ['-id']

@receiver(models.signals.post_delete, sender=UploadModel)
def auto_delete_file_delte(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

# 通用标准目录
class GStd(models.Model):
    name = models.CharField(max_length=255, unique=False)
    class Type(models.TextChoices):
        NATIONALITY = 'NATIONALITY'
        ETHNICITY = 'ETHNICITY'
        IDTYPE = 'IDTYPE'
        PROFESSION = 'PROFESSION'
        GENDER = 'GENDER'
        MARRIAGESTAT = 'MARRIAGESTAT'
        SETTLEMENTTYPE = 'SETTLEMENTTYPE'
        CONTACTRELATION = 'CONTACTRELATION'
        SPECIALPERSONTYPE = 'SPECIALPERSONTYPE'
        NEWBORNADMITTYPE = 'NEWBORNADMITTYPE'
        HOSPREASON = 'HOSPREASON'
        HEALTYPE = 'HEALTYPE'
        ADMITPATH = 'ADMITPATH'
        ANAESTHESIATYPE = 'ANAESTHESIATYPE'
        CUTYPE = 'CUTYPE'
        BLOODTYPE = 'BLOODTYPE'
        PAYMENTTYPE = 'PAYMENTTYPE'
        PURCHASEMETHOD = 'PURCHASEMETHOD'
        ADMITCONDITION = 'ADMITCONDITION'
        BLOODGROUP = 'BLOODGROUP'
        RH = 'RH'
        RECORDQUALITY = 'RECORDQUALITY'
        OPLVL = 'OPLVL'
        # WOUNDHEALINGLVL = 'WOUNDHEALINGLVL' # should be 2 layers
        RELEASETYPE = 'RELEASETYPE'
    type = models.CharField(
        max_length=32,
        choices=Type.choices,
        default=Type.NATIONALITY,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# 两层的通用标准目录
class G2Std(models.Model):
    name = models.CharField(max_length=255, unique=False)
    class Type(models.TextChoices):
        HEALTYPE = 'HEALTYPE'
        BLOODTYPE = 'BLOODTYPE'
        WOUNDHEALINGLVL = 'WOUNDHEALINGLVL'
    type = models.CharField(
        max_length=32,
        choices=Type.choices,
        default=Type.HEALTYPE,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# 科别标准
class SpecialtyStd(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=False)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# 诊断标准
class DiagStd(models.Model):
    name = models.CharField(max_length=255, unique=False)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# 应用中的通用标准
class AppliedGStds(models.Model):
    nationality_std = models.ForeignKey(GStd, related_name='applied_nationality_std', on_delete=models.SET_NULL, null=True, blank=True)
    ethnicity_std = models.ForeignKey(GStd, related_name='applied_ethnicity_std', on_delete=models.SET_NULL, null=True, blank=True)
    id_type_std = models.ForeignKey(GStd, related_name='applied_id_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    profession_std = models.ForeignKey(GStd, related_name='applied_profession_std', on_delete=models.SET_NULL, null=True, blank=True)
    gender_std = models.ForeignKey(GStd, related_name='applied_gender_std', on_delete=models.SET_NULL, null=True, blank=True)
    marriage_stat_std = models.ForeignKey(GStd, related_name='applied_marriage_stat_std', on_delete=models.SET_NULL, null=True, blank=True)
    settlemenet_type_std = models.ForeignKey(GStd, related_name='applied_settlement_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    contact_relation_std = models.ForeignKey(GStd, related_name='applied_contact_relation_std', on_delete=models.SET_NULL, null=True, blank=True)
    special_person_type_std = models.ForeignKey(GStd, related_name='applied_special_person_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    newborn_admit_type_std = models.ForeignKey(GStd, related_name='applied_newborn_admit_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    hosp_reason_std = models.ForeignKey(GStd, related_name='applied_reason_std', on_delete=models.SET_NULL, null=True, blank=True)
    # heal_type_std = models.ForeignKey(GStd, related_name='applied_heal_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    admit_path_std = models.ForeignKey(GStd, related_name='applied_applied_admit_path_std', on_delete=models.SET_NULL, null=True, blank=True)
    anaesthesia_type_std = models.ForeignKey(GStd, related_name='applied_anaesthesia_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    cu_type_std = models.ForeignKey(GStd, related_name='applied_cu_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    # blood_type_std = models.ForeignKey(GStd, related_name='applied_blood_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    payment_type_std = models.ForeignKey(GStd, related_name='applied_payment_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    purchase_method_std = models.ForeignKey(GStd, related_name='applied_purchase_method_std', on_delete=models.SET_NULL, null=True, blank=True)
    admit_condition_std = models.ForeignKey(GStd, related_name='applied_admit_condition_std', on_delete=models.SET_NULL, null=True, blank=True)
    blood_group_std = models.ForeignKey(GStd, related_name='applied_blood_group_std', on_delete=models.SET_NULL, null=True, blank=True)
    rh_std = models.ForeignKey(GStd, related_name='applied_rh_std', on_delete=models.SET_NULL, null=True, blank=True)
    record_quality_std = models.ForeignKey(GStd, related_name='applied_record_quality_std', on_delete=models.SET_NULL, null=True, blank=True)
    op_lvl_std = models.ForeignKey(GStd, related_name='applied_op_lvl_std', on_delete=models.SET_NULL, null=True, blank=True)
    # wound_healing_lvl_std = models.ForeignKey(GStd, related_name='applied_wound_healing_lvl_std', on_delete=models.SET_NULL, null=True, blank=True)
    release_type_std = models.ForeignKey(GStd, related_name='applied_release_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk and AppliedGStds.objects.exists():
            raise ValidationErr('There can only be one AppliedGStd instance')
        return super(AppliedGStds, self).save(*args, **kwargs)

# 应用中的二层通用标准
class AppliedG2Stds(models.Model):
    heal_type_std = models.ForeignKey(G2Std, related_name='applied_heal_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    blood_type_std = models.ForeignKey(G2Std, related_name='applied_blood_type_std', on_delete=models.SET_NULL, null=True, blank=True)
    wound_healing_lvl_std = models.ForeignKey(G2Std, related_name='applied_wound_healing_lvl_std', on_delete=models.SET_NULL, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.pk and AppliedG2Stds.objects.exists():
            raise ValidationErr('There can only be one AppliedG2Std instance')
        return super(AppliedG2Stds, self).save(*args, **kwargs)

# 应用中的科别标准
class AppliedSpStd(models.Model):
    spstd = models.OneToOneField(SpecialtyStd, related_name='applied_spstd', on_delete=models.CASCADE, default=None,)
    def save(self, *args, **kwargs):
        if not self.pk and AppliedSpStd.objects.exists():
            raise ValidationErr('There can only be one AppliedSpStd instance')
        return super(AppliedSpStd, self).save(*args, **kwargs)
# 应用中的诊断标准
class AppliedDgStd(models.Model):
    dgstd = models.OneToOneField(DiagStd, related_name='applied_dgstd', on_delete=models.CASCADE, default=None,)
    def save(self, *args, **kwargs):
        if not self.pk and AppliedDgStd.objects.exists():
            raise ValidationErr('There can only be one AppliedDgStd instance')
        return super(AppliedDgStd, self).save(*args, **kwargs)

# 通用一级目录
class General1(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    g2std = models.ForeignKey(G2Std, related_name='general1', on_delete=models.CASCADE)

    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.value
# 通用二级目录
class General2(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    general1 = models.ForeignKey(General1, related_name='general2', on_delete=models.CASCADE)

    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.value

# 科别一级目录
class Specialty1(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    description = models.TextField(max_length=256, default='', blank=True)
    specialtystd = models.ForeignKey(SpecialtyStd, related_name='specialty1', on_delete=models.CASCADE)

    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.value

# 科别二级目录
class Specialty2(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    description = models.TextField(max_length=256, default='', blank=True)
    specialty1 = models.ForeignKey(Specialty1, related_name='specialty2', on_delete=models.CASCADE)
    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.value

# 科别三级目录
class Specialty3(models.Model):
    value = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    description = models.TextField(max_length=256, default='', blank=True)
    specialty2 = models.ForeignKey(Specialty2, related_name='specialty3', on_delete=models.CASCADE)
    class Meta:
        ordering = ('value',)
    def __str__(self):
        return self.value

# 诊断目录
class Diag(models.Model):
    code = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=64, default='', blank=True)
    pinyin = models.CharField(max_length=256, default='', blank=True)
    pinyin_cap = models.CharField(max_length=256, default='', blank=True)
    description = models.TextField(max_length=256, default='', blank=True)
    diagstd = models.ForeignKey(DiagStd, related_name='diag', on_delete=models.CASCADE)

    class Meta:
        ordering = ('code',)
    def __str__(self):
        return self.code

# 通用目录
class General(models.Model):
    code = models.CharField(max_length=32, default='', blank=True)
    label = models.CharField(max_length=32, default='', blank=True)
    gstd = models.ForeignKey(GStd, related_name='general', on_delete=models.CASCADE)
