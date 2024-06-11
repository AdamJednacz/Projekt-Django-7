# Generated by Django 4.1 on 2024-06-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("name", models.CharField(max_length=40)),
                ("photo", models.ImageField(upload_to="images")),
                ("discription", models.TextField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Trip",
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
                ("name", models.CharField(max_length=40)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("discription", models.CharField(default="", max_length=100)),
                ("create", models.DateTimeField(auto_now_add=True)),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="www.place"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favorite",
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
                (
                    "trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="www.trip"
                    ),
                ),
            ],
        ),
    ]