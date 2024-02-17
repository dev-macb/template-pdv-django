from django.db import models


class Categoria(models.Model):
    titulo    = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    nome          = models.CharField(max_length=50)
    categoria     = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade    = models.FloatField()
    preco_custo   = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda   = models.DecimalField(max_digits=6, decimal_places=2)
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

    def gerar_desconto(self, desconto):
        return self.preco_venda - (self.preco_venda * desconto / 100 )
    
    def lucro(self):
        lucro = self.preco_venda - self.preco_custo
        return (lucro * 100) / self.preco_custo



class Imagem(models.Model):
    imagem     = models.ImageField(upload_to='img_produtos')
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)