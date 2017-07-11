import requests
from get_post_id import get_post_id
from constants import BASE_URL,APP_ACCESS_TOKEN
from colorama import *
#insta_username="vishavgupta97"

#this method is used for liking a particular post
def like_a_post(insta_username) :
    media_id=get_post_id(insta_username)
    request_url=BASE_URL+"media/%s/likes"%(media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print "Post Request URL:%s"%(request_url)  #using post request and payload is using for the purpose of
                                            #sending data to the server
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code']==200 :
        print Fore.BLUE+Style.BRIGHT+"Like Was Successful"
        Style.RESET_ALL
    else :
        print Fore.RED+"Like Was Not Successful!!!Kindly Try Again"
#like_a_post(insta_username)
