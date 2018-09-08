# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:34:35 2018

@author: Nikhil Anand
"""

#Reading the python files

import PyPDF2
pdf_file_obj=open('2018/Paper1.pdf','rb')
content=" "
pdf_reader=PyPDF2.PdfFileReader(pdf_file_obj)
for i in range(0,pdf_reader.numPages):
    content=content+pdf_reader.getPage(i).extractText()
    
content = " ".join(content.replace(u"\xa0", " ").strip().split())

for x in content:
    x.replace(' \n ','')


content.lower()    



#tokenizing words

import nltk
words=nltk.tokenize.word_tokenize(content)


#Removing stop words
from nltk.corpus import stopwords
stopword_list=set(stopwords.words('english'))
list_stop_char=['(',')',':','.',',','/','-','=','?',';'
                 ,'A','B','C','D'
                 ,'1','2','3','4','12','8','10','11'
                 ,'option','options'
                 ,'question','questions'
                 ,'The','If'
                 ,'Paper','Marks','marks'
                 ,'given','following'
                 ,'JEE','Advanced'
                 ,'PARAGRAPH'
                 ,'correct'
                 ,'answer'
                 ,'chosen'
                 ,'There'
                 ,'first','second','one','two','three','four','five'
                 ,'respectively'
                 ,'2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008'
                 ,'value'
                 ,'Let'
                 ,'This'
                 ,'result'
                 ,'constant'
                 ,'section','SECTION'
                 ,'contains'
                 ,'Answer'
                 ,'For'
                 ,'In'
                 ,'ONLY','let'
                 ,'marking','scheme'
                 ,'selecting','Selecting'
                 ,'according'
                 ,'Full'
                 ,'without'
                 ,'evaluated'
                 ,'figure'
                 ,'Then','Each','also'
                 ,'choose','Therefore','Based','defined','Ignore'
                 ,'none'
                 ,'e.g','i.e'
                 ,'based'
                 ,'undergoes'
                 ,'incorrect']
stopword_list.update(list_stop_char)


new_content=[]

for x in words:
    if x not in stopword_list:
        new_content.append(x) 

    
len(new_content)


#check frequency distribution
fdis=nltk.FreqDist(new_content)
fdis.most_common(139)


print(new_content)


""""Analyze and find pattern on which subjects, which topics, which sub-topics are asked most in previous year 
and create a trend analysis"""" 


# step1 : create a list of words belonging to particular topic
# step2 : check whether the words belong to the subject or not using for loops, take the count and plot the graph

from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = "https://www.vocabulary.com/lists/1549484"
response = http.request('GET', url)
soup = BeautifulSoup(response.data)


mechanics=set()

#scrapping the mechanics keywords
all_links = soup.find_all("a",class_="word dynamictext")
for link in all_links:
    mechanics.add(link.next) #contents can also be used
    



