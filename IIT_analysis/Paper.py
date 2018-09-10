import PyPDF2
from nltk.corpus import stopwords
import nltk


class Paper:
    
    
    
    def __init__(self,pdf):
        self.content = ""
        self.trimmed_content = []
        pdf_file_obj=open(pdf,'rb')
        pdf_reader=PyPDF2.PdfFileReader(pdf_file_obj)
        for i in range(0,pdf_reader.numPages):
            self.content = self.content + pdf_reader.getPage(i).extractText()
        self.content = " ".join(self.content.replace(u"\xa0", " ").strip().split())
        for x in self.content:
            x.replace(' \n ','')
        self.content.lower()    

    def get_pdf_content(self):
        return self.content
    
    def remove_stopwords(self):
        words=nltk.tokenize.word_tokenize(self.content)
        stopword_list=set(stopwords.words('english'))
        list_stop_char=['(',')',':','.',',','/','-','=','?',';','[',']'
                 ,'A','B','C','D','1','2','3','4','12','8','10','11'
                 ,'Q.1','Q.2','Q.3','Q.4','Q.5','Q.6','Q.7','Q.8','Q.9','Q.10','Q.11','Q.12'
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
        
        self.trimmed_content=[]
        
        for x in words:
            if x not in stopword_list:
                self.trimmed_content.append(x) 
        
        return self.trimmed_content        

    
    
    def check_tokens(self):
        return len(self.trimmed_content)

