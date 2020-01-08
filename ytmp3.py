import urllib.request
import urllib.parse
import re
from pytube import YouTube
import sys



name = input("What's the song name? ")

query_string = urllib.parse.urlencode({"search_query" : name})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url12="http://www.youtube.com/watch?v="+search_results[0]
print("http://www.youtube.com/watch?v=" + search_results[0])
yt = YouTube(url12)

# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first()

# download into working directory
stream.download()

sys.exit()
