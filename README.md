
# alim_talk_wrapper
https://smartsms.aligo.in/main.html<br />
aligo kakao alimtalk API wrapper<br />
<br />
test.py와 같이 template을 받아와서 .json파일을 받아와서 저장하고,<br />
template에서부터 메세지를 생성해서 알림톡을 보낼 수 있습니다.<br />
<br />
<br />
# alim_wrapper.py
알리고에서 제공하는 API의 파이썬 래퍼를 제공합니다.<br />
해당 함수들을 이용하기 전에 <br />
```python
    initSetting(apiKey, senderKey, userId)
    tokenSetting(alim.getToken(1))
```
위와 같은 함수들을 호출하여 기본적인 인증을 위한 값을 세팅해야합니다.<br />
<br />
<br />
# template_manager.py 
템플릿을 `./Template/[templatecode].json` 파일로 저장합니다. <br />
`#{변수}`를 찾아내어 `./Template/[templatecode]_vlist.json` 파일로 저장합니다.<br />
.json으로 저장된 template을 dictionary로 읽어옵니다. <br /> 
이후 해당 변수(`#{변수}`)들을 다른 값으로 수정합니다. <br />
<br />
<br />


--------------------------------------------------------------------------------------
# NOTE 

## template_manager.py for template saving and loading 
* [save] template list를 받아와서 json파일로 저장 (o)
* [save] template에서 사용하는 변수들 re 이용해서 txt로 저장 (vlist.txt) (o)

* [load] 저장된 template를 dictionary형태로 가져오기 //중복 제거 (o)
* [load] 저장된 vlist를 list 형태로 만들기 (o)

* 알림톡 보내는 형식 파악하기 (o) 
* [render] vlist의 값을 다른 값으로 replace하여 반환(o) 


## alim_wrapper.py for using kakao API 
* sendRequest, wrapper 기본적인 기능 만들기 (o)
* alim talk 보낼때 receivers, subjects, failover가 여러개인 경우 어떻게 처리할지 정하기 => (우선 한명에 대해서만 처리하는 함수로 작성해둠!) 
* 알림톡 보내는 함수, 결과 logging하는 함수 (o)


(+) alim_wrapper.py, tempalte_manager.py 독립적이게 유지할 것 
