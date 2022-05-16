from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from management.forms import Login
from management.models import Promotion, Teacher, Year


@login_required
def index(request):
    """
    Récupère les années, les professeurs et les promotions pour les envoyer à la vue.
    """
    year = Year.objects.all()
    teacher = Teacher.objects.all()
    promotion = Promotion.objects.all()

    return render(request, 'management/index.html', {'year': year, 'teacher': teacher, 'promotion': promotion})


def user_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET['next'])
            else:
                return render(request, 'management/login.html',
                              {'form': form, 'error': 'Utilisateur et/ou les mots de pass et incorrect',
                               'next_url': request.GET['next']})
    else:
        form = Login()
        return render(request, 'management/login.html', {'form': form, 'next_url': request.GET['next']})