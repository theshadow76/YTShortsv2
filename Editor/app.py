from pydub import AudioSegment
from pytube import YouTube

def GetAduioPart():
    # Load the song
    song = AudioSegment.from_file("audios/Syn Cole - Feel Good [NCS Release].mp3", format="mp3")

    # Define start and end times in milliseconds
    start_time = 10000  # e.g., 10 seconds
    end_time = 30000    # e.g., 30 seconds

    # Extract part of the song
    extracted_part = song[start_time:end_time]

    # Export the extracted part
    extracted_part.export("audios_preprocessed/FellGood_1.mp3", format="mp3")

def DownloadYoutubeVideo():
    # URL of the YouTube video
    url = 'https://youtu.be/--6rYxBcDpY?si=HmLpdVQPvFOy6EW3'

    # Create a YouTube object with the URL
    yt = YouTube(url)

    # Get the highest resolution video stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video
    stream.download(output_path='videos', filename='output10.mp4')

GetAduioPart()