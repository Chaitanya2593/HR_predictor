from django.db import models


class dl_model(models.Model):
    dl_model_text = models.CharField(max_length=200, default=1)


    def __str__(self):
        return self.dl_model_text

class satisfaction_level(models.Model):
     satisfaction_level = models.CharField(max_length=200)
     def __str__(self):
        return self.satisfaction_level

class last_evaluation(models.Model):
    last_evaluation = models.CharField(max_length=200)
    def __str__(self):
        return self.last_evaluation
    
class number_project(models.Model):
    number_project = models.CharField(max_length=200)
    def __str__(self):
        return self.number_project
    
class average_montly_hours(models.Model):
    average_montly_hours = models.CharField(max_length=200)
    def __str__(self):
        return self.average_montly_hours
    
class time_spend_company(models.Model):
    time_spend_company = models.CharField(max_length=200)
    def __str__(self):
        return self.time_spend_company
    
