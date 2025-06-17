from yt_dlp import YoutubeDL

def find_youtube_video_url(nombre_plato: str) -> str:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'no_warnings': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            resultados = ydl.extract_info(f"ytsearch:{nombre_plato}", download=False)
            video = resultados['entries'][0]
            return video['webpage_url']
        except Exception as e:
            return f"Error al buscar video: {e}"