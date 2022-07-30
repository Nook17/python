from django.urls import path

from .views import BookRecordFormView, FormSuccessView, BookCreateView, BookUpdateViews, BookDeleteViews, \
    FormSuccessDelete, BookRecordDetailView

urlpatterns = [
    path('new_book_record', BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('book_record_create', BookCreateView.as_view(), name='book_create'),
    path('book_record_update/<int:pk>', BookUpdateViews.as_view(), name='book_update'),
    path('book_record_delete/<int:pk>', BookDeleteViews.as_view(), name='book_delete'),
    path('delete_success', FormSuccessDelete.as_view(), name='form_delete_success'),
    path('book_record_detail/<int:pk>', BookRecordDetailView.as_view(), name='book_detail'),
]
