from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
    def handle_starttag(self, tag, attrs):
        self.data.append(f"Start : {tag}")
        for attr in attrs:
            self.data.append(f"-> {attr[0]} > {attr[1]}")
    def handle_endtag(self, tag):
        self.data.append(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        self.data.append(f"Empty : {tag}")
        for attr in attrs:
            self.data.append(f"-> {attr[0]} > {attr[1]}")

# instantiate the parser and fed it some HTML   
parser = MyHTMLParser()
for _ in range(int(input())):
    n = input()
    parser.feed(n)
    
for i in parser.data :
    print(i)