




import pyrebase
class Firebase():
    def __init__(self):
        pass

    def get_config(self):
        config={}
       
        return config

    def get_db(self):
        config=self.get_config()
        import pyrebase


        firebase = pyrebase.initialize_app(config)

        db=firebase.database()
        return db            

    

