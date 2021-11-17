from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

audio_downloader.extract_info("https://www.youtube.com/watch?v=0Yovl9HvpPU")

