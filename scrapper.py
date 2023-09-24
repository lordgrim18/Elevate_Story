import csv
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import re
import random
import unicodedata
import pandas as pd

CSV_FILE = 'data.csv'

URL = 'https://archiveofourown.org/media/Books%20*a*%20Literature/fandoms'
BASE_URL = 'https://archiveofourown.org'

# Initialize the WebDriver
def initialize_driver():
    driver = webdriver.Firefox()
    return driver

# Random sleep to mimic human behavior
def random_sleep(min_time=4, max_time=7):
    sleep_time = random.uniform(min_time, max_time)
    sleep(sleep_time)

# Get BeautifulSoup object from the current page
def get_soup(driver):
    return BeautifulSoup(driver.page_source, 'lxml')

# Main function
def main():

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
        fixed_url_list.append(BASE_URL + book_url)

    all_books_url = []
    fixed_all_books_url = []

    # for book_url in fixed_url_list:
    #     print(len(all_books_url))
    #     if (len(all_books_url) < 50):
    #         driver.get(book_url)
    #         random_sleep()
    #         soup = get_soup(driver)
    #         books_div_list = soup.find_all('div', class_='header module')
    #         for books_div in books_div_list:
    #             book_url = books_div.find('a')['href']
    #             fixed_all_books_url.append(BASE_URL + book_url)
    #     else :
    #         break

    # for book_url in all_books_url:
    #     fixed_all_books_url.append(BASE_URL + book_url)

    index = 1
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write CSV header
        csv_writer.writerow(['URL', 'Title', 'Content', 'Rating', 'Additional Tags'])
        for book_url in fixed_url_list:
            print(len(all_books_url))
            driver.get(book_url)
            random_sleep()
            soup = get_soup(driver)
            books_div_list = soup.find_all('div', class_='header module')
            for books_div in books_div_list:
                book_url = books_div.find('a')['href']
                url = BASE_URL + book_url
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

    #     # Open the CSV file for writing
    # with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     # Write CSV header
    #     csv_writer.writerow(['URL', 'Title', 'Content', 'Rating', 'Additional Tags'])
        
    #     # Iterate through each product and extract information
    #     for index, url in enumerate(fixed_all_books_url, start=1):
    #         if url:
    #             driver.get(url)
    #             random_sleep()
    #             soup = get_soup(driver)

    #             try:
    #                 title = soup.find('h2', class_='title heading').text.strip()
    #             except:
    #                 title = 'Not Found'

    #             try:
    #                 content_element = soup.find('div', class_='userstuff module')
    #                 content = content_element.text.strip()
    #             except:
    #                 content = 'Not Found'

    #             try:
    #                 rating_element = soup.find('dd', class_='rating tags')
    #                 rating = rating_element.text.strip()
    #             except:
    #                 rating = 'Not Found'

    #             try:
    #                 additional_tags_element = soup.find('dd', class_='freeform tags')
    #                 additional_tags = additional_tags_element.text.strip()
    #             except:
    #                 additional_tags = 'Not Found'

    #             # Write product information to the CSV file
    #             csv_writer.writerow([url, title, content, rating, additional_tags])
    #             print(index)





    print(f"Data written to {CSV_FILE}")
    driver.quit()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()