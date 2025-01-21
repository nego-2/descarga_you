import yt_dlp as youtube_dl

def des_mp3(url):
    ydl_opts = {
        'ffmpeg_location': 'C:/ffmpeg/ffmpeg.exe',  # Ruta a FFmpeg 
        'format': 'bestaudio/best',  
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  
            'preferredquality': '192', 
        }],
        'outtmpl': '%(title)s.%(ext)s', 
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) 

url = 'https://www.youtube.com/'
des_mp3(url)
