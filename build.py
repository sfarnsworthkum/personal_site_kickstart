def main():
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
    for item in all_files:
        create_file(item['file_name'], item['title'], item['css_id'])

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

if __name__ == '__main__':
    main()
