# Generated by Django 4.1 on 2022-09-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="predresult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("salary", models.FloatField()),
                ("age", models.FloatField()),
                ("room", models.FloatField()),
                ("bedroom", models.IntegerField()),
                ("population", models.IntegerField()),
                ("price", models.FloatField()),
            ],
        ),
    ]
