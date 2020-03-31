from pyvirtualdisplay import Display
import csv
import pdfkit
import os
display = Display()
display.start()

with open('ApplicationFormExam.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		DateTime = row[0]
		CRN = row[1]
		Programme = row[2]
		Branch = row[3]
		AdmissionYear = row[4]
		URN = row[5]
		Semester = row[6]
		NameSelf=row[7]
		NameFather=row[8]
		NameMother=row[9]
		MobileNumber=row[10]
		Email=row[11]
		SubjectCode1=row[12]
		SubjectName1=row[13]
		SubjectCode2=row[14]
		SubjectName2=row[15]
		Photo=row[16]

		with open("Eform.html",'r',encoding='utf-8')as f:
			var=f.read()
			var = var.replace("_UniversityRollNo._", URN )
			var = var.replace("_Programme_", Programme)
			var = var.replace("_Branch_", Branch)
			var = var.replace("_YearofAdmission_", AdmissionYear)
			var = var.replace("_Semester_",Semester )
			var = var.replace("_CandidateName_",NameSelf)
			var = var.replace("_FatherName_",NameFather )
			var = var.replace("_MotherName_", NameMother)
			var = var.replace("_MobileNumber_",MobileNumber)
			var = var.replace("_Email_",Email)
			var = var.replace("_Photo_",Photo)
			var = var.replace("_SubjectCode1_",SubjectCode1)
			var = var.replace("_SubjectCode2_",SubjectCode2)

		with open(URN+".html", "w") as outf:
			outf.write(str(var))

		pdfkit.from_file(URN+'.html', URN+'.pdf')
		os.remove(URN+".html")
