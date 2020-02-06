import praw
import requests
import io
from PIL import Image
import re
import os
from pathlib import Path
#establish reddit instance
reddit = praw.Reddit(client_id='oFIVlnHQfgXjYQ',
                     client_secret='xt6o0AWVDm23ytFkZaav4L-sKZc',
                     user_agent='imgextract 1.0 /u/forrealbro')

def main():
    #TODO:
        #check for duplicates
        #allow user to define their own search criteria(top/hot/recent/controversial)  
    user_sub = GetSub()
    num_download = GetNumDownload()

    download_count = 0 
    folder_loc = GetFolderName()
    for submission in user_sub.top(limit=999):
        if download_count == num_download:
            break
        if CheckForNonImage(submission):
            download_count += DownloadImage(submission,str(folder_loc))

def GetNumDownload():
    #returns the amount of of images user would like to download
    #currently softcapped at 100 until further error checking can be done
    while 1:
        try:
            requested_amount = int(input("How many images would you like to download (Min: 1 Max:100): "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if requested_amount < 1 or requested_amount > 100:
            print("Please enter a valid number")
            continue
        else:
            return requested_amount

def GetSub():
    #returns the subreddit instance of the subreddit we will be using
    exists = False
    while exists == False:
        user_req_sub = str(input("Please enter in a subreddit name: "))
        if(user_req_sub == ""):
            continue
        if CheckExists(user_req_sub) == True:
            print(user_req_sub + " is a valid subreddit")
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
def GetFolderName():
    #Allows user to define what the folder name is
    #if it does not exist already then it is created
    folder_name = input("Folder Name: ")
    folder_path = Path(os.path.join(os.getcwd() + "\\" + folder_name))
    if folder_path.is_dir() == False:
        os.makedirs(folder_path)
    return folder_path
def DownloadImage(sub,save_location):
    #downloads and stores image as jpg
    #returns 1 if succesful
    #0 if failed
    #TODO: 
        #Create dynamic filepath or create a folder for each time script is ran
        
    try:
        img_content = requests.get(sub.url).content
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')
        return 0
    #create filename based off url
    file_name = sub.id
    
    try:
        img_file = io.BytesIO(img_content)
        img = Image.open(img_file).convert('RGB')
        file_path = os.path.join(save_location +"\\" + file_name + '.jpg')
        with open(file_path, 'wb') as f:
            img.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {sub.url} - as {file_path}")
        return 1
    except Exception as e:
        print(f'Could not download {sub.url} - {e}')
        return 0

main()

    
   