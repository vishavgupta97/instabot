import requests
from get_post_id import get_post_id
from constants import BASE_URL,APP_ACCESS_TOKEN
def like_a_post(insta_username) :
    media_id=get_post_id(insta_username)
    request_url=BASE_URL+"media/%s/likes"%(media_id)
    payload={'access token':APP_ACCESS_TOKEN}
    print "Post Request URL:%s"%(request_url)
    post_a_like=requests.media_id(request_url,payload).json()
    if post_a_like['meta']['code']==200 :
        print "Like Was Successful"
    else :
        print "Like Was Not Successful!!!Kindly Try Again"
