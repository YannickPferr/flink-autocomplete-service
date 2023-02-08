import requests
from bs4 import BeautifulSoup
import config
import json

def code_block_to_str(code_snippet):
    code_str = ""
    # find all lines of this code snippet
    lines = code_snippet.find_all("span", class_="line")
    for idx, line in enumerate(lines):
        # get the words from each line and add them to the string
        words = line.find("span", class_="cl").find_all("span")
        for word in words:
            code_str += word.text
        
        # add a line break if it's not the last line
        if idx != len(lines) - 1:
            code_str += "\n"
    return code_str

def get_all_sql_code_snippets(url):
    # get the page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # find all sql code snippets on the page
    code_snippets = soup.find_all("code", class_="language-sql")
    code_snippet_strings = []
    # turn each code snippet into a string
    for code_snippet in code_snippets:
        code_snippet_strings.append(code_block_to_str(code_snippet))
    return code_snippet_strings

def get_all_relevant_pages():
    page = requests.get(config.scrape_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # navigate to sql accordeon: aside -> nav -> ul -> fourth li -> ul -> third li -> ul -> eighth li
    side_bar = soup.find("aside", class_="book-menu")
    nav_bar = side_bar.find("nav")
    nav_ul = nav_bar.find("ul", recursive=False).findChildren(recursive=False)
    app_dev_ul = nav_ul[3].find("ul", recursive=False).findChildren(recursive=False)
    table_api_and_sql_ul = app_dev_ul[2].find("ul", recursive=False).findChildren(recursive=False)
    sql_ul = table_api_and_sql_ul[7].find("ul", recursive=False)

    # find all list elements in SQL accordeon
    relevant_pages = sql_ul.find_all("li")
    # store relevant pages with urls in dict
    pages_to_scrape = {}
    for child in relevant_pages:
        a = child.find("a")
        pages_to_scrape[a.text] = "http:" + a["href"]
    return pages_to_scrape

# main
if not hasattr(config, "scrape_pages_to_scrape"):
    print("finding all relevant pages")
    config.scrape_pages_to_scrape = get_all_relevant_pages()
    print(config.scrape_pages_to_scrape)
    print()

print("finding all code snippets from relevant pages")
# get code snippets from relevant pages
code_snippets = {}
for page in config.scrape_pages_to_scrape:
    code_snippets[page] = get_all_sql_code_snippets(config.scrape_pages_to_scrape[page])

with open('snippets.json', 'w') as fp:
    json.dump(code_snippets, fp, indent=2)