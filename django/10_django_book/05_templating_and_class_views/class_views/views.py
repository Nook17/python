from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from .models import Book
from .forms import BookForm


class BookRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/class_views/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("model records have been saved")


# --------- CRUD ---------
class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/class_views/entry_success'


class BookUpdateViews(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/class_views/entry_success'


class BookDeleteViews(DeleteView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_delete_form.html'
    success_url = '/class_views/delete_success'


class FormSuccessDelete(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Your book has been deleted")


class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'