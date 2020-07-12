import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "url to crawl here"

# Look for folder and if folder doesn't exist, create it
folder_location = r'C:/Users/p4ill/OneDrive/Documents/DnD'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    # Name pdf files based on the last part of the link supplied
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)

folder = 'folder path for files to be renamed'

pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(folder)
    for filename in filenames
)

for path in pathiter:
    newname =  path.replace('%20', ' ')
    newname1 =  path.replace('%27', ' ')
    newname2 =  path.replace('%5', ' ')
    if newname != path:
        os.rename(path,newname)
    if newname1 != path:
        os.rename(path,newname1)
    if newname2 != path:
        os.rename(path,newname2)
