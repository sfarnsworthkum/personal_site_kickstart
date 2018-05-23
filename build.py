top_content = open('templates/top.html').read()
middle_content = open('content/index.html').read()
bottom_content = open('templates/bottom.html').read()

all_files = top_content + middle_content + bottom_content
output = open('docs/index.html', 'w')
output.write(all_files)




