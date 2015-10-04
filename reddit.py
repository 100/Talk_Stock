import praw
import private
import pymongo
import requests
from scipy import stats

SCOPES = set(['edit', 'flair', 'history', 'identity', 'modconfig', 'modcontributors', 'modflair', 'modothers', 'modposts', 'modself',	'privatemessages', 'read', 'report', 'submit', 'vote'])

def getToken():
	client_auth = requests.auth.HTTPBasicAuth(private.REDDIT_CLIENT_ID, private.REDDIT_CLIENT_SECRET)
	post_data = {"grant_type": "password", "username": private.REDDIT_USERNAME, "password": private.REDDIT_PASS}
	headers = {"User-Agent": "Talk Stock by /u/lavabender"}
	response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
	return dict(response.json())['access_token']

def createPRAW():
	r = praw.Reddit(user_agent="Talk Stock by /u/lavabender")
	r.set_oauth_app_info(client_id=private.REDDIT_CLIENT_ID, client_secret=private.REDDIT_CLIENT_SECRET,
		redirect_uri='http://127.0.0.1:65010/authorize_callback')
	r.set_access_credentials(SCOPES, getToken(), refresh_token=None, update_user=True)
	return r

def postSubmissions(articles):
    r = createPRAW();
    for key, value in articles.iteritems():
        title = "[" + key + "] " + value['headline']
        thread = r.submit("talkstock", title, url = value['url'])
        if value['abstract'] != 'none':
            thread.add_comment("[This post was made by a bot to summarize the article.] \n" + "Abstract: " + value['abstract'])

def createUserJSON(comment):
	user = {'user': comment.author.name,'karma': 0}
	return user

def updateUsers():
	client = pymongo.MongoClient()
	db = client.users
	users = db.users
	r = createPRAW()
	submissions = r.get_subreddit("talkstock").get_new()
	for sub in submissions:
		sub.replace_more_comments
		comments = sub.comments
		for comment in comments:
			users.insert_one(createUserJSON(comment))
			users.update_one({'user': comment.author.name}, {'$set': {'karma': 0}})
		for comment in comments:
			currKarma = users.find_one({'user': comment.author.name})['karma']
			users.update_one({'user': comment.author.name}, {'$set': {'karma': currKarma + comment.score}})
		client.close()

def startGold():
	client = pymongo.MongoClient()
	db = client.users
	users = db.users
	usersR = []
	karma = []
	gold = []
	for user in users.find():
		usersR.append(user['user'])
		karma.append(user['karma'])
	for index, karmaNum in enumerate(karma):
		if stats.percentileofscore(karma, karmaNum) > 90.0:
			gold.append(users[index])
	client.close()
	return usersR, karma, gold

def checkGold(users, karma, gold):
	for index, karmaNum in enumerate(karma):
		if stats.percentileofscore(karma, karmaNum) < 90.0:
			try:
				gold.remove(users[index])
			except Exception:
				pass
		if stats.percentileofscore(karma, karmaNum) > 90.0:
			gold.append(users[index])

def getTwenty():
	r = createPRAW()
	subs = []
	for sub in r.get_subreddit("talkstock").get_hot(limit=20):
		subs.append((sub.permalink, sub.title))
	return subs
