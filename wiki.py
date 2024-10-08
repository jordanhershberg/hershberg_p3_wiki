import wikipediaapi
import time

# setup stuff
user_agent = "hershberg_p3_wiki (maj1hershberg@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    print("Working on it...")
    start_time = time.time()

    queue = Queue() # queue for which items to check next
    visited = set() # keeps track of visited links
    parent = {} # dictionary to keep track of parent

    # start off by adding the start page to our queue and visited

    queue.put(start_page.title)
    visited.add(start_page.title)

    # keep looping as long as queue is now empty
    while not queue.empty():
        # get next item in our queue
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break

    



# start and end pages for our wikipedia game solver
start_page = wiki.page("Rocket League")
target_page = wiki.page("First-person shooter")
wikipedia_game_solver(start_page, target_page)