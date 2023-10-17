# Generated by Django 4.1 on 2023-10-15 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
            ],
        ),
        migrations.CreateModel(
            name="Coffee",
            fields=[
                (
                    "name",
                    models.CharField(max_length=25, primary_key=True, serialize=False),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="index.cart"
                    ),
                ),
                (
                    "coffee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="index.coffee"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(through="index.CartItem", to="index.coffee"),
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="index.customers"
            ),
        ),
    ]