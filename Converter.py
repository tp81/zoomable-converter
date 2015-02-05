import tkFileDialog as tf
from Tkinter import *
import os, datetime
from time import sleep
import VIPS_exe

'''
Converter : a simple file conversion dialog box to convert a bunch of files in a directory recursively to the Google Maps tiled format.

Just call
	python Converter.py

Author: Thomas Pengo
License : GPL 3
'''

class ConverterDialog(Frame):
	indir = ''
	outdir = ''

	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		
		self.initUI()
	
	def initUI(self):
		self.pack(fill=BOTH,expand=1)

		Label(self, text = "Welcome! Select an input and output directory to start.").grid(row=0,column=0,columnspan=3)

		Label(self, text = "Input directory").grid(row=1,column=0,sticky=E)
		Label(self, text = "Output directory").grid(row=2,column=0,sticky=E)

		self.indir_e = Entry(self, text=''); self.indir_e.grid(row=1,column=1,sticky=W+E)
		self.outdir_e = Entry(self, text=''); self.outdir_e.grid(row=2,column=1,sticky=W+E)

		self.indir_b = Button(self, text="Browse", command=self.changeInDir); self.indir_b.grid(row=1,column=2,sticky=W)
		self.outdir_b = Button(self, text="Browse", command=self.changeOutDir); self.outdir_b.grid(row=2,column=2,sticky=W)
		
		self.logBox = Text(self, width=100, height=10); 
		self.logBox.insert(END, str(datetime.datetime.today())); 
		self.logBox.grid(row=3,column=0,columnspan=3,rowspan=4,sticky=W+E+N+S);

		Button(self,text="Go!", command=self.go).grid(row=7,column=0,columnspan=3)

	def changeInDir(self):
		self.indir = tf.askdirectory()
		self.indir_e.delete(0)
		self.indir_e.insert(0,self.indir)
	
	def changeOutDir(self):
		self.outdir = tf.askdirectory()
		self.outdir_e.delete(0)
		self.outdir_e.insert(0,self.outdir)
	
	def log(self,text):
		for line in text.split('\n'):
			self.logBox.insert(END,"\n "+line)
		
		self.parent.update_idletasks()
		
		print text

	def doFile(self,input, output):
		self.log('Starting '+input+' >> '+output)
		
		VIPS_exe.VIPS_dzsave(input, output)

	def go(self):
		indir = self.indir_e.get()
		outdir = self.outdir_e.get()

		for root, dirs, files in os.walk(indir, topdown=True):
			for infile in files:
				infilepath = os.path.join(root,infile)
				outfilepath = os.path.join(outdir,infile.rsplit('.')[0])
				
				self.doFile(infilepath, outfilepath)

if __name__ == '__main__':
	root = Tk()
	app = ConverterDialog(root)
	root.mainloop()
