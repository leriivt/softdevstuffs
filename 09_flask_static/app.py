'''
VSM: Verit, Sebastian, Maya
SoftDev
K09 -- static files in Flask
2022-10-12
time spent: 0.6
'''

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
