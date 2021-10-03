
api_key = "AIzaSyCehMuAsWshx2TXtW3StRv3Mlusu-aGjPc"

from googleapiclient.discovery import build

resource = build("customsearch", 'v1', developerKey=api_key).cse()

result = resource.list(q='Black Holes', cx='009557628044748784875:5lejfe73wrw').execute()

result['items'][0]


len(result['items'])

for item in result['items']:
    print(item['title'], item['link'])

result = resource.list(q='Black Holes', cx='009557628044748784875:5lejfe73wrw', searchType='image').execute()

for item in result['items']:
    print(item['title'], item['link'])

images = []

for i in range(1, 60, 10):
    result = resource.list(q='Black Holes', cx='009557628044748784875:5lejfe73wrw',
                      searchType='image', start=i).execute()
    images += result['items']

len(images)

for item in images:
    print(item['title'], item['link'])
