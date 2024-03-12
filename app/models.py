from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural ="Cidade"

    def __str__(self):
        return f'{self.nome}'
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    email= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural ="Usuario"

    def __str__(self):
        return f'{self.nome , self.cpf , self.email}'
    
class Genero(models.Model):
    nome= models.CharField(max_length=100)
   
    class Meta:
        verbose_name_plural ="Genero"

    def __str__(self):
        return f'{self.nome}'

class Editora(models.Model):
    nome= models.CharField(max_length=100)
    site= models.CharField(max_length=100)
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="Editora"

    def __str__(self):
        return f'{self.nome , self.site, self.cidade}'

class Autor(models.Model):
    nome= models.CharField(max_length=100)
    cidade= models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural ="Autor"

    def __str__(self):
        return f'{self.nome , self.cidade}'
    
class Livro(models.Model):
    nome= models.CharField(max_length=100)
    preco= models.DecimalField(max_digits=10, decimal_places=2)
    datapublicacao= models.DateField()
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero= models.ForeignKey(Genero, on_delete=models.CASCADE)
    editora= models.ForeignKey(Editora, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="Livro"

    def __str__(self):
        return f'{self.nome, self.preco, self.datapublicacao, self.autor, self.genero, self.editora}'

class Emprestimo(models.Model):
    dataemprestimo= models.DateField()
    datedevolucao= models.DateField()
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro= models.ForeignKey(livro, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="Emprestimo"

    def __str__(self):
        return f'{self.dataemprestimo, self.datedevolucao, self.usuario, self.livro}'