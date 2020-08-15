#!/usr/local/bin/python3
import feedparser
import pandas as pd 
import numpy as np 
import smtplib
import os


if __name__ == '__main__':

	links = ["https://rss.dw.com/rdf/rss-en-all",
	"https://www.theatlantic.com/feed/all/",
	"https://www.vox.com/rss/index.xml",
	"https://www.thehindu.com/feeder/default.rss",
	"https://theintercept.com/feed/?lang=en",
	"http://rss.sciam.com/ScientificAmerican-Global",
	"http://www.reddit.com/r/python/.rss",
	"https://www.reddit.com/r/marketing/.rss",
	"https://www.reddit.com/r/AskReddit/.rss",]

	

	for link in links:
		with open('./output.txt', 'a') as f1:
			parsed_link = feedparser.parse(link)
			title = parsed_link['feed']['title']
			f1.write(title.capitalize() + '\n')
			for sno, post in enumerate(parsed_link.entries[:10],1):
				line = str(sno)+"."+" "+post.title + ": " + post.link + " "
				f1.write(line + os.linesep)
				f1.write('\n')


	from email.mime.text import MIMEText

	textfile = '/Users/ifrahkhanyaree/output.txt'
	with open(textfile, 'r') as fp:
		msg = MIMEText(fp.read())

	me = 'ifrah.94@gmail.com'
	you = 'ifrah.94@gmail.com'

	msg['Subject'] = 'Your content for the day'
	msg['From'] = me
	msg['To'] = you

	server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	password = 'pjsrgyneesbjdcxh'
	server.login(me,password)
	server.sendmail(me,you,msg.as_string())
	server.close()
	


		
