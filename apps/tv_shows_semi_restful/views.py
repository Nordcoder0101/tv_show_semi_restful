from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context ={
      'all_shows': Show.objects.all()
    }
    return render(request, 'tv_shows_semi_restful/all_shows.html', context)

def display_add_show(request):
    return render(request, 'tv_shows_semi_restful/new_show.html')

def create_show(request):
    if request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']

        print(description, title, network)

        new_show = Show.objects.create(title = title, network = network, release_date = release_date, description =  description)

        print(new_show)
        
        return redirect('/shows')
        
def view_edit_show(request, number):
    show_to_edit = Show.objects.get(id=number)
    context = {
      'current_show': show_to_edit
    }
    return render(request,'tv_shows_semi_restful/edit_show.html',context)

def edit_show(request, number):
    if request.method == "POST":
      show_to_edit = Show.objects.get(id=number)
      show_to_edit.title = request.POST['title']
      show_to_edit.network = request.POST['network']
      show_to_edit.release_date = request.POST['release_date']
      show_to_edit.description = request.POST['description']
      show_to_edit.save()

      return redirect(f'/shows/{number}')

def display_show(request, number):
    show_to_display = Show.objects.get(id=number)
    context = {
      'current_show': show_to_display
    }
    return render(request, 'tv_shows_semi_restful/display_show.html', context)

def delete_show(request,number):
    show_to_delete = Show.objects.get(id=number)
    show_to_delete.delete()
    print('delete successful')
    return redirect ('/shows')
