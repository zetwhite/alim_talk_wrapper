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
