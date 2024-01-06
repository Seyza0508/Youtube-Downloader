from pytube import YouTube

# The URL of the YOutube video you want to downlaod
videoUrl = ''

# Create a Youtube object with the URL
youtube = YouTube(videoUrl)

# Set the video stream resolution you want to download
stream = youtube.streams.get_highest_resolution()

# Download the video
stream.download()

print(f"Downloaded: {youtube.title}")
