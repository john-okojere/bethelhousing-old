# Generated by Django 3.2.16 on 2023-01-28 23:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='location/%y/%m/%d/')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedUids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('area', models.FloatField()),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('gdpr', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Uid',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('basicInfo', models.BooleanField(default=False)),
                ('locationInfo', models.BooleanField(default=False)),
                ('imageFile', models.BooleanField(default=False)),
                ('detailedInfo', models.BooleanField(default=False)),
                ('contactInfo', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_property', to='property.address')),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locationinfo', to='property.uid')),
            ],
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='property/%y/%m/%d/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageinfo', to='property.uid')),
            ],
        ),
        migrations.CreateModel(
            name='FiveReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.FloatField()),
                ('value_of_money', models.FloatField()),
                ('location', models.FloatField()),
                ('cleanliness', models.FloatField()),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fivereview', to='property.uid')),
            ],
        ),
        migrations.CreateModel(
            name='DetailedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('age', models.CharField(max_length=25)),
                ('garage', models.IntegerField()),
                ('Room', models.IntegerField()),
                ('airCondition', models.BooleanField(default=False)),
                ('Bedding', models.BooleanField(default=False)),
                ('Heating', models.BooleanField(default=False)),
                ('Internet', models.BooleanField(default=False)),
                ('Microwave', models.BooleanField(default=False)),
                ('SmokingAllow', models.BooleanField(default=False)),
                ('Terrace', models.BooleanField(default=False)),
                ('Balcony', models.BooleanField(default=False)),
                ('Icon', models.BooleanField(default=False)),
                ('Wi_Fi', models.BooleanField(default=False)),
                ('Beach', models.BooleanField(default=False)),
                ('Parking', models.BooleanField(default=False)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detailinfo', to='property.uid')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customercare', to='property.uid')),
            ],
        ),
    ]
