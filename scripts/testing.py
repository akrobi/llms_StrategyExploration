from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) # creates an app inside flask
api = Api(app) # wraps our app in an api (means we're doing a restful api)

if __name__ == "__main__":  # starts our server and starts our application
    app.run(debug=True) # the application is to be run in debug mode. i.e. 
    # logging and error info will be output so that we know what's going wrong if anything
    # debug=True only ever in deveopment env, never in production env

# if you just tun this code