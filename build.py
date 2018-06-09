import glob
import os
from jinja2 import Template

def main():
    all_html_files = glob.glob("content/*.html")

    for x in all_html_files:
        file_path = x
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        title = name_only.title()
        print(file_path, file_name, name_only, title)
        file_html = open(file_name).read()
        template_html = open("templates/layout.html").read()
        template = Template(template_html)
        template.render(
            title=title,
            content=file_html,
        )
#still need to figure out css id templating 

'''

jinja example:
index_html = open("index.html").read()
template_html = open("base.html").read()
template = Template(template_html)
template.render(
    title="Homepage",
    content=index_html,
)
'''

#------previous solution----------

'''
    all_files = [
        {
            'file_name': 'about',
            'title': 'About Me',
            'css_id': 'about'
        },
        {
            'file_name': 'blog',
            'title': 'Blog',
            'css_id': 'blog'
        },
        {
            'file_name': 'index',
            'title': 'Sarah Farnsworth-Kumli',
            'css_id' : 'index'
        },
        {
            'file_name': 'projects',
            'title': 'My Projects',
            'css_id': 'projects'
        },
    ]
'''

    #for item in all_files:
        #create_file(item['file_name'], item['title'], item['css_id'])

'''
def create_file(file_name, title, css_id):
    layout = open('templates/layout.html').read()
    middle_content = open('content/' + file_name + '.html').read()
    finished_page = construct_page(layout, middle_content, title, css_id)
    write_to_docs(file_name, finished_page)

def construct_page(layout, middle_content, title, css_id):
    constructed_page = layout.replace('{{content}}', middle_content).replace('{{title}}', title).replace('{{id}}', css_id)
    return constructed_page

def write_to_docs(file_name, finished_page):
    output = open('docs/' + file_name + '.html', 'w')
    output.write(finished_page)
'''

if __name__ == '__main__':
    main()
