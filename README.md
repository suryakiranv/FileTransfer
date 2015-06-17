                                             Projects_Cloud

                *********************PROJECT-1 Python File Sharing using RPyC**********************************

                              This project implements a file sharing system using rpyc.


*****Running the code on Linux*****

Starting a Server : On the command line go to the folder in which your server.py file is stored and 
enter "python server.py" This will start a server on your system on port "18861", if you wish to 
change the port number, open the server.py using a text editor and change the port number which is 
specified in the second last line of the code.

Running a client : Go to the folder which contains the files you wish to share. On the command line, type -- python client.py followed by one file name you wish to share as second argument and the ip of the machine having the server code as third argument (python client.py file.txt 10.0.1.10). Ignore the third argument if the server is running on the same machine (python client.py file.txt). Once you do this a menu will appear using which you can:

a)view the list of shared files
b)download any file from that list or 
c)exit the program. 

Note: You can share only one file at a time, if you wish to share multiple files, exit the program
and run it again. But multiple downloads are possible without exiting the program.

Example:

Client connecting to the same machine    :  $python client.py file.txt

Client connecting from a different machine :  $python client.py file.txt x.x.x.x

Starting a server                        :  $python server.py   

->The client must have the file that he is specifying for upload on the command line in the same
  directory as he is running the client code from.

->Once connected, every client will be able to view the list of files shared by other clients 
  which are connected.

->The clients can choose to download any of the files that are visible to them by giving the 
  filename in the menu and this will happen    asynchronously for all the clients connected.
 
->The file will be downloaded for the client in the same directory from where the client code
  is running.
  
Note: Python along with RPyC module needs to be installed on all the machines which run these programs.


          ****The programs have been tested on CSCloud and file transfer was done between two VMs successfully.****
