from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

class YouTubeUploader:
    def __init__(self, api_key, client_secrets_file):
        self.api_key = api_key
        self.client_secrets_file = client_secrets_file
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def upload_video(self, video_file_path, title, description, category_id, tags):
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': category_id
            },
            'status': {
                'privacyStatus': 'public'
            }
        }

        # Call the YouTube API to upload the video
        insert_request = self.youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
        )

        response = insert_request.execute()
        return response

# Example usage:
# uploader = YouTubeUploader(api_key='AIzaSyB9OBIkNPW3GOtMNWKeb6LHwj40oIw4gY8', client_secrets_file='dataclient.json')
# response = uploader.upload_video('path/to/video.mp4', 'My Video Title', 'Description of video', '22', ['tag1', 'tag2'])
