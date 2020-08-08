from django.shortcuts import render, redirect, get_object_or_404
from todo.models import ToDo
from todo.forms import TodoForm
from django.contrib.auth.decorators import login_required


@login_required
def todo(request):
    todo = ToDo.objects.order_by('stage', 'task').filter(user=request.user)

    context = {'todo': todo, 'form': TodoForm()}
    template_name = 'todo.html'

    return render(request, template_name, context=context)


@login_required
def addTodo(request):

    if request.method == 'POST':
        todoForm = TodoForm(request.POST)
        if todoForm.is_valid():
            task = todoForm.save(commit=False)
            task.stage = ToDo.ADICIONADO
            task.user_id = request.user.pk
            task.save()
        print(todoForm.errors)

    return redirect('todo:todo')


@login_required
def change_stage(request, task_id, new_stage):
    task = get_object_or_404(ToDo, pk=task_id, user_id=request.user.pk)
    task.stage = new_stage
    task.save()
    return redirect('todo:todo')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(ToDo, pk=task_id, user_id=request.user.pk)
    task.delete()
    return redirect('todo:todo')
