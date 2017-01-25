#! /usr/bin/python3
import os, shutil, sys

root_path = '/home/helman/Projects/Drones/San_Jose_de_Bavaria2/Bavaria_3_Nov/'
folders = ['Green_Folder','NIR_Folder','Red_Folder','REG_Folder','RGB_Folder']
for folder in folders:
	os.mkdir(os.path.join(root_path,folder))

lstDir = os.walk(root_path)
lstFiles=[]

for root, dirs, files in lstDir:
	for fichero in files:
		(nombreFichero, extension)= os.path.splitext(fichero)
		if(nombreFichero[23:26] == 'GRE'):
			shutil.move(root_path+nombreFichero+extension,root_path+folders[0]+'/'+nombreFichero+extension)
		elif(nombreFichero[23:26] == 'NIR'):	
			shutil.move(root_path+nombreFichero+extension,root_path+folders[1]+'/'+nombreFichero+extension)
		elif(nombreFichero[23:26] == 'RED'):	
			shutil.move(root_path+nombreFichero+extension,root_path+folders[2]+'/'+nombreFichero+extension)
		elif(nombreFichero[23:26] == 'REG'):	
			shutil.move(root_path+nombreFichero+extension,root_path+folders[3]+'/'+nombreFichero+extension)
		elif(nombreFichero[23:26] == 'RGB'):	
			shutil.move(root_path+nombreFichero+extension,root_path+folders[4]+'/'+nombreFichero+extension)
sys.exit()




