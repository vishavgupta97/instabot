import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_post_id import get_post_id
insta_username="royal_khann"
def post_a_comment(insta_username) :
    media_id=get_post_id(insta_username)
    comment_text=raw_input("Kindly Enter Your Comment:\n")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()
    if make_comment['meta']['code']==200 :
        print "Successfully Added New Comment"
    else :
        print "!!!Unable To add comment!!!Please try Again"
post_a_comment(insta_username)
