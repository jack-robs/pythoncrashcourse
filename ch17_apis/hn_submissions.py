import requests

from operator import itemgetter

#Make an API call and store the response
#1
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

#Process information about each submissino
#2convert json list to a python list
submission_ids = r.json()

#3 make empty list to store these dictionaries
submission_dicts = []
for submission_id in submission_ids[:30]:
    #make a separate API call for each submission.
    #4new API call for each submission id, print status request
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    #5create a dictionary currently being processed on each loop
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
      #6store number of comments in this dictionary
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)
#7sort submission_dicts by by comments
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

#8loop through list, print out three pieces of information about subs
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
