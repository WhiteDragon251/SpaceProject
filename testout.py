import urllib.request
import webbrowser
from PIL import Image
from googleapiclient.discovery import build

api_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"
# my_key= "AIzaSyCehMuAsWshx2TXtW3StRv3Mlusu-aGjPc"      Rahul205
# vansh_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"

question = input("\nSeach about the topic you want to know!\n") 

resource = build("customsearch", 'v1', developerKey=api_key).cse()
result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw').execute()

result['items'][0]

print("\nThe best documentations filtered from the web about your searched topic is opened in your browser!\n")
print("Here are few more links for more information about the searched topic\n")
count = 1
for item in result['items']:
    if (count >= 3):
        print(item['title'], item['link'])
    else:
        webbrowser.open_new_tab(item['link'])
    count+=1



result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw', searchType='image').execute()
count=1
print("\nThe images we found related to the search result is displayed!\n")

for item in result['items']:
    if (count == 4):
        break
    else:
        urllib.request.urlretrieve(item['link'], f"img{count}.png")
        img = Image.open(f"img{count}.png")
        img.show()
        count+=1