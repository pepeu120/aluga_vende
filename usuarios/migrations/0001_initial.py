# Generated by Django 4.2.3 on 2023-07-20 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('CPF', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd_suites', models.IntegerField()),
                ('qtd_quartos', models.IntegerField()),
                ('qtd_banheiros', models.IntegerField()),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=30)),
                ('bairro', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('cidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
                ('descricao', models.TextField()),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
