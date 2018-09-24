#!/usr/bin/python3
# imports
# adding Template library to be able to remove and replace stuff
from string import Template

# global variables

# functions

def main():
    template_text = open('templates/base.html').read()
    template = Template(template_text)
    
    pages = [
        {
            "content": "content/index.html",
            "output_file": "docs/index.html",
            "page_title": "Home",
            "index_active_class": " active",
            "index_current_class": " <span class=\"sr-only\">(current)</span>",
            "blog_active_class": "",
            "blog_current_class": "",
            "projects_active_class": "",
            "projects_current_class": "",
            "about_active_class": "",
            "about_current_class": "",
        },
        {
            "content": "content/blog.html",
            "output_file": "docs/blog.html",
            "page_title": "Blog",
            "index_active_class": "",
            "index_current_class": "",
            "blog_active_class": " active",
            "blog_current_class": " <span class=\"sr-only\">(current)</span>",
            "projects_active_class": "",
            "projects_current_class": "",
            "about_active_class": "",
            "about_current_class": "",
        },
        {
            "content": "content/projects.html",
            "output_file": "docs/projects.html",
            "page_title": "Projects",
            "index_active_class": "",
            "index_current_class": "",
            "blog_active_class": "",
            "blog_current_class": "",
            "projects_active_class": " active",
            "projects_current_class": " <span class=\"sr-only\">(current)</span>",
            "about_active_class": "",
            "about_current_class": "",
        },
        {
            "content": "content/about.html",
            "output_file": "docs/about.html",
            "page_title": "About",
            "index_active_class": "",
            "index_current_class": "",
            "blog_active_class": "",
            "blog_current_class": "",
            "projects_active_class": "",
            "projects_current_class": "",
            "about_active_class": " active",
            "about_current_class": " <span class=\"sr-only\">(current)</span>",
        },
    ]
    
    # remove and replace data according to current page
    for page in pages:
        content = open(page['content']).read()
        rendered_page = template.safe_substitute(
            page_title=page['page_title'],
            index_active_class=page['index_active_class'],
            index_current_class=page['index_current_class'],
            blog_active_class=page['blog_active_class'],
            blog_current_class=page['blog_current_class'],
            projects_active_class=page['projects_active_class'],
            projects_current_class=page['projects_current_class'],
            about_active_class=page['about_active_class'],
            about_current_class=page['about_current_class'],
            content=content,
        )
        open(page['output_file'], 'w+').write(rendered_page)

    

# invoke main function
if __name__ == "__main__":
    main()