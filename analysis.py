#importing the IIT_analysis package

#analyzing Physics
from IIT_analysis import Physics

#analyzing paper 1
paper1 = Physics('2014/Paper1.pdf')
paper1.get_pdf_content()  
paper1.remove_stopwords()
paper1.check_tokens()
data1=paper1.get_chapters()

#analyzing paper 2
paper2 = Physics('2014/Paper2.pdf')
paper2.get_pdf_content()  
paper2.remove_stopwords()
paper2.check_tokens()
data2=paper2.get_chapters()

#list to store topics and weights corresponding to topics
a=[]
b=[]
c=[]
d=[]

#iterating over the topics 
for key,value in data1.items():
    c.append(key)
    d.append(value)
for key,value in data2.items():
    a.append(key)
    b.append(value)

#plot for 2014 Paper 1
import matplotlib.pyplot as plt
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(d,labels=None,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal') 
plt.title("2014 Paper-1 Physics Analysis")
plt.legend(labels=c, loc="best")
plt.show()

#plot for 2014 Paper 2
import matplotlib.pyplot as plt
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(b,labels=None,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal')  
plt.title("2014 Paper-2 Physics Analysis")
plt.legend(labels=c, loc="best")
plt.show()


#analyzing Chemistry
from IIT_analysis import Chemistry

#analyzing paper 1
paper1 = Chemistry('2014/Paper1.pdf')
paper1.get_pdf_content()  
paper1.remove_stopwords()
paper1.check_tokens()
data1=paper1.get_chapters()

#analyzing paper 2
paper2 = Chemistry('2014/Paper2.pdf')
paper2.get_pdf_content()  
paper2.remove_stopwords()
paper2.check_tokens()
data2=paper2.get_chapters()

#list to store topics and weights corresponding to topics
a=[]
b=[]
c=[]
d=[]

#iterating over the topics 
for key,value in data1.items():
    c.append(key)
    d.append(value)
for key,value in data2.items():
    a.append(key)
    b.append(value)

#plot for 2014 Paper 1
import matplotlib.pyplot as plt
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(d,labels=None,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal') 
plt.title("2014 Paper-1 Chemistry Analysis")
plt.legend(labels=c, loc="best")
plt.show()

#plot for 2014 Paper 2
import matplotlib.pyplot as plt
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(b,labels=None,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal')  
plt.title("2014 Paper-2 Chemistry Analysis")
plt.legend(labels=c, loc="best")
plt.show()






