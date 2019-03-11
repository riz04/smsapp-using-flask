




import pyrebase
class Firebase():
    def __init__(self):
        pass

    def get_config(self):
        config={'apiKey': "AIzaSyD8F9THLpGE7UN_GZKlxC7yR4UWDEN5RO0",
                'authDomain': "vedimart-c67f7.firebaseapp.com",
                'databaseURL': "https://vedimart-c67f7.firebaseio.com",
                'projectId': "vedimart-c67f7",
                'storageBucket': "",
                'messagingSenderId': "111203891062"}
       
        return config

    def get_db(self):
        config=self.get_config()
        import pyrebase


        firebase = pyrebase.initialize_app(config)

        db=firebase.database()
        return db            

    

