#this program is kayles game
#auther:rawan tarek

ListOfNumbers = []
def List ():
    global number
    number = int(input(" how many numbers you want "))
    for number in range(0, number):
        ListOfNumbers.append(number)
    print(ListOfNumbers)
#this to determine the length of list according to user needs i trace i with 20
def twoenters1 ():
    global player1F,player1S
    player1F = int(input('player 1 first digit:'))
    player1S = int(input('player 1  second digit:'))
def twoenters2():
    global player2F
    global player2S
    player2F = int(input('player 2 first digit:'))
    player2S = int(input('player 2  second digit:'))
#to recieve first & second digit from each player
def enters () :
   global numberOfInputs
   numberOfInputs = int(input(' player 1 , do you want enter 1 or 2 numbers'))
   # to know from user if he want to enter 1 number or 2 numbers
   if numberOfInputs == 2:
    twoenters1()
    #if the user want to enter 2 numbers we recieve first and second number
    if player1F and player1S in ListOfNumbers:
        if ListOfNumbers[player1F] == ListOfNumbers[player1S] + 1 or ListOfNumbers[player1F] == ListOfNumbers[ player1S] - 1:
    #these conditions to ensure that the numbers the user entered are in the list and that they adjacent
            ListOfNumbers[player1F] = '-'
            ListOfNumbers[player1S] = '-'
            print(ListOfNumbers)
# to replace the digits the user choose to '-' then print the list
        else :
            print('please enter adjacent numbers ')
            enters()
            # if the numbers weren't adjacent call enters() to enter right inputs
    else:
      if player1F or player1S not in ListOfNumbers:
       if ListOfNumbers[player1F] == '-' or ListOfNumbers[player1S] == '-':
         print("already chosen")
         enters()
         # if the numbers the user enter weren't in the list and if the digits he entered were already ='-'
         #in the list tell the user that it were already chosen and call enters()
       else:
          print('Please Enter Valid Numbers')
          enters()
         # if numbers weren't in the list tell the user to enter valid numbers the call inputs()
   elif  numberOfInputs == 1:
       global player1
       player1 = int(input('player 1 :'))
       if player1 in ListOfNumbers:
           ListOfNumbers[player1] = '-'
           print(ListOfNumbers)
           # if the user want to enter one number and the number is in the list replace it with '-' in the list

       else:
        if player1 not in ListOfNumbers:
          if ListOfNumbers[player1] == '-':
           print("already chosen")
           enters()
          else:
              print('Please Enter Valid Number')
              enters()
        # if the number was already replaced in list with '-' tell user that is already chosen
   else:
       while numberOfInputs != 1 and numberOfInputs != 2:
           print("please Enter valid number ")
           enters()
       # while the user enter number of inputs more than 2 or less than 1 tell him to enter valid number
def enters2():
    global numberOfInputs
    numberOfInputs = int(input(' player 2 , do you want enter 1 or 2 numbers'))
    # to know from user if he want to enter 1 number or 2 numbers
    if numberOfInputs == 2:
        twoenters2()
    # if the user want to enter 2 numbers we recieve first and second number
        if player2F and player2S in ListOfNumbers:
            if  ListOfNumbers[player2F] == ListOfNumbers[player2S] + 1 or ListOfNumbers[player2F] == ListOfNumbers[player2S] - 1:
             # these conditions to ensure that the numbers the user entered are in the list and that they adjacent
             ListOfNumbers[player2F] = '-'
             ListOfNumbers[player2S] = '-'
             print(ListOfNumbers)
             # to replace the digits the user choose to '-' then print the list
            else :
                print('Please enter adjacent numbers ')
                enters2()
             # if the numbers weren't adjacent call enters() to enter right inputs
        else:
            if player2F or player2S not in ListOfNumbers:
                if ListOfNumbers[player2F] == '-' or ListOfNumbers[player2S] == '-':
                    print("already chosen")
                    enters2()
                # if the numbers the user enter weren't in the list and if the digits he entered were already ='-'
                # in the list tell the user that it were already chosen and call enters()
                else:
                    print('Please Enter Valid Numbers')
                    enters2()
                # if numbers weren't in the list tell the user to enter valid numbers the call inputs()
    elif numberOfInputs == 1:
        global player2
        player2 = int(input('player 2 :'))
        if player2 in ListOfNumbers:
            ListOfNumbers[player2] = '-'
            print(ListOfNumbers)
        # if the user want to enter one number and the number is in the list replace it with '-' in the list
        else:
            if player2 not in ListOfNumbers:
                if ListOfNumbers[player2] == '-':
                    print("already chosen")
                    enters2()
                    # if the number was already replaced in list with '-' tell user that is already chosen
    else:
        while numberOfInputs != 1 and numberOfInputs != 2:
            print("please Enter valid number ")
            enters2()
            # while the user enter number of inputs more than 2 or less than 1 tell him to enter valid number
List()
while ListOfNumbers[:] != '-':
    #to repeat actions untill the all indexes in the list be replaced with '-'
 enters()
 if ListOfNumbers.count(ListOfNumbers[0]) == len(ListOfNumbers):
     print('player 1 wins')
     break
 enters2()
 if ListOfNumbers.count(ListOfNumbers[0]) == len(ListOfNumbers):
     print('player 2 wins')
     break
    #if the first index is equal to all indexes in the list it means thai is empty then the last player
    #who choose the last digit is the winner