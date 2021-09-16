# Generated by Django 3.2.7 on 2021-09-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('criador', models.CharField(max_length=50)),
                ('datadelancamento', models.IntegerField()),
                ('generos', models.CharField(max_length=50)),
                ('plataformas', models.CharField(max_length=50)),
                ('enredo', models.TextField()),
                ('critica', models.CharField(max_length=150)),
                ('avaliacao', models.CharField(max_length=50)),
                ('desenvolvedores', models.ManyToManyField(to='jogos.Empresa')),
                ('usuario', models.ManyToManyField(to='jogos.Usuario')),
            ],
        ),
    ]
