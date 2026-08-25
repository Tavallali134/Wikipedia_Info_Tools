""" Wikipedia_Info_Tools: Created by Amir Mohammad Tavallali Nia!

You can refer to this link to see my games and apps:
https://t.me/A_M_T_N134
"""

import wikipediaapi

class Wiki_Tools():
    def __init__(self):
        self.user_name = input("Enter a user name for wikipedia: ")
        self.lang = input("Enter a language, example: en, fa, uk: ")
        self.wiki = wikipediaapi.Wikipedia(user_agent=self.user_name, language=self.lang)
        self._search = None
        self.page_name = None
        self.result = None
        self.page_loaded = False

    def search(self):
        self._search = input("enter your search: ").strip()
        self.result = self.wiki.search(self._search)
        print(self.result)

    def page_title(self):
        self.page_name = input("Enter the title of the page: ").strip()
        self.result = self.wiki.page(self.page_name).title
        self.page_loaded = True
        print(self.result)

    def page_summary(self):
        self.result = self.wiki.page(self.page_name).summary
        print(self.result)

    def page_text(self):
        self.result = self.wiki.page(self.page_name).text
        print(self.result)

    def page_address(self):
        self.result = self.wiki.page(self.page_name).fullurl
        print(self.result)

    def page_links(self):
        self.result = self.wiki.page(self.page_name).links
        print(self.result)

def main():
    print("Wikipedia_Info_Tools: Created by Amir Mohammad Tavallali Nia!")
    app = Wiki_Tools()
    
    while True:
        command = input("Enter a command: ").strip()
        try:
            if command == "search":
                app.search()
            elif command == "page title":
                app.page_title()
            elif command in ["page summary", "page text", "page address", "page links"]:
                if app.page_loaded == False:
                    print("Please use 'page title' first before using page commands!")
                else:
                    if command == "page summary":
                        app.page_summary()
                    elif command == "page text":
                        app.page_text()
                    elif command == "page address":
                        app.page_address()
                    elif command == "page links":
                        app.page_links()
            elif command == "help":
                print("""Available Commands:
search: Search for pages in Wikipedia
page title: Get and display the title of a specific page
page summary: Display the summary of the loaded page
page text: Display the full text content of the loaded page
page address: Display the URL of the loaded page
page links: Display all internal links from the loaded page
exit: Exit the program

Usage Guide:
1. First use 'search' to find pages related to your topic
2. Then use 'page title' to load a specific page
3. After loading a page, you can use:
   - 'page summary' to see a brief overview
   - 'page text' to see the complete content
   - 'page address' to get the Wikipedia URL
   - 'page links' to see all links within the page

Note: Always load a page using 'page title' before using other page commands.
""")
            elif command == "exit":
                print("exiting ...")
                break
            else:
                print("invalid command ...")
        except Exception as e:
            print(e)
            break

if __name__ == "__main__":
    main()
