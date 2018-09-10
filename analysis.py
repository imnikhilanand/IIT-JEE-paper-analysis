# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:21:58 2018

@author: Nikhil Anand
"""

from IIT_analysis import Physics

p3 = Physics('2018/Paper1.pdf')
p3.get_pdf_content()  
p3.remove_stopwords()
p3.check_tokens()
p3.get_chapters()








