# Generated by Django 5.0.7 on 2024-08-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='CybercrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_category', models.CharField(choices=[('Hacking', 'Hacking'), ('Cyberbullying', 'Cyberbullying'), ('Online Fraud', 'Online Fraud')], max_length=50)),
                ('crime_description', models.TextField()),
                ('crime_photo', models.ImageField(blank=True, null=True, upload_to='crime_photos/')),
                ('crime_document', models.FileField(blank=True, null=True, upload_to='crime_documents/')),
                ('contact_email', models.EmailField(max_length=254)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
