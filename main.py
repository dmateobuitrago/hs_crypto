file = open('blockchain.txt','r+')

print(file.read())

file.write('Hello World') 
file.write('This is our new text file') 
file.write('and this is another line.') 
file.write('Why? Because we can.') 

file.close()