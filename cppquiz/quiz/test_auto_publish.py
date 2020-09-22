from datetime import datetime, timedelta

from django.core.management import call_command
from django.test import TestCase

from .models import Question

class AutoPublishTest(TestCase):

    def test_publishes_scheduled_question_from_the_past(self):
        q = Question(state="SCH", hint="hint", difficulty=1, publish_time=datetime.now())
        q.save()
        call_command("auto_publish", "--skip-tweet")
        self.assertEqual("PUB", Question.objects.get(pk=q.pk).state)

    def test_does_not_publish_unscheduled_question_from_the_past(self):
        q = Question(state="ACC", hint="hint", difficulty=1, publish_time=datetime.now())
        q.save()
        call_command("auto_publish", "--skip-tweet")
        self.assertEqual("ACC", Question.objects.get(pk=q.pk).state)

    def test_does_not_publish_scheduled_question_from_the_future(self):
        future = datetime.now() + timedelta(hours=1)
        q = Question(state="SCH", hint="hint", difficulty=1, publish_time=future)
        q.save()
        call_command("auto_publish", "--skip-tweet")
        self.assertEqual("SCH", Question.objects.get(pk=q.pk).state)
