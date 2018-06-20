import os
files = os.listdir('./')
files = filter(os.path.isfile, files)
files.sort(key=os.path.getmtime)
print 'Plik modyfikowany najdawniej: %s' %files[0]
print 'Plik modyfikowany ostatnio: %s' %files[len(files)-1]
filestext = '\n'.join(files)
with open('ex10_2results.txt','w') as f:
	f.write(filestext)
