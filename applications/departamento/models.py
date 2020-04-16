from django.db import models

# Create your models here, blank_True -> el campo permite espacios o null=True
# str(self.id) el id es entero str permite un string
# editable=False -> bloquea el uso de ese campo

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True, null=True)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name') 

    def __str__(self):
        return str(self.id) + ' ' + self.name + '-' + self.shor_name

