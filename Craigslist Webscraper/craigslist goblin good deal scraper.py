# Import libraries that will allow us to scrape the chosen website for it's html data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import time


# Define a driver path for the chromium driver, as well as define the base URL to be worked with
DRIVER_PATH = 'C:\\py-app-dependencies\\chromedriver.exe'
BASEURL = 'https://vancouver.craigslist.org'
QUERY = 'rtx'
#QUERY = input('Enter your search keyword: ').lower()


# Required selenium cringe
options = Options()
options.headless = True
options.add_argument('--window-size=1920,1200')

# Define the driver variable via the webdriver plugin
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Define an empty list for use later with a defined function
totalPosts = []

# Define a function that will step through all the given pages for our desired section of craigslist via recursion
def stepThroughPages(posts, pageLink):
    
    driver.get(BASEURL + pageLink)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    nextButton = soup.find('a', class_='next')
    posts.extend(soup.find_all('li', 'result-row'))

    if nextButton is None: return posts
    return stepThroughPages(posts, nextButton.get('href'))

# Define a function to output the results of the search, including the title, price, time since posted, and URL.
def outputResults(posts):
    for i, post in enumerate(posts):
        titleDiv = post.find('a', class_='result-title')

        postTitle = titleDiv.get_text()
        postTimeText = post.find('time').get('datetime')
        postPrice = post.find('span', class_='result-price').get_text()
        postURL = titleDiv.get('href')

        postTime = datetime.strptime(postTimeText, '%Y-%m-%d %H:%M')
        elapsedMinutes = (datetime.now() - postTime)

        print(f'{postTitle}: {postPrice} || {elapsedMinutes} || {postURL}')


# Call the function previously defined to step through the pages of the given website
totalPosts = stepThroughPages([], '/search/syp')
#totalPosts = stepThroughPages([], '/d/pets/search/pet')
# Filter the posts gathered previously for the desired search object
totalPosts = [post for post in totalPosts if QUERY in post.find('a', class_='result-title').get_text().lower()]

# Display the amount of results for a given search
print(f'{len(totalPosts)} results containing: {QUERY}')

# Add time delay for readability increase
time.sleep(2)

# Call the function previously defined to list the gathered posts
outputResults(totalPosts)

# Quit the chromium driver called on earlier.
driver.quit