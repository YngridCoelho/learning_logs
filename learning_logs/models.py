from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Topic(models.Model):
    """um assunto sobre o qual o usuario esta aprendendo"""
    """"settings.AUTH_USER_MODEL contém o nome da tabela que o Django utiliza para guardar os usuários."""
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add = True)

    # deve -se fornecer um valor default para associar o owner e o assunto ao banco de dados, neste caso, passamos o id de um ususario 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """devolve uma representação em string do modelo""" #--> docstring
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:

        verbose_name_plural = 'entries'

    def __str__(self):

        if len(self.text) < 50:
            return self.text

        else:
            return self.text[:50] + "..."
