from django.db import models
from accounts.models import User


class Group(models.Model):
    GROUP_TYPE_CHOICES = [
        ("COMPANY", "企業"),
        ("NPO", "NPO法人"),
        ("VOLUNTARY", "ボランティア団体"),
        ("OTHER", "その他"),
    ]

    name = models.CharField("団体名", max_length=64)
    name_kana = models.CharField("団体名（カナ）", max_length=64)
    representative_name = models.CharField("代表者氏名", max_length=64)
    representative_email = models.EmailField("代表者メールアドレス")
    representative_phone_number = models.CharField("代表者電話番号", max_length=32)
    group_type = models.CharField("団体種類", max_length=16, choices=GROUP_TYPE_CHOICES)
    purpose = models.TextField("活動目的")
    activities = models.TextField("活動内容")
    members = models.ManyToManyField(User, verbose_name="メンバー", related_name="member_groups")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "団体"
        db_table = "group"
