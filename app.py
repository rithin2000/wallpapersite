from flask import Flask, render_template,request
import requests

app = Flask(__name__,static_url_path='/static')



def extract(query):
        global wallpapers
        url = "https://pixabay.com/api/"
        key = "40619552-457b1b093b2decc1d98b11041"
        params = { "key":f"{key}",
                   "q":f"{query}",
                   "min_width":1920,
                   "min_height":1920,
                   "image_type":"photo",
                   "orientation":"horizontal"}
        response = requests.get(url,params)
        data = response.json()  
        wallpapers=data['hits']

@app.route('/')
def index():
    extract("forest")
    return render_template('index.html', wallpapers=wallpapers)



@app.route('/search')
def search():
    query = request.args.get('query', '')
    extract(query)
    return render_template('index.html', wallpapers=wallpapers, query=query)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002)

