from constants import BASE_URL,APP_ACCESS_TOKEN
from get_user_id import get_user_id
import urllib
import requests
insta_username="royal_khann"
def get_users_post(insta_username) :
    user_id=get_user_id(insta_username)
    if user_id==None :
        print "Oooop!!!!!!User Doesn't Exists!!!!!"
        exit()
    request_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(user_id,APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(request_url)
    user_media=requests.get(request_url).json()
    if user_media['meta']['code']==200 :
        if len(user_media['data']) :
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "Your image has been downloaded!"
            #return user_media['data'][0][id]
        else :
            print "THERE IS NOT ANY RECENT POSTS"
    else :
        print "Status Code Other Than 200 Is Recieved"
    #return None

get_users_post(insta_username)
