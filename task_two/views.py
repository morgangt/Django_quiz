from django.shortcuts import render
from .models import Action_User
from .forms import Action_UserForm
from django.contrib.auth.models import User
from django.utils import timezone
import datetime 


def task_two(request):
    forma = Action_UserForm()
    the_user = request.user
    today = datetime.date.today()

    if the_user.is_authenticated():
        last_action = Action_User.objects.filter(user=the_user).last()
        if request.method == "POST":
            set_form = Action_UserForm(request.POST)
            if set_form.is_valid():
                action = set_form.save(commit=False)
                action.user = request.user
                action.date = timezone.now()
                action.save()
    else:
        return render(request, 'task_two.html', {"error": "Please log in"})
    return render(request, 'task_two.html', {"form": forma, "user": request.user, "action": last_action})
