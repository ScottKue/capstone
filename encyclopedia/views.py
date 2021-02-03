from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        
    })
def showEntry(request, title):
    if title in util.list_entries():
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': util.get_entry(title),
            'exist': True
        })
    else:
        if title in util.list_entrie():
            return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': util.get_entry(title),
            'exist': True
        })
        else:
                return render(request, 'encyclopedia/entry.html', {
            'title': f"{title.capitalize()} not found!",
            'message': f"Do not exist a page with the name {title.capitalize()} :(",
            'exist': False
        })
def Place1(request):
    return render(request, 'Place.html')