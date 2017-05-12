from django.shortcuts import render
from models import Transportation, TRANSPORT_CAT
from django.utils import timezone
from .forms import NewTransForm
# Bad option, print this date

def task_one(request):
    response = Transportation.objects.all()
    forma = NewTransForm()
    if request.method == "POST":
        set_form = NewTransForm(request.POST)
        if set_form.is_valid():
            post = set_form.save(commit=False)
            post.save()
    return render(request, 'task_one.html', {'trans': response, 'cats': TRANSPORT_CAT, 'form': forma, 'date_create': timezone.now()})
