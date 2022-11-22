


import requests
from flask import Flask, render_template

app = Flask(__name__)


with open('key_nasa.txt') as f:
    key = f.read()

#print(key)
nasa_url = "https://api.nasa.gov/planetary/apod?api_key=" + key
print(nasa_url)
res = requests.get(nasa_url)
json = res.json()
pic_url = json["url"]

@app.route("/")
def picture():
    
    return render_template('main.html', url=pic_url)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
