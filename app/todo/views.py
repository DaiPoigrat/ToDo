import os.path

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UserRegisterForm, UserAuthForm, AddTaskForm, UserUpdateForm
from .models import Users, TodoList
from datetime import date, timedelta


# Create your views here.
def register(request):
    error = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = Users.objects.filter(mail=form.data['mail'])
            if user:
                error = 'Данный email уже зарегистрирован'
            else:
                new_user = form.save()
                # print(f"USER ID === {new_user.id}")
                return redirect(f'{new_user.id}/today')
        else:
            error = 'Форма заполнена неверно'

    form = UserRegisterForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request=request, template_name='todo/reg.html', context=data)


def login(request):
    print("LOGIN PAGE")
    error = ''
    if request.method == 'POST':
        form = UserAuthForm(request.POST)

        if form.is_valid():
            user = Users.objects.filter(mail=form.data['mail'], password=form.data['password'])

            if user:
                return redirect(f'{user.get().id}/today')
            else:
                error = 'Неверные email или пароль'

    form = UserAuthForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request=request, template_name='todo/login.html', context=data)


#
# class TodayView(DetailView):
#     model = TodoList
#

def today(request, user_id):
    user = Users.objects.filter(id=user_id).get()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)

        if form.is_valid():
            print("NEW DATA UPLOAD:")
            print(form.data)
            task = TodoList.objects.create(user=user, name=form.data['name'], text=form.data['text'], passed=False)
            task.save()

            return redirect(today, user_id=user_id)
        else:
            print('ERROR')

    form = AddTaskForm()
    all_tasks = TodoList.objects.filter(user=user, date=date.today())
    current_tasks = TodoList.objects.filter(user=user, passed=True, date=date.today()).count()
    all_tasks_count = all_tasks.count()

    data = {
        'user_id': user_id,
        'form': form,
        'tasks': all_tasks,
        'current': current_tasks,
        'all': all_tasks_count,
        'user': user
    }
    return render(request=request, template_name='todo/today.html', context=data)


def passTask(request, user_id, task_id, arg):
    task = TodoList.objects.filter(id=task_id).get()
    task.passed = not task.passed
    task.save()
    return redirect(f'{arg}', user_id=user_id)


def editTask(request, user_id, task_id, arg):
    task = TodoList.objects.filter(id=task_id).get()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task.name = form.data['name']
            task.text = form.data['text']
            task.save()

    return redirect(f'{arg}', user_id=user_id)


def deleteTask(request, user_id, task_id, arg):
    task = TodoList.objects.filter(id=task_id).get()
    task.delete()
    return redirect(f'{arg}', user_id=user_id)


def yesterday(request, user_id):
    user = Users.objects.filter(id=user_id).get()

    form = AddTaskForm()
    all_tasks = TodoList.objects.filter(user=user, date=date.today() - timedelta(days=1))
    current_tasks = TodoList.objects.filter(user=user, passed=True, date=date.today() - timedelta(days=1)).count()
    all_tasks_count = all_tasks.count()

    data = {
        'user_id': user_id,
        'form': form,
        'tasks': all_tasks,
        'current': current_tasks,
        'all': all_tasks_count,
        'user': user
    }
    return render(request=request, template_name='todo/yesterday.html', context=data)


def upcoming(request, user_id):
    user = Users.objects.filter(id=user_id).get()

    form = AddTaskForm()
    all_tasks = TodoList.objects.filter(user=user, date=date.today() - timedelta(days=1))
    current_tasks = TodoList.objects.filter(user=user, passed=True, date=date.today() - timedelta(days=1)).count()
    all_tasks_count = all_tasks.count()

    data = {
        'user_id': user_id,
        'form': form,
        'tasks': all_tasks,
        'current': current_tasks,
        'all': all_tasks_count,
        'user': user
    }
    return render(request=request, template_name='todo/upcoming.html', context=data)


def select_day(request, user_id, selected_day):
    print(f"DAY {selected_day} HAS BEEN SELECTED")
    return redirect('upcoming', user_id=user_id)


def profile(request, user_id):
    user = Users.objects.filter(id=user_id).get()
    print(f'USER ID = {user_id}')
    form = UserUpdateForm()
    data = {
        'user_id': user_id,
        'user': user,
        'form': form
    }
    return render(request=request, template_name='todo/profile.html', context=data)


def profile_update(request, user_id):
    user = Users.objects.filter(id=user_id).get()
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES['profile_photo']:
                fss = FileSystemStorage()
                upload_photo = request.FILES['profile_photo']
                # print(os.listdir('media/app/images/'))
                if f'{user_id}_profile.jpg' in os.listdir('media/app/images/'):
                    os.remove(f'media/app/images/{user_id}_profile.jpg')
                fss.save(name=f'app/images/{user_id}_profile.jpg', content=upload_photo)
                user.profile_photo = f'app/images/{user_id}_profile.jpg'
            user.username = form.data['username']
            # form.data['profile_photo'].save()
            user.save()
    return redirect('profile', user_id=user_id)
