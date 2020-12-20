# Generated by Django 3.1.4 on 2020-12-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=50)),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField()),
            ],
        ),
    ]