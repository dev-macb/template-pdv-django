# Generated by Django 5.0.2 on 2024-02-16 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='img_produtos')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]
