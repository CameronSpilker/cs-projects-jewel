import os, os.path, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


#imports for our project
from django.core import management
from django.db import connection
from homepage.models import Choice, Question  # Import the model classes we just wrote.
from django.utils import timezone

from datetime import datetime
from decimal import Decimal

# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

# No questions are in the system yet.
Question.objects.all()

q = Question(question_text="What's new?", pub_date=timezone.now())
print('1')
print(q)
# Save the object into the database. You have to call save() explicitly.
q.save()

# Now it has an ID.
q.id
print('2')
print(q.id)

# Access model field values via Python attributes.
q.question_text
print('3')
print(q.question_text)
q.pub_date
print('4')
print(q.pub_date)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
print('5')
print(q.question_text)
q.save()

# objects.all() displays all the questions in the database.
Question.objects.all()
