import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('750x750+0+0')
root.title("Rock Paper Scissor")
root.resizable(False, False)
root.configure(bg="#d2f0e6")


def play():
    rock_btn.configure(state=NORMAL)
    paper_btn.configure(state=NORMAL)
    sicssors_btn.configure(state=NORMAL)
    prompt_lbl.configure(text="Make your choice!")


def replay():
    rock_btn.configure(state=DISABLED)
    sicssors_btn.configure(state=DISABLED)
    paper_btn.configure(state=DISABLED)
    result.set("")
    prompt_lbl.configure(text="Click on Play Button")


def onclick(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result_text.set("Computer chose: " + computer_choice)

    player_image_label.configure(image=choice_images1[player_choice])
    computer_image_label.configure(image=choice_images2[computer_choice])

    if player_choice == computer_choice:
        result.set("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        result.set("You win!")
    else:
        result.set("Computer wins!")
    replay_btn = Button(font=('arial', 18, 'bold'), text='Replay', bd=3, width=6, bg='white', fg="red", command=replay)
    replay_btn.place(x=330, y=680)


# Load choice images
choice_images1 = {
    "Rock": ImageTk.PhotoImage(Image.open("rock_right.jpg")),
    "Paper": ImageTk.PhotoImage(Image.open("paper_right.jpg")),
    "Scissors": ImageTk.PhotoImage(Image.open("scissors_right.jpg"))
}
choice_images2 = {
    "Rock": ImageTk.PhotoImage(Image.open("rock_right.jpg")),
    "Paper": ImageTk.PhotoImage(Image.open("paper_left.jpg")),
    "Scissors": ImageTk.PhotoImage(Image.open("scissors_left .jpg"))
}

Welcome_lbl = Label(root, font=('arial', 28, 'bold'), text='Welcome!\nto', bg="#d2f0e6", width=18, justify='center')
Welcome_lbl.place(x=160, y=40)

Game_lbl = Label(root, font=('arial', 28, 'bold'), text='Rock, Paper, Scissors Game', bg="#d2f0e6", width=22, justify='center')
Game_lbl.place(x=130, y=140)

play_btn = Button(font=('arial', 18, 'bold'), text='Play', bd=3, width=6, bg='white', fg="blue", command=play)
play_btn.place(x=330, y=190)

rock_img = ImageTk.PhotoImage(Image.open("rock_right.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("paper_left.jpg"))
sicssors_img = ImageTk.PhotoImage(Image.open("scissors_left .jpg"))


rock_btn = Button(image=rock_img, width=150, height=130, bg="#d2f0e6", command=lambda: onclick("Rock"), state=DISABLED)
rock_btn.place(x=130, y=250)
paper_btn = Button(image=paper_img, width=150, height=130, bg="#d2f0e6", command=lambda: onclick("Paper"), state=DISABLED)
paper_btn.place(x=310, y=250)
sicssors_btn = Button(image=sicssors_img, width=150, height=130, bg="#d2f0e6", command=lambda: onclick("Scissors"), state=DISABLED)
sicssors_btn.place(x=490, y=250)

prompt_lbl = Label(font=("arial", 18, 'bold'), width=40, text="click on Play Button!", bg="#d2f0e6", justify='center', state=NORMAL)
prompt_lbl.place(x=80, y=400)

player_image_label = Label(root, width=150, height=150, bg="#d2f0e6")
player_image_label.place(x=150, y=450)

computer_image_label = Label(root, width=150, height=150, bg="#d2f0e6")
computer_image_label.place(x=450, y=450)

result_text = StringVar()
result_label = Label(root, textvariable=result_text,font=("arial", 18, 'bold'), bg="#d2f0e6", width=40, text="click on Play Button!", justify='center', state=NORMAL)
result_label.place(x=80, y=610)

result = StringVar()
result_label = Label(root, textvariable=result,font=("arial", 18, 'bold'), width=40, bg="#d2f0e6", text="click on Play Button!", justify='center', state=NORMAL)
result_label.place(x=80, y=650)


root.mainloop()