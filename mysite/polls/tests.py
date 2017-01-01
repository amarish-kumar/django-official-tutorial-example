import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Question

class QuestionMethodTests(TestCase):

	def test_was_pubished_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(question_text='Sample bad question', pub_date=time)

		self.assertFalse(future_question.was_published_recently())

class QuestionViewTest(TestCase):

	def test_index(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)

	def test_detail(self):
		response = self.client.get(reverse('polls:detail', args=(1,)))
		self.assertEqual(response.status_code, 200)

	def test_results(self):
		response = self.client.get(reverse('polls:results', args=(1,)))
		self.assertEqual(response.status_code, 200)