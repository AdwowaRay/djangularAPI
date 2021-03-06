# Generated by Django 3.2.6 on 2021-10-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeId', models.AutoField(primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=100)),
                ('departmentName', models.CharField(max_length=100)),
                ('dateOfJoining', models.DateField(max_length=100)),
                ('photoFileName', models.CharField(max_length=100)),
            ],
        ),
    ]
