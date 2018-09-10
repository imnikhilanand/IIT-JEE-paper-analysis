
#Importing the IIT_analysis package

from IIT_analysis import Physics

p3 = Physics('2018/Paper1.pdf')
p3.get_pdf_content()  
p3.remove_stopwords()
p3.check_tokens()
p3.get_chapters()








