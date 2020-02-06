import praw
import requests
import io
from PIL import Image
import re
import os
#establish reddit instance
reddit = praw.Reddit(client_id='oFIVlnHQfgXjYQ',
                     client_secret='xt6o0AWVDm23ytFkZaav4L-sKZc',
                     user_agent='imgextract 1.0 /u/forrealbro')

def main():
    #TODO:
        #check for duplicates
        #allow user to define their own subreddit
        #allow user to define their own search criteria(top/hot/recent/controversial)
        #allow user to define how many they would like to retrieve

    #stores a list of urls to a list of 10 hottest submissions
    
    user_sub = GetSub()
    for submission in user_sub.top(limit=10):
        if CheckForNonImage(submission):
            DownloadImage(submission)
def GetSub():
    #returns the subreddit instance of the subreddit we will be using
    
    exists = False
    while exists == False:
        user_req_sub = str(input("Please enter in a subreddit name: "))
        if(user_req_sub == ""):
            continue
        if CheckExists(user_req_sub) == True:
            return reddit.subreddit(user_req_sub)
        
def CheckExists(sub_name):
    #checks if a subreddit exists
    try:
        reddit.subreddits.search_by_name(sub_name, exact = True)
        return True
    except Exception as e:
        print(f'Error with subreddt {sub_name} - {e}')
        return False
    

def CheckForNonImage(sub):
    #check to see if the passed in URL is a direct image
    #returns True or False 
    domain = sub.domain
    if domain == "i.redd.it" or domain == "i.imgur.com":
        return True
    else:
        return False

def DownloadImage(sub):
    #downloads and stores image as jpg
    #TODO: 
        #Create dynamic filepath or create a folder for each time script is ran
        
    try:
        img_content = requests.get(sub.url).content
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')
    #create filename based off url
    file_name = sub.id
    try:
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file).convert('RGB')
        file_path = os.path.join('C:\\Users\\bagui\\Images\\' + file_name + '.jpg')
        with open(file_path, 'wb') as f:
            img.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {sub.url} - as {file_path}")
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')

main()

    
   