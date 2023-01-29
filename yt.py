from pytube import YouTube


def download(link,reso):

    res=[]
    video = YouTube(link)
    for stream in video.streams.filter(type="video", audio_codec="mp4a.40.2"):
        if stream.resolution!=None:
            res.append(stream.resolution)
    res=set(res)
    if reso in res:
        downloads = video.streams.filter(type="video", audio_codec="mp4a.40.2" , resolution=reso).first().download(filename='download.mp4')
        return downloads
    else:
        return "Resolution Not Found"
