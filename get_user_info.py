import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
def get_user_info(insta_username) :
    user_id=get_user_id(insta_username)
    if user_id == None:
        print "User does not exist!!"
        exit()
    request_url=BASE_URL+"users/%s?access_token=%s"%(user_id,APP_ACCESS_TOKEN)
    print "GET REQUESTED URL:%s"%(request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200 :
        if len(user_info['data']) :
            print "Username Is : %s"%(user_info['data']['username'])
            print "There are Total %s Followers for This User"%(user_info['data']['counts']['followed_by'])
            print "No. Of posts are %s"%(user_info['data']['counts']['media'])
            print "Follows:"%(user_info['data']['counts']['follows'])
        else :
            print "THERE IS NO DATA FOR THIS USER"
    else :
        print "Status Code Other Than 200 Is Recieved"