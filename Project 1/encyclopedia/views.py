from django.shortcuts import render,redirect

from . import util
from . import forms
import random
from django.core.files import File

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    #entries = util.list_entries()
    for entry in util.list_entries():
        #print(title.upper())
        #print(entry.upper())
        if title.upper() == entry.upper() : 
            return render(request, "encyclopedia/article.html", {
                    "name": title,
                    "markdown": util.convert_to_html(util.get_entry(title))
                })
    return render(request, "encyclopedia/error.html", {
        "error": 'no such article',
    })

def search(request):
    searched = request.GET['q']
    for entry in util.list_entries():
        #print(entry.upper())
        if entry.upper() == searched.upper() :
            return redirect("entry" , title = searched)
    else:
        results = []
        for entry in util.list_entries():
            #print(searched in entry)
            if searched.upper() in entry.upper():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "results": results
        })
    
def create(request):
    if request.method =="POST":
        form = forms.new_article_form(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            title = form.cleaned_data['article_title']
            content = form.cleaned_data['article_content']
            if title.upper() in (x.upper() for x in util.list_entries()):
                return render(request, 'encyclopedia/error.html', {
                    "error": 'article already exist'
                })
            else :
                #print("i used save_entry !!! ")
                util.save_entry(title,content)
                return redirect("entry", title=title)
            
    else :
        form = forms.new_article_form()
        return render(request, "encyclopedia/create.html", {
            'form': form
        })
    
def randome(request):
    random_integer = random.randint(0,len(util.list_entries())-1)
    random_article = util.list_entries()[random_integer]
    print(random_article)
    return render(request,'encyclopedia/article.html',{
        "name": random_article,
        "markdown": util.convert_to_html(util.get_entry(random_article))
    })





