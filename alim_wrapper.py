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
    #setting apiKey, senderKey, userId for basic auth infomation 
    basicSetting['apikey'] = apiKey 
    basicSetting['senderkey'] = senderKey
    basicSetting['userid'] = userId


def tokenSetting(token) : 
    #setting token for using API 
    basicSetting['token'] = token
     

def sendRequest(url, data={}) :  
    #send request to url and data as json format 
    res = requests.post(url, data = {**basicSetting, **data} ) 
    response = res.json()
    if(response['code'] != 0) : 
        raise ResponseError(response['code'], response['message']) 
    return response


def getToken(time) : 
    #get token from API server
    #time : token validation duration (minutes) 
    url = host + "/akv10/token/create/" + str(time) + "/i/" 
    result = sendRequest(url)
    if(debug) : 
        log()
        printer.pprint(result)
    return result["token"]


def authChannel(plusid, phonenumber) : 
    data = locals()
    url = host + "/akv10/profile/auth/" 
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
    return result["data"]


def addFriendChannel(plusid, authnum, phonenumber, categorycode) : 
    data = locals() 
    url = host + "/akv10/profile/add/"
    result = sendRequest(url, data)
    if(debug) : 
        log() 
        print.pprint(result)


def listChannel(plusid = None, senderkey = None) : 
    data = locals()
    for i in list(data) : 
        if(data[i] is None) : 
            del(data[i])
    url = host + "/akv10/profile/list/"
    result = sendRequest(url, data)
    if(debug) : 
        log() 
        printer.pprint(result)
    return result["list"]


def listTemplates(tpl_code = None) : 
    data = locals() 
    for i in list(data) : 
        if(data[i] is None) : 
            del(data[i])
    url = host + "/akv10/template/list/"
    result = sendRequest(url, data)
    if(debug) : 
        log() 
        printer.pprint(result)
    return result["list"]


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
    #listTemplates()
    #istHistory() 
    #listChannel()
    #print(listTemplates())