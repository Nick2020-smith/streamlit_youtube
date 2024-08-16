from pytube import YouTube

def download(link):
    try:
        yt = YouTube(link).streams
        video_stream = yt.get_highest_resolution()
        video_stream.download()
        print("Descarga Completa", "Video descargado satisfactoriamente!")
    except Exception as e:
        print("Error", f"Ha ocurrido un error: {str(e)}")

if __name__ == '__main__':
    link = input("Link de Youtube AQUI:")
    download(link)
    
