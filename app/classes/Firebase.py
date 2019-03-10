




import pyrebase
class Firebase():
    def __init__(self):
        pass

    def get_config(self):
        config={}
        # config = {
        #     'apiKey': "AIzaSyC0hXZcnKHdO54XRVbP4afs7924JkmGpwo",
        #     'authDomain': "sachkyahai-newsplugin.firebaseapp.com",
        #     'databaseURL': "https://sachkyahai-newsplugin.firebaseio.com",
        #     'projectId': "sachkyahai-newsplugin",
        #     'storageBucket': "sachkyahai-newsplugin.appspot.com",
        #     'messagingSenderId': "1059885073178"
        # };
        return config

    def get_db(self):
        config=self.get_config()
        import pyrebase


        firebase = pyrebase.initialize_app(config)

        db=firebase.database()
        return db            

    

