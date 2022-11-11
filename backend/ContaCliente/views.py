from django.shortcuts import render
from .forms import ClienteForm
def home_view(request):
    context = {}

    form = ClienteForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "home.html", context)

