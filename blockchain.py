# Variables
import hashlib as hl
import json
import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

# string = 'sataeta'
# hashed = hl.sha256(string.encode())


# dictionary = {'key1':1,'key2':2}

# json_dumped = json.dumps(dictionary, sort_keys=True)
# print(json_dumped)
BLOCKCHAIN = []
TRANSACTION_QUEUE = []
USERNAME = ""
PARTICIPANTS = set()

def init():
  global BLOCKCHAIN, TRANSACTION_QUEUE

  file = open('blockchain.txt','r')
  try:
    data_from_file = eval(file.read())

    BLOCKCHAIN = data_from_file['blockchain']
    TRANSACTION_QUEUE = data_from_file['transactions_queue']
    # todo: save participants info from file to PARTICIPANTS variable
  except:
    BLOCKCHAIN = []
    TRANSACTION_QUEUE = []
    USERNAME = ""
    PARTICIPANTS = set()


def getusername():
 global USERNAME, PARTICIPANTS
 USERNAME = input('Hi, what is your name? ')
 PARTICIPANTS.add(USERNAME)

def getuserinput(showinstructions=False):
 checkblockchainhealth() 
 if showinstructions:
  print('')
  print('/++++++++++/')
  print('a: for adding a transaction')
  print('p: for printing the blockchain blocks')
  print('b: for getting balance')
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
    print_blockchain()
    getuserinput() 
  elif userinput == 'h':
    print('')
    print('hacking..')
    manipulateblockchain()
    getuserinput() 
  elif userinput == 'b':
    print('')
    print('getting balance..')
    print_balance(USERNAME)
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

def create_gensis_block():

  global USERNAME

  transaction = {
    'sender':'WELCOME_REWARD',
    'recipient':USERNAME,
    'amount':1000
  }

  genblock = {
    'previous_hash': '',
    'index': 0,
    'transactions': [transaction]
  }

  BLOCKCHAIN.append(genblock)

def print_blockchain():
  print(BLOCKCHAIN)
  print(PARTICIPANTS)
  print(TRANSACTION_QUEUE)

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

def get_user_balance(user):
  global BLOCKCHAIN

  user_balance = 0

  for index, block in enumerate(BLOCKCHAIN):
    transactions = block['transactions']

    for transaction in transactions:
      if user == transaction['recipient']:
        amount = int(transaction['amount'])
        user_balance += amount

      if user == transaction['sender']:
        amount = int(transaction['amount'])
        user_balance -= amount

  for index, item in enumerate(TRANSACTION_QUEUE):
    pending_transaction = item

    if user == pending_transaction['recipient']:
      amount = int(pending_transaction['amount'])
      user_balance += amount

    if user == pending_transaction['sender']:
      amount = int(pending_transaction['amount'])
      user_balance -= amount
  
  return user_balance

def print_balance(user):
  balance = get_user_balance(user)
  print('Your current balance', balance)

def create_transaction():
  #  create transaction dictionary
  global PARTICIPANTS, USERNAME
  recipient = input("Who are you sending money? ")
  PARTICIPANTS.add(recipient)
  user_balance = get_user_balance(USERNAME)

  try:
    amount = int(input("How much are you sending? $"))

    if user_balance > amount:
      add_transaction(amount,recipient,USERNAME,user_balance)
    else:
      print('You do not have enough money!')

  except:
    print("Wrong input, please input a number")
    create_transaction()


def add_transaction(amount,recipient,sender,user_balance):
  global TRANSACTION_QUEUE

  transaction = {
    'sender':sender,
    'recipient':recipient,
    'amount':amount
  }

  TRANSACTION_QUEUE.append(transaction)

  print('')
  print('Initial balance', user_balance)
  print('Transfer', amount)
  print('Final balance', user_balance - amount)
  print('')

def reward_miner(username):
  reward = {
   'sender':'MINING',
   'recipient':username,
   'amount':200
  }

  TRANSACTION_QUEUE.append(reward)

def mine():
  # add block to blockchain
  global BLOCKCHAIN, TRANSACTION_QUEUE, USERNAME

  index = len(BLOCKCHAIN)

  previous_hash = get_block_hash(index-1)


  need_proof_work = True

  nonce = 0
  # Proof of work

  while(need_proof_work):
    nonce += 1
    new_block = {
      'previous_hash':previous_hash,
      'index':index,
      'transactions':TRANSACTION_QUEUE,
      'nonce': nonce
    }

    new_block_dumped = json.dumps(new_block, sort_keys=True)
    new_block_hash = hl.sha256(new_block_dumped.encode()).hexdigest()

    proof_of_work = new_block_hash[:2]

    if(proof_of_work == 'aa'):
      need_proof_work = False


  TRANSACTION_QUEUE = []

  BLOCKCHAIN.append(new_block)

  # # reward miner
  reward_miner(USERNAME)
  save_blockchain()


def save_blockchain():
  global BLOCKCHAIN, TRANSACTION_QUEUE, PARTICIPANTS

  participants = repr(PARTICIPANTS)

  file_info = {
    'blockchain': BLOCKCHAIN,
    'transactions_queue': TRANSACTION_QUEUE,
    'participants': participants
  }

  file_info = json.dumps(file_info, sort_keys=True)
  
  file = open('blockchain.txt','w')
  file.write(file_info)

def checkblockchainhealth():
  is_healthy = True

  if len(BLOCKCHAIN)>1:

    # compare hash with previous block
    for index, block in enumerate(BLOCKCHAIN):
      if index > 0:
        previous_hash_from_actual_block = get_block_hash(index-1)
        previous_hash_from_current_block = block['previous_hash']

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
init()
getusername()
create_gensis_block()
getuserinput(True)