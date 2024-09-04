import random
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
import markdown2
from django import forms

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    # Fetches the entry content based on the title
    entry_content = util.get_entry(title)
    
    # Checks if the entry exists
    if entry_content is None:
        return render(request, "encyclopedia/error.html", status=404)
    
    # Converts Markdown content to HTML
    entry_html = markdown2.markdown(entry_content)

    entries = util.list_entries()

    for entry in entries:
        if title == entry.lower():
            title = entry
            break

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry_html,
    })

#search and entry have redundancy fix that
def search(request):

    query = request.GET.get('q', "").strip().lower()

    if query:
        entries = util.list_entries()
        matched_entries = []

        # If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
        for entry in entries:
            if query == entry.lower():
                # Exact match, redirect to the entry page
                return redirect('encyclopedia:entry', title=entry)
            elif query in entry.lower():
                # Partial match, add to the results list
                matched_entries.append(entry)
        
        
        # If no exact match, render the search results page
        return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "results": matched_entries
        })
    
    # If no query provided, redirect back to the index page or handle it as needed
    return redirect("encyclopedia:index")


def create(request):
    
    # Check if method is POST
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            util.save_entry(title, content)

            return redirect('encyclopedia:entry', title=title)
        
    else:
        form = NewEntryForm()

    return render(request, "encyclopedia/create.html", {
        "form": form
    })

def validate_title(value):
    forbidden_titles = util.list_entries()
    value = value.lower()
    for title in forbidden_titles:
        if value == title.lower():
            raise ValidationError(f"The title '{value}' already exists.")        

class NewEntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=True, validators=[validate_title])
    content = forms.CharField(label='Markdown content for the page', required=True, widget=forms.Textarea(attrs={'id': 'content'}))

class EditForm(forms.Form):
    content = forms.CharField(label='Markdown content for the page', required=True, widget=forms.Textarea(attrs={'id': 'content'}))

def edit(request):

    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            title = request.session.get('original_title', "")
            content = form.cleaned_data['content']

            util.save_entry(title, content)

            return redirect('encyclopedia:entry', title=title)



    title = request.GET.get('title', "")

    entry_content = util.get_entry(title)

    if entry_content is None:
        return render(request, "encyclopedia/error.html", status=404)
    
    # Store the original title in session to prevent tampering
    request.session['original_title'] = title

    initial_data = {'content': entry_content, 'title': title}
    form = EditForm(initial=initial_data)

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": form
    })

def random_page(request):
    title = random.choice(util.list_entries())

    return redirect('encyclopedia:entry', title=title)