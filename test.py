import alim_wrapper as aw
import admin_config
import template_manager as tm
import json

greetingCode = "TB_7754"

if __name__ == '__main__' : 
    aw.initSetting(admin_config.apiKey, admin_config.senderKey, admin_config.userId)
    aw.tokenSetting(aw.getToken(1))

    #authChannel("@neo_2020", "01083118428")
    #getCategory()
    #listTemplates()
    #istHistory() 
    #listChannel()

    '''
    templateList = aw.listTemplates()
    print(json.dumps(templateList, indent = 2))
    for t in templateList :
        tm.saveTemplate(t)
        tCode = t["templtCode"]
        variables = tm.getVariableList(t)
        tm.saveVariableList(tCode, variables)
    '''
    
    template = tm.loadTemplate(greetingCode)
    variables = tm.loadVariableList(greetingCode)
    inputVariables = ["youn seung hui"]
    template = tm.RenderTemplate(greetingCode, variables, inputVariables)
    

    sendInfo = aw.getSendInfo("01083118428", "01083118428")
    tplContent = aw.getTplContent(template)
    failContent = aw.getFailContent(template)
    aw.sendAlimTalk(sendInfo, tplContent, failContent)