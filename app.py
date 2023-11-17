from flask import Flask, render_template,request,send_file
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
                   "orientation":"horizontal",
                   "page": 1,
                   "per_page": 100}
        response = requests.get(url,params)
        data = response.json()  
        if response.status_code==200:
             wallpapers=data['hits']
        else:
             wallpapers =[]

@app.route('/')
def index():
    extract("forest")
    return render_template('index.html', wallpapers=wallpapers)



@app.route('/search')
def search():
    query = request.args.get('query', '')
    extract(query)
    if not wallpapers:
         return render_template('error.html',error="Search not found")
    else:
         return render_template('index.html', wallpapers=wallpapers, query=query)
    
@app.errorhandler(404)
def page_not_found_error(e):
    return render_template('error.html', error="Page Not Found")




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002)

