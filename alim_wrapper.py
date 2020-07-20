import requests 
import json
import inspect

basicSetting = {}
host = "https://kakaoapi.aligo.in" 
debug = True
printFunc = lambda: print("[", inspect.stack()[1][3], "]")
printLog = lambda log: print(json.dumps(log, indent = 2, ensure_ascii=False))


class ResponseError(Exception) : 
    def __init__(self, code, msg) :
        self.code = code 
        self.msg = msg 
    def __str__(self) : 
        return str(self.code) + " : " + self.msg 
        

def initSetting(apiKey, senderKey, userId) : 
    """Initialize basic settings; this settings are used for all request

    Args : 
        apiKey(string) : apiKey for using kakao alim talk service (need to get from smart aligo homepage)
        senderKey(string) : senderKey for check sender Info (need to get from smart aligo homepage)
        userId(string) : smart aligo user id 
    """
    basicSetting['apikey'] = apiKey 
    basicSetting['senderkey'] = senderKey
    basicSetting['userid'] = userId


def tokenSetting(token) : 
    """Initialize token value; token is used for all request

    Args :
        token(string) : token string, get from getToken function
    """
    basicSetting['token'] = token
     

def sendRequest(url, data={}) :
    #send data as json fomat to url, and return result as dict
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
        printFunc()
        printLog(result)
    return result["token"]


def authChannel(plusid, phonenumber) : 
    data = locals()
    url = host + "/akv10/profile/auth/" 
    result = sendRequest(url, data)
    if(debug) : 
        printFunc()
        printLog(result)


def getCategory() : 
    url = host + "/akv10/category/"
    result = sendRequest(url)
    if(debug) : 
        printFunc()
        printLog(result)
    return result["data"]


def addFriendChannel(plusid, authnum, phonenumber, categorycode) : 
    data = locals() 
    url = host + "/akv10/profile/add/"
    result = sendRequest(url, data)
    if(debug) : 
        printFunc()
        printLog(result)
    return result["data"]


def listChannel(plusid = None, senderkey = None) : 
    data = locals()
    for i in list(data) : 
        if(data[i] is None) : 
            del(data[i])
    url = host + "/akv10/profile/list/"
    result = sendRequest(url, data)
    if(debug) : 
        printFunc()
        printLog(result)
    return result["list"]


def listTemplates(tpl_code = None) : 
    """ get Lists of all template 

    Args :
        tpl_code(string) : if not None, print a template which has this tpl_code
    
    Returns : 
        list : return list of dict for template info   
    """
    data = locals() 
    for i in list(data) : 
        if(data[i] is None) : 
            del(data[i])
    url = host + "/akv10/template/list/"
    result = sendRequest(url, data)
    if(debug) : 
        printFunc() 
        printLog(result)
    return result["list"]


def listHistory(page = 1, limit = 50, startdate = None, enddate = None) :
    data = locals()  
    for i in list(data) :
        if(data[i] is None) :
            del(data[i])
    url = host + "/akv10/history/list/"
    result = sendRequest(url, data)
    if(debug) : 
        printFunc()
        printLog(result)
    return result["list"], result["currentPage"], result["totalPage"], result["totalCount"]


def getSendInfo(sender, receiver_1, senddate = None, recvname_1 = None) :
    '''make sendInfo dictionary form 

    Args :
        sender(string) : sender phone number(010XXXXXXX)
        senddate(string) : reservation time (YYYYMMDDHHMMSS), if None send right now!

    Returns :
        dict : return sendInfo in dictionary form 
    '''
    data = locals() 
    for i in list(data) :
        if(data[i] is None) : 
            del(data[i])
    return data


def getTplContent(template) :
    data = {} 
    data["tpl_code"] = template["templtCode"]
    data["subject_1"] = template["templtName"]
    data["message_1"] = template["templtContent"]
    data["button_1"] = template["buttons"]
    return data


def getFailContent(template, failover = "N"):
    data = {}
    data["failover"] = failover 
    if(failover == "N") :
        return data
    data["fsubject_1"] = template["templtName"]
    data["fmessage_1"] = template["templtContent"] 
    return data


def sendAlimTalk( sendInfo, tplContent, failContent ) :
    data = {**sendInfo, **tplContent, **failContent}
    print(data)
    url = host + "/akv10/alimtalk/send/"
    result = sendRequest(url, data) 
    if(debug) :
        printFunc() 
        printLog(result)
    return result["info"]
