import requests
from bs4 import BeautifulSoup
import json

topicDb = []
topicDic = dict()

# key-value Pair
productList = {"AirPods": ["Airpods", "AirPods", "airpods"],  
               "MacBook": ["MacBook", "Macbook", "macbook"],
               "iPhone": ["iPhone", "iphone"],
               "iPad": ["ipad", "iPad","I pad"],
               "Pencil": ["pencil", "Pencil"],
               "Watch": ["watch", "Watch"],
               "iMac": ["iMac", "imac"],
               }
global title_list
title_list=[]



    
URL="https://www.ptt.cc/bbs/MacShop/index.html"
RES=requests.get(URL)
soup = BeautifulSoup(RES.text, "html.parser")

title_list=[]
# Maintain Topic DB
i=1   
for article in soup.select('.r-list-container .r-ent .title a'):
    title = article.string
    href = "https://www.ptt.cc/" + article["href"] 
        
        # Filter: seller
    if ("[販售]" in title):
        topicDic = {"title": title, "href": href, "sent": False}
            
        # Save new topic in DB
        if topicDic not in topicDb:
            topicDb.append(topicDic)
    
    # Check whether keyword in DB each round
    for index in topicDb: 
        for checkCorrectWord in productList['AirPods']:
            if (checkCorrectWord in index["title"]) and (index['sent'] == False):
                # For Testing can be eliminated.
                #print("最新文章: "+index["title"]+"\n"+"連結: "+index["href"] )
                
                temp="["+str(i)+"]  "+index["title"]+"\n"+index["href"]+"\n"
                
                title_list.append(temp)
                msgtmp='\n'.join(title_list)
                msg=f'{msgtmp}'
                
                print(msg)
                #print('\n'.join(title_list))
                index['sent'] = True
                i+=1
                
            
                

def post(message, token):
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        payload = {
            'message': message
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload
        )
        if response.status_code == 200:
            print(f"Success -> {response.text}")
    except Exception as _:
        print("occur exception")

if __name__ == "__main__":
    token = "1OV4CuPUH3hYKBLqxbuDufUnnyY3wEP5uziQSlEuOyy" # 您的 Token
    message = msg     # 要發送的訊息
    post(message, token)
                    
   
            




