import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "two.settings")
django.setup()

from appname.models import Student
students = Student.objects.filter(status='adjoining', paid_fees=0)

print(f"Total students with paid_fees=0: {students.count()}")

for s in students:
    print(f"Student: {s.id}, remaining_fees: {s.remaining_fees}, paid_fees: {s.paid_fees}")
