import urllib.request
import webbrowser
from PIL import Image
from googleapiclient.discovery import build

api_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"
# my_key= "AIzaSyCehMuAsWshx2TXtW3StRv3Mlusu-aGjPc"      Rahul205
# vansh_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"

question = input("\nSeach about the topic you want to know!\n") 
resource = build("customsearch", 'v1', developerKey=api_key).cse()

def web_scrapper():
    result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw').execute()

    result['items'][0]

    print("\nThe best documentations filtered from the web about your searched topic is opened in your browser!\n")
    print("Here are few more links for more information about the searched topic:\n")
    count = 1
    for item in result['items']:
        if (count >= 3):
            print(item['title'], item['link'])
        else:
            webbrowser.open_new_tab(item['link'])
        count+=1


def image_scrapper():
    result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw', searchType='image').execute()

    count=1
    print("\nThe images we found related to the search result is displayed now!\n")

    for item in result['items']:
        if (count == 4):
            break
        else:
            urllib.request.urlretrieve(item['link'], f"img{count}.png")
            img = Image.open(f"img{count}.png")
            img.show()
            count+=1
try:
    user_response_main = int(input("PLease enter the option which you want to use from below:\n1. Online Resource Gatherer\n2. Real-time Orbit Viewer\n"))
    if (user_response_main == 1):
        try:
            user_response2 = int(input("PLease enter the option which you want to use from below:\n1. View the best websites from your search\n2. View best images about your search\n3. View Both\n"))
            if (user_response2 == 1):
                web_scrapper()
            elif (user_response2 == 2):
                image_scrapper()
            elif (user_response2 == 3):
                web_scrapper()
                image_scrapper()
            else: print("Invalid number entered! PLease select a number from 1-3")

        except (ValueError, NameError):
            print("Invalid command entered! PLease enter only numbers from (1-3).")

    elif (user_response_main == 2):
        print("abhinav r code")
    else: print("Invalid number entered! PLease select a number from 1-2")
except (ValueError, NameError):
    print("Invalid command entered! PLease enter only numbers from (1-2).")