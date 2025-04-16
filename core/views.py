from django.http import JsonResponse
from .models import Student, Subject
from collections import defaultdict

def students_view(request):
    students = list(Student.objects.values("name", "program"))
    return JsonResponse(students, safe=False)

def subjects_view(request):
    subjects = Subject.objects.all()
    data = defaultdict(list)
    for subject in subjects:
        data[f"Year {subject.year}"].append(subject.name)
    return JsonResponse(data)
