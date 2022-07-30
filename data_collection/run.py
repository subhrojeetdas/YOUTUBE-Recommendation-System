import sys
import comments_collector as cc
import csv
def get_comments(video_url, api_key_file,i,order = 'time',part = 'snippet', maxResults = 100):
    yt_service = cc.build_service(api_key_file)
    video_ID = cc.get_id(video_url)
    comments_dict, title = cc.comments_helper(video_ID, api_key_file, yt_service)
    filename=f'Video{i}'
    cc.save_to_csv(comments_dict, filename)
    print(f'Done for {video_url}.')
def main():
    api_key_path = "creds.json";
    url_file="url.csv"
    with open(url_file) as text:
        text_data=csv.reader(text,delimiter=',')
        i=1
        for row in text_data:
            print(row[0])
            get_comments(row[0], api_key_path,i)
            print(f'Done for video: {i}')
            i += 1
if __name__=="__main__":
    main()