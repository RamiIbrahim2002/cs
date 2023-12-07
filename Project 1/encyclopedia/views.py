from django.shortcuts import render,redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    #entries = util.list_entries()
    for entry in util.list_entries():
        print(title.upper())
        print(entry.upper())
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
    return render(request,"encyclopedia/create.html")