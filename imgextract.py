import praw
import requests
import io
from PIL import Image
import re
import os
import pprint

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
    earth_porn_sr = reddit.subreddit('EarthPorn')
    ids = []
    num_images = 5
    for submission in earth_porn_sr.top():
        if len(ids) == num_images:
            break
        if CheckForNonImage(submission.id) == True:
            ids.append(submission.id)
    for i in ids:
        DownloadImage(i)


   

def CheckForNonImage(submission_id):
    #check .is_reddit_media_domain
    #and also ensure the .domain == 'i.redd.it'
    #may  have false flags by allowing videos or gifs through

    post = reddit.submission(id = submission_id)
    domain = post.domain
    if domain == 'i.redd.it' or domain == 'i.imgur.com':
        return True
    else:
        #print("Not an image: " + post.title + " " +  post.url + " " + post.domain)
        return False
   
def DownloadImage(submission_id):
    #downloads and stores image as jpg
    #TODO: 
        #Create dynamic filepath or create a folder for each time script is ran

    x = reddit.submission(id=submission_id)
    url_link = x.url
    try:
        img_content = requests.get(url_link).content
    except Exception as e:
        print(f'Could not download {url_link} - {e}')
    #create filename based off id given
    file_name = submission_id
    try:
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file).convert('RGB')
        file_path = os.path.join('C:\\Users\\Bryan\\Py\\Save Images Here\\' + file_name + '.jpg')
        with open(file_path, 'wb') as f:
            img.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {submission_id} - as {file_path}")
    except Exception as e:
        print(f'Could not download {url_link} - {e}')

main()

    
   