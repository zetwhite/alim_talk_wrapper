import requests 
import json
import user_config
import inspect
import pprint

basicSetting = {}
host = "https://kakaoapi.aligo.in" 
debug = True
log = lambda: print("[", inspect.stack()[1][3], "]")
printer = pprint.PrettyPrinter(indent = 2)

class ResponseError(Exception) : 
    def __init__(self, code, msg) :
        self.code = code 
        self.msg = msg 
    def __str__(self) : 
        return str(self.code) + " : " + self.msg 
        

def initSetting(apiKey, senderKey, userId) : 
    basicSetting['apikey'] = apiKey 
    basicSetting['senderkey'] = senderKey
    basicSetting['userid'] = userId


def tokenSetting(token) : 
    basicSetting['token'] = token
     

def sendRequest(url, data={}) :  
    res = requests.post(url, data = {**basicSetting, **data} ) 
    response = res.json()
    if(response['code'] != 0) : 
        raise ResponseError(response['code'], response['message']) 
    return response


'''
def logging(func) : 
    def new_function(*args, **kwargs) : 
        log() 
        result = func(*args, **kwargs)
        pp = pprint.PrettyPrinter(indent = 2)
        pp.pprint(result) 
        return result 
    return new_function
'''


def getToken(time) : 
    url = host + "/akv10/token/create/" + str(time) + "/i/" 
    result = sendRequest(url)
    if(debug) : 
        log()
        printer.pprint(result)
    return result["token"]


def authChannel(plusId, phoneNumber) : 
    url = host + "/akv10/profile/auth/" 
    data = {
        "plusid" : plusId, 
        "phonenumber" : phoneNumber
    }
    result = sendRequest(url, data)
    if(debug) : 
        log()
        printer.pprint(result)


def getCategory() : 
    url = host + "/akv10/category/"
    result = sendRequest(url)
    if(debug) : 
        log()
        printer.pprint(result)


def listTemplates() : 
    url = host + "/akv10/template/list/"
    result = sendRequest(url)
    if(debug) : 
        log() 
        printer.pprint(result)

def listHistory(page = 1, limit = 50) : 
    url = host + "/akv10/history/list/"
    data = {
        "page" : page, 
        "limit" : limit, 
    }
    result = sendRequest(url, data)
    if(debug) : 
        log() 
        printer.pprint(result)


if __name__ == '__main__' : 
    initSetting(user_config.apiKey, user_config.senderKey, user_config.userId)
    tokenSetting(getToken(1))

    #authChannel("@neo_2020", "01083118428")
    #getCategory()
    listTemplates()
    listHistory() 
