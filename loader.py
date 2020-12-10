import os
from lxml import html


class Loader:
    
    def load_pages_leaves(self,path,site,limit):
        pages = []
        path = os.path.join(path,site)
        files = sorted(os.listdir(path))[:limit]
        for filename in files:
            filename = os.path.join(path,filename)
            file = open(filename, "r")
            page = file.read()
            tree = html.fromstring(page)
            all_leaves = tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
            page = ""
            for elem in all_leaves:
                page = page + " "+ elem 
            pages.append(page)
        return pages
    

