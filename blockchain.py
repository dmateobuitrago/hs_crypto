# Variables
import hashlib as hl
import json

# string = 'sataeta'
# hashed = hl.sha256(string.encode())


# dictionary = {'key1':1,'key2':2}

# json_dumped = json.dumps(dictionary, sort_keys=True)
# print(json_dumped)

BLOCKCHAIN = []
TRANSACTION_QUEUE = []
USERNAME = ""

def getusername():
 global USERNAME
 USERNAME = input('Hi, what is your name? ')

def getuserinput(showinstructions=False):
 checkblockchainhealth() 
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
  create_transaction()
  getuserinput() 
 elif userinput == 'p':
  print('')
  print('printing...')
  printblockchain()
  getuserinput() 
 elif userinput == 'h':
  print('')
  print('hacking..')
  manipulateblockchain()
  getuserinput() 
 elif userinput == 'm':
  print('')
  print('mining..')
  mine()
  getuserinput() 
 elif userinput == 'c':
  print('')
  print('checking blockchain..')
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
 genblock = {
   'previous_hash': '',
   'index': 0,
   'transactions': []
 }
 BLOCKCHAIN.append(genblock)

def printblockchain():
  print(BLOCKCHAIN)

def get_block_hash(index):
  """[summary]
  
  Arguments:
    index {[int]} -- [index from hashable block]
  """
  global BLOCKCHAIN

  previous_block = BLOCKCHAIN[index]
  previous_block_dump = json.dumps(previous_block, sort_keys=True)
  previous_block_hashed = hl.sha256(previous_block_dump.encode()).hexdigest()

  return previous_block_hashed

  # get previous block
  # hash previous block


def create_transaction():
 #  create transaction dictionary
 recipient = input("Who are you sending money? ")
 amount = input("How much are you sending? $")

 transaction = {
   'sender':USERNAME,
   'recipient':recipient,
   'amount':amount
 }

 TRANSACTION_QUEUE.append(transaction)


def mine():
  # add block to blockchain
  global BLOCKCHAIN
  global TRANSACTION_QUEUE

  index = len(BLOCKCHAIN)

  previous_hash = get_block_hash(index-1)

  new_block = {
    'previous_hash':previous_hash,
    'index':index,
    'transactions':TRANSACTION_QUEUE
  }

  TRANSACTION_QUEUE = []

  BLOCKCHAIN.append(new_block)

  # # reward miner


def checkblockchainhealth():
  is_healthy = True

  # compare hash with previous block
  for index, block in enumerate(BLOCKCHAIN):
    print(block,index)
    previous_hash_from_actual_block = get_block_hash(index-1)
    previous_hash_from_current_block = block.previous_block

    if(previous_hash_from_actual_block != previous_hash_from_current_block):
      is_healthy = False
  
  if is_healthy:
    print('The blockchain is fine!')
  else:
    print('The blockchain was hacked!')

def manipulateblockchain():
  block_to_change = input('Which block do you want to hack? Type a number from 1 to ' + str(len(BLOCKCHAIN) - 1) + ' -> ')

  block_to_change = int(block_to_change)

  BLOCKCHAIN[block_to_change - 1] = 'hacked block'



# Init program
getusername()
creategensisblock()
getuserinput(True)