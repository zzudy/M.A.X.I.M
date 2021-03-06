# Generated by Django 2.2.2 on 2019-06-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_class_academy_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_class', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='class_description',
            name='classSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='classList',
            field=models.CharField(default='0000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='request',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
