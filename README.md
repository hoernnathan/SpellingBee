# SpellingBee
This is a text-based version of the New York Times Spelling Bee game written in Python.

The New York Times version can be played here: https://www.nytimes.com/puzzles/spelling-bee

A disadvantage of the NYT version is that you can only play one game per day. This text-based version allows you to play as many games as you want in a session. Additionally, it will show the total number of points and words for a given puzzle, so it is easier for users to know how close they are to getting all the words accepted in the puzzle. 

The acceptable word list here does not match up with the word list in the NYT version. This one will be updated over time to try to match the NYT one as best as possible. You can also replace the filename "wordlist.txt" with your own word list file if you have a file with more words. Currently, the puzzle list includes a large archive of NYT puzzles from past years, called "archive.txt". You can replace the filename variable in the main function with a different filename, such as the "puzzlelist.txt" file which includes additional puzzles. This file will be updated periodically to include more puzzles to play. This will allow users to try many more letter combinations in order to improve their performance on the actual game, should these letter combinations come up again. You also have the ability to play puzzles with a random set of letters, so you'll never get bored!

Rules of the game:
  - Create words by using the letters around the letter board (the hive)
  - Words must be at least 4 letters long, and every word must contain the center letter
  - You can reuse letters as much as you want in a word
  - For words of length 4, you earn 1 point. For words of greater length, you earn 1 point per letter
  - Every puzzle has at least 1 pangram word, which contains all the letters around the hive at least once. These are worth 7 extra points!
  - As you obtain more words, you will move up in the rankings starting from BEGINNER all the way to GENIUS. The total number of points needed to reach each ranking is a percentage of how many points are in the puzzle.
  
When prompted to enter a word, you can also type one of the following commands:
  - B to view the letter board
  - S to shuffle the letter board
  - P to view your number of words and points, the total number of words and points, and the number of points to reach each ranking
  - W to view the words you have obtained
  - Q to quit a puzzle
  - H to bring up the help menu
