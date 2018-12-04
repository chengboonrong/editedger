from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todo(request):
	all_todo_item = TodoItem.objects.all()
	return render(request, 'todo.html', 
		{'all_items': all_todo_item}
	)

def addTodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id = todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/todo/')