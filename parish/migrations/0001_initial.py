# Generated by Django 3.2.8 on 2022-05-11 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_date', models.DateField()),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10)),
                ('nida', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('mobile_phone', models.CharField(max_length=15, unique=True)),
                ('work_phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='member_photos')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Church Member',
                'verbose_name_plural': 'Church Members',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='MemberContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('contribution_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='church_contribution', to='parish.churchmember')),
            ],
            options={
                'verbose_name': 'Member Contribution',
                'verbose_name_plural': 'Member Contributions',
                'ordering': ['-pk'],
            },
        ),
    ]