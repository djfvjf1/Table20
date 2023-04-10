from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import NameForm
from .models import Table


def new_form(request):
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        # check if form data is valid
        if form.is_valid():
            #form.save(commit=False)
            form.author = request.user
            table = form.save()
            return redirect('/tables/table/' + str(table.id) + '/')
    else:
        form = NameForm()
     

    return render(request, "form/form.html", {'form': form})

def table_page(request, pk):
    table = Table.objects.get(id=pk)
    return render(request, "form/table_page.html", {'table': table})
