from django.shortcuts import render

developers = [
    {
        "username": "hassan",
        "first_name": "Hassan",
        "last_name": "Kabirian",
        "skills": ["Python", "Django", "Vue.js"],
    },
    {
        "username": "sara",
        "first_name": "Sara",
        "last_name": "Ahmadi",
        "skills": ["JavaScript", "React", "CSS"],
    },
    {
        "username": "ali",
        "first_name": "Ali",
        "last_name": "Rezayi",
        "skills": ["Java", "Spring Boot", "SQL"],
    },
]

def developers_list(request):
    context = {'developers': developers}
    return render(request, 'developers_list.html', context)

from django.http import Http404

def developer_cv(request, username):
    for dev in developers:
        if dev['username'] == username:
            context = {'developer': dev}
            return render(request, 'developer_cv.html', context)
    raise Http404("Developer not found")