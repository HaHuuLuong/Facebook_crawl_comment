import json
# import facebook_scraper
from facebook_scraper import get_posts, set_noscript
from facebook_scraper import get_group_info


ginfo = get_group_info("FPTUHCMStudents")

## We need to login Facebook with this account in a browser before running the code.

listposts=[]
#for post in get_posts("nintendo", pages=2):
posts = get_posts(post_urls=["https://www.facebook.com/groups/FPTUHCMStudents/permalink/1408453373294001/","https://www.facebook.com/groups/FPTUHCMStudents/permalink/1312454792893860/"],  options={"comments":True})
# if want to get comment from  group not public
# First step: join group by account personal 
# Fix code row 13, add credential: posts = get_posts(post_urls=["https://www.facebook.com/groups/FPTUHCMStudents/permalink/1408453373294001/","https://www.facebook.com/groups/FPTUHCMStudents/permalink/1312454792893860/"],credentials=('tk','pass'),  options={"comments":True})


for post in posts:
#   print post on the screen
#    print(json.dumps(post,indent=2, default=str))
#    for x in post:
#        print(x, post[x])
#  print json object to file one object/post per line
    with open('fb.json', 'a', encoding='utf-8') as f:
        json.dump(post, f, ensure_ascii=False, default=str)
        f.write("\n")
    print(post['post_text'])
    for cmt in post['comments_full']:
        print(cmt['commenter_name']," : ", cmt['comment_text'].replace("\n",""))