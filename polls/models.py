from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
string_error = 'Неверный формат, только буквы латинского или русского алфавита'


class Employee(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя", help_text="Enter first name",
                                  validators=[RegexValidator(r'^(?i)([a-z \-]+|[а-я \-]+)$', string_error), ])
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", help_text="Enter last name",
                                 validators=[RegexValidator(r'^(?i)([a-z \-]+|[а-я \-]+)$', string_error), ])
    second_name = models.CharField(max_length=200, verbose_name='Отчество', help_text="Enter second name", blank=True,
                                   null=True,
                                   validators=[RegexValidator(r'^(?i)([a-z \-]+|[а-я \-]+)$', string_error), ])
    birth_date = models.DateField(verbose_name='Дата рождения', help_text='Введите дату рождения')
    email = models.EmailField(max_length=200, verbose_name='Эл. почта', help_text='Введите эл. почту')
    phone_number = models.CharField(max_length=200, verbose_name='Телефон', help_text='Введите номер телефона',
                                    validators=[RegexValidator(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                                               'Неверный формат номера телефона'), ])
    start_work_date = models.DateField(verbose_name='Дата начала работы', help_text='Введите дату начала работы', )
    end_work_date = models.DateField(verbose_name='Дата окончания работы', help_text='Введите дату окончания работы',
                                     blank=True, null=True)
    position = models.ForeignKey('Position', verbose_name='Должность', on_delete=models.CASCADE,
                                 help_text='Введите должность',
                                 validators=[RegexValidator(r'^(?i)([a-z \-]+|[а-я \-]+)$', string_error), ])
    department = models.ForeignKey('Department', verbose_name='Отдел', on_delete=models.CASCADE,
                                   help_text='Введите отдел',
                                   validators=[RegexValidator(r'^(?i)([a-z \-]+|[а-я \-]+)$', string_error), ])

    def __str__(self):
        return f" {self.last_name} {self.first_name} {self.second_name}"

    def iswork(self):
        return "Работает" if self.end_work_date is None else "Уволен"

    iswork.short_description = 'Состояние'

    class Meta:
        ordering = ["last_name", "first_name", "second_name"]
        verbose_name_plural = "Работники"


class Position(models.Model):
    position = models.CharField(max_length=200, verbose_name="Должность", help_text="Enter first name")

    class Meta:
        ordering = ["position"]
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.position


class Department(models.Model):
    department = models.CharField(max_length=200, verbose_name="Department", help_text="Enter first name")

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["department"]
        verbose_name_plural = "Отделы"
