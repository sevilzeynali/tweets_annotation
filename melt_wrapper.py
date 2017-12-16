#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This program tags tweets with Melt
from __future__ import unicode_literals
from subprocess import Popen, PIPE
import re

class meltWrapper():
	def __init__(self, MElt_bin, MElt_options):
		self.MElt_bin=MElt_bin
		self.MElt_options=MElt_options
	#This function gets the list of tweets to tag as parameter 
	def tagListOfTexts(self,liste):	
		string="\n".join(liste)
		res=self.tag(string)
		return res
	#function for annotating with Melt
	def tag(self,texte):
		cmd = [self.MElt_bin, self.MElt_options]
		p = Popen(cmd,stdin=PIPE,stdout=PIPE, stderr=PIPE)
		(stdout, stderr) = p.communicate(texte.encode('utf-8'))
		stdout=stdout.decode('utf8')			
#exemple of output of stdout:
#Au/P+D/0.90305676909 tel/ADJ/0.976219163052 avec/P/0.99319435586 Stacy/NPP/0.997467420283
		texts_tagged=[]#list to put the results of Melt
		for line in stdout.split("\n"):			  
			tags = 'ADJ|ADJWH|ADV|ADVWH|CC|CLO|CLR|CLS|CS|DET|DETWH|ET|I|NC|NPP|P|P\+D|P\+PRO|PONCT|PREF|PRO|PROREL|PROWH|V|VIMP|VINF|VPP|VPR|VS|KK'
			#regular expression to get taged elements in form of a list
			exp = u'(?:\{(?P<normalisation>.*?)\} )?(?P<token>\S+)?/(?P<tag>%s)/?(?P<proba>\d\.\d+)?(?: |$|\n)'%tags
			# if output of Melt is not empty
			if line!="":
				l = re.compile(exp).findall(line)
				l2=[]
				for e in l:
					if e[0]=='': # if the normalisation is empty in Melt
						l2.append({'normalization':e[0],'token':e[1],'tag':e[2],'probability':e[3]})			
					else:
						l2.append({'normalization':e[1],'token':e[0],'tag':e[2],'probability':e[3]})
					#appending all in a list
				texts_tagged.append(l2)
		return texts_tagged

		
		
		
		
		
	
	
	





