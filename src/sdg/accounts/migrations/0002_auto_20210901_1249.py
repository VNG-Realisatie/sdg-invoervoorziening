# Generated by Django 2.2.24 on 2021-09-01 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("accounts", "0001_initial"),
        ("organisaties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="lokale_overheid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="lokale_overheden",
                to="organisaties.LokaleOverheid",
            ),
        ),
        migrations.AddField(
            model_name="role",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="roles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddConstraint(
            model_name="role",
            constraint=models.UniqueConstraint(
                fields=("user", "lokale_overheid"),
                name="unique_user_per_lokaleoverheid",
            ),
        ),
    ]
