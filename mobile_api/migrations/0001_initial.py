# Generated by Django 2.0.6 on 2018-10-18 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField()),
                ('step', models.CharField(choices=[('I', 'install'), ('L', 'launch'), ('R', 'review')], max_length=1)),
                ('status', models.CharField(choices=[('I', 'install'), ('L', 'launch'), ('R', 'review')], default='TD', max_length=2)),
            ],
            options={
                'ordering': ['day', 'step'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('launches', models.PositiveIntegerField()),
                ('do_review', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mobile_api.Task'),
        ),
        migrations.AddField(
            model_name='step',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mobile_api.User'),
        ),
    ]
