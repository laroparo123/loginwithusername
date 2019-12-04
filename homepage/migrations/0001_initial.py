# Generated by Django 2.1.4 on 2019-12-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('price', models.FloatField()),
                ('offer', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=20)),
            ],
        ),
    ]
