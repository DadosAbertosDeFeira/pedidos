# Generated by Django 3.2.6 on 2021-10-15 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('information_requests', '0002_auto_20211015_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='model_updated_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='informationrequest',
            old_name='model_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='informationrequest',
            old_name='model_updated_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='publicagency',
            old_name='model_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='publicagency',
            old_name='model_updated_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='model_created_at',
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_created_at',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='Data de criação da denúncia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
    ]
