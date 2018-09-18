#!/bin/bash -x

# This script is to create the MO Musial's website

# Refresh docs/
rm -rf docs/
mkdir docs/

# Copy CSS and images to docs/
cp -R css docs
cp -R images docs

cat templates/top.html content/index.html templates/bottom.html > docs/index.html
# Add page title
sed -i '' 's/${page_title}/Home | MO Musial/' docs/index.html
# Add active class to menu item
sed -i '' 's/${index_active_class}/ active/' docs/index.html
sed -i '' 's/${blog_active_class}//' docs/index.html
sed -i '' 's/${projects_active_class}//' docs/index.html
sed -i '' 's/${about_active_class}//' docs/index.html
# Add current text for screen reader
sed -i '' 's/${index_current_class}/ <span class=\"sr-only\"\>(current)\<\/span\>/' docs/index.html
sed -i '' 's/${blog_current_class}//' docs/index.html
sed -i '' 's/${projects_current_class}//' docs/index.html
sed -i '' 's/${about_current_class}//' docs/index.html

cat templates/top.html content/blog.html templates/bottom.html > docs/blog.html
# Add page title
sed -i '' 's/${page_title}/Blog | MO Musial/' docs/blog.html
# Add active class to menu item
sed -i '' 's/${index_active_class}//' docs/blog.html
sed -i '' 's/${blog_active_class}/ active/' docs/blog.html
sed -i '' 's/${projects_active_class}//' docs/blog.html
sed -i '' 's/${about_active_class}//' docs/blog.html
# Add current text for screen reader
sed -i '' 's/${index_current_class}//' docs/blog.html
sed -i '' 's/${blog_current_class}/ <span class=\"sr-only\"\>(current)\<\/span\>/' docs/blog.html
sed -i '' 's/${projects_current_class}//' docs/blog.html
sed -i '' 's/${about_current_class}//' docs/blog.html

cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html
# Add page title
sed -i '' 's/${page_title}/Projects | MO Musial/' docs/projects.html
# Add active class to menu item
sed -i '' 's/${index_active_class}//' docs/projects.html
sed -i '' 's/${blog_active_class}//' docs/projects.html
sed -i '' 's/${projects_active_class}/ active/' docs/projects.html
sed -i '' 's/${about_active_class}//' docs/projects.html
# Add current text for screen reader
sed -i '' 's/${index_current_class}//' docs/projects.html
sed -i '' 's/${blog_current_class}//' docs/projects.html
sed -i '' 's/${projects_current_class}/ <span class=\"sr-only\"\>(current)\<\/span\>/' docs/projects.html
sed -i '' 's/${about_current_class}//' docs/projects.html

cat templates/top.html content/about.html templates/bottom.html > docs/about.html
# Add page title
sed -i '' 's/${page_title}/About | MO Musial/' docs/about.html
# Add active class to menu item
sed -i '' 's/${index_active_class}//' docs/about.html
sed -i '' 's/${blog_active_class}//' docs/about.html
sed -i '' 's/${projects_active_class}//' docs/about.html
sed -i '' 's/${about_active_class}/ active/' docs/about.html
# Add current text for screen reader
sed -i '' 's/${index_current_class}//' docs/about.html
sed -i '' 's/${blog_current_class}//' docs/about.html
sed -i '' 's/${projects_current_class}//' docs/about.html
sed -i '' 's/${about_current_class}/ <span class=\"sr-only\"\>(current)\<\/span\>/' docs/about.html

open docs/index.html