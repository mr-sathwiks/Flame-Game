
from tkinter import *    

from PIL import ImageTk, Image                   #    pip install Pillow
import os

root=Tk()

#root.geometry('250x300')
root.resizable(False,False)
root.title("FLAMES")

def flames():
	
	n1=entry_1.get()
	n2=entry_2.get()

	lst1=list(n1.upper())
	lst2=list(n2.upper())
	
	#print(lst1)
	#print(lst2)

	for l in lst1:
		if l in lst2:
			idx=lst1.index(l)
			lst1[idx]="_"
			idx=lst2.index(l)
			lst2[idx]="_"
	cnt=0

	

	#print("\n",lst1)
	#print(lst2,"\n")

	lst=lst1+lst2
	
	for l in lst:
		if (l!="_" and l!=" "):
			cnt+=1

	f=list('FLAME')
	index=0
	while len(f)>1:
		for i in range(cnt):
			index+=1
			if index>len(f):
				index=1
		f.remove(f[index-1])

		index-=1
	#print(f)
	
	if f == ["F"]:
		img = Image.open('Artboard 1-100.jpg')
		img.show()

	if f == ["L"]:
		img = Image.open('Artboard 2-100.jpg')
		img.show()

	if f == ["A"]:
		img = Image.open('Artboard 3-100.jpg')
		img.show()

	if f == ["M"]:
		img = Image.open('Artboard 4-100.jpg')
		img.show()
		
	if f == ["E"]:
		img = Image.open('Artboard 5-100.jpg')
		img.show()

fr=Frame(root,bg="light pink").grid(row=0)

img = ImageTk.PhotoImage(Image.open("Artboard 1-8.png"))
panel = Label(fr, image = img)
panel.grid(row=0,columnspan=5)



label1=Label(fr,text="NAME 1")
entry_1 = Entry(fr,width=25)

label2=Label(fr,text="NAME 2")
entry_2 =Entry(fr,width=25)

btn_1 = Button(fr, text = " CHECK ",bg="black", fg="white",command = flames)

l=Label(fr).grid(row=4,columnspan=5)

label1.grid(row=1)
entry_1.grid(row = 1, column = 1,columnspan=4)
label2.grid(row=2)
entry_2.grid(row = 2, column = 1,columnspan=4)
btn_1.grid(row = 3,columnspan=2)


root.mainloop()

