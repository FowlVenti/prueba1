from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class tasks(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    project=models.ForeignKey(project, on_delete=models.CASCADE)
    done =models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + ' - '  + self.project.name
