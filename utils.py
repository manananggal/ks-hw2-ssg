#!/usr/bin/python3

# imports
import glob
import os
from jinja2 import Template
import sys
import textwrap

# global variables
all_html_files = glob.glob("content/*.html") # ['content/blog.html', 'content/index.html', 'content/about.html', 'content/projects.html']

# functions

def get_filename_no_ext(file):
    name_only, _ = os.path.splitext(os.path.basename(file))
    return name_only

def get_title(file):
    if get_filename_no_ext(file) == "index":
        title = "Home"
    else:
        title = get_filename_no_ext(file).capitalize()
    return title

def nav_loop(nav_list):
    nav = []
    for item in nav_list:
        if get_filename_no_ext(item) != "index":
            nav.append({
                "filename": os.path.basename(item),
                "title": get_title(item),
            })
    return nav

def page_loop(page_list):
    pages = []
    for page in page_list:
        pages.append({
            "content": page,
            "title": get_title(page),
            "output_file": "docs/" + os.path.basename(page),
            "nav": nav_loop(page_list)
        })
    return pages

def new_content_page():
    filename = input('Input filename (including .html): ')
    title = get_title(filename)
    template_html = open('templates/new_page.html').read()
    template = Template(template_html)
    rendered_page = template.render(page_title=title)
    open(f'content/{filename}', 'w+').write(rendered_page)

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "build":
            template_html = open('templates/base.html').read()
            template = Template(template_html)
            site_pages = page_loop(all_html_files)
            generate_site(site_pages, template)

        elif command == "new":
            new_content_page()
    else:
        print(textwrap.dedent('''
            Usage:
            Rebuild site:    python manage.py build
            Create new page: python manage.py new
            '''))

def read_content(path):
    content = open(path).read()
    return content
    
def generate_site(page_list, template_file):
    for page in page_list:
        content = read_content(page['content'])
        rendered_page = template_file.render(
            page_title=page['title'],
            active=page['title'],
            nav=page['nav'],
            content=content,
        )
        open(page['output_file'], 'w+').write(rendered_page)
