from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    def __str__(self):
        return self.title 
class Team_member(models.Model):
    name = models.CharField(max_length=50)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        return self.name