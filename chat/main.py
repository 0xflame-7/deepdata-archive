from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# ydl_opts = {'format': 'bestvideo+bestaudio', 'outtmpl': '%(title)s.%(ext)s'}
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'concurrent_fragment_downloads': 5,
    'ffmpeg_location': 'ffmpeg',  # Optional if in PATH
    'windowsfilenames': True,     # Avoid problematic characters in filenames
    'postprocessor_args': [
        '-avoid_negative_ts', 'make_zero'
    ]
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")