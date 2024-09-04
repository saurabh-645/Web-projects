# Wikipedia - Clone Project

## Description

This project is an implementation of a Wikipedia-like online encyclopedia. Users can view, search, create, edit, and navigate encyclopedia entries, all stored in Markdown format and rendered as HTML. The project is built using Django, a Python web framework.

## Features

- **Entry Page**: Displays the content of an encyclopedia entry by visiting `/wiki/TITLE`. If the entry does not exist, an error page is shown.
- **Index Page**: Lists all encyclopedia entries, with each name clickable to view the respective entry.
- **Search**: Allows users to search for encyclopedia entries. If the search matches an entry name, the user is redirected to that entry. Otherwise, search results showing partial matches are displayed.
- **New Page**: Users can create a new encyclopedia entry. If an entry with the same title already exists, an error is shown.
- **Edit Page**: Allows users to edit an existing entry. The edit page is pre-populated with the current content.
- **Random Page**: A link to view a random encyclopedia entry.
- **Markdown to HTML Conversion**: Entries are written in Markdown and converted to HTML for display.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- [markdown2](https://github.com/trentm/python-markdown2) package

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/saurabh-645/wikipedia-clone.git
    cd wikipedia-clone
    ```

2. **Install the required Python packages**:
    ```bash
    pip install django markdown2
    ```

3. **Run the Django development server**:
    ```bash
    python manage.py runserver
    ```

4. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Project Structure

- **encyclopedia/urls.py**: Defines URL routes for the application.
- **encyclopedia/util.py**: Contains utility functions for interacting with encyclopedia entries.
- **encyclopedia/views.py**: Handles the logic for rendering different pages of the application.
- **encyclopedia/templates/encyclopedia**: Contains HTML templates for the application.

## Usage

- **Viewing Entries**: Visit `/wiki/EntryName` to view an entry.
- **Searching**: Use the search bar to find entries by name or substring.
- **Creating Entries**: Use the "Create New Page" link to add a new entry.
- **Editing Entries**: Use the "Edit" link on an entry page to modify content.
- **Random Entry**: Use the "Random Page" link to view a random entry.

## Contact

Saurabh Gupta - [saurabhgupta89691@gmail.com](mailto:saurabhgupta89691@gmail.com)

Project Link: [https://github.com/saurabh-645/wikipedia-clone](https://github.com/saurabh-645/wikipedia-clone)
