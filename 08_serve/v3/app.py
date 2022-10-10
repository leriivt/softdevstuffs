'''
VSM: Verit, Sebastian, Maya
SoftDev
K08 -- introduction to Flask
2022-10-06
time spent: 0.1
'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? the terminal
    return "No hablo queso!"

app.debug = True #allows editing the function without having to physically rerun the program(only save)
app.run()    #debug being False helps make sure the website isn't accidentally altered
