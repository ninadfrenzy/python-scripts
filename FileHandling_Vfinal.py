
#open method takes two parameters filename and mode of opening(to create new file "w" mode is mandatory)
FileObject = open("new_file.txt",'w')

#writing a string into file and user defined string too
#FileObject.write("this is a file that i want to read and perform several operations on it\n")
#FileObject.write("also US is a superpower , JAPAN makes some great ramen , and candies are sweet\n")
FileObject.write(input("Enter something"))

#close file
FileObject.close()

#we will need this list of words for multiple functions
def CreateList():
    FileObject = open("new_file.txt", 'r+')
    ListOfWords = list()
    for lines in FileObject:
        ListOfWords = ListOfWords + list(lines.split())
    FileObject.close()
    return ListOfWords

def CountingWords():
    # open file in rw mode
    FileObject = open("new_file.txt", 'r+')

    # make a list of all words from the file

    ListOfWords=CreateList()
    print("Number of words : " + str(len(ListOfWords)))
    print("Number of unique words : " + str(len(set(ListOfWords))))

    FileObject.close()

def CountingSpaces():
    FileObject = open("new_file.txt", 'r+')

    CompleteString=FileObject.read()

    print("Number of spaces : "+str(CompleteString.count(' ')))
    print("Number of new lines : " + str(CompleteString.count('\n')))
    print("Number of tabs : " + str(CompleteString.count('\t')))

    FileObject.close()

def CountingCharacters():
    FileObject = open("new_file.txt", 'r+')
    CharCounter = 0
    UpperCase = 0
    LowerCase=0
    Digit=0
    ListOfWords=CreateList()
    CompleteString=FileObject.read()
    # count characters in file
    for Element in ListOfWords:
        for Letter in Element:
            CharCounter = CharCounter + 1
            if(Letter.isupper()):
                UpperCase=UpperCase+1
            elif(Letter.islower()):
                LowerCase=LowerCase+1
            elif(Letter.isdigit()):
                Digit=Digit+1


    print("Number of characters : " + (str(CharCounter)))
    print("Number of uppercase letters : " + (str(UpperCase)))
    print("Number of lowercase letters : " + (str(LowerCase)))
    print("Number of digit : " + (str(Digit)))
    print("Number of special characters : " + (str(sum(CompleteString.count(x) for x in ['[','!','@','#','$','%','^','&','*','(',')']))))
    FileObject.close()

def GetFrequency():
    ListOfWords=CreateList()
    FrequencyDictionary={Item:ListOfWords.count(Item) for Item in ListOfWords}
    print("Frequency is : ")
    print(FrequencyDictionary)
while True:
    print("1.NUMBER OF WORDS\n2.NUMBER OF SPACES\n3.NUMBER OF CHARACTERS\n4.FREQUENCY LIST\n5.EXIT")
    choice=int(input("enter a number(0 to exit)"))
    if(choice==1):
        CountingWords()
    elif(choice==2):
        CountingSpaces()
        print("2")
    elif(choice==3):
        CountingCharacters()
        print("3")
    elif(choice==4):
        GetFrequency()
        print("4")
    elif(choice==5):
        break
    else:
        print("invalid choice re enter")
