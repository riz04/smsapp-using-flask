class Registration():
    def __init__(self):
        self.__name=None
        self.__number=None

    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_number(self,number):
        self.__number=number
    def get_number(self):
        return self.__number
    
    def save_resgistration(self):
        from Firebase import Firebase
        firebase=Firebase()
        db=firebase.get_db()
        url_full='/registration/'
        payload={
            'name':self.get_name(),
            'number':self.get_number()
        }
        db.child(url_full).push(payload)
