print('Hello!')
s = input("What's your name? ")

count = 0

w, h = 3, 3
transactions = [[0 for x in range(w)] for y in range(h)] 

print('')

while count < 3:
 n = str(count + 1)
 print('')
 print('/------Transaction #' + n +'--------/')
 print('')
 transactions[count][0] = input("Who are you sending money? ")
 transactions[count][1] = input("How much are you sending to "+ transactions[count][0] +"? $")
 transactions[count][2] = s
 count += 1

print('')
print('')
print('/----Transaction summary-----/')
print('')
print(transactions)
print('')