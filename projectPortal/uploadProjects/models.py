from django.db import models

class College(models.Model):
    name = models.CharField(max_length=300)

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.SET_NULL)

class Domain(models.Model):
    domain = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=500)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.SET_NULL)
    #do we store the project files in a zip archive here or shall we store it in some third party cloud and just store the link
    project_zip = models.FileField()
