from bs4 import BeautifulSoup
import requests
import csv


def extract_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    href_list = []
    for link in soup.find_all('a', href=True):
        href_list.append(link['href'])
    return href_list


url = 'YOUR_URL_HERE'
href_list = extract_href(url)

# Save href attributes to CSV file
with open('Data/urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for href in href_list:
        writer.writerow([href])
