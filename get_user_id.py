from constants import BASE_URL,APP_ACCESS_TOKEN
import requests
#method for getting user id of the user and method takes instagram username as an input
def get_user_id(insta_username) :
    request_url=BASE_URL+"users/search?q=%s&access_token=%s"%(insta_username,APP_ACCESS_TOKEN)
    print "GET REQUEST URL :%s"%(request_url)
    user_info=requests.get(request_url).json()  #get method is used for fetching the information from server
    if user_info['meta']['code']==200 :
        if len(user_info['data']) :              #if some data comes from server than perform,
            return user_info['data'][0]['id']
        else :                                   #if nothing comes from the server than
            return None
    else :
        print "Status Code Other Than 200 Is Recieved\n"
        exit()