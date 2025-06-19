from django.db import models

class Configuration(models.Model):
    configurationId = models.CharField(max_length=100, unique=True)
    array = models.JSONField()
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.configurationId





# from django.db import models

# # Create your models here.
# from djongo import models

# class Configuration(models.Model):
#     _id = models.ObjectIdField()
#     configurationId = models.CharField(max_length=100, unique=True)
#     array = models.JSONField()
#     remark = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.configurationId