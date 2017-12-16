#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#This program annotat tweets in the MongoDB data base 
#We send the bags of 20 000 tweets to Melt and we get a list of tweet annotated 
from __future__ import unicode_literals   
from melt_wrapper import meltWrapper
from pymongo import MongoClient
import timeit	

start = timeit.default_timer()
#Melt options 
MElt_bin="MElt"
MElt_options="-TNKP"

#connecting to Mongodb
mongodb_path=""
client = MongoClient(Mogodb_path)
db=client.db_name 
collection=db.dataset

listOfTexts=[] #list of tweets
listOfIds=[] # list of identification number of tweets
limit=20000# nb of tweet that I want to tag in each loop
loopCounter=0 
melt = meltWrapper.meltWrapper(MElt_bin, MElt_options)
#query to get all tweets from mongodb
for tweet in collection.find({},{'tweet':1,'id':1},no_cursor_timeout=True):
	#replace \n and \r in tweets with space
	tweetWithoutN=tweet['tweet'].replace("\n"," ")
	tweetWithoutNR=tweetWithoutN.replace("\r"," ")
	id_tweet=tweet['id']
	# put in a list the results of the query	
	listOfTexts.append(tweetWithoutNR)
	listOfIds.append(id_tweet)
	#checking for 20 000 tweets
	if len(listOfTexts)>=limit:
		#tagging with Melt with the function tagListOfTexts in melt_wrapper.py
		texts_taged = melt.tagListOfTexts(listOfTexts)
		for i in range(len(listOfIds)): 
			#update mongodb with new results
			collection.update({'id':listOfIds[i]},{'$set':{'melt':texts_taged[i]}})
		stop = timeit.default_timer()
		loopCounter=loopCounter+limit		 
		#initialising the lists
		listOfTexts=[]
		listOfIds=[]
		print('run time for '+ str(loopCounter) +' tweets ' + str(stop - start))
		











	
	

