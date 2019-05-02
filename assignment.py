#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:16:26 2019

@author: manzar
"""
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = "https://www.german-furniture-brands.com/companies"

header = "Company name, Email, Website\n"
file = open("assignment.csv", "w")
file.write(header)

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
divs = soup.findAll("div", {"class": "list-entry"})
for div in divs:
    rqsr = requests.get(urljoin(url, div.div.a.attrs['href']))
    #print(rqsr.url)
    soup_inside = BeautifulSoup(rqsr.text, "lxml")
    block = soup_inside.findAll("a", {"class": "ellips"})
    website = block[0].attrs['href']
    try:
        em = soup_inside.findAll("a", {"class": "btn btn-primary"})
        email = em[0].attrs['href'].split("mailto:")[1]
    except:
        email = 'NaN'
    #print(email.split("mailto:")[1])
    name = soup_inside.findAll("div", {"class": "mod_article first last block"})
    name = name[0].h1.text
    #print(name)
    file.write(name.replace(",", '') + "," + email.replace(",", '') + "," + website.replace(",", '') + "\n")
file.close()
import pandas
file = pandas.read_csv("assignment.csv")    