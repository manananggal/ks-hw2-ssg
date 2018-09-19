#! /usr/bin/python3

#This Python3 script will build mo_musial website
print("Hello World!")

#adding Template library to be able to remove and replace stuff
from string import Template
template_text = open('templates/template.html').read()
template = Template(template_text)

# open to read index.html file and define it as the content for the Home page
# Combines earlier defined top and bottom HTML template code 
# with index content HTML code to create complete home page
# add Home to title 
# add active class to mo_musial home/logo 
# adds span to let screen reader it is current page
# gives me write capabilities to file
# code:
index_content = open('content/index.html').read()
index_html = template.safe_substitute(
    page_title="Home",
    index_active_class=" active",
    index_current_class=" <span class=\"sr-only\">(current)</span>",
    blog_active_class="",
    blog_current_class="",
    projects_active_class="",
    projects_current_class="",
    about_active_class="",
    about_current_class="",
    content=index_content,
)
open('docs/index.html', 'w+').write(index_html)

# sets blog.html file as the content for the Blog page
# Combines earlier defined top and bottom HTML template code 
# with Blog content HTML code to create complete Blog page
# updates blog title, 
# makes blog nav link active, 
# adds span to let screen reader it is current page
# code:
blog_content = open('content/blog.html').read()
blog_html = template.safe_substitute(
    page_title="Blog",
    index_active_class="",
    index_current_class="",
    blog_active_class=" active",
    blog_current_class=" <span class=\"sr-only\">(current)</span>",
    projects_active_class="",
    projects_current_class="",
    about_active_class="",
    about_current_class="",
    content=blog_content,
)
open('docs/blog.html', 'w+').write(blog_html)

# open to read projects.html file and define it as the content for the Projects page
# Combine earlier defined top and bottom HTML template code 
# with Project page content HTML code to create complete Project page
# remove and replace updates for Projects page
# adding span to give screen reader it is current page
# code:
projects_content = open('content/projects.html').read()
projects_html = template.safe_substitute(
    page_title="Projects",
    index_active_class="",
    index_current_class="",
    blog_active_class="",
    blog_current_class="",
    projects_active_class=" active",
    projects_current_class=" <span class=\"sr-only\">(current)</span>",
    about_active_class="",
    about_current_class="",
    content=projects_content,
)
open('docs/projects.html', 'w+').write(projects_html)

# open to read about.html file and define it as the content for the About page
# Combine earlier defined top and bottom HTML template code 
# with About page content HTML code to create complete About page
# remove and replace updates for About page
# to update About page to let screen reader know it is the current page
# code:
about_content = open('content/about.html').read()
about_html = template.safe_substitute(
    page_title="About",
    index_active_class="",
    index_current_class="",
    blog_active_class="",
    blog_current_class="",
    projects_active_class="",
    projects_current_class="",
    about_active_class=" active",
    about_current_class=" <span class=\"sr-only\">(current)</span>",
    content=about_content,
)
open('docs/about.html', 'w+').write(about_html)
