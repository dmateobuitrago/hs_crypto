# Variables

blockchain = []
username = ""

def getusername():
 global username
 username = input('Hi, what is your name? ')

def getuserinput(showinstructions=False):
 if showinstructions:
  print('')
  print('/++++++++++/')
  print('a: for adding a transaction')
  print('p: for printing the blockchain blocks')
  print('m: for manipulating the chain')
  print('c: for checking the blockchain health')
  print('h: for help')
  print('q: for quiting')
  print('/++++++++++/')
  print('')
 print('') 
 userinput = input('Type your instructions: ')
 
 inputHandler(userinput)

def inputHandler(userinput):
 if userinput == 'a':
  print('')
  print('adding a transaction...')
  createtransaction()
  getuserinput() 
 elif userinput == 'p':
  print('')
  print('printing...')
  printblockchain()
  getuserinput() 
 elif userinput == 'm':
  print('')
  print('manipulating..')
  manipulateblockchain()
  getuserinput() 
 elif userinput == 'c':
  print('')
  print('checking blockchain..')
  checkblockchainhealth()
  getuserinput() 
 elif userinput == 'h':
  getuserinput(True) 
 elif userinput == 'q':
  print('')
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
  for index, value in enumerate(blockchain):
    print('',index, value, '')

def createtransaction():
 transaction = [blockchain[-1],'','','']
 transaction_number = str(len(blockchain))
 print('')
 print('/------Transaction #' + transaction_number +'--------/')
 print('')
 transaction[1] = input("Who are you sending money? ")
 transaction[2] = input("How much are you sending to "+ transaction[1] +"? $")
 transaction[3] = username
 appendtransaction(transaction)

def appendtransaction(transaction):
  blockchain.append(transaction)

def checkblockchainhealth():
  ishealthy = True
  for index, value in enumerate(blockchain[1:], 1):
    if(blockchain[index-1] != value[0]):
      ishealthy = False
    else:
      print('',index, value, '')
  
  if ishealthy:
    print('The blockchain is fine!')
  else:
    print('The blockchain was hacked!')

def manipulateblockchain():
  blocktochange = input('Which block do you want to hack? Type a number from 1 to ' + str(len(blockchain)) + ' -> ')

  blocktochange = int(blocktochange)

  blockchain[blocktochange - 1] = 'hacked block'



# Init program
getusername()
creategensisblock()
getuserinput(True)