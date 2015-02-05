# File conversion utilities library
import os, shutil

'''
Tiny wrapper around the VIPS executable.

To use it simply:
	import VIPS_exe
	
	VIPS_dzsave('path-to-input-file','path-to-output-dirName')

Author: Thomas Pengo
License: GPL 3
'''

VIPS_EXECUTABLE="C:\\vips-dev-7.42.0\\bin\\vips.exe "
TEMPLATE_FILE=os.path.join(os.path.dirname(__file__),"template.html")

def VIPS_setPath(newPath):
	VIPS_EXECUTABLE=newPath

def VIPS_call(command, inputFile, outputFile, parameters):
	import subprocess
	
	subprocess.call(" ".join((VIPS_EXECUTABLE,command,'"'+inputFile+'"','"'+outputFile+'"',parameters)))

def VIPS_dzsave(inputFile, outputFile, layout="google", progress=True, suffix=".png[compression=9]"):
	if layout=='google':	
		if outputFile.endswith('.gmaps'):
			templateFile = outputFile[0:len(outputFile)-len('.gmaps')]+'.html'
		else:
			outputFile=outputFile+".gmaps"
			templateFile=outputFile+".html"
		
	VIPS_call("dzsave",
		inputFile,
		outputFile,
		" ".join((
			"--layout",layout,
			"--vips-progress" if progress else "")))

	if layout=='google':
		shutil.copyfile(TEMPLATE_FILE,templateFile)
