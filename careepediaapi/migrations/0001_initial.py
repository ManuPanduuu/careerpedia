# Generated by Django 3.0 on 2019-12-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bachelor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=500)),
                ('eligibility', models.CharField(max_length=10)),
                ('education_level', models.CharField(max_length=10)),
                ('serial', models.CharField(max_length=10)),
                ('government_recognition', models.CharField(max_length=10)),
                ('career_opportunities_one', models.CharField(max_length=10)),
                ('career_opportunities_two', models.CharField(max_length=10)),
                ('career_opportunities_three', models.CharField(max_length=10)),
                ('career_opportunities_four', models.CharField(max_length=10)),
                ('career_opportunities_five', models.CharField(max_length=10)),
                ('career_opportunities_six', models.CharField(max_length=10)),
                ('subject_one', models.CharField(max_length=10)),
                ('subject_two', models.CharField(max_length=10)),
                ('subject_three', models.CharField(max_length=10)),
                ('subject_four', models.CharField(max_length=10)),
                ('subject_five', models.CharField(max_length=10)),
                ('subject_six', models.CharField(max_length=10)),
                ('subject_seven', models.CharField(max_length=10)),
                ('subject_eight', models.CharField(max_length=10)),
                ('subject_nine', models.CharField(max_length=10)),
                ('subject_ten', models.CharField(max_length=10)),
                ('subject_eleven', models.CharField(max_length=10)),
                ('subject_twelve', models.CharField(max_length=10)),
                ('subject_thirteen', models.CharField(max_length=10)),
                ('subject_fourteen', models.CharField(max_length=10)),
                ('subject_fifteen', models.CharField(max_length=10)),
                ('subject_sixteen', models.CharField(max_length=10)),
                ('subject_seventeen', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=500)),
                ('eligibility', models.CharField(max_length=10)),
                ('education_level', models.CharField(max_length=10)),
                ('serial', models.CharField(max_length=10)),
                ('government_recognition', models.CharField(max_length=10)),
                ('career_opportunities_one', models.CharField(max_length=10)),
                ('career_opportunities_two', models.CharField(max_length=10)),
                ('career_opportunities_three', models.CharField(max_length=10)),
                ('career_opportunities_four', models.CharField(max_length=10)),
                ('career_opportunities_five', models.CharField(max_length=10)),
                ('career_opportunities_six', models.CharField(max_length=10)),
                ('subject_one', models.CharField(max_length=10)),
                ('subject_two', models.CharField(max_length=10)),
                ('subject_three', models.CharField(max_length=10)),
                ('subject_four', models.CharField(max_length=10)),
                ('subject_five', models.CharField(max_length=10)),
                ('subject_six', models.CharField(max_length=10)),
                ('subject_seven', models.CharField(max_length=10)),
                ('subject_eight', models.CharField(max_length=10)),
                ('subject_nine', models.CharField(max_length=10)),
                ('subject_ten', models.CharField(max_length=10)),
                ('subject_eleven', models.CharField(max_length=10)),
                ('subject_twelve', models.CharField(max_length=10)),
                ('subject_thirteen', models.CharField(max_length=10)),
                ('subject_fourteen', models.CharField(max_length=10)),
                ('subject_fifteen', models.CharField(max_length=10)),
                ('subject_sixteen', models.CharField(max_length=10)),
                ('subject_seventeen', models.CharField(max_length=10)),
            ],
        ),
    ]
