top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()


content = open('index.html').read()
index_html = top + content + bottom
open('index.html', 'w+').write(index_html)


content = open('about.html').read()
about_html = top + content + bottom
open('about.html', 'w+').write(about_html)


content = open('resume.html').read()
resume_html = top + content + bottom
open('resume.html', 'w+').write(resume_html)
