import os
import shutil

def isQuant(dirName):
	if("Math" in dirName):
		return False
	Maths = ['Algebra', 'Data Interpretation', 'Counting', 'Fraction', 'Geometry', 'Integer', 'Percents', 'Powers_Roots', 'Probability', 'Statistics']
	for elem in Maths:
		if elem in dirName:
			return True
	return	False

def isVerbal(dirName):
	if("Verbal" in dirName):
		return False
	Verbal = ['RC', 'SE', 'TC 1_2', 'TC 3', 'Word Problems']
	for elem in Verbal:
		if elem in dirName:
			return True
	return	False	

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_files_directory(destdir):
	return [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

def buildFolderStructure(oldDir, newDir, QuesDir, AnsDir):
	if os.path.exists(QuesDir):
		shutil.rmtree(QuesDir)
	os.makedirs(QuesDir)
	if os.path.exists(AnsDir):
		shutil.rmtree(AnsDir)
	os.makedirs(AnsDir)
	dirnames = get_immediate_subdirectories(oldDir)
	for dirname in dirnames:
		root = os.path.join(oldDir, dirname)
		filenames = get_files_directory(os.path.join(oldDir, dirname))
		for filename in filenames:
			newSubDir = ""
			# copy file accordingly
			if "Capture" in filename or ("Problem" in filename and ".webm" not in filename):
				newSubDir = os.path.join(QuesDir, dirname)
				if not os.path.exists(newSubDir):
					os.makedirs(newSubDir)
				shutil.copy2(os.path.join(root, filename), newSubDir)
			else:
				newSubDir = os.path.join(AnsDir, dirname)
				if not os.path.exists(newSubDir):
					os.makedirs(newSubDir)
				shutil.copy2(os.path.join(root,filename), newSubDir)
			print newSubDir

def directoryParse(source):
	print source
	mainDirNames = get_immediate_subdirectories(source)
	mainRoot = source
	for dirName in mainDirNames:
		if(isQuant(dirName)):
			localQuesfolder = 'Math\\'+dirName+'\Question'
			localAnsfolder = 'Math\\'+dirName+'\Answer'
			oldDir = os.path.join(mainRoot, dirName)
			newDir = os.path.join(mainRoot, 'Math\\'+dirName)
			QuesDir = os.path.join(mainRoot, localQuesfolder)
			AnsDir = os.path.join(mainRoot, localAnsfolder)
			buildFolderStructure(oldDir, newDir, QuesDir, AnsDir)
		# verbal to-do
		if(isVerbal(dirName)):
			localQuesfolder = 'Verbal\\'+dirName+'\Question'
			localAnsfolder = 'Verbal\\'+dirName+'\Answer'
			oldDir = os.path.join(mainRoot, dirName)
			newDir = os.path.join(mainRoot, 'Verbal\\'+dirName)
			QuesDir = os.path.join(mainRoot, localQuesfolder)
			AnsDir = os.path.join(mainRoot, localAnsfolder)
			buildFolderStructure(oldDir, newDir, QuesDir, AnsDir)

def main():
	path = "E:\Magoosh GRE Package 2020"
	directoryParse(".\Magoosh GRE Package 2020")

if __name__ == '__main__':
	main()