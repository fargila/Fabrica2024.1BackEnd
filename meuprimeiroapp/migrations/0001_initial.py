# Generated by Django 4.2.11 on 2024-03-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=20, verbose_name='Meu primeiro nome')),
                ('segundo_nome', models.CharField(max_length=25, verbose_name='Meu segundo nome')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Minha idade')),
            ],
        ),
    ]
