import csv
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import random
import pandas as pd

# name of the csv file to store the data
CSV_FILE = 'data.csv'

# URL of the page to scrape
URL = 'https://archiveofourown.org/media/Books%20*a*%20Literature/fandoms'
BASE_URL = 'https://archiveofourown.org'

# Initialize the WebDriver
def initialize_driver():
    """
    return: WebDriver instance (Chrome in this case)
    """    
    driver = webdriver.Firefox()
    return driver

# Random sleep to mimic human behavior
def random_sleep(min_time=4, max_time=7):
    """
    delays program execution for a random amount of time between min_time and max_time
    here uniform function is used which takes decimal values as well and not just whole numbers
    thus showing somewhat more natural human behavior

    :param min_time: minimum time to sleep, default value is 4
    :param max_time: maximum time to sleep, default value is 7

    we use a range of 4-7 seconds as selenium sometimes requires quite a bit of time to load the page
    """
    sleep_time = random.uniform(min_time, max_time)
    sleep(sleep_time)

# Get BeautifulSoup object from the current page
def get_soup(driver):
    """
    :param driver: WebDriver instance
    :return: BeautifulSoup object
    """
    return BeautifulSoup(driver.page_source, 'lxml')

# Main function
def main():
    """
    the main flow is as follows
    - driver is initialized and the url is opened
    - soup object is created and the random sleep function is called
    - url of each set of books is obtained
    - csv file is opened and headers are written
    - iterates over each url obtaining url of chapters and then opens each chapter url
    - title, content, rating and additional_tags are created which contain the respective information
    - the details are written to the csv file
    - index is incremented by 1
    """
    driver = initialize_driver()
    driver.get(URL)

    soup = get_soup(driver)
    random_sleep()
    books_ul_list = soup.find_all('ul', class_='tags index group')

    books_url_list = []
    for books_ul in books_ul_list:
        book_li_list = books_ul.find_all('li')
        for book_li in book_li_list:
            book_url = book_li.find('a')['href']
            books_url_list.append(book_url)

    fixed_url_list = []
    for book_url in books_url_list:
        fixed_url_list.append(BASE_URL + book_url) # append the base url to the book url to get the full url

    chapters_url = []
    index = 1
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write CSV header
        csv_writer.writerow(['URL', 'Title', 'Content', 'Rating', 'Additional Tags'])
        for book_url in fixed_url_list:
            driver.get(book_url)
            random_sleep()
            soup = get_soup(driver)
            chapters_div_list = soup.find_all('div', class_='header module')
            for chapter_div in chapters_div_list:
                chapter_url = chapters_div.find('a')['href']
                url = BASE_URL + chapter_url
                if url:
                    driver.get(url)
                    random_sleep()
                    soup = get_soup(driver)

                    try:
                        title = soup.find('h2', class_='title heading').text.strip()
                    except:
                        title = 'Not Found'

                    try:
                        content_element = soup.find('div', class_='userstuff module')
                        content = content_element.text.strip()
                    except:
                        content = 'Not Found'

                    try:
                        rating_element = soup.find('dd', class_='rating tags')
                        rating = rating_element.text.strip()
                    except:
                        rating = 'Not Found'

                    try:
                        additional_tags_element = soup.find('dd', class_='freeform tags')
                        additional_tags = additional_tags_element.text.strip()
                    except:
                        additional_tags = 'Not Found'

                    # Write product information to the CSV file
                    csv_writer.writerow([url, title, content, rating, additional_tags])
                    print(index)
                    index = index + 1

    driver.quit()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()