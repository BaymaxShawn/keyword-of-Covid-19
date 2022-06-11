import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

aaa = requests.get('https://news.google.com/search?q=booster%20shot%2BOmicron&hl=en-US&gl=US&ceid=US%3Aen&num=50')

page_object = BeautifulSoup(aaa.text, 'html.parser')
news_title = page_object.find_all('h3')
searching_result = []
count = 0
for i in news_title:
    if count == 50:
        break
    searching_result.append(i.getText())
    count += 1

result = pd.DataFrame(searching_result, columns=['news_name'])  # transfer the searching result to data frame
print(result)
path = r'/Users/huchangguo/pythonProject'
file_name = 'HW1.json'
print(os.path.join(path, file_name))
result.to_json(os.path.join(path, file_name))  # store the result to json file

key_word = ['side effect', 'Omicron', 'Booster', 'vaccine']
summary = pd.DataFrame([[0, 0, 0, 0]], columns=key_word)

for i in range(result.shape[0]):
    content = result.iloc[i][0]
    for j in range(4):
        word = key_word[j]
        if word.upper() in content.upper():
            summary[word][0] += 1
plt.bar(range(summary.shape[1]), summary.iloc[0].to_list(), tick_label=key_word)
plt.show()

