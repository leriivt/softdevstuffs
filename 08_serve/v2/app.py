'''
VSM: Verit, Sebastian, Maya
SoftDev
K08 -- introduction to Flask
2022-10-06
time spent: 0.2
'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") # prints '__name__' just like that
    print(__name__)   #where will this go?  In the terminal
    return "No hablo queso!"  # displays in localhost, 127.0.0.1:5000

app.run()

