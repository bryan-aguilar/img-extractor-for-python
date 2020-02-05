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
    links = []
    for submission in earth_porn_sr.top(limit=10):
        links.append(submission.url)
    for i in links:
        print(CheckForNonImage(i))
def CheckForNonImage(url):
    #check to see if the passed in URL is a direct image
    #returns True or False 
    content = requests.get(url).text
    title = content[content.find('<title>') + 7 : content.find('</title>')]
    return title

def ParseTitle(url):
    #parses the title using regular expressions.
    #this title will be used as our file name
    #TODO:
        #clean up the regex
        #pretty sure the stripping loop isnt neccessary

    title = re.compile(r'/\w+(?:\.\w{3}$)')
    
    #convert list to string so its only single element
    parsed = parsed[0]
    final = ''
    #strips the first slash and file extension
    for i in range(1,len(parsed)):
        if parsed[i] == '.':
            break
        else:
            final += parsed[i]
    return final


def DownloadImage(url):
    #downloads and stores image as jpg
    #TODO: 
        #Create dynamic filepath or create a folder for each time script is ran
        #Done - 2/4/2020-BGA Create dynamic filename
        #

    try:
        img_content = requests.get(url).content
    except Exception as e:
        print(f'Could not download {url} - {e}')
    #create filename based off url
    file_name = ParseTitle(url)
    try:
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file).convert('RGB')
        file_path = os.path.join('C:\\Users\\bagui\\py\\imgextract\\' + file_name + '.jpg')
        with open(file_path, 'wb') as f:
            img.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f'Could not download {url} - {e}')

main()

    
   