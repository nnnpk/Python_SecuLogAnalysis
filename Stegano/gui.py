from tkinter import filedialog
import tkinter as tk
from main import *
from PIL import ImageTk, Image






def tkgui():
	root = tk.Tk()

	root.title("Stegano")

	root.geometry("300x100")

	root.resizable(width=False, height=False)


	root.grid_columnconfigure(0, weight=1)
	root.grid_columnconfigure(4, weight=1)
	root.grid_rowconfigure(0, weight=1)
	root.grid_rowconfigure(4, weight=1)



	#########################################################
	####################### main page #######################
	#########################################################

	mainwindow = tk.Frame(root,height=80,width=300)

	embedwindow = tk.Frame(root,height=80,width=300)

	detachwindow = tk.Frame(root,height=80,width=300)

	mainwindow.grid(row=1,column=1,sticky="nsew")

	embedwindow.grid(row=1,column=1,sticky="nsew")

	detachwindow.grid(row=1,column=1,sticky="nsew")

	logoimg = Image.open('logo.jpg')

	logoimg = logoimg.resize((120,80),resample=0)

	logoimg = ImageTk.PhotoImage(logoimg)

	logopanel = tk.Label(mainwindow,image = logoimg)



	tk.Button(mainwindow,text='Embed Image',command=lambda: embedwindow.tkraise()).grid(row=1,column=1,padx=20)
	tk.Button(mainwindow,text='Detach Image',command=lambda: detachwindow.tkraise()).grid(row=2,column=1,padx=20)
	tk.Button(mainwindow,text= 'Help!',command=lambda: Helpmenu()).grid(row=3,column=1)

	logopanel.grid(row=1,column =3, rowspan =3, padx=20, pady=10)


	mainwindow.tkraise()




	#########################################################
	####################### Embed page ###	#################
	#########################################################

#	embedwindow.title("Stegano")
#	embedwindow.geometry("300x80")


	tk.Label(embedwindow,text="Secret image: ").grid(row=0)
	tk.Label(embedwindow,text="Media image: ").grid(row=1)
	tk.Label(embedwindow,text="Password: ").grid(row=2)

	embinput1 = tk.Entry(embedwindow)
	embinput2 = tk.Entry(embedwindow)
	embinput3 = tk.Entry(embedwindow)

	embinput1.grid(row=0,column=1)
	embinput2.grid(row=1,column=1)
	embinput3.grid(row=2,column=1)


	def getsecfilename():
		embinput1.delete(0,"end")
		embedwindow.sec_filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		embinput1.insert(0,embedwindow.sec_filename)

	def getmedfilename():
		embinput2.delete(0,"end")
		embedwindow.med_filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		embinput2.insert(0,embedwindow.med_filename)

	def Embedbutton():
		try:
			secimage_path = embinput1.get()
			medimage_path = embinput2.get()
			passphrase = embinput3.get()
			hideimage(medimage_path,secimage_path,passphrase)

		except:
			popup = tk.Tk()
			popup.geometry("220x30")
			popup.wm_title("!")

			message = "Please select the correct images!"

			label = tk.Label(popup, text=message)
			label.grid(row=0,column=0,sticky="NSWE",padx=10)

			popup.mainloop()

			

		

	def Backbutton():
		mainwindow.tkraise()



	tk.Button(embedwindow,text='Select File',command=getsecfilename).grid(row=0,column=2)
	tk.Button(embedwindow,text='Select File',command=getmedfilename).grid(row=1,column=2)


	tk.Button(embedwindow,text='Embed',command=Embedbutton).grid(row=3,column=1)
	tk.Button(embedwindow,text='Back',command=Backbutton).grid(row=3,column=2)



	#########################################################
	####################### Detach page ###	#################
	#########################################################

	tk.Label(detachwindow,text="Embedded Image: ").grid(row=0)
	tk.Label(detachwindow,text="Password: ").grid(row=1)

	deinput1 = tk.Entry(detachwindow)
	deinput2 = tk.Entry(detachwindow)

	deinput1.grid(row=0,column=1)
	deinput2.grid(row=1,column=1)

	def getembeddedimage():
		deinput1.delete(0,"end")
		detachwindow.emb_filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("PNG file","*.png"),("all files","*.*")))
		deinput1.insert(0,detachwindow.emb_filename)

	def Detachbutton():
		try:
			embeddedimage = deinput1.get()
			passphrase = deinput2.get()
			unhideimage(embeddedimage,passphrase)

		except:
			popup = tk.Tk()
			popup.geometry("220x30")
			popup.wm_title("!")

			message = "Please select the correct image!"

			label = tk.Label(popup, text=message)
			label.grid(row=0,column=0,sticky="NSWE",padx=10)

			popup.mainloop()

	tk.Button(detachwindow,text='Select File',command=getembeddedimage).grid(row=0,column=2)


	tk.Button(detachwindow,text='Detach',command=Detachbutton).grid(row=3,column=1,pady=20)
	tk.Button(detachwindow,text='Back',command=Backbutton).grid(row=3,column=2,pady=20)

#	detachwindow.grid_rowconfigure(2, weight=1)


	#########################################################
	###################### Help Menu ########################
	#########################################################

	helpmessage1 = "Choose Embed Mode:To embed the Secret image into the Media image"
	
	helpmessage2 = "Choose Detach Mode:To detach the Secret image from the Embedded image"

	helpmessage3 = "Please check the ouput folder for all output image files"

	def Helpmenu():
		popup = tk.Tk()
		popup.geometry("450x100")
		popup.wm_title("!")
#		popup.grid_columnconfigure(0,weight=1)

		label = tk.Label(popup, text=helpmessage1)
		label.grid(row=0,column=0,sticky="W",padx=10)

		label2 = tk.Label(popup, text=helpmessage2)
		label2.grid(row=1,column=0,sticky="W",padx=10)

		label3 = tk.Label(popup, text=helpmessage3)
		label3.grid(row=2,column=0,sticky="W",padx=10)

		B1 = tk.Button(popup, text="Back", command = popup.destroy)
		B1.grid(row=3,column=0,pady=10)

		popup.mainloop()





	root.mainloop()





if __name__ == '__main__':
	tkgui()