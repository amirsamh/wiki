from django.shortcuts import render, redirect
from . import util
from .forms import Search
from markdown2 import markdown
from random import choice

form = Search()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })


def entry(request, title):
    data = util.get_entry(title)
    if data is None:
        return render(request, "encyclopedia/error.html", {
            "form": form
        })
    return render(request, "encyclopedia/entry.html", {
        "data": markdown(data),
        "form": form,
        "title": title
    })


def random(request):
    return entry(request, choice(util.list_entries()))


def result(request):
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            query = form.cleaned_data["search"]
            list = util.list_entries()
            results = []

            for i in range(len(list)):
                if query.lower() == list[i].lower():
                    return entry(request, query)

            for i in range(len(list)):
                if query.lower() in list[i].lower():
                    results.append(list[i])

            if not results:
                return render(request, "encyclopedia/notfound.html", {
                    "query": query,
                    "form": form
                })
            else:
                return render(request, "encyclopedia/result.html", {
                    "results": results,
                    "query": query,
                    "form": form
                })


def new(request):
    if request.method == "POST":
        if request.POST.get("title") and request.POST.get("body"):
            title = request.POST.get("title")
            body = request.POST.get("body")
            list = util.list_entries()
            
            for i in range(len(list)):
                if title.lower() == list[i].lower():
                    return render(request, "encyclopedia/already.html", {
                        "title": title
                    })
                         
            util.save_entry(title, body)
            return entry(request, title)

    return render(request, "encyclopedia/new.html", {
        "form": form
    })


def edit(request):
    if request.method == "POST":
        title = request.POST.get("title")
        data = util.get_entry(title)

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "data": data,
        "title": title
    })


def show_edit(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        util.save_entry(title, body)
        
        return entry(request, title)