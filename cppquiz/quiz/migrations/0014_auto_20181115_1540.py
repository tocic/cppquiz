# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 15:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_question_retraction_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='retraction_message',
            field=models.TextField(blank=True, default=b'', help_text=b'Use markdown'),
        ),
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.CharField(choices=[(b'NEW', b'New'), (b'WAI', b'Waiting'), (b'ACC', b'Accepted'), (b'REF', b'Refused'), (b'PUB', b'Published'), (b'RET', b'Retracted')], default=b'NEW', max_length=3),
        ),
    ]
