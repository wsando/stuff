from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLvKbarVtwhUtfd0HpR9IUCGGgXQRInyyu')
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams.first().download()
    
