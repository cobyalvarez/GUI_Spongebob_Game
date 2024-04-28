import tkinter as tk
window=tk.Tk()
window.geometry("600x600")
window.title("CS Group Project- Game")

def exit_program():
    exit()
#---------------------------------------------this is the start of it (go to the chum bucket)
def o_window_two():
    def window_three():
        window_three=tk.Tk()
        window_three.geometry("600x600")
        window_two.withdraw()
        label1b=tk.Label(window_three, text="You have fallen into Planktons trap")
        label1b.pack()
        label2b=tk.Button(window_three, text="You fail",command=exit_program)
        label2b.pack()
        def exit_program():
            exit()
        def close_three():
            window_three.destroy()
            window_two.deiconify()
            #addind widgets to top one
        window_three.mainloop()
#-------------------------------------------------below is for window 4
    def window_four():
        window_four=tk.Tk()
        window_four.geometry("600x600")
        #adding widgets to top one (retrace squidwards smell)
        label1a=tk.Label(window_four, text="You spot Sandy and Patrick on a hill. You ask if they have seen Squidward.")
        label1a.pack()
        label1b=tk.Label(window_four, text="They say he is down the hill as they watch him fight Bubble Bass, a minion of Plankton.")
        label1b.pack()
        button1a=tk.Button(window_four, text="Rush over to help Squidward", command=window_five)
        button1a.pack()
        button1b=tk.Button(window_four, text="Stay with Sandy and Patrick and eat ice cream.", command=altwindow_five)
        button1b.pack()

        def exit_program():
            exit()
        def close_four():
            window_four.destroy()
            window_two.deiconify()
        window_four.mainloop()
#__________________________________________________ stay with patrick and sandy
    def altwindow_five():
        altwindow_five=tk.Tk()
        altwindow_five.geometry("600x600")
        label2c=tk.Label(altwindow_five, text="You failed to get the secret formula. Squidward gets beaten up.")
        label2c.pack()
        button2c=tk.Button(altwindow_five, text="Bad End", command=exit_program)
        button2c.pack()
#_______________________________________________________rush over to help squidward
    def window_five():
        window_five=tk.Tk()
        window_five.geometry("600x600")
        label2a=tk.Label(window_five, text="You've found Squidward injured, but he has successfully recovered the secret formula.")
        label2a.pack()
        label2b=tk.Label(window_five, text="Squidward goes unconscious while Bubble Bass mocks you.")
        label2b.pack()
        button2a=tk.Button(window_five, text="Punch him and protect Squidward", command=window_six)
        button2a.pack()
        button2b=tk.Button(window_five, text="Take Squidward and flee", command=altwindow_six)
        button2b.pack()
#__________________________________________________________take squidward and flee
    def altwindow_six():
        altwindow_six=tk.Tk()
        altwindow_six.geometry("600x600")
        label3a=tk.Label(altwindow_six, text="Bubble Bass catches up to you and beats you up.")
        label3a.pack()
        button3a=tk.Button(altwindow_six, text="Bad end", command=exit_program)
        button3a.pack()
#__________________________________________________________punch him and protect squidward
    def window_six():
        window_six=tk.Tk()
        window_six.geometry("600x600")
        label4a=tk.Label(window_six,text="He blocks it and is too strong")
        label4a.pack()
        button4a=tk.Button(window_six,text="take Squidward and Flee",command=window_seven)
        button4a.pack()
        button4b=tk.Button(window_six,text="call Sandy and Patrick for back up",command=window_eight)
        button4b.pack()
        button4c=tk.Button(window_six,text="inject yourself with the secret formula and fight",command=window_nine)
        button4c.pack()
#_______________________________________________________take Squidward and flee
    def window_seven():
        window_seven=tk.Tk()
        window_seven.geometry("600x600")
        label5a=tk.Label(window_seven,text="Mr.Krabs is ashamed in you the Krusty Krab is ruined")
        label5a.pack()
        button5a=tk.Button(window_seven,text="Terrible Ending",command=exit_program)
        button5a.pack()
#_________________________________________________________call sandy and patrick for back up
    def window_eight():
        window_eight=tk.Tk()
        window_eight.geometry("600x600")
        label6a=tk.Label(window_eight,text="As they arrive to back you up Plankton and Karen also arrive its a 3v3")
        label6a.pack()
        button6a=tk.Button(window_eight,text="Call in Mr.Krabs to help deal with them all",command=window_ten)
        button6a.pack()
        button6b=tk.Button(window_eight,text="Use Karate to put a stop to them",command=window_ten)
        button6b.pack()
#__________________________________________________________Inject yourself with the secret formula
    def window_nine():
        window_nine=tk.Tk()
        window_nine.geometry("600x600")
        label7a=tk.Label(window_nine,text="You one punched Planktons minion but soon as you think its over ")
        label7a.pack()
        label7b=tk.Label(window_nine,text="Plankton arrives and inject him with chum as you are now evenly matched")
        label7b.pack()
        button7a=tk.Button(window_nine,text="Give it your all and attack with a full powered bikini bottom smash",command=window_eleven)
        button7a.pack()
        button7b=tk.Button(window_nine,text="Inject squidward with the formula",command=window_twelve)
        button7b.pack()
#___________________________________________________________you defeated bubble bass
    def window_ten():
        window_ten=tk.Tk()
        window_ten.geometry("600x600")
        label8a=tk.Label(window_ten,text="You've defeated Bubble Bass,and Squidward wakes up.")
        label8a.pack()
        label8b=tk.Label(window_ten,text="Peace has returned.. for now.")
        label8b.pack()
#___________________________________________________________attack knocked him out
    def window_eleven():
        window_eleven=tk.Tk()
        window_eleven.geometry("600x600")
        label9a=tk.Label(window_eleven,text="Your attack knocked him out but you have fallen as well.")
        label9a.pack()
        label9b=tk.Label(window_eleven,text="As you wake up in a hospital with everyone thanking you for saving the day")
        label9b.pack()
#____________________________________________________________SQUIDWARD COMBO ATTACK
    def window_twelve():
        window_twelve=tk.Tk()
        window_twelve.geometry("600x600")
        label10a=tk.Label(window_twelve,text="Squidward awakens and you both combine your attack to overwhelm the enemy")
        label10a.pack()
        label10b=tk.Label(window_twelve,text="Plankton has been stopped and you and Squidward return")
        label10b.pack()
        label10c=tk.Label(window_twelve,text="the formula to the Krusty Krab and peace has returned for now.")
        label10c.pack()
#====================================================This bellow is what opens after you press start 
    window_two=tk.Tk()
    window.geometry("600x600")
    window.withdraw()

    lbl=tk.Label(window_two,text="What will you do?")
    lbl.pack()
    
    Button.L=tk.Button(window_two,fg="red",text="retrace Squidwards smell to find him",command=window_four)
    Button.L.pack()
    
    Button.R=tk.Button(window_two,fg="blue",text="Go to the chum Bucket",command=window_three)
    Button.R.pack()
    
    window_two.mainloop()
#introduction----------------------------------- this is the first one that oepns
Label_1=tk.Label(window,text="The krabby Patty secret formula has just been stolen by Plankton.")
Label_2=tk.Label(window,text="Mr.Krabs has just ordered you to go on a mission to retrieve it.")
Label_3=tk.Label(window,text="He tells you he has already sent squidward ahead of time to try to get it.")
Label_4=tk.Label(window,text="As you are furious squidward might get hurt")
Label_1.pack()
Label_2.pack()
Label_3.pack()
Label_4.pack()
Button=tk.Button(window,text="Start",command=o_window_two)
Button.pack()
Button2=tk.Button(window,text="Exit",command=exit_program)
Button2.pack()
#----------------------------------------------
window.mainloop()
