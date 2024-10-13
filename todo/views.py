from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    if request.method=='POST':
        task_title=request.POST.get('title')
        task_description=request.POST.get('description')
        
        # Obtener el valor del checkbox y convertirlo en booleano
        task_completed = request.POST.get('completed') == 'on'
        
        # Creamos una nueva tarea y la guardamos en la base de datos
        Task.objects.create(
            title=task_title,
            description=task_description,
            completed=task_completed
        )
        
        # Redirigimos a la misma vista después de crear la tarea
        return redirect('index')
    
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})