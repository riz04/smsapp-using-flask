def send_sms(mobileNumber,message,schtime):
    
    
    
    import requests as req
    
    API_ENDPOINT='http://api.msg91.com/api/v2/sendsms?'
    API_KEY='' ######116541AFfuiXoRp2X57639f86
    url=API_ENDPOINT+'authkey='+API_KEY+'&country=91&sender=Classp&route=4&message='+str(message)
    url=url+'&mobiles='+str(mobileNumber)
    

    #headers = {'content-type': 'application/json'}
    if(schtime==None):
        pass
    else:
        url=url+'&schtime='+str(schtime)
    print url
    #print database.set_sms_request(url)
    conn=req.get(url=url)
    print conn.json()
    return conn.json()