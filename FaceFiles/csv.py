import glob,os
filename = 'C:\\Users\\MY PC\\PycharmProjects\\untitled\\testfile'
folder = 'C:\\Users\\MY PC\\PycharmProjects\\untitled'
for filename in glob.iglob(os.path.join(folder,'*.txt')):
    os.rename(filename,filename[:-4]+'.csv')