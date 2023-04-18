from bs4 import BeautifulSoup as bfs
import requests
from csv import writer
import time
from selenium import webdriver

property_type = 'mieszkanie'
region = 'slaskie'
driver = webdriver.Chrome(r'C:\Users\krzys\Downloads\chromedriver')
ad_count = 0

url = f'https://www.otodom.pl/pl/oferty/sprzedaz/{property_type}/{region}'

def driver_scrape_page(url, wait_time = 0.5):
    driver.get(url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(wait_time)

driver_scrape_page(url)
doc = bfs(driver.page_source, 'html.parser')
# last_page_number = doc.find(attrs = { 'data-cy' : 'search-list-pagination' }).find_all('button', class_ = 'eo9qioj1 css-ehn1gc e1e6gtx31')[-2].text
last_page_number = 10

with open(f'{property_type}_{region}.csv', 'w', encoding='utf-8', newline='') as file:
    csv_writer = writer(file)
    header = ['obszar', 'lokacja', 'cena', 'przestrzeń_m2', 'cena_m2', 'ilość pokoi']
    csv_writer.writerow(header)

    for page in range(1, int(last_page_number) + 1):
        print(f'scraping page {page}')
        page_url = f'{url}?page={page}'
        driver_scrape_page(page_url)

        parsed_page = bfs(driver.page_source, 'html.parser')
        items_container = parsed_page.find(attrs={ 'data-cy' : 'search.listing.organic' })
        listing_items = items_container.find_all('li', class_ = 'css-iq9jxc e1n6ljqa1')
        ad_count += (len(listing_items))

        for listing_item in listing_items:
            item = listing_item.a
            link = item['href']
            location = item.find('p', class_ = 'css-14aokuk e1n6ljqa7').text
            description = list(item.find('div', class_= 'e1n6ljqa19 css-6vtodn ei6hyam0'))

            price = None if ("Zapytaj" in description[0].text or 'od' in description[0].text) else ''.join(description[0].text.split('\xa0')[:-1]).replace(',','.')
            sq_price = ''.join(description[1].text.split('\xa0')[:-1]).replace(',','.') if len(str(description[1].text).split('\xa0')[0]) > 0 else None
            num_rooms = description[2].text.split(' ')[0]
            sq_meters = description[3].text.split(' ')[0]

            csv_writer.writerow([region, location, price, sq_meters, sq_price, num_rooms])

driver.quit()
print(f'Number of ads: {ad_count}')