# Generated by Django 3.1.7 on 2021-07-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210728_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='employee_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='is_accountant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_administrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_dos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_head',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_lab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_librarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_nurse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_secretary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
