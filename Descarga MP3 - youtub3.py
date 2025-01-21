#El postprocesador FFmpegAudioConvertor depende de tener FFmpeg correctamente instalado en tu sistema por lo que se debe descargar.
#pip install yt-dlp
#pip install -U yt-dlp

import yt_dlp as youtube_dl

def des_mp3(url):
    ydl_opts = {
        'ffmpeg_location': 'C:/ffmpeg/ffmpeg.exe',  # Ruta a FFmpeg
        'format': 'bestaudio/best',  # Descargar el mejor audio disponible
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usamos el nombre correcto del postprocesador
            'preferredcodec': 'mp3',  # Convertir a MP3
            'preferredquality': '192',  # Calidad 192 kbps
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Guardar con el título del video y la extensión
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Descargar el video desde la URL

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=hTILrvRkliQ'
des_mp3(url)
