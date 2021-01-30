# Generated by Django 3.1.5 on 2021-01-30 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(help_text='Enter first name', max_length=200, verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Отделы',
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(help_text='Enter first name', max_length=200, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должности',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name', max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Enter last name', max_length=200, verbose_name='Фамилия')),
                ('second_name', models.CharField(blank=True, help_text='Enter second name', max_length=200, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения')),
                ('email', models.EmailField(help_text='Введите эл. почту', max_length=200, verbose_name='Эл. почта')),
                ('phone_number', models.CharField(help_text='Введите номер телефона', max_length=200, verbose_name='Телефон')),
                ('start_work_date', models.DateField(help_text='Введите дату начала работы', verbose_name='Дата начала работы')),
                ('end_work_date', models.DateField(blank=True, help_text='Введите дату окончания работы', null=True, verbose_name='Дата окончания работы')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.position')),
            ],
            options={
                'verbose_name': 'Работники',
                'ordering': ['last_name', 'first_name', 'second_name'],
            },
        ),
    ]
