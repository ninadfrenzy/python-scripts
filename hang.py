# import getpass to read input without echo on console

import getpass


# define a function for the game
def Hangman():
	print("\t\t\tWELCOME TO HANGMAN")
	PlayerName = input("\n\nENTER PLAYER NAME : ")
	print("\nHello "+ PlayerName + ",let's play hangman!")
	print("\n RULES:\n1.one player enters a secret word\n2.other player guesses the alphabets from the word\n3.valid input is only a single alphabet(a-z) and digits,special chars,etc are\n not allowed\n4.only one character at a time \n5.5 chances allowed for incorrect guess\n6.Have fun!")
	Word = getpass.getpass("\nEnter the word : ")
# set chances and create an empty string
	Chances = 5
	Guessed	= ''
	while Chances>0:
# maintain a counter for number of _ printed
		FailCount=0
# for every letter in the word we check if the letter has been entered 
		for Letter in Word:
			if(Letter in Guessed):
				print(Letter,end='')
			else:
				print("_",end='')
				FailCount=FailCount+1
#checking if player won?
		if(FailCount==0):
			print("\nAll hail lord " + PlayerName + "!!")
			break
#accepting input from user
		while True:
			NewGuess=input("\nGuess a Letter : ")			
			if(len(NewGuess)==1 and NewGuess.isalpha() and NewGuess not in Guessed):
				break
			print("\nRE-ENTER (INVALID INPUT READ RULES)")
#append this input to our empty string
		Guessed=Guessed+NewGuess.lower()
		if(NewGuess not in Word):
			print("\nSorry wrong guess")
			Chances=Chances-1
#checking if player lost
	if(Chances==0):
		print("\nSorry! you lose")
Hangman()
