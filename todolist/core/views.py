from extra_views import ModelFormSetView
from todolist.core.models import ToDo

class ToDoFormSetView(ModelFormSetView):
    template_name = 'todo.html'
    model = ToDo
    fields = ('done', 'title', 'order')
    extra = 1
    can_delete = True
