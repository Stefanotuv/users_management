from django.db import models
from django.urls import reverse
from datetime import date, datetime
import sys
from users.models import User
# Create your models here.

def get_model_class(select_table):
    model_class = getattr(sys.modules[__name__], select_table)
    return model_class

class DocFile(models.Model):
    file = models.FileField(upload_to='documents/', blank=True, null=True, default='None')

    def __str__(self):
        return '%s' % (self.file)

    def name(self):
        pass

class Project(models.Model):

    # status = created (basic info), started (file uploaded), reviewed (checks done), final (submitted for reivew)

    STATUS = (
            ('created', 'created'),
            ('started', 'started'),
            ('reviewed', 'reviewed'),
            ('final', 'final'),
    )
    owner = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=True, blank=True, choices=STATUS)
    project_name = models.CharField(max_length=254, null=True, blank=True)
    user = models.CharField(max_length=254, null=True, blank=True)
    # input_documents = models.ManyToManyField(DocFile,null=True,blank=True)
    input_documents = models.ForeignKey(DocFile, null=True, blank=True,on_delete=models.CASCADE)
    json_document = models.JSONField(null=True,)
    created = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s' % (self.pk)

    def get_absolute_url(self):
        return reverse('project_review_view', kwargs={'pk': self.pk})


# all the data tables with the constraints to run the analysis

class Constraints(models.Model):
    pass

class Nationality(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)

class JobTitle(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)

class Company(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)

class ProfessionalCategory(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)

class JobFunction(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)

class GMATScore(models.Model):
    min = models.IntegerField()
    max = models.IntegerField()

class TableFieldsMandatory(models.Model):
    value = models.CharField(max_length=254, null=True, blank=True)
    pass