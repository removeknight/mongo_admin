# from django.db import models

from djongo import models


class HealthCheckCondition(models.Model):
    OPERATORS = (
        ('=', '='),
        ('include', 'include')
    )
    attribute = models.CharField(max_length=50)
    operator = models.CharField(max_length=20, choices=OPERATORS)
    value = models.CharField(max_length=30)
    level = models.IntegerField(default=1)

    def __str__(self):
        return '%s %s %s' %(self.attribute, self.operator, self.value)


class HealtchCheck(models.Model):
    TYPES = (
        ('U', 'Users'),
        ('A', 'Agency'),
        ('G', 'Group'),
    )

    object_category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    when = models.ManyToManyField(HealthCheckCondition, related_name="all_conditions")
    failed_if = models.ForeignKey(HealthCheckCondition, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.title

