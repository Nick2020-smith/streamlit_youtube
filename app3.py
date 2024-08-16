from pytube import YouTube

url = "https://www.youtube.com/watch?v=Y5fBdpreJiU"
mi_video = YouTube(url)
mi_video = mi_video.streams.get_highest_resolution()
mi_video.download() 
