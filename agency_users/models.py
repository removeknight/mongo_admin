from djongo import models


class Agency(models.Model):
    location_code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)


class User(models.Model):
    uid = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(null=True)
    licenses = models.ListField(models.CharField(max_length=30), null=True)

    def __str__(self):
        return self.name


