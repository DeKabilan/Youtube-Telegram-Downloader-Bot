from pytube import YouTube
import pyshorteners
import os
from dotenv import load_dotenv

load_dotenv()

apkey=os.getenv("apkey")



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
