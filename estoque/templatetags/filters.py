from django import template
from estoque.models import Imagem

register = template.Library()

@register.filter(name='obter_img_produto')
def obter_img_produto(produto):
    imagem = Imagem.objects.filter(id_produto=produto).first()
    if imagem:
        return imagem.imagem.url
    
    return False