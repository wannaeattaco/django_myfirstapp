from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from datetime import timedelta

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_q = Question(pub_date=timezone.now() + timedelta(days=30))
        self.assertIs(future_q.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_q = Question(pub_date=timezone.now() - timedelta(days=2))
        self.assertIs(old_q.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_q = Question(pub_date=timezone.now() - timedelta(hours=12))
        self.assertIs(recent_q.was_published_recently(), True)

