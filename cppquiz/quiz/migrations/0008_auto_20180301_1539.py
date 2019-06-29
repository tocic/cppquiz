# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-01 15:39


from django.db import migrations

def forwards_func(apps, schema_editor):
    Question = apps.get_model("quiz", "Question")
    db_alias = schema_editor.connection.alias
    print()
    for q in Question.objects.using(db_alias).all():
        print("Migrating " + str(q.pk))
        if (q.retracted):
            print("- Retracted")
            q.state = 'RET'
        elif (q.published):
            print("- Published")
            q.state = 'PUB'
        elif (q.refused):
            print("- Refused")
            q.state = 'REF'
        q.save()

def reverse_func(apps, schema_editor):
    Question = apps.get_model("quiz", "Question")
    db_alias = schema_editor.connection.alias
    print()
    for q in Question.objects.using(db_alias).all():
        print("Migrating " + str(q.pk))
        if (q.state == 'RET'):
            print("- Retracted and published")
            q.retracted = True
            q.published = True
            q.refused = False
        elif (q.state == 'PUB'):
            print("- Published")
            q.retracted = False
            q.published = True
            q.refused = False
        elif (q.state == 'REF'):
            print("- Refused")
            q.retracted = False
            q.published = False
            q.refused = True
        else:
            print("- New")
            q.retracted = False
            q.published = False
            q.refused = False
        q.save()

class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_question_state'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
