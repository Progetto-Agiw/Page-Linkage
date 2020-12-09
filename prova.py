from lxml import html



html_first_source = []
file = open('./nba/site-a/bam-adebayo.html', "r")
page = file.read()
tree = html.fromstring(page)
print(page + '\n\n')
all_leaves = tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
page = []
for elem in all_leaves:
    page.append(elem)  
html_first_source.append(page)

print(str(html_first_source[0]) + '\n\n')

