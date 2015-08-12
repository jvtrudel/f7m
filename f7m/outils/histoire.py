try:
    from IPython.core.display import Markdown
except:
    def Markdown(txt):
        return txt
        
import os

class Histoire(object):
    def __init__(self,content):
        self.content=content
    def md(self):
        return Markdown(self.content)
    def pdf(self,fname,title,author):
        pre="%"+title+"\n"
        pre=pre+"%"+author+"\n"
        with open(fname+".md","w") as f:
            f.write(pre+self.content)
        os.system("pandoc -o "+fname+".pdf "+fname+".md" )
        os.remove(fname+".md")
        
