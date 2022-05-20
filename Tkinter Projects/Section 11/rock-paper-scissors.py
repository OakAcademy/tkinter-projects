from tkinter import *
import tkinter.font as font
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("750x350")
window.resizable(0, 0)

appFont = font.Font(size=14)

gameTitle = Label(window, text="Rock Paper Scissors", font=appFont, fg="gray")
gameTitle.pack()

winnerLabel = Label(window, text="Let's Start the Game", font= appFont, pady=8)
winnerLabel.pack()

frame = Frame(window)
frame.pack()

playerScore = 0
computerScore = 0
options = [("Rock",0),("Paper", 1),("Scissors", 0)]

def getComputerChoice():
    return random.choice(options)

def playerChoice(playerInput):
    global playerScore, computerScore

    computerInput = getComputerChoice()

    playerChoiceLabel.config(text = "Your Choice: " + playerInput[0])
    computerChoiceLabel.config(text= "Computer Choice: " + computerInput[0])

    if playerInput == computerInput:
        winnerLabel.config(text="Tie")
    elif (playerInput[1] - computerInput[1])%3 == 1:
        playerScore +=1
        winnerLabel.config(text="You Win")
        playerScoreLabel.config(text="Your Score: " + str(playerScore))
    else:
        computerScore +=1
        winnerLabel.config(text="Computer Win")
        computerScoreLabel.config(text="Computer Score: " + str(computerScore))



playerOption = Label(frame, text="Your Options", font=appFont, fg="gray")
playerOption.grid(row=0, column=0, pady=8)

rockButton = Button(frame, text="Rock", width=15, bd=0, bg="pink", command=lambda: playerChoice(options[0]))
rockButton.grid(row=0, column=1, padx=8, pady=5)

paperButton = Button(frame, text="Paper", width=15, bd=0, bg="pink", command=lambda: playerChoice(options[1]))
paperButton.grid(row=0, column=2, padx=8, pady=5)

scissorsButton = Button(frame, text="Scissors", width=15, bd=0, bg="pink", command=lambda: playerChoice(options[2]))
scissorsButton.grid(row=0, column=3, padx=8, pady=5)

scoreLabel = Label(frame, text="Score: ", font=appFont, fg="gray")
scoreLabel.grid(row=2, column=0)

playerChoiceLabel = Label(frame, text="Your Choice: - ", font=appFont)
playerChoiceLabel.grid(row=3, column=1, pady=5)

playerScoreLabel = Label(frame, text="Your Score: - ", font=appFont)
playerScoreLabel.grid(row=3, column=2, pady=5)

computerChoiceLabel = Label(frame, text="Computer Choice: - ", font=appFont)
computerChoiceLabel.grid(row=4, column=1, pady=5)

computerScoreLabel = Label(frame, text="Computer Score: - ", font=appFont)
computerScoreLabel.grid(row=4, column=2, pady=5)



window.mainloop()