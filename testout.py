import urllib.request
from PIL import Image
from googleapiclient.discovery import build

api_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"
# my_key= "AIzaSyCehMuAsWshx2TXtW3StRv3Mlusu-aGjPc"      Rahul205
# vansh_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"

question = input("\nSeach about the topic you want to know!\n") 

resource = build("customsearch", 'v1', developerKey=api_key).cse()
result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw').execute()

result['items'][0]

print("Here are some results we have found for you: \n")

for item in result['items']:
    print(item['title'], item['link'])

result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw', searchType='image').execute()
count=1
print("Here are some images we found related to the search results: \n")

for item in result['items']:
    if (count == 4):
        break
    else:
        urllib.request.urlretrieve(item['link'], f"img{count}.png")
        img = Image.open(f"img{count}.png")
        img.show()
        count+=1

