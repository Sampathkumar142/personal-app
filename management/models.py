from django.db import models

# Create your models here.


class level1Work(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title



class level2Work(models.Model):
    title = models.CharField(max_length=250)
    startDate = models.DateField(null = True,blank=True)
    endDate = models.DateField(null=True,blank = True)
    description = models.TextField(null=True,blank=True)
    amount = models.IntegerField(default=0,blank=True)
    parent = models.ForeignKey(level1Work,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class relatedInformation(models.Model):
    document = models.FileField(null =True, blank =True,upload_to=f'documents/')
    level2Work = models.ForeignKey(level2Work,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "document-" + str(self.id) 


class PersonalDocument(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class RelatedDocument(models.Model):
    title = models.CharField(max_length=250)
    document = models.FileField(upload_to='personaldocuments/',null=True,blank=True)
    personaldoc = models.ForeignKey(PersonalDocument,on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "document -" + self.title