import re
import os
from posixpath import splitext
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files import File


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    with open(filename, "w", encoding="utf-8") as f:
        file = File(f)
        file.write(content)


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    for dirpath, dirnames, filenames in os.walk("entries"):
        for filename in filenames:
           
            no_ext_file = splitext(filename)[0]

            if no_ext_file.lower() == title.lower():
                print(filename)
                try:
                    f = default_storage.open(f"entries/{title}.md")
                    return f.read().decode("Windows-1251")#"utf-8"

                except FileNotFoundError:
                    return None
        return None
