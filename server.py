import rpyc

#Class to store all external function calls
class Service(rpyc.Service):
  def on_connect(self):
    pass

  def on_disconnect(self):
    print "Someone left!"

  def exposed_setCallback(self,check):
    f.setCallback(check)

  def exposed_initiateTransfer(self,sendandwrite):
    f.initiateTransfer(sendandwrite)

  def exposed_seek(self, uid,filename):
    f.seek(uid,filename)

  def exposed_send(self, byte,filename,uid):
    f.send(byte,filename,uid)
  
  def exposed_retlist(self):
    return newlist

  def exposed_files(self,ava):
    newlist.append(ava)
  

''' 
  A fileserver class
  This stores data for all the clients connected
  The self.callbacks private variable is used to store the check object of each client.
  The self.call private variable to call an object which writes the file for the client which initated file transfer.
'''
class FileServer:
  
  #constructor method
  def __init__(self):
    self.callbacks = []
    self.buffer = []
    self.filelist =[]
    self.dlist=[]

  #store function call  of the  client which requested the file
  def initiateTransfer(self, sendandwrite):
    self.call = sendandwrite 
    
  #Append the check function call to the list of clients
  def setCallback(self, check):
    self.callbacks = self.callbacks + [check]
  
  #Send the requested filename to everyone's check method
  def seek(self, uid,filename):
    for fn in self.callbacks:
      try:  
        fn(filename,uid)
      except:
        pass
  
  #method that calls the function to write to the particular client using the buffer self.call
  def send(self,byte,filename,uid):
    self.call(byte,filename)
     
if __name__ == "__main__":
  newlist=['****Available Files****']
  from rpyc.utils.server import ThreadedServer
  f = FileServer()
  t = ThreadedServer(Service, port = 18861)
  t.start()

