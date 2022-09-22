# Generated by Django 4.1.1 on 2022-09-20 11:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobilio_modelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(max_length=100, verbose_name='Automobilio marke')),
                ('modelis', models.CharField(max_length=100, verbose_name='Automobilio modelis')),
                ('metai', models.CharField(max_length=10, verbose_name='Pagaminimo metai')),
            ],
            options={
                'verbose_name': 'Automobilio modelis',
                'verbose_name_plural': 'Automobilio modeliai',
            },
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valstyb_nr', models.CharField(help_text='Iveskite Valstyb. Numeri', max_length=20)),
                ('vin_kodas', models.CharField(max_length=50, verbose_name='Bus prieinama')),
                ('klientas', models.CharField(max_length=100, verbose_name='Vardas, Pavarde')),
                ('automobilio_modelis_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilio_modelis')),
            ],
            options={
                'verbose_name': 'Automobilis',
                'verbose_name_plural': 'Automobiliai',
            },
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('kaina', models.FloatField(verbose_name='Kaina')),
            ],
            options={
                'verbose_name': 'Paslauga',
                'verbose_name_plural': 'Paslaugos',
            },
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unikalus ID Kiekvienam Uzsakymui', primary_key=True, serialize=False)),
                ('data', models.DateField(help_text='Iveskite Data')),
                ('suma', models.CharField(max_length=20, verbose_name='Kaina Viso:')),
                ('status', models.CharField(blank=True, choices=[('x', 'Administratorius'), ('p', 'Priimta, dar nevykdoma'), ('v', 'Vykdoma'), ('a', 'Atlikta')], default='x', help_text='Statusas', max_length=1)),
                ('automobilis_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilis')),
            ],
            options={
                'verbose_name': 'Uzsakymas',
                'verbose_name_plural': 'Uzsakymai',
            },
        ),
        migrations.CreateModel(
            name='Uzsakymo_eilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.IntegerField(max_length=20, verbose_name='Kiekis')),
                ('kaina', models.FloatField(max_length=20, verbose_name='Kaina')),
                ('paslauga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.paslauga')),
                ('uzsakymas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.uzsakymas')),
            ],
            options={
                'verbose_name': 'Užsakymo eilutė',
                'verbose_name_plural': 'Užsakymo eilutės',
            },
        ),
    ]