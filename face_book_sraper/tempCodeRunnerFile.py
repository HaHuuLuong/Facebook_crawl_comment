
# listposts=[]
# #for post in get_posts("nintendo", pages=2):
# posts = get_posts(post_urls=["https://www.facebook.com/groups/tradahvnh/permalink/3165357933763906/","https://www.facebook.com/groups/tradahvnh/permalink/3161929864106713/"], credentials=('23a4040079@bav.edu.vn','crawl_login_des1'), options={"comments":True})


# for post in posts:
# #   print post on the screen
# #    print(json.dumps(post,indent=2, default=str))
# #    for x in post:
# #        print(x, post[x])
# #  print json object to file one object/post per line
#     with open('fb.json', 'a', encoding='utf-8') as f:
#         json.dump(post, f, ensure_ascii=False, default=str)
#         f.write("\n")
#     print(post['post_text'])
#     for cmt in post['comments_full']:
#         print(cmt['commenter_name']," : ", cmt['comment_text'].replace("\n",""))