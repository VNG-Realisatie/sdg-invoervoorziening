# # Generated by Django 2.2.24 on 2022-01-22 15:24

# from django.db import migrations, models
# import django.db.models.deletion
# import sdg.core.models.validators


# class Migration(migrations.Migration):

#     dependencies = [
#         ('organisaties', '0015_auto_20220122_1516'),
#     ]

#     operations = [
#         migrations.AlterModelOptions(
#             name='locatie',
#             options={'verbose_name': 'locatie', 'verbose_name_plural': 'locaties'},
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='land',
#             field=models.CharField(help_text='Het land van de locatie.', max_length=128, verbose_name='land'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='lokale_overheid',
#             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locaties', to='organisaties.LokaleOverheid', verbose_name='lokale overheid'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='naam',
#             field=models.CharField(help_text='De naam van de locatie.', max_length=40, verbose_name='naam'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='nummer',
#             field=models.PositiveIntegerField(help_text='Het huisnummer van de locatie.', verbose_name='nummer'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='plaats',
#             field=models.CharField(help_text='De plaatsnaam van de locatie.', max_length=256, verbose_name='plaats'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='postcode',
#             field=models.CharField(help_text='De postcode van de locatie.', max_length=6, validators=[sdg.core.models.validators.validate_postcode], verbose_name='postcode'),
#         ),
#         migrations.AlterField(
#             model_name='locatie',
#             name='straat',
#             field=models.CharField(help_text='De straatnaam van de locatie.', max_length=256, verbose_name='straat'),
#         ),
#     ]
