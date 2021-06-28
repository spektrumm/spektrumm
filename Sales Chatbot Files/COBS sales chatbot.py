# COBS Sales Chatbot
# Author: Nathan Hare
# Date started: Oct 14th, 2020
# Date completed: TBD


# import libraries for use later in the program
import random
import time
import decimal

# define lists for different products offered at COBS

loafList = ['sourdough loaf',
        'white loaf',
        'whole wheat loaf',
        'sunflower flax sourdough loaf',
        'cape seed loaf',
        'country grain loaf',
        'german rye',
        'challah braid',
        'challah loaf',
        'pane di casa loaf',
        'olive pane di casa loaf',
        'chia white loaf',
        'apricot delight log',
        'chia fruit loaf',
        'chia whole wheat loaf',
        'garlic cheddar sourdough vienna',
        'sourdough vienna',
        'sourdough cob',
        'high fibre loaf',
        'cinnamon loaf'
        ]

miniLoafList = ['white mini loaf',
            'whole wheat mini loaf',
            'country grain mini loaf',
            'sourdough demi cob',
            'high fibre mini loaf',
            'cape seed mini loaf',
            'cinnamon mini loaf'
            ]

farmersLoafList = ['white farmers loaf',
                'whole wheat farmers loaf',
                'country grain farmers loaf'
                ]

baguetteList = ['herb and garlic half baguette',
            'french baguette',
            'pane di casa baguette',
            'pane di casa half baguette',
            'sourdough baguette',
            'garlic cheddar sourdough baguette'
            ]

sconeList = ['double chocolate scone',
            'lemon blueberry scone',
            'strawberry passion fruit scone',
            'berry and white chocolate scone',
            'cinnamon scone',
            'pumpkin scone',
            'banana chocolate scone'
            ]


# define prices for items - WIP
sconePrice = 2.68

# define some lists containing different strings for use with the random function

listRandomAE = ['Anything else?',
                'Anything else for you today?',
                'Was there anything else you were looking for?'
                ]

listRandomCanI = ['What else can I grab you?',
                'What can I get for you?',
                'Anything in particular you were looking for?'
                ]

randomPartingList = ['Enjoy the rest of your day!',
                    'Have a good day!',
                    'See you next time.',
                    'Enjoy your purchase.', # @ Linda
                    'Goodbye.'
                    ]

# use the imported random function
responseRandomAE =  random.choice(listRandomAE)
responseRandomCanI = random.choice(listRandomCanI)
randomPartingMessage = random.choice(randomPartingList)

# display a welcoming message
print('Hello! Welcome to COBS Bread.')

# add natural reading delay
time.sleep(0.5)

# define an empty list to begin the order
yourOrder = []

# set the total order cost to 0, for addition to later
totalCostOrder = 0

# ask the user the first input
getYou = input('What can I get for you? ').lower()

# define a set of functions used to ask the user certain questions and manipulate their order as a list

def getYouFunction():
    getYou = input(f'{responseRandomCanI} ').lower()
    if getYou == 'cinnamon bun' or getYou == 'cinnamon roll' or getYou == 'pumpkin scone':
        icingFunction()
    elif (getYou) in loafList:
        sliceFunction()
    elif (getYou) in miniLoafList:
        sliceFunction()
    elif (getYou) in farmersLoafList:
        sliceFunction()
    else:
        yourOrder.append(getYou)

def sliceFunction():
    slicedQ = input('Sliced or Unsliced? ').lower()
    if slicedQ == 'sliced':
        regularOr = input('Regular or Thick sliced? ').lower()
        if regularOr == 'regular':
            updatedGetYou = (f'{getYou} - R')
            yourOrder.append(updatedGetYou)
        elif regularOr == 'thick':
            updatedGetYou = (f'{getYou} - T')
            yourOrder.append(updatedGetYou)
    else:
        yourOrder.append(getYou)

def icingFunction():
    icingQ = input('With or without icing? ').lower()
    if icingQ == 'with' or icingQ == 'with icing':
            updatedGetYou = (f'{getYou} - Iced')
            yourOrder.append(updatedGetYou)
    else:
            yourOrder.append(getYou)

def firstGetYouFunction():
    if getYou == 'cinnamon bun' or getYou == 'cinnamon roll' or getYou == 'pumpkin scone':
        icingFunction()
    elif (getYou) in loafList:
        sliceFunction()
    elif (getYou) in miniLoafList:
        sliceFunction()
    elif (getYou) in farmersLoafList:
        sliceFunction()
    else:
        yourOrder.append(getYou)


# call the first getYou function for the first question asked before the while loop
firstGetYouFunction()

# ask the user an input that will serve as the conditionary statement for our while loop
anythingAnswer = input(f'{responseRandomAE} (Y/N) ').lower()

# run a while loop based on the conditionary statement with regards to our anythingAnswer input taken previously

while anythingAnswer != 'no':
    getYouFunction()
    
    anythingAnswer = input(f'{responseRandomAE} (Y/N) ').lower()

# print out the final order for the user along with the total cost of their order

print(yourOrder)
print(f'Your total today is: ${float(totalCostOrder)}.')

# define a function to check the method in which the user chooses to pay by
def paymentMethodCheck():
    paymentQuestion = input('How would you like to pay? (Cash, Card, Gift Card) ').lower()

    if paymentQuestion == 'cash':
        cashGiven = float(input('Enter the amount of cash you will be paying with: '))
        if cashGiven == totalCostOrder:
            print('Exact change, awesome!')
        else:
            changeGiven = cashGiven - float(totalCostOrder)
            print(f'Here is your change: ${changeGiven}')
    
    elif paymentQuestion == 'card':
        print('Should be ready on the machine in just a moment.')
    
    elif paymentQuestion == 'gift card': # WIP
        print('Go ahead and swipe your card on the machine.')
        #time.sleep(0.5)
        #remainingBalanceGC = input('Would you like a receipt with your remaining balance? (Y/N) ').lower()
        #if remainingBalanceGC == 'yes':
            #print(balanceGCreceipt)
        #else:
            #continue
    
    else:
        print("Hmm, sorry I'm not quite sure we accept that here.")

        time.sleep(1)
        paymentMethodCheck()

paymentMethodCheck()

#time.sleep(.4)
#bagCheck() - WIP

#time.sleep(.3)
#receiptCheck() - WIP

#with open ('COBS-sales-bot-transaction-history.txt', 'a') as 'previousTransactionFile':
    #WIP

time.sleep(0.8)
print(randomPartingMessage)
