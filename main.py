import random
"""
f = open("wordlist2.txt", "r")
g = open("wordlist4.txt", "a")
with open("wordlist3.txt") as w:
    items = f.readlines()
    items2 = w.readlines()
    #items3 = g.readlines()
    print(items)
    for item in items2:
        if item not in items:
            g.write(item)
        #inFile = False
        #for word in w:
        #    if word == item:
        #        inFile = True
        #        break
        #if not inFile:
        #    g.write(item)
f.close()
g.close()
"""


def PrintBoard(letters):
    middle_letter = letters[0]
    other_letters = letters[1:7]
    print("           _______          ")
    print("          /       \         ")
    print("  _______/   ", other_letters[0], "   \_______   ")
    print(" /       \         /       \  ")
    print("/   ", other_letters[1], "   \_______/   ", other_letters[2], "   \ ")
    print("\         /       \         / ")
    print(" \_______/   ", middle_letter, "   \_______/  ")
    print(" /       \         /       \  ")
    print("/   ", other_letters[3], "   \_______/   ", other_letters[4], "   \ ")
    print("\         /       \         / ")
    print(" \_______/   ", other_letters[5], "   \_______/  ")
    print("         \         /        ")
    print("          \_______/         ")


def AddWords(letters, showBoard):
    if showBoard:
        PrintBoard(letters)
    words = []
    with open("wordlist2.txt") as w:

        # parse the word list file to add all possible words with the given letters (that contain the middle letter) to a list
        for line in w:
            letterInPuzzle = True
            middle_letter_count = 0
            for letter in line:
                if letter == '\n':
                    break
                if letter not in letters:
                    letterInPuzzle = False
                    break
                if letter == letters[0]:
                    middle_letter_count += 1
            if letterInPuzzle and middle_letter_count > 0:
                if len(line) >= 5:
                    words.append(line[0:-1])
    w.close()
    return words, letters


def PlayGame(words, letters, totalPoints):
    option = ""
    myWords = []
    lettered_list = letters

    # set the point values for each ranking
    pointTotals = {
        "GENIUS": round(totalPoints*0.7),
        "AMAZING": round(totalPoints*0.5),
        "GREAT": round(totalPoints*0.4),
        "NICE": round(totalPoints*0.25),
        "SOLID": round(totalPoints*0.15),
        "GOOD": round(totalPoints*0.08),
        "MOVING UP": round(totalPoints*0.05),
        "GOOD START": round(totalPoints*0.02),
        "BEGINNER": 0
    }
    userPoints = 0
    currentLevel = 'BEGINNER'

    # play puzzle until user quits or obtains all the words
    while option != 'Q' and len(myWords) != len(words):

        # check if the user reached a new ranking
        for key in pointTotals:
            if userPoints >= pointTotals[key]:
                if key == currentLevel:
                    break
                print("New level reached:", key)
                currentLevel = key
                break
        option = input("Enter word:")

        # check if the user entered a command: S, B, H, W, P, or Q

        # S: shuffle the board
        if option == 'S':
            lettered_list = []
            middle_letter = letters[0]
            other_letters = letters[1:7]
            random.shuffle(other_letters)
            lettered_list.append(middle_letter)
            for item in other_letters:
                lettered_list.append(item)
            PrintBoard(lettered_list)

        # B: print the board
        elif option == 'B':
            PrintBoard(lettered_list)

        # H: display the help menu
        elif option == 'H':
            print("\nHere is the help guide for Spelling Bee!")
            print("Rules:")
            print("  - Create words by using the letters around the letter board (the hive)")
            print("  - Words must be at least 4 letters long, and every word must contain the center letter")
            print("  - You can reuse letters as much as you want in a word")
            print("  - For words of length 4, you earn 1 point. For words of greater length, you earn 1 point per letter")
            print("  - Every puzzle has at least 1 pangram word, which contains all the letters around the hive at least once. These are worth 7 extra points!")
            print("When prompted for a word, you can also type one of the following commands:")
            print("  - B to view the letter board (the hive)")
            print("  - S to shuffle the letter board (the hive)")
            print("  - P to view your number of words, point totals, and the total number of words and points to reach each level")
            print("  - W to view the words you have obtained")
            print("  - Q to quit this puzzle")
            print("  - H to bring up this help menu\n")

        # W: display all the user's obtained words
        elif option == 'W':
            print("\nYou have found", len(myWords), "words:")
            for word in myWords:
                print(word)
            print("")

        # P: display the points for each ranking, and the user's total points and ranking
        elif option == 'P':
            print("\nTotal number of words:", len(words))
            print("Total number of points:", totalPoints)
            print("Your number of words:", len(myWords))
            print("Your current score:", userPoints)
            print("Your current level:", currentLevel)
            print("Point totals:")
            for key, value in pointTotals.items():
                print(" ", key, value)
            print("")

        # Q: quit the puzzle
        elif option == 'Q':
            break

        # check the user didn't already obtain the word they entered
        elif option in myWords:
            print("You've already gotten this word.")

        # check if the user's word matches a word in the word list
        elif option.upper() in words:
            letter_list = []

            # count the number of distinct letters in the user's word
            for letter in option:
                if letter not in letter_list:
                    letter_list.append(letter)

            # checks if the user's word contains all the letters, this is a pangram and the user earns 7 extra points
            if len(letter_list) == 7:
                print("PANGRAM! +{} points".format(len(option)+7))
                userPoints += len(option)+7

            # otherwise, the user earns 1 point for a 4-letter word and n points for an n-length word > 4
            elif len(option) == 4:
                print("Good! +1 point")
                userPoints += 1
            elif len(option) <= 6:
                print("Nice! +{} points".format(len(option)))
                userPoints += len(option)
            else:
                print("Awesome! +{} points".format(len(option)))
                userPoints += len(option)
            myWords.append(option)
            myWords.sort()
        else:
            print("Not accepted. Either this word is not in the word list, contains letters not in the hive, is too short, or it does not contain the middle letter.")

        # checks if the user obtained all the words in the puzzle
        if len(myWords) == len(words):
            print("YOU FOUND ALL THE WORDS. YOU ARE A QUEEN BEE!")

    # print any words in the puzzle that the user did not obtain
    if len(myWords) != len(words):
        print("Here are the words that you missed:")
        words.sort()
        counter = 0
        for word in words:
            if word not in myWords:
                if counter % 10 == 9:
                    print(word)
                else:
                    print(word, "", end="")
                counter += 1
        print("")


def RandomGen():
    lettersList = ['A', 'B', 'C', 'D', 'E',
             'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    acceptableLetters = False
    randLetList = []

    # generate a set of seven unique letters until all the following conditions hold
    while not acceptableLetters:
        randLetList = random.sample(lettersList, 7)
        vowelList = ['A','E','I','O','U']
        vowelCount = 0
        for letter in randLetList:
            if letter in vowelList:
                vowelCount += 1

        # check for no I, N, G
        #if 'I' in randLetList and 'N' in randLetList and 'G' in randLetList:
        #    acceptableLetters = False

        # check for no E and D
        #elif 'E' in randLetList and 'D' in randLetList:
        #    acceptableLetters = False

        # check for no S
        if 'S' in randLetList:
            acceptableLetters = False

        # check for no E and R
        elif 'E' in randLetList and 'R' in randLetList:
            acceptableLetters = False

        # check for U with Q
        elif 'Q' in randLetList and 'U' not in randLetList:
            acceptableLetters = False

        # check vowel count
        elif vowelCount < 1 or vowelCount > 3:
            acceptableLetters = False

        else:
            words, letters = AddWords(randLetList, False)

            # check acceptable word count
            if len(words) < 17 or len(words) > 81:
                acceptableLetters = False
            else:

                # check that a pangram exists in this set of letters
                pangram = False
                for word in words:
                    letArr = []
                    for letter in word:
                        if letter not in letArr:
                            letArr.append(letter)
                    if len(letArr) == 7:
                        pangram = True
                if pangram:
                    acceptableLetters = True
    return randLetList


if __name__ == '__main__':
    print("Welcome to Spelling Bee! Press P to start a new puzzle. Press Q to quit.")
    option = ""
    with open("letterlist.txt") as l:
        while option != 'Q':
            option = input("Enter:")
            if option == 'P':
                l.seek(0)
                content = l.readlines()

                # format the output of the file to make it more readable for the user when selecting a puzzle to play
                for line in content:
                    lets = line[3:-1]
                    arr = []
                    for let in lets:
                        arr.append(let)
                    arr.sort()
                    print("Puzzle #", line[0:2], end="")
                    print(" (letters: ", end="")
                    for let in arr:
                        print(let, "", end="")
                    print(") ", end="")
                    print("( middle letter:", line[3], ")")
                validPuzzle = False
                randomPuzzle = False

                # input validation to check the user entered a valid puzzle number or R for a random puzzle
                while not validPuzzle:
                    puzzleNum = input("\nWhich puzzle would you like to play? (type the number, or R for a random set of letters): ")
                    if puzzleNum == 'R':
                        randomPuzzle = True
                        validPuzzle = True
                    elif puzzleNum.isdigit() and 0 < int(puzzleNum) <= len(content):
                        validPuzzle = True

                # call a function to generate random letters if random puzzle
                if randomPuzzle:
                    randLetList = RandomGen()
                    words, letters = AddWords(randLetList, True)

                # otherwise, pass the letters for the appropriate puzzle in to AddWords
                else:
                    c = content[int(puzzleNum)-1]
                    let = c[3:]
                    letterArray = []
                    for letter in let:
                        letterArray.append(letter)
                    words, letters = AddWords(letterArray, True)
                totalPoints = 0

                # count the total number of points in this puzzle
                for word in words:
                    if len(word) == 4:
                        totalPoints += 1
                    elif len(word) < 7:
                        totalPoints += len(word)
                    else:
                        letter_list = []
                        
                        # checks if the word contains all 7 letters, this is a pangram
                        for letter in word:
                            if letter not in letter_list:
                                letter_list.append(letter)
                        if len(letter_list) == 7:
                            totalPoints += len(word) + 7
                        else:
                            totalPoints += len(word)

                PlayGame(words, letters, totalPoints)
                print("Would you like to play again with a different set of letters? Press P to play again, Q to quit.")
    l.close()
