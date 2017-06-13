from extra_views import ModelFormSetView
from todolist.core.models import ToDo

class ToDoFormSetView(ModelFormSetView):
    template_name = 'todo.html'
    model = ToDo
    fields = ('title', 'order', 'done')
