from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip

class Editor:
    def __init__(self, category: str = "science-tech"):
        # Paths to your media files
        self.image_top_path = "memes/1/1271.png"
        self.image_bottom_path = "memes/2/844.png"
        self.video_path = "videos/output9.mp4"
        self.audio_path = "audios/Janji - Heroes Tonight (feat. Johnning) [NCS Release].mp3"
        # Output file path
        self.output_path = "output/youtube_shorts_video2.mp4"
        
    def edit(self):
        # Load the video and resize it for YouTube Shorts (9:16 aspect ratio)
        video_clip = VideoFileClip(self.video_path).resize(height=1920, width=1080)

        # Load the images
        image_top = ImageClip(self.image_top_path).set_duration(video_clip.duration)
        image_bottom = ImageClip(self.image_bottom_path).set_duration(video_clip.duration)

        # Load the audio
        audio_clip = AudioFileClip(self.audio_path).set_duration(video_clip.duration)

        # Resize images to fit within the video frame with margins
        # Adjust the width as needed and maintain aspect ratio
        image_top = image_top.resize(width=video_clip.size[0] * 0.8)  # Resize to 80% of video width
        image_bottom = image_bottom.resize(width=video_clip.size[0] * 0.8)

        # Calculate margins
        margin = 30  # Margin in pixels
        top_image_pos = ("center", margin)
        bottom_image_pos = ("center", image_top.size[1] + 2 * margin)

        # Set the position of the images
        image_top = image_top.set_position(top_image_pos)
        image_bottom = image_bottom.set_position(bottom_image_pos)

        # Create a composition
        final_clip = CompositeVideoClip([video_clip, image_top, image_bottom], size=video_clip.size)

        # Set the audio to the final video
        final_clip = final_clip.set_audio(audio_clip)

        # Write the video file
        final_clip.write_videofile(self.output_path, codec="libx264", fps=24)
        
if __name__ == "__main__":
    pass 
    """test here the class Editor"""