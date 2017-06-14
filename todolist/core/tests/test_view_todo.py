from django.test import TestCase
from todolist.core.models import ToDo
from todolist.core.views import ToDoFormSetView

class ToDoViewTest(TestCase):
    def setUp(self):
        for i in range(2):
            ToDo.objects.create(
                title='Create tests for ToDo project',
                order=i,
            )
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'todo.html')

    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        '''HTML must contain input tags'''
        tags = (('<form', 1),
                ('<input', 20),
                ('type="text"', 5),
                ('type="submit"', 1),
                ('name="form-TOTAL_FORMS"', 1),
                ('name="form-INITIAL_FORMS"', 1),
                ('name="form-MIN_NUM_FORMS"', 1),
                ('name="form-MAX_NUM_FORMS"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_has_formset(self):
        form = self.response.context['formset']
        self.assertIsNotNone(form)

    def test_formset_view(self):
        expected_attrs = (('template_name', 'todo.html'),
                          ('model', ToDo),
                          ('fields', ('done', 'title', 'order')),
                          ('extra', 1),
                          ('can_delete', True))

        for attr, expected in expected_attrs:
            with self.subTest():
                value = getattr(ToDoFormSetView, attr)
                self.assertEqual(value, expected)

