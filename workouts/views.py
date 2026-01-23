from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Exercise
from .forms import ExerciseForm


@login_required
def index(request):
    """Главная страница приложения"""
    exercises = Exercise.objects.all().order_by('name')

    # Пагинация - по 10 упражнений на странице
    paginator = Paginator(exercises, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_exercises': exercises.count(),
    }
    return render(request, 'workouts/index.html', context)


@login_required
def add_exercise(request):
    """Добавление нового упражнения"""
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, f'Упражнение "{exercise.name}" успешно добавлено!')
            return redirect('workouts:index')
    else:
        form = ExerciseForm()

    return render(request, 'workouts/add_exercise.html', {'form': form})


@login_required
def exercise_list(request):
    """Список всех упражнений"""
    exercises = Exercise.objects.all().order_by('name')
    return render(request, 'workouts/exercise_list.html', {'exercises': exercises})


@login_required
def delete_exercise(request, exercise_id):
    """Удаление упражнения"""
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.method == 'POST':
        exercise_name = exercise.name
        exercise.delete()
        messages.success(request, f'Упражнение "{exercise_name}" удалено.')
        return redirect('workouts:index')

    return render(request, 'workouts/confirm_delete.html', {'exercise': exercise})