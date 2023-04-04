from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary
from .forms import DiaryForm

# Create your views here.

def diary(request, year=None, month=None):
    diaries = Diary.objects.order_by('record_date')
    year = request.GET.get('year')
    month = request.GET.get('month')

    if year and month:
        diaries = diaries.filter(record_date__year=year, record_date__month=month)

    context = {
        'diaries' : diaries,
        'years' : range(2020,2024),
        'months' : range(1,13),
    }
    return render(request, 'diaries/diary.html', context)  

def diarypage(request, pk):
    diary = Diary.objects.get(pk=pk)
    context = {
        'diary' : diary,
    }
    return render(request,'diaries/diarypage.html', context)


def write(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:diarypage', diary.pk)
    else:
        form = DiaryForm()
    context = {
        'form' : form,
    }
    return render(request, 'diaries/write.html', context)


def delete(request, pk):
    diary = Diary.objects.get(pk=pk)
    diary.delete()
    return redirect("diaries:diary")


def edit(request, pk):
    if request.method == 'POST':
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(request.POST, request.FILES, instance=diary)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:diarypage', diary.pk)
    else:
        diary = Diary.objects.get(pk=pk)
        form = DiaryForm(instance=diary)
    context = {
        'diary': diary,
        'form' : form,
    }
    return render(request, 'diaries/edit.html', context)
