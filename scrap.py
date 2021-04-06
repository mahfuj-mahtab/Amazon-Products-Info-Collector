from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

search_query=str(input("Please Input What Products You Want to Search : "))
base_url='https://www.amazon.com/s?k='+search_query.lower()
r= requests.get(base_url, headers=HEADERS)
soup=BeautifulSoup(r.content, 'html.parser')
page_number_finder = soup.find_all("li" , class_="a-disabled") #finding all li
page_number = page_number_finder[-1].text

link_collect=[] #list to collect all link
title_collect = [] #title collect
rating_collect=[] #rating collect
rating_number_collect=[] #rating number collect
split=[]
info_collect = []
left_info =[]
right_info = []

for i in range(1, int(page_number) +1):
    base_url='https://www.amazon.com/s?k='+search_query.lower()+"&page="+str(i)
    r= requests.get(base_url, headers=HEADERS)
    print(base_url)
    soup=BeautifulSoup(r.content, 'html.parser')
    a_finder=soup.find_all("a", class_="a-link-normal a-text-normal")
    for item in a_finder:
        link_collect.append("https://www.amazon.com"+item.get('href'))

for item in link_collect:
    r= requests.get(item, headers=HEADERS)
    print(item)
    soup=BeautifulSoup(r.content, 'html.parser')
    title_find = soup.find("span", class_="a-size-large product-title-word-break")
    title_collect.append(title_find.text.strip())
    rating_find=soup.find("i", class_="a-icon a-icon-star a-star-4-5")
    split = rating_find.text.split( )
    rating_collect.append(split[0])
    rating_number_finder=soup.find("span", class_="a-size-base")
    rating_number_collect.append(rating_number_finder.text)
    info_finder = soup.find("div", class_="a-section a-spacing-small a-spacing-top-small")
    info_text = info_finder.find_all("span", class_="a-size-base")
    info_num= len(info_text)
    for i in range(0, info_num-1,2):
        info_collect.append(info_text[i].text + ' : '+ info_text[i+1].text)
 

    # df= pd.DataFrame({"products title": title_collect,"Rating ": rating_collect, "Number of rater": rating_number_collect, "products info":info_collect})
    # df.to_csv("output.csv")

print(title_collect)
print(rating_collect)
print(rating_number_collect)
print(info_collect)




