import bs4 as bs
import time
import urllib.request
url = input("enter the url for product")
your_price = int(input("enter the expected price"))
index = url.find("B0")
index = index + 10
url = url[:index]
while(1):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    page = resp.read()

    soup = bs.BeautifulSoup(page, 'html.parser') 
    js_test = soup.find('span', id ='priceblock_ourprice') 
    if js_test is None: 
        js_test = soup.find('span', id ='priceblock_dealprice')         
    str = "" 
    numbers = ['0','1','2','4','5','6','7','8','9']
    for line in js_test.stripped_strings : 
        str = line 
        val = ""
        print(str)
        for letter in str:
            if(letter in numbers):
                val = val + letter
            elif(letter == '.'):
                break
    
        # convert to integer 
        current_price = int(val)
    
        if current_price < your_price : 
            print("Price decreased book now")
            
         
        else: 
            print("Price is high please wait for the best deal")
        time.sleep(3600)