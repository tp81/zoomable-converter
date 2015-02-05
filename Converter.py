import tkFileDialog as tf
from Tkinter import *

root = Tk()

Label(root, text = "Welcome! Select an input and output directory to start.").grid(row=0,column=0,columnspan=3)

Label(root, text = "Input directory").grid(row=1,column=0)
Label(root, text = "Output directory").grid(row=2,column=0)

indir = ''
outdir = ''

indir_e = Entry(root, text=''); indir_e.grid(row=1,column=1)
outdir_e = Entry(root, text=''); outdir_e.grid(row=2,column=1)

def changeInDir():
	indir = tf.askdirectory()
	indir_e.delete(0)
	indir_e.insert(0,indir)
	
def changeOutDir():
	outdir = tf.askdirectory()
	outdir_e.delete(0)
	outdir_e.insert(0,outdir)
	
indir_b = Button(root, text="Browse", command=changeInDir); indir_b.grid(row=1,column=2)
outdir_b = Button(root, text="Browse", command=changeOutDir); outdir_b.grid(row=2,column=2)

log = Entry(root); log.insert(0, ">>"); log.grid(row=3,column=0,columnspan=3,rowspan=4,sticky=W+E+N+S);

def go():
	indir = indir_e.get()
	outdir = outdir_e.get()
	
	print indir, outdir

Button(root,text="Go!", command=go).grid(row=7,column=0,columnspan=3)

root.mainloop()
