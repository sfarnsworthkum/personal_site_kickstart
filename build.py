
'''
Must have a Python script named “build.py” that generates the site
• All code in Python script must be in functions – no “loose” code (with the exception of the initial invocation of the “main()” function, see below)
• Python script must use lists to store information about all pages
• Python script must use at least one for loop to process all pages
• You must create and use at least 3 functions (it’s up to you how you separate your code into functions)
• As with before, all code must be submitted as a Pull Request
• Don’t worry about the build.sh file – you can delete that. From now on your site is Python only.
'''
def main():
    all_files = [
        {
            'file_name': 'about',
            'title': 'About Me'
        },
        {
            'file_name': 'blog',
            'title': 'Blog'
        },
        {
            'file_name': 'index',
            'title': 'Sarah Farnsworth-Kumli'
        },
        {
            'file_name': 'projects',
            'title': 'My Projects'
        },
    ]
    for item in all_files:
        create_file(item['file_name'], item['title'])


def create_file(file_name, title):
    layout = open('templates/layout.html').read()
    middle_content = open('content/' + file_name + '.html').read()
    finished_page = layout.replace('{{content}}', middle_content).replace('{{title}}', title)
    output = open('docs/' + file_name + '.html', 'w')
    output.write(finished_page)


if __name__ == '__main__':
    main()
