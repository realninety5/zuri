# Generated by Django 3.2.6 on 2021-08-19 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=30)),
                ('course', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compro', models.CharField(blank=True, max_length=20, null=True)),
                ('date_start', models.DateField()),
                ('date_stop', models.DateField()),
                ('comp', models.BooleanField(default=False)),
                ('position', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30)),
                ('skill_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='my_resume.skill')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs_done', models.TextField()),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='my_resume.experience')),
            ],
        ),
    ]
