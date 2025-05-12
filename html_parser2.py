from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        
        
    def handle_comment(self, data):
        if  '\n' in data:
            self.data.append(">>> Multi-line Comment") 
        else:
            self.data.append(">>> Single-line Comment")
        self.data.append(data.strip())
                         
    def handle_data(self, data):
        if data.strip():
            self.data.append(">>> Data")
            self.data.append(data)
 
parser = MyHTMLParser()
html = ""         

for _ in range(int(input())):
    html += input().rstrip() + "\n"
parser.feed(html)
    
for i in parser.data :
    print(i)
    
    