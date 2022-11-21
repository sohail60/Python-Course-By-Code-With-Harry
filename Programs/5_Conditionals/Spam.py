from operator import truediv
from tkinter.tix import InputOnly


text=input("Enter the Text: ")

spam=False

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True

if(spam):
    print("Spam")
else:
    print("No Spam")