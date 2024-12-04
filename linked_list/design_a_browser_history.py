class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Browser:
    def __init__(self,home_page):
        self.current_page = Node(home_page)
    
    def visit(self,url):
        new_node = Node(url)
        self.current_page.next = new_node
        new_node.prev = self.current_page
        self.current_page = self.current_page.next

    def back(self,steps):
        while steps!=0:
            if self.current_page.prev:
                self.current_page = self.current_page.prev
                steps -= 1
            else:
                break
        
        return self.current_page.data
    

    def forward(self,steps):
        while steps:
            if self.current_page.next:
                self.current_page = self.current_page.next
                steps -= 1
            else:
                break
            
        return self.current_page.data


if __name__ == "__main__":
    browser = Browser("homepage.com")
    queries = [
        ["visit", "google.com"],
        ["visit", "Bing.com"],
        ["back","1"],
        ["forward",'1']
    ]

    print(queries)


    for query in queries:
        if query[0] == "visit":
            print("Visited",query[1])
            browser.visit(query[1])

        elif query[0] == "back":
            print("Back",query[1],"Steps:", end = " ")
            print(browser.back(int(query[1])))
        
        else:
            print("Forward",query[1],"Steps:",end = " ")
            print(browser.forward(int(query[1])))
