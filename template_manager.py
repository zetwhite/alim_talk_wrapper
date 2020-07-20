import os 
import json
import re

dir = "./Template"
varPattern = ""


class RenderingError(Exception) : 
    def __init__(vlistLen, inputLen) : 
        self.vlistLen = vlistLen 
        self.inputLen = inputLen
    def __str__(self) : 
        return "template - RenderingError variable is " + self.vlistLen + ", but your input is " + self.inputLen


def checkTemplateFolder() :
    #check there is template folder, if not exist, makes folder 
    try :
        if not os.path.exists(dir) :
            os.makedirs(dir)
    except OSError :
            print('Error : Creating directory ' + dir)
        

def saveTemplate(template) :
    #save template as dir/[templtCode].json file 
    checkTemplateFolder()
    fileName = dir + "/" + template['templtCode'] + ".json"
    with open(fileName, "w+") as jsfile :
        json.dump(template, jsfile, indent = "\t", ensure_ascii = False)


def getVariableList(template) : 
    #get variable List from template content 
    pattern = "#\{.*?\}"
    variableList = re.findall(pattern, template["templtContent"])
    finalList = []
    for v in variableList :
        if v not in finalList : 
            finalList.append(v)
    return finalList


def saveVariableList(templateCode, variableList) :
    #save variable list to file 
    fileName = dir +"/" + templateCode + "_vlist.txt"
    with open(fileName, 'w+') as txtfile : 
        for v in variableList :
            txtfile.write("%s\n" % v)


def loadTemplate(templateCode) :
    #load template from dir[templtCode].json file 
    fileName = dir + "/" + templateCode + ".json"
    with open(fileName, "r") as jsfile :
        template = json.load(jsfile)
    return template


def loadVariableList(templateCode) : 
    #get variable list from [filename]_vlist.txt 
    variableList = [] 
    fileName = dir + "/" + templateCode + "_vlist.txt"
    with open(fileName, "r") as txtfile : 
        for line in txtfile : 
            currentPlace = line[:-1]
            variableList.append(currentPlace)
    return variableList


def RenderTemplate(templateCode, variableList, inputList) :
    #rendering template
    template = loadTemplate(templateCode)

    if(len(variableList) != len(inputList)) :
        raise RenderingError(len(variableList), len(inputList))
    for i in range(0, len(variableList)) :
        template["templtContent"] = template["templtContent"].replace(variableList[i], inputList[i])
    return template
        