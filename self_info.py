import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
def self_info() :
    requests_url=(BASE_URL)+"/users/self/?access_token=%s"%(APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(requests_url)
    user_info=requests.get(requests_url).json()
    if user_info['meta']['code']==200 :
        if len(user_info['data']) :
            print "USERNAME: %s"%(user_info['data']['username'])
            print "You have %s followers"%(user_info['data']['counts']['followed_by'])
            print "you are following %s people" % (user_info['data']['counts']['follows'])
            print "You Have %s No. of posts" % (user_info['data']['counts']['media'])
        else :
            print "Sorry!!!!This User Doesn't Exists"
    else :
        print "!!!Status Code Other Than 200 Recieved!!!"





