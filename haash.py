import hashlib


def hash(filename):

     h = hashlib.sha1()

     with open(filename,'rb') as file:

         chunk = 0
         while chunk != b'':
               chunk = file.read(1024)

               h.update(chunk)

         return h.hexdigest()

print('The hash of the function :',hash('home/dell-intership/Contact list.docx')
