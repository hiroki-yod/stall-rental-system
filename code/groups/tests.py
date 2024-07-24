from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from groups.models import Group


User = get_user_model()

class GroupListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.group1 = Group.objects.create(
            name="Group 1",
            name_kana="グループ 1",
            representative_name="代表者 1",
            representative_email="rep1@example.com",
            representative_phone_number="000-0000-0000",
            group_type="COMPANY",
            purpose="Purpose 1",
            activities="Activities 1"
        )
        self.group2 = Group.objects.create(
            name="Group 2",
            name_kana="グループ 2",
            representative_name="代表者 2",
            representative_email="rep2@example.com",
            representative_phone_number="111-1111-1111",
            group_type="NPO",
            purpose="Purpose 2",
            activities="Activities 2"
        )
        self.group1.members.add(self.user)

    def test_group_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('groups:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertContains(response, self.group1.name)
        self.assertNotContains(response, self.group2.name)
