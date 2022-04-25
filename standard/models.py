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

# 科别标准
class SpecialtyStd(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=False)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# 应用中的标准
class AppliedStds(models.Model):
    spstd = models.OneToOneField(SpecialtyStd, related_name='applied_stds', on_delete=models.CASCADE, default=None)
    def save(self, *args, **kwargs):
        if not self.pk and AppliedStds.objects.exists():
            raise ValidationErr('There is can be only one AppliedStds instance')
        return super(AppliedStds, self).save(*args, **kwargs)


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