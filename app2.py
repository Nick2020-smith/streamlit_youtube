import pytube
import streamlit as st

class YoutubeDownloader:
    def init(self, url):
        self.url = url
        self.youtube = pytube.Youtube(self.url, on_progress_callback=YoutubeDownloader.onProgress)
        self.stream = None

    def showTitle(self):
        st.write(f"**Titulo:** {self.youtube.title}")
        self.showStreams()

    def showStreams(self):
        streams = self.youtube.streams
        streams_options = [
            f"Resolucion: {stream.resolution or 'N/A'} / FPS: {getattr(stream, 'fps', 'N/A')} / Tipo: {stream.mime_type}"
            for stream in streams
        ]
        choice = st.selectbox("Elija una opcion de stream :", stream_options)
        self.streams = streams[stream_options.index(choice)]

    def getFileSize(self):
        file_size = self.streams.filesize / 1000000
        return file_size

    def getPermissionToContinue(self, file_size):
        st.write(f"**Titulo:** {self.youtube.title}")
        st.write(f"**Autor:** {self.youtube.author}")
        st.write(f"**Tamaño:** {file_size:.2f} MB")
        st.write(f"**Resolucion:** {self.stream.resolution or 'N/A'}")
        st.write(f"**FPS:** {getattr(self.stream, 'fps', 'N/A')}")

        if st.button("Descargar"):
            self.download()

    def download(self):
        self.stream.download()
        st.success("¡Descarga completada!")

    @staticmethod
    def onProgress(stream=None, chunk=None, remaining=None):
        file_size = stream.filesize / 1000000
        file_downloaded = file_size - (remaining / 1000000)
        st.progress(file_downloaded / file_size)

if __name__ == "__main__":
    st.title("Descargador de videos de Youtube")
    url=st.text_input("Ingrese URL del video:")

    if url:
        downloader = YouTubeDownloader(url)
        downloader.showTitle()
        if downloader.stream:
            file_size = downloader.getFileSize(url)
            downloader.getPermissionToContinue(file_size)

