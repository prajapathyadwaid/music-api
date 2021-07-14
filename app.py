from flask import Flask,request,redirect,url_for
from youtube_search import YoutubeSearch
import json
import pafy

app = Flask(__name__)

#home page
@app.route('/',methods = ["GET"])
def home():

    return '''<h1>Music App</h1>'''

#search page
@app.route('/search',methods = ["GET","POST"])
def Search():
    name = request.args.get("q",type=str)
    if name!=None:
        str_result = YoutubeSearch(name, max_results=1).to_json()
        json_res = json.loads(str_result)
        print(json_res)
        link = "https://www.youtube.com"+json_res["videos"][0]["url_suffix"]
        
        return redirect(url_for("Result",link = link))
    return """<h1>Error:404</h1>"""

#result page    
@app.route('/result',methods = ["GET","POST"])
def Result():

    link = str(request.args.get('link'))
    audio = pafy.new(link)
    best = audio.audiostreams
    audiourl = str(best[1].url)
    return {"youtube-link":link,"audio-link":audiourl}

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
