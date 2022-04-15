from django.db import models

class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = 'files'
        ordering = ['-id']

# 科别标准
class SpecialtyStd(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

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