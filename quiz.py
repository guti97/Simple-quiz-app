############################################
#tbd: - in db speichern daten wie punkte
#     (1)- Erläuterung zu den Fragen -> DONE
#     - Bieptöne bei letzten 5s
#     - Bieptöne bei falscher/korrekter Antwort -> DONE
#     (1)- Fragenkatalog erweitern
#     - Lustige Bilder einfügen
#     - Highscore Liste  -> in Progress
#     - Timer für die gesamte Quizzeit
#     - Punktevergabe für schnelle Antworten
#     - Ändern des Hintergrundbildes
#     - Je nach Punktzahl ein anderes Bild anzeigen
#     - Ausführbare Datei erstellen -> DONE
#     - doppelte Benutzernamen verhindern 
############################################

import tkinter as tk
from tkinter import *
from tkinter import font
import random
import sqlite3 
import time
from PIL import Image, ImageTk
from tkinter import messagebox
import winsound


def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    
    user_name = StringVar()
    password = StringVar()



    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()-70



    #sup_frame = Frame(sup_canvas)
    #sup_frame.pack()
    #sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    login_canvas = Canvas(login,width=screen_width,height=screen_height,bg='white')
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="red")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Royal Quiz App Login",fg="white",bg="red")
    heading.config(font=('Helvetica 40'), anchor=CENTER)
    heading.place(relx=0.2,rely=0.1)
    

    #USER NAME
    ulabel = Label(login_frame,text="Benutzername",fg='white',bg='black')
    ulabel.place(relx=0.05,rely=0.3)
    ulabel.config(width=13,font=('Helvetica 25'))
    uname = Entry(login_frame,bg='light grey',fg='black',textvariable = user_name)
    uname.config(width=21, font=('Helvetica 25'))
    uname.place(relx=0.31,rely=0.3)

    #PASSWORD
    plabel = Label(login_frame,text="Passwort",fg='white',bg='black')
    plabel.place(relx=0.1,rely=0.5)
    plabel.config(width=10,font=('Helvetica 25'))
    pas = Entry(login_frame,bg='light grey',fg='black',textvariable = password,show="*")
    pas.config(width=21, font=('Helvetica 25'))
    pas.place(relx=0.31,rely=0.5)

    def check():
        for b,c in logdata:
            if b == uname.get() and c == pas.get():
                #print(logdata)
                
                menu(b)
                break
        else:
            error = Label(login_frame,text="Falscher Benutzername oder falsches Passwort!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.8)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    global user
    sup = Tk()
    sup.title('Royal Quiz App')
    
    uname = StringVar()
    passW = StringVar()
    
    screen_width = sup.winfo_screenwidth()
    screen_height = sup.winfo_screenheight()-70

    sup_canvas = Canvas(sup,width=screen_width,height=screen_height,bg="#27408b")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas)
    sup_frame.pack()
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./files/Flag_UK.png").resize((int(screen_width*0.8), int(screen_height*0.8))))

    # Create a label widget to display the image 
    label = Label(sup_frame, image=img)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    heading = Label(sup_frame,text="Royal Quiz App",fg='white',bg='black')
    heading.config(font=('Helvetica 40'))
    heading.place(relx=0.5, rely=0.1, anchor='center')

    #username
    ulabel = Label(sup_frame,text="Benutzername",fg='white',bg='black')
    ulabel.place(relx=0.05,rely=0.3)
    ulabel.config(width=13,font=('Helvetica 25'))
    user = Entry(sup_frame,bg='light grey',fg='black',textvariable = uname)
    user.config(width=21, font=('Helvetica 25'))
    user.place(relx=0.31,rely=0.3)
    
    
    #password
    plabel = Label(sup_frame,text="Passwort",fg='white',bg='black')
    plabel.place(relx=0.1,rely=0.5)
    plabel.config(width=10,font=('Helvetica 25'))
    pas = Entry(sup_frame,bg='light grey',fg='black',textvariable = passW,show="*")
    pas.config(width=21, font=('Helvetica 25'))
    pas.place(relx=0.31,rely=0.5)
    
    
    
  

    def addUserToDataBase():
        
        username = user.get()
        password = pas.get()
        #score = 1
        #score = score.get()
        #score = score.get() #tbd: add score to db
        
        if  len(user.get())==0 and len(pas.get())==0 :
            error = Label(text="Sie haben kein Feld ausgefüllt...Bitte geben Sie in allen Felder etwas an",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif  len(user.get())==0 or len(pas.get())==0:
            error = Label(text="Bitte alle Felder ausfüllen",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Benutzername und Passwort dürfen nicht leer sein",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Der Benutzername darf nicht leer sein",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Das Passwort darf nicht leer sein",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp( USERNAME text,PASSWORD text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?)",(username,password)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            #print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)

    from tkinter import Scrollbar, Y
    
    #def showHighscoreList():
    #    conn = sqlite3.connect('quiz.db')
    #    create = conn.cursor()
    #    conn.commit()
    #    create.execute('SELECT * FROM userSignUp')
    #    z=create.fetchall()
    #    print(len(z))
    #    print(z)
    #    highscore = Tk()
    #    highscore.title('Highscore List')
    #    highscore.geometry('400x400')
    #    highscore_canvas = Canvas(highscore)
    #    highscore_canvas.pack(side="left", fill="both", expand=True)
    #    scrollbar = Scrollbar(highscore, command=highscore_canvas.yview)
    #    scrollbar.pack(side="right", fill="y")
    #    highscore_canvas.configure(yscrollcommand=scrollbar.set)
    #    highscore_frame = Frame(highscore_canvas)
    #    highscore_frame.bind(
    #        "<Configure>",
    #        lambda e: highscore_canvas.configure(
    #            scrollregion=highscore_canvas.bbox("all")
    #        )
    #    )
    #    highscore_canvas.create_window((0, 0), window=highscore_frame, anchor="nw")
    #    for i in range(len(z)):
    #        Label(highscore_frame,text="Username: "+z[i][0]+"\nScore: "+str(z[i][2]),font="Helvetica 15").pack()  #tbd:add highscore
    #    highscore.mainloop()

    
    #signup BUTTON
    sp = Button(sup_frame,text='Registrieren',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.3,rely=0.8)

    #highscore_button = Button(sup_frame, text="Highscore List", padx=5,pady=5,width=5, command=showHighscoreList, bg="black", fg="white")
    #highscore_button.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)    
    #highscore_button.place(relx=0.5,rely=0.8)

    log = Button(sup_frame,text='Sie haben bereits ein Konto?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 20,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)



    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Royal Quiz App Menu')
    
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()-70
    
    menu_canvas = Canvas(menu,width=screen_width,height=screen_height,bg="red")
    menu_canvas.pack()

        
    img = ImageTk.PhotoImage(Image.open("./files/funny_queen.jpg").resize((int(screen_width/2), int(screen_height/2.0))))
    menu_canvas.create_image(screen_width/2, screen_height/2, image=img)


    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.pack()
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    # Create an object of tkinter ImageTk
    img1 = ImageTk.PhotoImage(Image.open("./files/funny_queen.jpg").resize((int(screen_width*0.3), int(screen_height*0.4))))
    img2 = Image.open("./files/funny_king.jpg")
    # img2 = img2.rotate(-90, expand=True)
    img2 = img2.resize((int(screen_width*0.2), int(screen_height*0.55)))
    img2 = ImageTk.PhotoImage(img2)
  

    # Create a label widget to display the image 
    label1 = Label(menu_frame, image=img1, bg= "white")
    label1.place(relx=-0.20, rely=0, relwidth=1, relheight=1)

    label2 = Label(menu_frame, image=img2, bg= "white")
    label2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  T H E  R O Y A L  F A M I L Y  Q U I Z ',fg="black",bg="red") 
    wel.config(font=('Century 30'))
    wel.place(relx=0,rely=0.02)
    
    abcdefgh='Willkommen '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="black",font="Helvetica 40",fg="white")
    level34.place(relx=0.17,rely=0.1)






    def navigate():
        

        menu.destroy()
        quiz()
    
    letsgo = Button(menu_frame,text="Los gehts",bg="black",fg="white",font="Helvetica 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()

counter = 0

def my_counter():   
        global counter
        counter += 1
        if counter > 30:
            counter = 1
        return counter

def quiz():
    global counter
    global e
    global score
    global quizQ
    global randnr
    score = 0
    global explanation_window
    explanation_window = None

    e = Tk()
    e.title('Royal Quiz App ')

    screen_height = e.winfo_screenheight()-70
    screen_width = e.winfo_screenwidth()
    
    quiz_canvas = Canvas(e,width=screen_width,height=screen_height,bg="red")
    quiz_canvas.pack()

    quiz_frame = Frame(quiz_canvas,bg="white")
    quiz_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    def showExplanation(index):
        global e
        global explanation_window
        explanation_window = Tk()

        screen_height = e.winfo_screenheight()
        screen_width = e.winfo_screenwidth()

        window_height = 150
        y_coordinate = screen_height - window_height - 90

        explanation_window.geometry(f'400x{window_height}+0+{y_coordinate}')
        explanation_window.title('Erklärung')

        customFont = font.Font(family="Helvetica", size=15)
        explanation_label = Label(explanation_window, text=explanation[index], font=customFont, wraplength=380, justify=LEFT)
        explanation_label.pack()


    def next_and_close():
        global explanation_window
        if explanation_window is not None:
            explanation_window.destroy()
            explanation_window = None
        display()

    
    def countDown():
        check = 0
        for k in range(40, 0, -1):
            if k <= 6:
                winsound.Beep(1000, 100)  # Beep sound
                if k == 1:
                    check=-1
            timer.configure(text=k)
            quiz_frame.update()
            time.sleep(1)

        
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    
    # Fünf Fragen, Antworten und Erläuterungen
    quizQ = [
                [
                     "Wer war der/die erste Monarch/in, der/die eine Radio-Weihnachtsansprache hielt?",
                     "König George VI\t",
                     "Königin Victoria",
                     "Königin Elizabeth II\t",
                     "König Edward VII\t" 
                ],
                [
                     "Wie viele Räume hat der Buckingham Palace?" ,
                    "500",
                    "775",
                    "1000",
                    "1200"
                     
                ],
                [
                    "Wie viele Premierminister des Vereinigten Königreichs hat Königin Elizabeth II. erlebt?" ,
                    "8",
                    "17",
                    "14",
                    "25"
                ],
                [
                    "Welche königliche Tochter nahm als erste an den Olympischen Spielen teil?" ,
                    "Prinzessin Anne",
                    "Prinzessin Beatrice\t",
                    "Prinzessin Eugenie",
                    "Prinzessin Charlotte"
                ],
                [
                    "Welches ist der offizielle Geheimdienst der königlichen Familie?" ,
                    "MI5",
                    "MI6",
                    "Special Branch",
                    "CIA"
                ],
                [
                    "Welche königliche Hochzeit wurde als erste im Fernsehen übertragen?" ,
                    "Prinz William und Kate Middleton",
                    "Prinz Charles und Prinzessin Diana",
                    "Prinzessin Margaret und Anthony Armstrong-Jones",
                    "Prinzessin Elizabeth und Philip Mountbatton"
                ],
                [
                    "Wer war der/die am längsten regierende Monarch/in im Vereinigten Königreich vor Königin Elizabeth II.?" ,
                    "Georg III\t",
                    "Georg II\t",
                    "Viktoria",
                    "Wilhelm IV\t"
                ],
                [
                    "Wie viele Wohltätigkeitsorganisationen unterstützte Königin Elizabeth II. als Schirmherrin?" ,
                    "200",
                    "400",
                    "600",
                    "800"
                ],
                [
                    "Welches Mitglied der britischen Royalfamilie ließ sich einst von einem Parfümberater beraten, \n ob seine natürlichen Körperausdünstungen angenehm rochen?" ,
                    "Queen Elizabeth II",
                    "Prinz Charles",
                    "Prinzessin Diana",
                    "Prinz Philip"
                ],
                [
                    "Welcher Größe entspricht die durchschnittliche Schuhgröße von Queen Elizabeth II?" ,
                    "34",
                    "38",
                    "42",
                    "40",
                ],
                [
                    "Welches Mitglied der Royals besitzt eine Sammlung von über 100 ungewöhnlichen Hüten?" ,
                    "Queen Elizabeth II",
                    "Prinzessin Beatrice",
                    "Prinz Andrew",
                    "Prinzessin Anne\t"
                ],
                [
                    "Welches Familienmitglied der Royals hat einen schwarzen Gürtel in Karate?" ,
                    "Prinz Andrew",
                    "Prinz William",
                    "Prinz Edward",
                    "König George V"
                ],
                [
                    "Welche royale Dame ist die erste Frau in der Geschichte der britischen Monarchie,\n die an einer öffentlichen Universität einen Abschluss erworben hat?" ,
                    "Herzogin Meghan\t",
                    "Prinzessin Eugenie",
                    "Herzogin Kate",
                    "Prinzessin Beatrice\t"
                ],
                [
                    "Welches Mitglied der britischen Royals war als Kind professionell als Schauspielerin tätig und spielte in mehreren Filmen mit?" ,
                    "Prinzessin Beatrice",
                    "Prinzessin Eugenie",
                    "Herzogin Kate\t",
                    "Prinzessin Anne\t"
                ],
                [
                    "Welches Mitglied der königlichen Familie ist bekannt für seine ungewöhnliche Vorliebe für Selfies\n und hat bereits mehrere Selfie-Flashmobs organisiert?" ,
                    "Prinz William\t",
                    "Prinz Harry",
                    "Herzogin Meghan\t",
                    "Herzogin Kate\t"
                ],
                [
                    "Welcher royalen Dame wurde nach ihrer Hochzeit der offizielle Titel '"'Herzogin von Essex'"' verliehen?" ,
                    "Herzogin Camilla",
                    "Herzogin Meghan\t",
                    "Herzogin Kate\t",
                    "Prinzessin Eugenie\t"
                ],
                [
                    "Welches royale Familienmitglied publizierte eine eigene Reihe von Kinderbüchern unter einem Pseudonym?" ,
                    "Prinzessin Beatrice",
                    "Herzogin Kate\t",
                    "Prinzessin Eugenie",
                    "Herzogin Meghan"
                ],
                [
                    "Wie hießen Hunde von Queen Elizabeth?" ,
                    "Rex und Fido",
                    "Charlie und Buddy",
                    "Lupo und Tilly",
                    "Willow und Holly"
                ],
                [
                    "Welches Tier besitzt der/die König/in offiziell im Namen des britischen Königshauses?" ,
                    "Tauben",
                    "Schwäne",
                    "Rehe",
                    "Füchse"
                ],
                [
                    "Wie viele Hunde (Corgis) hatte die Königin Elizabeth II. im Laufe ihres Lebens?" ,
                    "15",
                    "22",
                    "30",
                    "14"
                ],
                [
                    "Was ist eine der ungewöhnlichsten Einnahmequellen des britischen Königshauses?" ,
                    "Verkauf von königlichem Honig",
                    "Vermietung von königlichen Juwelen",
                    "Gebühren für das Nutzen von Kronen-Marken",
                    "Tourismus-Einnahmen durch den Besuch von königlichen Gärten"
                ],
                [
                    "Welches Kleidungsstück wurde nach einem Mitglied des britischen Königshauses benannt?" ,
                    "Der Kilt",
                    "Der Bolero",
                    "Der Blazer",
                    "Die Wellington-Stiefel"
                ],
                [
                    "Welcher britische Monarch führte die Tradition der Weihnachtsansprache im Radio ein?" ,
                    "König George IV",
                    "Königin Victoria",
                    "König Edward VIII",
                    "König George V"
                ],
                [
                    "Welches britische Königshaus ist bekannt für seine königliche Brauerei und stellt eigenes Bier her?" ,
                    "Balmoral Castle",
                    "Sandringham House",
                    "Windsor Castle\t",
                    "Buckingham Palace\t"
                ],
                [
                    "Welches Gericht wurde nach einem Mitglied des britischen Königshauses benannt?" ,
                    "Der Edwardian Pie",
                    "Der Victoria Sponge Cake",
                    "Der George Pudding",
                    "Der Windsor Roast"
                ],
                [
                    "Welches britische Königshaus ist bekannt für seine umfangreiche Uhren- und Uhrensammlung?" ,
                    "Windsor Castle",
                    "Buckingham Palace\t",
                    "Balmoral Castle",
                    "Clarence House"
                ],
                [
                    "Welche königliche Residenz ist bekannt für ihren Rosengarten, der über 2.000 Rosensträucher beherbergt?" ,
                    "Balmoral Castle",
                    "Windsor Castle\t",
                    "Sandringham House\t",
                    "Buckingham Palace"
                ],
                [
                    "Welches königliche Gericht besteht aus gerösteten Schweinefleischscheiben mit einer Schicht Apfelmus?" ,
                    "Der Windsor Roast",
                    "Der Queen's Pork",
                    "Der Royal Apple Pie",
                    "Der Sandringham Pork"
                ],
                [
                    "Welches königliche Ritual beinhaltet das Entzünden von Feuern auf verschiedenen Hügeln in ganz Großbritannien?" ,
                    "Das Jubilee Feuerritual",
                    "Das Königsfeuer-Ritual",
                    "Das Beacon Feuerritual",
                    "Das Highland Feuerfest"
                ],
                [
                    "Welche königliche Residenz wird als ältestes bewohntes Schloss der Welt angesehen?" ,
                    "Windsor Castle",
                    "Buckingham Palace\t",
                    "Sandringham House\t",
                    "Balmoral Castle"
                ]
            ]
    
    answer = [
                "König George VI.",
                "775",
                "14",
                "Prinzessin Anne",
                "Special Branch",
                "Prinzessin Margaret und Anthony Armstrong-Jones",
                "Viktoria",
                "600",
                "Prinz Charles",
                "34",
                "Prinzessin Beatrice",
                "Prinz William",
                "Herzogin Kate",
                "Prinzessin Beatrice",
                "Prinz Harry",
                "Herzogin Camilla",
                "Herzogin Meghan",
                "Willow und Holly",
                "Schwäne",
                "30",
                "Gebühren für das Nutzen von Kronen-Marken",
                "Die Wellington-Stiefel",
                "König George V",
                "Sandringham House",
                "Der Victoria Sponge Cake",
                "Windsor Castle",
                "Buckingham Palace",
                "Der Sandringham Pork",
                "Das Beacon Feuerritual",
                "Windsor Castle",
             ]
    
    explanation = [
        "König George VI. war der erste Monarch, der eine Radio-Weihnachtsansprache hielt. Die erste Ansprache wurde 1932 ausgestrahlt.",
        "Der Buckingham Palace hat 775 Räume, darunter 19 Staatsschlafzimmer, 92 Büros, 78 Badezimmer, 52 königliche und Gästeschlafzimmer und 188 Angestelltenzimmer.",
        "Königin Elizabeth II. hat 14 Premierminister erlebt, von Winston Churchill bis Boris Johnson.",
        "Prinzessin Anne war die erste königliche Tochter, die an den Olympischen Spielen teilnahm. Sie nahm 1976 in Montreal an den Olympischen Spielen teil.",
        "Der offizielle Geheimdienst der königlichen Familie ist der Special Branch, der für den Schutz der königlichen Familie zuständig ist.",
        "Die Hochzeit von Prinzessin Margaret und Anthony Armstrong-Jones war die erste königliche Hochzeit, die im Jahre 1960 im Fernsehen übertragen wurde.",
        "Königin Viktoria war die am längsten regierende Monarchin im Vereinigten Königreich vor Königin Elizabeth II. Sie regierte von 1837 bis 1901.",
        "Königin Elizabeth II. war die Schirmherrin von mehr als 600 verschiedenen Wohltätigkeitsorganisationen und Vereinigungen, die sie regelmäßig unterstützt und besucht.",
        "Der Prinz von Wales war bekannt dafür, dass er seine Vorliebe für alternative Heilmethoden und Esoterik hatte, was auch die Konsultation eines Parfümberaters einschloss.",
        "34 - Die Queen hat eine zierliche Statur und entsprechend kleine Füße, was oft zu Schwierigkeiten bei der Auswahl von passenden Schuhen führt.",
        "Prinzessin Beatrice - Die Tochter von Prinz Andrew und Sarah Ferguson ist bekannt für ihre extravaganten Hutkreationen und hat eine beeindruckende Sammlung von über 100 verschiedenen Modellen.",
        "Prinz William - Der Herzog von Cambridge ist ein erfahrener Karateka und hat einen schwarzen Gürtel in dieser Kampfkunst, die er während seiner Ausbildung am Eton College erlernt hat.",
        "Herzogin Kate - Catherine, Duchess of Cambridge, hat an der University of St. Andrews Kunstgeschichte studiert und ihren Abschluss erfolgreich abgeschlossen, bevor sie Mitglied der königlichen Familie wurde.",  
        "Prinzessin Beatrice - Die Tochter von Prinz Andrew und Sarah Ferguson hatte bereits als Kind einige Schauspielrollen in Filmen und Fernsehserien, bevor sie sich ganz ihrer königlichen Verpflichtungen widmete.",
        "Prinz Harry - Der Herzog von Sussex ist bekannt dafür, dass er gerne Selfies macht und sich gerne spontan mit Fans und Passanten für Fotos ablichten lässt, was zu ungewöhnlichen Selfie-Flashmobs geführt hat.",
        "Herzogin Camilla - Camilla Parker Bowles erhielt den Titel '"'Herzogin von Essex'"' nach ihrer Hochzeit mit Prinz Charles im Jahr 2005, bevor sie offiziell den Titel '"'Herzogin von Cornwall'"' annahm.",
        "Herzogin Meghan - Meghan Markle veröffentlichte unter dem Pseudonym '"'Meghan, The Duchess of Sussex'"' eine Reihe von Kinderbüchern über Themen wie Feminismus, Vielfalt und Inklusion.",
        "Willow und Holly - Queen Elizabeth II hat tatsächlich viele Corgis und Dorgis, darunter auch Willow und Holly.",
        "Die Königin von England besitzt offiziell alle unmarkierten Schwäne auf der Themse. Diese Tradition stammt aus dem Mittelalter und wird durch die jährliche '"'Swan Upping'"' Zeremonie geehrt, bei der die Schwäne gezählt und markiert werden.",
        "Königin Elizabeth II. war bekannt für ihre Liebe zu Corgis und hatte insgesamt 30 im Laufe ihres Lebens. Ihr erster Corgi war ein Geschenk zu ihrem 18. Geburtstag.",
        "Das britische Königshaus erhält Einnahmen, wenn Unternehmen königliche Wappen oder Kronen-Marken auf ihren Produkten verwenden möchten. Diese Gebühren werden durch den '"'Royal Warrant'"' reguliert.",
        "Die Wellington-Stiefel wurden nach Arthur Wellesley, 1. Herzog von Wellington, benannt, der sie als bequeme Reitstiefel trug. Heute sind sie ein klassisches Accessoire für regnerisches Wetter.",
        "König George V führte 1932 die Tradition der Weihnachtsansprache im Radio ein, um die Bürger des britischen Empire zu erreichen und ihnen Weihnachtsgrüße zu übermitteln. Diese Tradition wird bis heute von der königlichen Familie fortgesetzt.",
        "Sandringham House, ein Landsitz der königlichen Familie, ist bekannt für seine eigene königliche Brauerei, die eigenes Bier herstellt. Der Bierverkauf trägt zur Finanzierung des Anwesens bei.",
        "Der Victoria Sponge Cake wurde nach Königin Victoria benannt, die bekannt war, diesen Kuchen mit einer Schicht Marmelade in der Mitte zu essen. Dieses Gericht ist bis heute ein beliebter Klassiker in Großbritannien.",
        "Windsor Castle ist bekannt für seine umfangreiche Uhrensammlung, die aus mehreren Jahrhunderten stammt. Die Sammlung umfasst sowohl kunstvolle als auch funktionale Zeitmesser.",
        "Der Rosengarten im Buckingham Palace ist einer der bekanntesten in Großbritannien und beherbergt über 2.000 Rosensträucher. Der Garten wird für offizielle Veranstaltungen und private Feiern genutzt.",
        "Der Sandringham Pork ist ein traditionelles Gericht, das aus gerösteten Schweinefleischscheiben mit einer Schicht Apfelmus besteht. Dieses Gericht ist ein beliebter Bestandteil königlicher Mahlzeiten auf dem Anwesen Sandringham House.",
        "Das Beacon Feuerritual ist ein königliches Ritual, bei dem auf verschiedenen Hügeln in ganz Großbritannien Feuer entzündet werden, um besondere Anlässe wie das Jubiläum der Königin zu feiern.",
        "Windsor Castle ist das älteste und größte durchgehend bewohnte Schloss der Welt. Es wurde im 11. Jahrhundert von Wilhelm dem Eroberer gebaut und ist bis heute eine königliche Residenz.",
    ]

     
    questionIndex = ['',0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    randnr = random.choice(questionIndex[1:])
    
    global prevIndex
    prevIndex = randnr

    #print("before "+ str(randnr))


    ques = Label(quiz_frame,text =f"{my_counter()}. {quizQ[randnr][0]}",font="Helvetica 20",bg="white", wraplength=800)
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    
    var = StringVar()
    
    a = Radiobutton(quiz_frame,text=quizQ[randnr][1],font="Helvetica 15",value=quizQ[randnr][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(quiz_frame,text=quizQ[randnr][2],font="Helvetica 15",value=quizQ[randnr][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(quiz_frame,text=quizQ[randnr][3],font="Helvetica 15",value=quizQ[randnr][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(quiz_frame,text=quizQ[randnr][4],font="Helvetica 15",value=quizQ[randnr][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 

    
    
    questionIndex.remove(randnr)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER) 
    
    def display():
            
        global score
        global prevIndex
    
        
        if (var.get() in answer):
            score += 1
            winsound.PlaySound('./files/youWin.wav', winsound.SND_FILENAME)  # Play a custom win sound
        else:
            winsound.PlaySound('./files/youFailed.wav', winsound.SND_FILENAME)  # Play a custom fail sound
        
        if len(questionIndex) == 1:
            e.destroy()
            showMark(score)
            # Save the score in the database
            #username = user.get() # Get the username of the current user
            #conn = sqlite3.connect('quiz.db')  # Connect to the database
            #create = conn.cursor()
            #create.execute("UPDATE userSignUp SET SCORE = ? WHERE USERNAME = ?", (score, username))  # Update the score
            #conn.commit()  # Commit the changes
            #conn.close()  # Close the connection
        if len(questionIndex) == 2:
            nextQuestion.configure(text='End',command=display)

        
                
        if questionIndex:
            randnr = random.choice(questionIndex[1:])
            
            ques.configure(text =f"{my_counter()}. {quizQ[randnr][0]}")
            
            a.configure(text=quizQ[randnr][1],value=quizQ[randnr][1])
      
            b.configure(text=quizQ[randnr][2],value=quizQ[randnr][2])
      
            c.configure(text=quizQ[randnr][3],value=quizQ[randnr][3])
      
            d.configure(text=quizQ[randnr][4],value=quizQ[randnr][4])


            questionIndex.remove(randnr)

            if prevIndex is not None:  # If there was a previous question
                showExplanation(prevIndex)  # Show explanation for the previous question
            prevIndex = randnr  # Update prevIndex
            
             
            y = countDown()
            if y == -1:
                next_and_close()
        
        return score
           
            
   # def calc():
    #    global score
    #    if (var.get() in answer):
    #        score+=1
    #    display()
    
   # submit = Button(quiz_frame,command=calc,text="Submit", fg="white", bg="black")
   # submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(quiz_frame,command=next_and_close,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(quiz_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
   
def showMark(mark):
    sh = Tk()
    sh.title('Deine Punktzahl')
    
    st = "Deine Punktzahl: "+str(mark)+"/"+ str(len(quizQ))
    mlabel = Label(sh,text=st,fg="black", bg="white")
    mlabel.pack()
    
    def callsignUpPage():
        sh.destroy()
        start()
    
    def myquiz():
        sh.destroy()
        quiz()
    
    b24=Button(text="Erneut Versuchen", command=myquiz, bg="black", fg="white")
    b24.pack()
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(6, 5), dpi=100)
    labels = 'Erreichte Punkte','Totale Punkte'
    sizes = [int(mark),30-int(mark)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b23=Button(text="Abmelden",command=callsignUpPage,fg="white", bg="black")
    b23.pack()
    
    sh.mainloop()

def start():
    global root 
    root = Tk()
    root.title('Wilkomen bei Royal Quiz App')
    root.attributes('-fullscreen', True)
   
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()-70

    canvas = Canvas(root, width=screen_width, height=screen_height, bg='red')
    canvas.grid(column = 0 , row = 1)

    
    img = ImageTk.PhotoImage(Image.open("./files/startscreen.jpg").resize((screen_width-70, screen_height)))
    canvas.create_image(0, 0, image=img, anchor=NW)

    button = Button(root, text='S T A R T', command=signUpPage, bg="red", fg="white", font=("Helvetica", 11))
    button.configure(width = 90,height=3, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0, row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
