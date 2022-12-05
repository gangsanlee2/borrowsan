from django.db import models

from admins.models import Admin


class User(models.Model):
    use_in_migration = True
    user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.IntegerField()
    address = models.TextField()
    most_used_location = models.TextField()
    count_month = models.IntegerField()
    current_location = models.TextField()
    pay_info = models.TextField()

    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.user_id} {self.email} {self.nickname} {self.password} {self.age} {self.age} {self.address} {self.most_used_location} {self.count_month} {self.current_location} {self.pay_info} {self.admin}'
