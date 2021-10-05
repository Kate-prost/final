from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Operation, Budget

User = get_user_model()


class BudgetTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Продукты')

