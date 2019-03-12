class Offers():
    def __init__(self):
        pass
    def get_offers(self):
        from Firebase import Firebase
        firebase=Firebase()
        db=firebase.get_db()
        data=db.child('/offers')
        data_value=data.get().val()
        return data_value
