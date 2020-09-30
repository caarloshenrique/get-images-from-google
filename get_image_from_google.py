# -*- coding: utf-8 -*-
###############################################################
# Get images from google images
###############################################################
import time
import urllib
import os
from bs4 import BeautifulSoup
from mechanize import Browser

keyword = "bird"
url_google = "https://www.google.com/imghp?hl=pt-BR&q="

timestamp = time.asctime()

br = Browser()
br.set_handle_robots(False)
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open(url_google + keyword)
br.select_form(nr=0)
page = br.submit()
content = page.read()
# print(content)

soup = BeautifulSoup(content, "html.parser")

# procura por imagens no html
links = soup.find_all('img', src=True)

counter_img = 1

# cria a pasta com o nome da palavra buscada
try:
    os.mkdir(keyword)
except OSError:
    print("Creation of the directory %s failed" % keyword)


print "###################################"
print "Downloading Images of " + keyword
print "###################################"

# ignora primeiro link da busca (logo google)
for linkdata in links[1:]:
    link = linkdata["src"].split("src=")[-1]
    print "Downloading Image " + keyword + str(counter_img) + '.jpg ...'
    f = open(keyword + '/' + keyword + str(counter_img) + '.jpg', 'wb')
    f.write(urllib.urlopen(link).read())
    f.close()
    print link
    counter_img += 1
