import rpyc
import sys
import random
dl=[]
jj=[]
val=[]
newlist=[]
availfiles=[]

#method to read and store bytes of files from clients
def check(filename,uid):
  for a in availfiles:
    if a==filename:
      koo=open(filename,"rb")
      with koo:   
        byte=koo.read()
      f.root.send(byte,filename,uid)

#method to write bytes for the client requesting a download
def sendandwrite(byte1,filename):
  fname=filename
  foo=open(fname,"wb")
  foo.write(byte1)

#determining if ip given on command line.
length=len(sys.argv)
if length==2:
  lo="localhost"
else:	
  lo=sys.argv[2]  

f = rpyc.connect(lo, 18861)
f.root.setCallback(check)

bgsrv = rpyc.BgServingThread(f)

name = raw_input("Hi there! Welcome. Press enter to continue")
uid=random.randrange(1,100,1)
availfiles=[]
availfiles.append(sys.argv[1])
f.root.files(sys.argv[1])

print "Your client id is %d" % uid#unimplemented feature.
while True:
  opt=raw_input("Enter what you want to do:\nls:list available files shared for download\nd:download a file\ne:exit\n")
  if(opt=="ls"):
    jj=f.root.retlist()
    for mg in jj:
      print mg
    print "\n"
  if(opt=="d"):
    filename=raw_input("Enter the exact name of the file you wish to download: ")
    newfile=filename
    f.root.initiateTransfer(sendandwrite)
    f.root.seek(uid,filename)
  if(opt=="e"):
    exit()
    print "\n"
bgsrv.stop()
f.close()
