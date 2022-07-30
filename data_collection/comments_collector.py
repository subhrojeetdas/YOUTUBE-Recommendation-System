import requests
import json
import pandas as pd
from apiclient.discovery import build
from csv import writer
from urllib.parse import urlparse, parse_qs
def get_keys(filename):
    with open(filename) as f:
        key = f.readline()
    DEVELOPER_KEY = key
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return {'key': key, 'name': 'youtube', 'version': 'v3'}

def build_service(filename):
    with open(filename) as f:
        key = f.readline()
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=key)

def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]

def save_to_csv(output_dict, filename):
    output_df = pd.DataFrame(output_dict, columns = output_dict.keys())
    output_df.to_csv(f'data/{filename}.csv')

def comments_helper(video_ID, api_key_file, service):
    # put comments extracted in specific lists for each column
    comments, commentsId, likesCount, authors = [], [], [], []
    # response to get the title of the video
    response_title = service.videos().list(
        part = 'snippet',
        id = video_ID
    ).execute()
    # get the video title
    video_title = response_title['items'][0]['snippet']['title']
    #print("Video-title: ",video_title)
    #get the first response from the YT service
    response = service.commentThreads().list(
        part="snippet",
        videoId = video_ID,
        textFormat="plainText").execute()
    #print("Response: ",response)
    while response:
        # for every comment in the response received
        for item in response['items']:
            comment = item["snippet"]["topLevelComment"]
            author = comment["snippet"]["authorDisplayName"]
            text = comment["snippet"]["textDisplay"]
            comment_id = item['snippet']['topLevelComment']['id']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            # append the comment to the lists
            comments.append(text)
            commentsId.append(comment_id)
            likesCount.append(like_count)
            authors.append(author)
        # get next page of comments
        if 'nextPageToken' in response:
            response = service.commentThreads().list(part="snippet",
            videoId = video_ID,
            textFormat="plainText",
            pageToken=response['nextPageToken']
            ).execute()
        # if no response is received, break
        else:
            break
        # return the whole thing as a dict and the video title to   calling function in run.py
    '''print("Comments: ",comments)
    print("Author: ",authors)
    print("Comment ID: ",commentsId)
    print("Like Count: ",likesCount)'''
    return dict({'Comment' : comments, 'Author' : authors, 'Comment ID' : commentsId, 'Like Count' : likesCount}), video_title