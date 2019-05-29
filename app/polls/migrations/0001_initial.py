# Generated by Django 2.2.1 on 2019-05-23 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    migration = False
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsMentor', models.BooleanField()),
                ('Person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Person')),
                ('Project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='many_to_many_mapping_proj_person',
            field=models.ManyToManyField(through='polls.Project_User', to='polls.Person'),
        ),
    ]
