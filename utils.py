#!/usr/bin/python3

# imports
import glob
import os
from jinja2 import Template

# global variables
all_html_files = glob.glob("content/*.html") # ['content/blog.html', 'content/index.html', 'content/about.html', 'content/projects.html']

# functions
def get_filename(file):
    return os.path.basename(file)

def get_filename_no_ext(file):
    name_only, _ = os.path.splitext(get_filename(file))
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
                "filename": get_filename(item),
                "title": get_title(item),
            })
    return nav

def page_loop(page_list):
    pages = []
    for page in page_list:
        pages.append({
            "content": page,
            "title": get_title(page),
            "output_file": "docs/" + get_filename(page),
            "nav": nav_loop(page_list)
        })
    return pages

def main():
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    site_pages = page_loop(all_html_files)
    generate_site(site_pages, template)

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