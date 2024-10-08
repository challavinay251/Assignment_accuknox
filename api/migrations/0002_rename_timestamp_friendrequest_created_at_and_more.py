# Generated by Django 5.1 on 2024-08-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='to_user',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='from_user',
            new_name='sender',
        ),
        migrations.AlterUniqueTogether(
            name='friendrequest',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
