# "Blocking Code"

import requests
import time 

def blocking_fetch_urls(urls):
    results=[]
    start_time = time.time()

    for url in urls:
        try:
            print(f"Fetching {url}")

            responce = requests.get(url)
            
            results.append({
                'url':url,
                'status' :responce.status_code,
                'length' :len(responce.text)
            })
        except Exception as e:            
            results.append(
                {
                    'url' : url 
                    
                }
            )