import wikipediaapi
import time

# setup stuff
user_agent = "hershberg_p3_wiki (maj1hershberg@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

links_list =
def fetch_links(page):
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)
    for title in links():
        if target_page.title == links(title):
            print("yippee!!")

# start and end pages for our wikipedia game solver
start_page = wiki.page("Rocket League")
target_page = wiki.page("Microtransaction")

print(start_page.links)

wikipedia_game_solver(start_page, target_page)