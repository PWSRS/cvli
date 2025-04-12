INTERVALO_CHOICES = [
    ('00-02', '00-02'),
    ('02-04', '02-04'),
    ('04-06', '04-06'),
    ('06-08', '06-08'),
    ('08-10', '08-10'),
    ('10-12', '10-12'),
    ('12-14', '12-14'),
    ('14-16', '14-16'),
    ('16-18', '16-18'),
    ('18-20', '18-20'),
    ('20-22', '20-22'),
    ('22-00', '22-00'),
]


class Intervalo(models.Model):
    descricao = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.descricao

# na classe
class Ocorrencia(models.Model):
    # outros campos...
    intervalo = models.ForeignKey(Intervalo, on_delete=models.SET_NULL, null=True, blank=True)