import praw
import pymysql
import requests
from bs4 import BeautifulSoup

connection = pymysql.connect(user='config.dbUser', password='config.dbPass',
                              host='config.host',
                              database='config.database')

reddit = praw.Reddit(client_id='config.clientID',
                     client_secret='config.clientSecret',
                     user_agent='config.agent',
                     username='config.username',
                     password='config.password')

cursor = connection.cursor()

subreddit = reddit.subreddit('chess')

for comment in subreddit.stream.comments():

	commentBody = comment.body.split(" ")

	if commentBody[0].lower() == '!fenfinder':

		commentBody[0] = ""

		query = "SELECT * from replied_to where userID='" + comment.id + "';"
		cursor.execute(query)

		if cursor.rowcount < 1:
			fen = ""
			i = 1
			while i in range(len(commentBody)):
				fen += commentBody[i] + " "
				i = i + 1

			theurl = 'https://chess-db.com/public/explorer.jsp?fen=' + fen + '&moves=&interactive=true&avelo=2000&etype=2';

			r  = requests.get(theurl)

			data = r.text

			soup = BeautifulSoup(data, 'html.parser')

			matchName = ""
			matchLink = ""
			matchFound = False

			for link in soup.find_all('a'):
				temp = link.get('href')

				separator = temp.split('?')

				if(len(separator) > 1):
					if(separator[0] == '/public/game.jsp'):
						matchName = link.text.replace("&nbsp", "")
						matchLink = 'https://chess-db.com' + separator[0] + '?' + separator[1]
						matchFound = True
						break;

			if matchFound == True:
				comment.reply('**Match Found**:[**' + matchName.replace(';', '') + '**](' + matchLink 
					+ ')  \n\n *^Hi, ^I\'m ^a ^bot! ^If ^there ^is ^an ^issue ^please ^send ^a ^message ^to ^/u/I_Love_CS.*')
			else:
				comment.reply('**No Match Found**: Unable to find a game with that FEN, sorry. \n\n *^Hi, ^I\'m ^a ^bot! ^If ^there ^is ^an ^issue ^please ^send ^a ^message ^to ^/u/I_Love_CS.*')

			insert = "INSERT INTO replied_to (userID) VALUES ('" + comment.id + "');"
			cursor.execute(insert)
			connection.commit()

connection.close()


			




