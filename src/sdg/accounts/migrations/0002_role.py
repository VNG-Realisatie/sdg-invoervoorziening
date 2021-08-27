# Generated by Django 2.2.24 on 2021-08-27 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210827_1612'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_beheerder', models.BooleanField(default=False, help_text='Designates whether this user is a manager. ', verbose_name='beheerder')),
                ('is_redacteur', models.BooleanField(default=False, help_text='Designates whether this user can edit the reference texts. ', verbose_name='redacteur')),
                ('lokale_overheid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.LokaleOverheid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
