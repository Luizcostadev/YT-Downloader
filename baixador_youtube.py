#importando a lib
#lembre-se de baixar a bilbioteca pelo terminal usando pip install pytube

from pytube import YouTube

#definindo a função para baixar vídeos

def baixa_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print('Vídeo baixado com sucesso!!')
    except Exception as e:
        print("Erro algo de errado não está certo", str(e))

#Agora sim você pode colocar o link do vídeo

video_url = input ('Coloque o link do vídeo:')

#Chamando o download do vídeo

baixa_video(video_url)

        