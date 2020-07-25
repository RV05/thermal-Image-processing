import pyrebase

config={
    "apiKey": "
    "authDomain": 
    "databaseURL": 
    "projectId": "
    "storageBucket": ",
    "messagingSenderId": ,
    "appId": "
    "measurementId": "


}

firebase=pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud="files/demo1.xlsx"
path_local = "demo1.xlsx"


storage.child(path_on_cloud).put(path_local)
