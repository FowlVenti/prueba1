from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import project, tasks
from .forms import CreateNewTask, CreateNewProject


def index(request):
    title = "WOW!!!!!!"
    return render(request, "index.html", {"title": title})


def jamon(request):
    username = 67
    return render(request, "jamon.html", {"username": username})


def hello(request, username):
    return HttpResponse("<h1>HOLA %s </h1>" % username)


def Project(request):
    # p = list(project.objects.values())
    p = project.objects.all()
    return render(request, "projects.html", {"projects": p})


def Tasks(request):

    # t= get_object_or_404(tasks, titulo=titulo)
    # return HttpResponse('Tarea: %s' % t.id)
    t = tasks.objects.all()
    return render(request, "tasks.html", {"tasks": t})


def create_Task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": CreateNewTask()})
    else:
        tasks.objects.create(
            titulo=request.POST["titulo"],
            descripcion=request.POST["descripcion"],
            project_id=2,
        )
        return redirect("tasks")


def create_Project(request):
    if request.method == "GET":
        return render(request, "create_project.html", {"form": CreateNewProject})
    else:
        project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_details(request,id):
    p = get_object_or_404(project,id=id)
    print(id)
    t=tasks.objects.filter(project_id=id)
    return render(request, "details.html",{
        'projectx':p,
        'tasks': t
    })
