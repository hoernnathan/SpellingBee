import random

def CreateBoard(letters):
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

def AddWords(c):
    letters = []
    for letter in c:
        letters.append(letter)
    #print(letters)
    CreateBoard(letters)
    words = []
    with open("wordlist2.txt") as w:
        for line in w:
            flag = True
            middle_letter_count = 0
            for letter in line:
                if letter == '\n':
                    break
                if letter not in letters:
                    flag = False
                    break
                if letter == letters[0]:
                    middle_letter_count += 1
            if flag and middle_letter_count > 0:
                if len(line) >= 5:
                    words.append(line[0:-1])
    w.close()
    #for word in words:
        #print(word)
    return words, letters

def PlayGame(words, letters, totalPoints):
    option = ""
    myWords = []
    lettered_list = letters
    #print(totalPoints)
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
    while option != 'Q' and len(myWords) != len(words):
        #print("Enter a word by typing it below. Enter S to shuffle the letters in the hive, W to view your words, or H to bring up a help menu, or G when you are ready to give up.")
        for key in pointTotals:
            if userPoints >= pointTotals[key]:
                if key == currentLevel:
                    break
                print("New level reached:", key)
                currentLevel = key
                break
        option = input("Enter:")
        if option == 'S':
            lettered_list = []
            middle_letter = letters[0]
            other_letters = letters[1:7]
            random.shuffle(other_letters)
            lettered_list.append(middle_letter)
            for item in other_letters:
                lettered_list.append(item)
            CreateBoard(lettered_list)
        elif option == 'B':
            CreateBoard(lettered_list)
        elif option == 'H':
            print("Here is the help guide for Spelling Bee!")
            print("Rules:")
            print("  - Create words by using the letters around the letter board (the hive)")
            print("  - Words must be at least 4 letters long, and every word must contain the center letter")
            print("  - You can reuse letters as much as you want in a word")
            print("  - For words of length 4, you earn 1 point. For words of greater length, you earn 1 point per letter")
            print("  - Every puzzle has at least 1 pangram word, which contains all the letters around the hive at least once. These are worth 7 extra points!")
            print("When prompted for a word, you can also type one of the following:")
            print("Commands:")
            print("  - B to view the letter board (the hive)")
            print("  - S to shuffle the letter board (the hive)")
            print("  - P to view your number of words, point totals, and the total number of words and points to reach each level")
            print("  - Q to quit this puzzle")
            print("  - H to bring up this help menu")
        elif option == 'W':
            print("Obtained words: ")
            for word in myWords:
                print(word)
            print("")
        elif option == 'P':
            print("Total number of words:", len(words))
            print("Total number of points:", totalPoints)
            print("Your number of words:", len(myWords))
            print("Your current score:", userPoints)
            print("Your current level:", currentLevel)
            print("Point totals:")
            for key, value in pointTotals.items():
                print(" ", key, value)
        elif option == 'Q':
            break
        elif option in myWords:
            print("You've already gotten this word.")
        elif option.upper() in words:
            letter_list = []
            # checks if the user's word contains all the letters, this is a pangram
            for letter in option:
                if letter not in letter_list:
                    letter_list.append(letter)
            if len(letter_list) == 7:
                print("PANGRAM! +", len(option)+7, "points")
                userPoints += len(option)+7
            elif len(option) == 4:
                print("Good! +", 1, "point")
                userPoints += 1
            elif len(option) <= 6:
                print("Nice! +", len(option), "points")
                userPoints += len(option)
            else:
                print("Awesome! +", len(option), "points")
                userPoints += len(option)
            myWords.append(option)
            myWords.sort()
        else:
            print("Not accepted. Either this word is not in the word list, contains letters not in the hive, is too short, or it does not contain the middle letter.")
        if len(myWords) == len(words):
            print("YOU FOUND ALL THE WORDS. YOU ARE A QUEEN BEE!")
    if len(myWords) != len(words):
        print("Here are the words that you missed:")
        counter = 0
        for word in words:
            if word not in myWords:
                if counter % 10 == 9:
                    print(word)
                else:
                    print(word, "", end="")
                counter += 1
        print("")


if __name__ == '__main__':
    print("Welcome to Spelling Bee! Press P to start a new puzzle. Press Q to quit.")
    option = ""
    # TODO: make the input file dynamic for users
    with open("letterlist.txt") as l:
        while option != 'Q':
            option = input("Enter:")
            if option == 'P':
                l.seek(0)
                content = l.readlines()
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
                puzzleNum = input("Which puzzle would you like to play? (type the number)")
                c = content[int(puzzleNum)-1]
                let = c[3:]
                words, letters = AddWords(let)
                totalPoints = 0
                for word in words:
                    if len(word) == 4:
                        totalPoints += 1
                    elif len(word) < 7:
                        totalPoints += len(word)
                    else:
                        letter_list = []
                        # checks if the user's word contains all the letters, this is a pangram
                        for letter in word:
                            if letter not in letter_list:
                                letter_list.append(letter)
                        if len(letter_list) == 7:
                            totalPoints += len(word) + 7
                        else:
                            totalPoints += len(word)
                    #print("Total points in this puzzle:", totalPoints)
                PlayGame(words, letters, totalPoints)
                print("Would you like to play again with a different set of letters? Press P to play again, Q to quit.")
    l.close()