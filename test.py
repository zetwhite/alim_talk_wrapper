import alim_wrapper as alim
import admin_config
import template_manager as tpl
import json
import time

greetingCode = "TB_7754"

if __name__ == "__main__":
    # initial Setting for authentication
    alim.initSetting(admin_config.apiKey, admin_config.senderKey, admin_config.userId)
    alim.tokenSetting(alim.getToken(1))

    # traverse template list and save as json file
    templateList = alim.listTemplates()
    for t in templateList:
        tpl.saveTemplate(t)
        tpl.saveVariableList(t)

    # get template from ./Template/code.json file and rendering
    t = tpl.loadTemplate(greetingCode)
    v = tpl.loadVariableList(greetingCode)
    inputV = ["user name"]
    msg = tpl.RenderTemplate(t, v, inputV)

    # send alim talk
    sendInfo = alim.getSendInfo(sender="XXXXXXXXXXX", receiver_1="00000000000")
    sendResult = alim.sendAlimTalk(sendInfo, msg)

    # wait for k
    time.sleep(3)
    alim.getDetailHistory(sendResult["mid"])

    """example for another func
    alim.authChannel("@neo_2020", "01083118428")
    alim.getCategory()
    alim.listHistory() 
    alim.listChannel()
    """

