# Generated by Django 3.2.7 on 2022-07-23 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='学年')),
            ],
            options={
                'verbose_name_plural': '学年',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20, verbose_name='学年')),
                ('se1', models.CharField(max_length=10, verbose_name='選択肢1')),
                ('se2', models.CharField(max_length=10, verbose_name='選択肢2')),
                ('se3', models.CharField(max_length=10, verbose_name='選択肢3')),
                ('se4', models.CharField(max_length=10, verbose_name='選択肢4')),
                ('ans', models.CharField(max_length=10, verbose_name='正解')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q_grade', to='survey.grade', verbose_name='学年')),
            ],
            options={
                'verbose_name_plural': '問題',
            },
        ),
    ]
