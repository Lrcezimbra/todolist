from django.test import TestCase
from todolist.core.models import ToDo

class ToDoTest(TestCase):
    def setUp(self):
        self.obj = ToDo.objects.create(
            title='Create tests for ToDo project',
            order=1,
            done=True,
        )

    def test_create(self):
        self.assertTrue(ToDo.objects.exists())

    def test_done_default_is_False(self):
        todo = ToDo.objects.create(
            title='Create tests for ToDo project',
            order=1,
        )
        self.assertFalse(todo.done)

    def test_ordering(self):
        expected_ordering = ('order',)
        self.assertEqual(expected_ordering, self.obj._meta.ordering)
