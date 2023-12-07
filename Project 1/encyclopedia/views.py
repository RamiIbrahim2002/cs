from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    entries = util.list_entries()
    if title in entries : 
        return render(request, "encyclopedia/article.html", {
                "name": title,
                "markdown": util.convert_to_html(util.get_entry(title))
            })
    else :
        return render(request, "encyclopedia/error.html", {
            "error": 'no such article',
        })

