import sys
top_content = open('templates/top.html').read()
middle_content = open(sys.argv[1]).read()
bottom_content = open('templates/bottom.html').read()

all_files = top_content + middle_content + bottom_content
output = open('docs/' + sys.argv[2], 'w')
output.write(all_files)




