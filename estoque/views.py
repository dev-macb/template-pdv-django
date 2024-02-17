from django.shortcuts import render, HttpResponse
from PIL import Image
from datetime import date
from .models import Produto, Categoria, Imagem
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def novo_produto(request):
    if request.method == 'POST':
        imagens     = request.FILES.getlist('imagens')
        nome        = request.POST.get('nome')
        categoria   = request.POST.get('categoria')
        quantidade  = request.POST.get('quantidade')
        preco_custo = request.POST.get('preco_custo')
        preco_venda = request.POST.get('preco_venda')

        novo_produto = Produto(
            nome         = nome,
            categoria_id = categoria,
            quantidade   = quantidade,
            preco_custo  = preco_custo,
            preco_venda  = preco_venda
        )
        novo_produto.save()

        for arquivo in imagens:
            saida = BytesIO()
            nome_arquivo = f'{date.today()}_{novo_produto.id}.jpg'
            
            img = Image.open(arquivo)
            img.convert('RGB')
            img.resize((300, 300))
            img.save(saida, format='JPEG', qualit=100)
            saida.seek(0)
            img_temporaria = InMemoryUploadedFile(
                saida, 
                'ImageField', 
                nome_arquivo, 
                'image/jpeg', 
                sys.getsizeof(saida), 
                None
            )
            
            imagem = Imagem(imagem=img_temporaria, id_produto=novo_produto)
            imagem.save()


    categorias = Categoria.objects.all()
    return render(request, 'novo_produto.html', {'categorias': categorias})