import requests 
from bs4 import BeautifulSoup 

#news website to fetch data
url = "https://www.bbc.com/news"

response = requests.get(url)


if response.status_code == 200:
    print("Successfully Website Loaded")
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tags = soup.find_all('h2')
    headlines = []
    for tag in h2_tags:
        text = tag.get_text(strip=True) 
        if text: 
            headlines.append(text)

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines[:10], start=1):
            file.write(f"{i}. {headline}\n")

    print("Saved Headlines are in 'headlines.txt'")

else:
    print(f" Can't load the website, The Response code is : {response.status_code}")
