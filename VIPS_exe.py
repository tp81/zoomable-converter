# File conversion utilities library
import os, shutil

VIPS_EXECUTABLE="C:\\vips-dev-7.42.0\\bin\\vips.exe "
TEMPLATE_FILE=os.path.join(os.path.dirname(__file__),"template.html")

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
