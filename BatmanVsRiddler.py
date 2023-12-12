import tkinter as tk
from PIL import ImageTk, Image
import webbrowser


def callback(url):
    webbrowser.open_new_tab(url)


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    # frame1 widgets
    tk.Label(frame1,
             text="Welcome batman to the world of Riddler",
             bg="white",
             fg="green",
             font=("TkMenuFont", 30)
             ).pack()

    image = Image.open("bat.png")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame1, image=logo_img, bg="white", fg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Button(frame1,
              text="Ready?",
              font=("TkHeadingFont", 14),
              bg="#28393a",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame2()
              ).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    # frame2 widgets
    tk.Label(frame2,
             text="Press Enter each time to continue",
             bg="black",
             fg="green",
             font=("TkMenuFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame2, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame2,
              text="Next <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame4()
              ).pack(pady=20)

    tk.Button(frame2,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame1()
              ).pack(pady=20)


def load_frame4():
    clear_widgets(frame2)
    frame4.tkraise()
    # frame2 widgets
    tk.Label(frame4,
             text="The Riddler is planning to take revenge on the Dark Knight",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame4,
             text="on The Dark Knight by killing the hostages he has taken at the church.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame4,
             text="The only way Batman can save the hostages by winning the tricky games of Enigma.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame4, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame4,
              text="Next <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame5()
              ).pack(pady=20)

    tk.Button(frame4,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame2()
              ).pack(pady=20)


def load_frame5():
    clear_widgets(frame4)
    frame5.tkraise()
    # frame2 widgets
    tk.Label(frame5,
             text="As the name suggests 'Riddler', the game is of riddles.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame5,
             text="To save those hostages you to solve 3 of his riddles.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame5,
             text="Each riddle you solve will help batman find a hostage.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame5, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame5,
              text="Next <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame7()
              ).pack(pady=20)

    tk.Button(frame5,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame4()
              ).pack(pady=20)


def load_frame7():
    clear_widgets(frame5)
    frame7.tkraise()
    tk.Label(frame7,
             text="Let's get started!",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame7, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame7,
              text="Ready!",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame8()
              ).pack(pady=20)

    tk.Button(frame7,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame5()
              ).pack(pady=20)


def load_frame8():
    clear_widgets(frame7)
    frame8.tkraise()
    # frame2 widgets
    tk.Label(frame8,
             text="Riddler: To win this fight, riddle me this dark knight",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame8,
             text="What belongs to you, but others will use it?",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame8, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame8,
              text="Clue <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame9()
              ).pack(pady=20)

    tk.Button(frame8,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame7()
              ).pack(pady=20)


def load_frame9():
    clear_widgets(frame8)
    frame9.tkraise()
    # frame2 widgets
    tk.Label(frame9,
             text="Clue: Without it you have no recognition.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame9, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    global name_var
    name_var = tk.StringVar()

    tk.Entry(frame9,
             textvariable=name_var,
             width=30,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack(pady=20)

    tk.Button(frame9,
              text="Enter <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame10()
              ).pack(pady=20)
    tk.Button(frame9,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame8()
              ).pack(pady=20)


def load_frame10():
    clear_widgets(frame9)
    frame10.tkraise()
    global ans
    ans = name_var.get()
    ans.lower()
    if ans == "name":
        tk.Label(frame10,
                 text="Riddler: Congratulations Batman you gave the right answer but that doesn't mean you can get "
                      "lucky to save them all!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack()

        tk.Label(frame10,
                 text="Nice one! Solve just two more riddles to save the hostages",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack()

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame10, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame10,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame11()
                  ).pack(pady=20)

    else:
        tk.Label(frame10,
                 text="Too bad detective that's the wrong answer let's see if you can answer the next one.",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame10, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Label(frame10,
                 text="Don't worry you still have 2 chances to beat riddler and save the day.",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Button(frame10,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame11()
                  ).pack(pady=20)


def load_frame11():
    clear_widgets(frame10)
    frame11.tkraise()
    tk.Label(frame11,
             text="Riddle me this...I am a five-letter word and a fruit.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    frame11.tkraise()
    tk.Label(frame11,
             text="Take out my first letter, and I am a crime,",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame11,
             text="take out my second letter too, and I am an animal.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame11,
             text="Take out only my first and last letters, and I become a kind of music",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame11,
             text="WHAT AM I?",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame11,
             text="It's an easy one you can do it."
                  "No Clue for this one :(",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame11, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    global riddle2
    riddle2 = tk.StringVar()

    tk.Entry(frame11,
             textvariable=riddle2,
             width=30,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack(pady=20)

    tk.Button(frame11,
              text="Enter <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame12()
              ).pack(pady=20)


def load_frame12():
    clear_widgets(frame11)
    frame12.tkraise()
    global ans1
    ans1 = riddle2.get()
    ans1.lower()
    if ans1 == "grape" and ans == "name":
        tk.Label(frame12,
                 text="Riddler: This is just beginner's luck. You can't get away with my riddles so easily!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack()

        tk.Label(frame12,
                 text="Looks like you have to answer just one more riddle correctly detective, but that doesn't mean "
                      "you can!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack()

        tk.Label(frame12,
                 text="Just one more riddle to go!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack()

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame12, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame12,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame13()
                  ).pack(pady=20)

    elif ans1 == "grape" and ans != "name":
        tk.Label(frame12,
                 text="Riddler: This is just beginner's luck. You can't get away with my riddles so easily!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame12,
                 text="That's a blow to riddler's face! Nice one keep going like that!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame12,
                 text="But you have to answer next 2 riddles correctly",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame12, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame12,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame13()
                  ).pack(pady=20)

    elif ans1 != "grape" and ans == "name":
        tk.Label(frame12,
                 text="Riddler: HAHAHA.... Looks like the Dark Knight isn't that smart like I anticipated him to be.",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame12,
                 text="Perhaps, I expected too much from you!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame12,
                 text="You have to answer next 2 riddles correctly",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame12, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame12,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame11()
                  ).pack(pady=20)

    else:
        load_frame13()


def load_frame13():
    clear_widgets(frame12)
    frame13.tkraise()
    tk.Label(frame13,
             text="Riddler: Okay detective, riddle me this...I am always around but unseen.   What am I?",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    tk.Label(frame13,
             text="I am often avoided but never outrun.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame13,
             text="I could find you at the end of the road or even the next corner.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame13,
             text="WHAT AM I?",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()
    tk.Label(frame13,
             text="It's an easy one you can do it.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame13, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(frame13,
              text="Clue <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame14()
              ).pack(pady=20)

    tk.Button(frame13,
              text="Enter <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame15()
              ).pack(pady=20)


def load_frame14():
    clear_widgets(frame13)
    frame14.tkraise()
    tk.Label(frame14,
             text="Clue: It is inevitable and everyone is scared of it but it is an important aspect of life.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame14, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    global riddle3
    riddle3 = tk.StringVar()

    tk.Entry(frame14,
             textvariable=riddle3,
             width=30,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack(pady=20)

    tk.Button(frame14,
              text="Enter <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame15()
              ).pack(pady=20)

    tk.Button(frame14,
              text="Back <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame13()
              ).pack(pady=20)


def load_frame15():
    clear_widgets(frame14)
    frame15.tkraise()
    global ans2
    ans2 = riddle3.get()
    ans2.lower()
    if ans1 == "grape" and ans == "name" and ans2 == "death":
        tk.Label(frame15,
                 text="Riddler: This is just beginner's luck. You can't get away with my riddles so easily!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),
                 ).pack()

        tk.Label(frame15,
                 text="Okay detective you saved all the hostages but if you solve last riddle then I will surrender!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack()

        tk.Label(frame15,
                 text="But I know you can't!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack()

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame15, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame15,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame16()
                  ).pack(pady=20)

    elif ans1 == "grape" and ans != "name" and ans2 == "death":
        tk.Label(frame15,
                 text="Riddler: ARGHH......LAST RIDDLE IS GONNA TO BE YOUR DOOM!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame15,
                 text="That's awesome! You just need to solve the last riddle!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame15, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame15,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame16()
                  ).pack(pady=20)

    elif ans1 == "grape" and ans == "name" and ans2 != "death":
        tk.Label(frame15,
                 text="Riddler: Poor Batman! Those hostages have a lot of faith on you....",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame15,
                 text="Perhaps, They expect too much from you!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame15,
                 text="You have to answer the last riddle correctly!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame15, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame15,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame16()
                  ).pack(pady=20)

    elif ans1 != "grape" and ans == "name" and ans2 == "death":
        tk.Label(frame15,
                 text="Riddler:ARGHH......LAST RIDDLE IS GONNA TO BE YOUR DOOM!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame15,
                 text="That's awesome! You just need to solve the last riddle!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame15, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame15,
                  text="Next Riddle <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=lambda: load_frame16()
                  ).pack(pady=20)

    else:
        load_exit_frame()


def load_frame16():
    clear_widgets(frame15)
    frame16.tkraise()
    tk.Label(frame16,
             text="Riddler: THIS IS YOUR LAST CHANCE DETECTIVE!",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    tk.Label(frame16,
             text="The less of them you have, the more one is worth.",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    tk.Label(frame16,
             text="No Clue for the last riddle Dark Knight",
             bg="black",
             fg="green",
             font=("TkHeadingFont", 15)
             ).pack()

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame16, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    global riddle4
    riddle4 = tk.StringVar()

    tk.Entry(frame16,
             textvariable=riddle4,
             width=30,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack(pady=20)

    tk.Button(frame16,
              text="Enter <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame17()
              ).pack(pady=20)


def load_frame17():
    clear_widgets(frame16)
    frame17.tkraise()
    global ans3
    ans3 = riddle4.get()
    ans3.lower()
    if ans1 == "grape" and ans == "name" and ans2 == "death" and (ans3 in ["friend", "friends"]):

        tk.Label(frame17,
                 text="Riddler: THIS IT NOT POSSIBLE! I CAN'T BELIEVE I LOST!!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame17,
                 text="I'LL COME BACK STRONGER NEXT TIME YOU WON'T BE ABLE TO DO ANYTHING!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="Congrats on winning the game successfully. \n You even caught the Riddler. \n GCPD is on it's"
                      "to capture Riddler \n Gotham is saved again! :)",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="CLICK THE LINK TO KNOW MORE!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        link = tk.Label(frame17, text="<?>", font=('Helveticabold', 30), fg="green", bg="black", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e:
        callback("https://www.rataalada.com"))

        tk.Button(frame17,
                  text="Exit <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=root.quit
                  ).pack(pady=20)

    elif ans1 == "grape" and ans != "name" and ans2 == "death" and (ans3 in ["friend", "friends"]):

        tk.Label(frame17,
                 text="YOU MAY HAVE SAVED THE HOSTAGES BATMAN BUT YOU'LL NEVER BE ABLE TO CATCH ME!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame17,
                 text="I'LL COME BACK STRONGER NEXT TIME YOU WON'T BE ABLE TO DO ANYTHING!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="Congrats on winning the game successfully! Hope you liked the game \n :)",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame17, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame17,
                  text="Exit <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=root.quit
                  ).pack(pady=20)

    elif ans1 == "grape" and ans == "name" and ans2 != "death" and (ans3 in ["friend", "friends"]):

        tk.Label(frame17,
                 text="YOU MAY HAVE SAVED THE HOSTAGES BATMAN BUT YOU'LL NEVER BE ABLE TO CATCH ME!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame17,
                 text="I'LL COME BACK STRONGER NEXT TIME YOU WON'T BE ABLE TO DO ANYTHING!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="Congrats on winning the game successfully! Hope you liked the game \n :)",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame17, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame17,
                  text="Exit <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=root.quit
                  ).pack(pady=20)

    elif ans1 != "grape" and ans == "name" and ans2 == "death" and (ans3 in ["friend", "friends"]):

        tk.Label(frame17,
                 text="THIS IT NOT POSSIBLE! I CAN'T BELIEVE I LOST!!!!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame17,
                 text="I'LL COME BACK STRONGER NEXT TIME YOU WON'T BE ABLE TO DO ANYTHING!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="Congrats on winning the game successfully. \n You even caught Riddler. Hope you liked the game "
                      "\n :)",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame17, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame17,
                  text="Exit <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=root.quit
                  ).pack(pady=20)

    elif ans1 == "grape" and ans == "name" and ans2 == "death" and (ans3 not in ["friend", "friends"]):
        tk.Label(frame17,
                 text="Riddler:Uh-oh! I'm afraid that's the wrong answer Dark knight",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15),

                 ).pack(pady=20)

        tk.Label(frame17,
                 text="You may have saved the hostages but you couldn't catch me!\n Next time I'll come back stronger!",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        tk.Label(frame17,
                 text="Congrats on winning the game successfully! Hope you liked the game \n :)",
                 bg="black",
                 fg="green",
                 font=("TkHeadingFont", 15)
                 ).pack(pady=20)

        image = Image.open("batman.jpg")
        logo_img = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame17, image=logo_img, bg="black", width=250, height=100)
        logo_widget.image = logo_img
        logo_widget.pack(pady=20)

        tk.Button(frame17,
                  text="Exit <?>",
                  font=("TkHeadingFont", 14),
                  bg="black",
                  fg="white",
                  cursor="hand2",
                  activebackground="#badee2",
                  activeforeground="black",
                  command=root.quit
                  ).pack(pady=20)

    else:
        load_exit_frame()


def load_exit_frame():
    clear_widgets(frame)
    frame.tkraise(exit_frame)
    tk.Label(exit_frame,
             text="Riddler: Jokes on you Batman! You couldn't even solve these easy riddles!",
             font=("TkHeadingFont", 14),
             bg="black",
             fg="white",
             ).pack(pady=20)

    tk.Label(exit_frame,
             text="City's hero! What a joke!",
             font=("TkHeadingFont", 14),
             bg="black",
             fg="white",
             ).pack(pady=20)

    tk.Label(exit_frame,
             text="Sorry you lost the game!",
             font=("TkHeadingFont", 14),
             bg="black",
             fg="white",
             ).pack(pady=20)

    image = Image.open("batman.jpg")
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(exit_frame, image=logo_img, bg="black", width=250, height=100)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Button(exit_frame,
              text="Try Again <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame1()
              ).pack(pady=20)

    tk.Button(exit_frame,
              text="Exit <?>",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=root.quit
              ).pack(pady=20)


root = tk.Tk()
root.title("Batman Vs Riddler")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=1280, height=720, bg="white")
frame2 = tk.Frame(root, bg="black")
frame4 = tk.Frame(root, bg="black")
frame5 = tk.Frame(root, bg="black")
frame7 = tk.Frame(root, bg="black")
frame8 = tk.Frame(root, bg="black")
frame9 = tk.Frame(root, bg="black")
frame10 = tk.Frame(root, bg="black")
frame11 = tk.Frame(root, bg="black")
frame12 = tk.Frame(root, bg="black")
frame13 = tk.Frame(root, bg="black")
frame14 = tk.Frame(root, bg="black")
frame15 = tk.Frame(root, bg="black")
frame16 = tk.Frame(root, bg="black")
frame17 = tk.Frame(root, bg="black")
exit_frame = tk.Frame(root, bg="black")

for frame in (frame1, frame2, frame4, frame5, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14,
              frame15, frame16, frame17, exit_frame):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()

root.mainloop()
