'''
VSM: Verit, Sebastian, Maya
SoftDev
K11 -- forms in Flask
2022-10-16
time spent: 1.3
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST']) #methods might make it so the app can only GET and POST
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #predict: print __main__ in the terminal ; actually prints <Flask 'app'> in the terminal (__main__ is from printing __name__)
    print('------')
    print("***DIAG: request obj ***")
    print(request) #predit: will work, print what is requested by the form? ; actually prints url requested by the user
    print("***DIAG: request.args ***")
    print(request.args) #prints the ImmutableMultiDict which seems like a way to collect user inputs
    print("***DIAG: request.args['username']  ***")
    try:
        print(request.args['username']) #prints the the value associated with the key 'username' in ImmutableMultiDict
    except:
        print("ERROR: there is no username")  
    print("***DIAG: request.headers ***")
    print(request.headers) #prints a variety of information including host ip address, user web browser, and user computer information
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    try:
        print(request.args['username']) 
    except:
        print("ERROR: there is no username")
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

