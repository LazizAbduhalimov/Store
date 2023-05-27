# Generated by Django 4.2.1 on 2023-05-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Title')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('location', models.TextField(default='', verbose_name='Location')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Phone number')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='Email')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=25, verbose_name='Title')),
                ('subtitle', models.CharField(default='', max_length=50, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images/slider/', verbose_name='Image')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=25, verbose_name='Title')),
                ('subtitle', models.CharField(default='', max_length=50, verbose_name='Title')),
                ('image', models.ImageField(upload_to='images/slider/', verbose_name='Image')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
            ],
        ),
    ]
