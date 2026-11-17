""" Wikipedia_Info_Tools: Created by Amir Mohammad Tavallali Nia!

You can refer to this link to see my games and apps:
https://t.me/A_M_T_N134
"""

import wikipediaapi

class WikiTools:
    def __init__(self, user_name, language ):
        self.user_name = user_name
        self.lang = language
        self.wiki = wikipediaapi.Wikipedia(user_agent=self.user_name, language=self.lang)
        self._page = None

    def search(self, query):
        return self.wiki.search(query)

    def load_page(self, title):
        page = self.wiki.page(title)
        if page.exists():
            self._page = page
            return page.title
        else:
            self._page = None
            return None

    def page_summary(self):
        return self._page.summary

    def page_text(self):
        return self._page.text

    def page_address(self):
        return self._page.fullurl

    def page_links(self):
        return self._page.links

def main():
    print("Wikipedia_Info_Tools: Created by Amir Mohammad Tavallali Nia!")

    user_name = input("Enter a user Name:")
    language = input("Enter a language:")
    app = WikiTools(user_name, language)
    
    while True:
        command = input("Enter a command: ").strip().lower()
        try:
            if command == "search":
                query = input("enter your search: ").strip()
                results = app.search(query)
                if results.totalhits == 0: print("Nothing found!")
                else:
                    for i, title in enumerate(results, 1): print(f"{i}. {title}")
            elif command == "load page":
                page_title = input("Enter the page:").strip()
                print(app.load_page(page_title))
            elif command in ["page summary", "page text", "page address", "page links"]:
                if app._page is None: print("Please use 'load page' first before using page commands!")
                else:
                    if command == "page summary": print(app.page_summary())
                    elif command == "page text": print(app.page_text())
                    elif command == "page address": print(app.page_address())
                    elif command == "page links":
                        for l in app.page_links(): print(l)
            elif command == "help":
                print("""Available Commands:
search: Search for pages in Wikipedia
load page: Get and display the title of a specific page
page summary: Display the summary of the loaded page
page text: Display the full text content of the loaded page
page address: Display the URL of the loaded page
page links: Display all internal links from the loaded page
exit: Exit the program

Usage Guide:
1. First use 'search' to find pages related to your topic
2. Then use 'load page' to load a specific page
3. After loading a page, you can use:
   - 'page summary' to see a brief overview
   - 'page text' to see the complete content
   - 'page address' to get the Wikipedia URL
   - 'page links' to see all links within the page

Note: Always load a page using 'load page' before using other page commands.
""")
            elif command == "exit":
                print("exiting ...")
                break
            else:
                print("invalid command ...")
                continue
        except Exception as e:
            print(e)
            break

if __name__ == "__main__":
    main()
