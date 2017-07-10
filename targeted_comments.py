from constants import BASE_URL,APP_ACCESS_TOKEN
from get_user_id import get_user_id
import urllib
import requests
from post_a_comment import post_a_comment
def targeted_commenting_for_marketing(insta_username) :
    user_id=get_user_id(insta_username)
    if user_id==None :
        print "Oooop!!!!!!User Doesn't Exists!!!!!"
        exit()
    request_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(user_id,APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(request_url)
    user_media=requests.get(request_url).json()
    #caption=user_media['data'][0]['caption']['text']
    #if "pizza" in caption:
        #print("checkout dominoz pizza at baddi hub")
    service=['pizza','food','clothes','coffee']
    for post in user_media['data'] :
        for serve in service :
            if serve in post['caption']['text'] :
                post_a_comment(insta_username)

targeted_commenting_for_marketing("vishavgupta97")