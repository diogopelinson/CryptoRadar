from flask import Flask
import requests
#flask wtf forms

app = Flask(__name__)

from views import *

url ='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,brl'
response = requests.get(url)
dados = response.json()

if __name__ == "__main__":
    app.run(debug=True)