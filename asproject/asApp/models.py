from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Request(models.Model):
    type = (
        ('plumbing','Plumbing'),
        ('electric','Electric'),
        ('painting','Painting'),
        ('deep cleaning','Deep Cleaning'),
    )

    gk = (
        ('rj','Rajasthan'),
        ('kr','Karnataka'),
        ('bi','Bihar'),
        ('guj','Gujrat'),
        ('maharashtra','Maharashtra'),
        ('goa','Goa'),
        ('sikkim','Sikkim'),
        ('bang','Banglore'),
    )
    Request_Type = models.CharField(choices=type,max_length=15)
    Request_Desc = models.CharField(max_length=150)
    Request_Date = models.DateTimeField(default=timezone.now)
    City = models.CharField(max_length=20)
    State = models.CharField(choices=gk,max_length=20)
    Pin_Code = models.IntegerField()
    Alternate_Phone_N = models.IntegerField()

    def __str__(self):
        return self.Request_Type

class Update(models.Model):
    status = (
        ('Pending','pending'),
        ('In Progress','in progress'),
        ('Completed','completed')
    )
    Status = models.CharField(choices=status,max_length=15)
    #request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)
    Remark = models.CharField(max_length=150)

    def __str__(self):
        return self.Status





