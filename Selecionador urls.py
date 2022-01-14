import urllib.request
import re
import youtube_dl
def pegarURL(text):
    video_ids = []
    titulos = []
    search_keyword = (' '.join(text))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword.replace(' ', '+'))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_ids = list(set(video_ids))
    YDL_OPTIONS = {'outtmpl': '%(title)s',}
    for video_id in video_ids:
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(('https://www.youtube.com/watch?v='+str(video_id)), download=False)
            titulo = info['title']
            titulos.append(titulo)
        if len(titulos) >= 5:
            for titulo in titulos:
                print('{:2} {}'.format((titulos.index(titulo)+1), titulo))
            quest = input('Qual Música: ')
            nome = titulos.pop((int(quest)-1))
            link = 'https://www.youtube.com/watch?v='+ str(video_ids.pop((int(quest)-1)))
            print('Título da música: {},Link da música: {}'.format(nome,link))
            video_ids = []
            titulos = []
            return

while True:
    resp = input('qual a musica vc quer: ')
    pegarURL(resp)
