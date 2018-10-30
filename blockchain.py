# Variables

blockchain = []
username = ""

def getusername():
 global username
 username = input('Hi, what is your name? ')

def getuserinput(firstime=False):
 if firstime:
  print('')
  print('/++++++++++/')
  print('a: for adding a transaction')
  print('p: for printing the blockchain blocks')
  print('m: for manipulation the chain')
  print('q: for quiting')
  print('/++++++++++/')
  print('')
 userinput = input('Type your instructions: ')
 
 inputHandler(userinput)

def inputHandler(userinput):
 if userinput == 'a':
  print('adding a transaction')
  createtransaction()
  getuserinput() 
 elif userinput == 'p':
  print('printing')
  printblockchain()
  getuserinput() 
 elif userinput == 'm':
  print('manipulating..')
  getuserinput() 
 elif userinput == 'q':
  print('quiting...')
  exit()
 else:
  print('/++++++++++/')
  print('Invalid request')
  print('/++++++++++/')
  getuserinput() 

def creategensisblock():
 genblock = ['genesis', 'genesis', 'genesis']
 blockchain.append(genblock)

def printblockchain():
 print(blockchain)

def createtransaction():
 transaction = [blockchain[-1],'','','']
 transaction_number = str(len(blockchain))
 print('/------Transaction #' + transaction_number +'--------/')
 print('')
 transaction[1] = input("Who are you sending money? ")
 transaction[2] = input("How much are you sending to "+ transaction[1] +"? $")
 transaction[3] = username
 appendtransaction(transaction)

def appendtransaction(transaction):
  blockchain.append(transaction)


# Init program
getusername()
creategensisblock()
getuserinput(True)