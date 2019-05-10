from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/index.html', {'lottos': lottos})

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            #return redirect(index)
            return render(request, 'lotto/index.html', {})
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})
