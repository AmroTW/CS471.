from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name= "books.index"), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"), 
    path('html5/links', views.links_page, name='books.links'),
    path('html5/text/formatting', views.formatting_page, name='books.formatting'),
    path('html5/listing', views.listing_page, name='books.listing'),
    path('html5/tables', views.tables_page, name='books.tables'),
    path('search', views.search_view, name='books.search'),
    path('list_books/', views.list_books, name='list_books'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('lab8/task1', views.lab8_task1, name='books.lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='books.lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='books.lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='books.lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='books.lab8_task5'),
    path('lab8/task7', views.students_per_city, name='books.lab8_task7'),
    path('lab9/task1/', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2/', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3/', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4/', views.lab9_task4, name='lab9_task4'),
    path('lab10/create/', views.create_book, name='create_book'),
    path('lab10/', views.list_books2, name='list_books2'),
    path('lab10/update/<int:book_id>/', views.update_book, name='update_book'),
    path('lab10/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('lab10/form/', views.list_books_form, name='list_books_form'),
    path('lab10/form/create/', views.create_book_form, name='create_book_form'),
    path('lab10/form/update/<int:book_id>/', views.update_book_form, name='update_book_form'),
    path('lab10/form/delete/<int:book_id>/', views.delete_book_form, name='delete_book_form'),
    path('lab11/task1/', views.lab11_task1, name='lab11_task1'),
    path('lab11/add/', views.add_student, name='add_student'),
    path('lab11/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('lab11/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('lab11/tudents2/', views.list_students2, name='list_students2'),
    path('lab11/students2/add/', views.add_student2, name='add_student2'),
    path('lab11/students2/<int:student_id>/edit/', views.edit_student2, name='edit_student2'),
    path('lab11/students2/<int:student_id>/delete/', views.delete_student2, name='delete_student2'),
    path('lab11/gallery/', views.upload_image, name='upload_image'),
    path('lab11/gallery/list/', views.gallery_list, name='gallery_list'),
 



    
    
] 
