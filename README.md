# Mini-Project

In this project csv file data has been taken and from that data examination forms has been generated in form of pdf

## Things need to be installed

`pip install pdfkit`

`apt-get install wkhtmltopdf`



## File Structure
 `ApplicationFormExam.csv`- File where data is stored 
 
 `Eform.html`-File which contains HTML code of examination form.
 
 `data.py`-File which firstly reads csv file then I have used replace function that replaces HTML content with csv data.Then file is open in write mode and required changes has been made and pdf file has been generated.
 
