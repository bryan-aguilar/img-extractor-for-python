# img-extractor-for-python
## Overview
This is a command line python script that will scrape images off of a specified subreddit. Utilizes the PRAW library to communicate with the reddit API.
## Requirements
Python >= version 3.8<br>
Ensure proper dependencies are installed using requirements file<br>
`pip install -r requirements.txt`<br>
Script needs to be contained in its own subdirectory to avoid permission issues with saving the images
### Getting your own reddit auth token
Click [here](https://www.reddit.com/prefs/apps/) to create your own reddit app.  Use this [guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to answer basic questions about authentication.
### Creating a credentials file
A cred.txt file will need to be created and should have this exact format. Your creds.txt file should also be located in the src directory. This should all be on one line. 
```
client_id=INSERT YOUR CLIENT ID HERE,client_secret=INSERT YOUR CLIENT SECRET HERE,user_agent=INSERT YOUR USER AGENT HERE
``` 

