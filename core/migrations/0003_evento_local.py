# Generated by Django 4.0.4 on 2022-05-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.TextField(default='Local não definido', max_length=100, null=True),
        ),
    ]
