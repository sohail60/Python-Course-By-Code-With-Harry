name=input("Enter Name: ")
date=input("Enter Date: ")

letter='''Dear <name>,
You are selected!
<date>
'''

letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)