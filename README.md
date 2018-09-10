# IIT-JEE-paper-analysis
This project is based on the analysis of IIT JEE question paper of last 10 years.


<h2><b>How to Use</b></h2>
For importing package, include the IIT_analysis file in your directory and call the package as follows - 
<br>
<code>from IIT_analysis import Paper</code>
<br>
<br>
To analyze the Question Paper, pass the file as the parameter of the Paper Object - 
<br>
<code>paper_object = Physics('Paper1.pdf')</code>
<br>
<br>
To get the entire textual content of Question Paper as a string - 
<br>
<code>paper_content = paper_object.get_pdf_content()</code>
<br>
<br>
To remove the Stopwords from the string - 
<br>
<code>paper_object.remove_stopwords()</code>
<br>
<br>
To get the number of words in Question Paper after removing stopwords - 
<br>
<code>paper_object.check_tokens()</code>
<br>
<br>




