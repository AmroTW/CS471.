from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Address, Student, Card, Department, Course,Students, Students2, GalleryImage
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import BookForm, StudentsForm, Students2Form, GalleryImageForm

def index(request): 
    return render(request, "bookmodule/index.html") 
def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 
def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 
def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')
def links_page(request):
    return render(request, 'bookmodule/html5/links.html')
def formatting_page(request):
    return render(request, 'bookmodule/html5/formatting.html')
def listing_page(request):
    return render(request, 'bookmodule/html5/listing.html')
def tables_page(request):
    return render(request, 'bookmodule/html5/tables.html')
def search_view(request):
    if request.method == "POST": 
        string = request.POST.get('keyword').lower() 
        isTitle = request.POST.get('option1') 
        isAuthor = request.POST.get('option2') 
        # now filter 
        books = __getBooksList() 
        newBooks = [] 
        for item in books: 
            contained = False 
            if isTitle and string in item['title'].lower(): contained = True 
            if not contained and isAuthor and string in item['author'].lower():contained = True 
            if contained: newBooks.append(item) 
            return render(request, 'bookmodule/html5/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')
def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3] 

def list_books(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})

def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = 
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
        return render(request, 'bookmodule/list_books.html', {'books':mybooks}) 
    else: 
        return render(request, 'bookmodule/index.html') 
    
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

from django.db.models import Count, Sum, Avg, Max, Min

def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})


def students_per_city(request):
    data = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'data': data})

def lab9_task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab9/task1.html', {'departments': departments})

def lab9_task2(request):
    courses = Course.objects.all()
    course_counts = []

    for course in courses:
        student_count = course.student_set.count() 
        course_counts.append({
            'title': course.title,
            'count': student_count
        })

    return render(request, 'bookmodule/lab9/task2.html', {'course_counts': course_counts})

from django.shortcuts import render
from .models import Student

def lab9_task3(request):
    departments = Department.objects.annotate(oldest_student_id=Min('student__id'))

    department_with_oldest_student = []
    for dept in departments:
        if dept.oldest_student_id is not None:
            oldest_student = Student.objects.get(id=dept.oldest_student_id)
            department_with_oldest_student.append({
                'department': dept.name,
                'oldest_student': oldest_student.name
            })

    return render(request, 'bookmodule/lab9/task3.html', {
        'department_with_oldest_student': department_with_oldest_student
    })
    
def lab9_task4(request):
    departments = Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/lab9/task4.html', {'departments': departments})

def list_books2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/list_books2.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books2')
    return render(request, 'bookmodule/lab10/create_book.html')

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books2')
    return render(request, 'bookmodule/lab10/update_book.html', {'book': book})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('list_books2')


def list_books_form(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/form/list_form.html', {'books': books})

def create_book_form(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books2')
    return render(request, 'bookmodule/lab10/form/create_form.html', {'form': form})

def update_book_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books2')
    return render(request, 'bookmodule/lab10/form/update_form.html', {'form': form})

def delete_book_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books2')
    return render(request, 'bookmodule/lab10/form/delete_form.html', {'book': book})

def lab11_task1(request):
    students = Students.objects.all()
    return render(request, 'bookmodule/lab11/task1.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab11_task1')  
    else:
        form = StudentsForm()
    return render(request, 'bookmodule/lab11/add_student.html', {'form': form}) 

def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)

    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab11_task1')      
    else:
        form = StudentsForm(instance=student)

    return render(request, 'bookmodule/lab11/edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    student.delete()
    return redirect('lab11_task1')

def list_students2(request):
    students = Students2.objects.all()
    return render(request, 'bookmodule/lab11/students2/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Students2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Students2Form()
    return render(request, 'bookmodule/lab11/students2/add_student2.html', {'form': form})

def edit_student2(request, student_id):
    student = get_object_or_404(Students2, id=student_id)
    if request.method == 'POST':
        form = Students2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Students2Form(instance=student)
    return render(request, 'bookmodule/lab11/students2/edit_student2.html', {'form': form})

def delete_student2(request, student_id):
    student = get_object_or_404(Students2, id=student_id)
    student.delete()
    return redirect('bookmodule/lab11/students2/list_students2')


def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryImageForm()
    return render(request, 'bookmodule/lab11/gallery/upload_image.html', {'form': form})

def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'bookmodule/lab11/gallery/gallery_list.html', {'images': images})


