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
        #scrub the list to find remove non img links
        #check for duplicates
        #allow user to define their own subreddit
        #allow user to define their own search criteria(top/hot/recent/controversial)
        #allow user to define how many they would like to retrieve

    #stores a list of urls to a list of 10 hottest submissions
    earth_porn_sr = reddit.subreddit('EarthPorn')
    for submission in earth_porn_sr.top(limit=10):
        if CheckForNonImage(submission):
            DownloadImage(submission)
            
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
        #Done - 2/4/2020-BGA Create dynamic filename
        #

    try:
        img_content = requests.get(sub.url).content
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')
    #create filename based off url
    file_name = sub.id
    try:
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file).convert('RGB')
        file_path = os.path.join('C:\\Users\\bagui\\py\\imgextract\\' + file_name + '.jpg')
        with open(file_path, 'wb') as f:
            img.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {sub.url} - as {file_path}")
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')

main()

    
   