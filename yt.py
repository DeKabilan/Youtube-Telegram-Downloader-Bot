from pytube import YouTube
import pyshorteners
import os
apkey=os.getenv("apkey")
apkey="4f05b12112626b8960b71013d87d28767b62e57d"



def download(link,reso):

    res=[]
    video = YouTube(link)
    for stream in video.streams:
        if stream.resolution!=None:
            res.append(stream.resolution)
    res=set(res)
    if reso in res:
        downloads = video.streams.filter(progressive="True", file_extension="mp4", res=reso).first().url
        s = pyshorteners.Shortener(api_key=apkey)
        dl=(s.bitly.short(downloads))
        return dl
    else:
        return "Resolution Not Found"

