from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import game_100

rules_txt = "Trenutno se nalazite u glavnom izborniku. Odaberite 'Igraj' za početak igre. Igra se sastoji od 15 pitanja čija težina raste. Svako pitanje vrijedi određen novčani iznos koji se ostvaruje točnim odgovorom. U slučaju netočnog odgovora gubite sav osvojen novac i vraćate se na 0kn ili na najbilžu 'garantiranu granicu'. Ukupno postoje 3 takve granice (1000kn, 32000kn i 1000000kn). Također, postoji mogućnost odustajanja te ukoliko se za istu odlučite osvajate zadnji osvojen iznos. Za pomoć tijekom igre imate na raspolaganu 3 jokera (50/50, Zovi, Publika). Joker '50/50' uklanja dva netočna odgovora. Joker 'Zovi' poziva prijatelja koji vam daje svoje mišljenje o točnom odgovoru te sigurnost u isto. Joker 'Publika' prikazuje vam mišljenje publike o točnom odgovoru kroz postotke. Imajte na umu da se šanse da će jokeri 'Zovi' i 'Publika' dati točan odgovor smanjuju povećanjem iznosa. Igra je gotova kada odgovorite netočno, odustanete ili odgovorite točno na posljednje pitanje. U glavnom iborniku osim opcije 'Igraj', 'Izlaz' i 'Pravila' imate i opciju 'Prijedlozi i primjedbe'. Odabirom iste opcije otvara vam se polje gdje možete dati bilo kakav prijedlog (poboljšanje izgleda, novo pitanje, nove opcije, ...), primjedbu (netočan odgovor, greška u igri, ...) ili postaviti bilo kakvo pitanje. Ukoliko želite biti anonimni polje 'Ime:' ostavite prazno ili u suprotnom u njega unesite vaše ime ili ako želite odgovor na postavljeno pitanje vaš email. Sretno i Uživajte u igri." 

#functions
def play_func(event):

	#game jokers .txt file setup
	jok_test_file = open("jok_test.txt","w")
	jok_test_file.write("")
	jok_test_file.close()

	game_100.run()

def rules_func(event):
	rul = Toplevel(main)
	rul.geometry("800x500+0+0")
	rul.title("Pravila")
	rul.resizable(False,False)
	rul.config(bg="black")

	rules_label = Label(rul,text=rules_txt,bg="black",fg="lightblue",font="arial 15 bold",wraplength=700)
	rules_label.config(width=65,height=30)
	rules_label.pack()

def feedback_func(event):
	def send_func(event):
		email = "antoniosalov.tzbm@gmail.com"
		password = "TZBMtzbm"
		send_to_email = "antoniosalov.tzbm@gmail.com"

		ime = name_entry.get()
		if ime == "":
			ime = "Anonimno"

		if radio_subject.get() == 3:
			subject = "[Prijedlog - " + ime + " ]"
		if radio_subject.get() == 2:
			subject = "[Primjedba - " + ime + " ]"
		if radio_subject.get() == 1:
			subject = "[Ostalo - " + ime + " ]"

		message = textbox.get("1.0",END)

		msg = MIMEMultipart()
		msg["From"] = email
		msg["To"] = send_to_email
		msg["Subject"] = subject

		msg.attach(MIMEText(message,"plain"))

		server = smtplib.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.login(email,password)
		text = msg.as_string()
		server.sendmail(email,send_to_email,text)
		server.quit()

	fdb = Toplevel(main)
	fdb.title("Prijedlozi i primjedbe")
	fdb.geometry("800x500+0+0")
	fdb.resizable(False,False)
	fdb.config(bg="black")

	radio_frame = Frame(fdb,bg="black",width=800,height=100)
	radio_frame.grid(row=0,column=0)	#done

	text_frame = Frame(fdb,bg="black",width=800,height=300)
	text_frame.grid(row=1,column=0)	#done

	bottom_frame = Frame(fdb,bg="black",width=800,height=100)
	bottom_frame.grid(row=2,column=0)	#done

	radio_subject =  IntVar()
	Radiobutton(radio_frame,text="Prijedlog",variable=radio_subject,value=3,bg="black",fg="lightblue",font="arial 26 bold",width=10,height=2).grid(row=0,column=0)
	Radiobutton(radio_frame,text="Primjedba",variable=radio_subject,value=2,bg="black",fg="lightblue",font="arial 26 bold",width=10,height=2).grid(row=0,column=1)
	Radiobutton(radio_frame,text="Ostalo",variable=radio_subject,value=1,bg="black",fg="lightblue",font="arial 26 bold",width=10,height=2).grid(row=0,column=2)

	textbox = Text(text_frame,width=100,height=19)
	textbox.pack()

	email_frame = Frame(bottom_frame,bg="black",width=600,height=100)
	email_frame.grid(row=0,column=0)	#done

	send_frame = Frame(bottom_frame,bg="black",width=200,height=100)
	send_frame.grid(row=0,column=1)	#done

	email_label = Label(email_frame,text="Ime:",bg="black",fg="lightblue",font="arial 31 bold")
	email_label.config(width=6,height=2)
	email_label.grid(row=0,column=0)

	name_entry = Entry(email_frame)
	name_entry.config(width=25,bg="black",fg="lightblue",font="arial 25 bold")
	name_entry.grid(row=0,column=1,ipady=30)

	send_button = Button(send_frame,text="Pošalji",bg="black",fg="lightblue",font="arial 24 bold")
	send_button.config(width=10,height=2)
	send_button.bind("<Button>",send_func)
	send_button.pack()


def close_func(event):
	main.destroy()

#main setup
main = Tk()

main.title("Tko Želi biti Milijunaš")
main.geometry("800x500+0+0")
main.config(bg="black")
main.resizable(False,False)

#frame setup
title_frame = Frame(main,bg="black",width=800,height=200)
title_frame.grid(row=0,column=0)	#done

first_row_frame = Frame(main,bg="black",width=800,height=150)
first_row_frame.grid(row=1,column=0)	#done

second_row_frame = Frame(main,bg="black",width=800,height=150)
second_row_frame.grid(row=2,column=0)	#done

play_frame = Frame(first_row_frame,bg="black",width=400,height=150)
play_frame.grid(row=0,column=0)	#done

rules_frame = Frame(first_row_frame,bg="black",width=400,height=150)
rules_frame.grid(row=0,column=1)	#done

feedback_frame = Frame(second_row_frame,bg="black",width=400,height=150)
feedback_frame.grid(row=0,column=0)	#done

close_frame = Frame(second_row_frame,bg="black",width=400,height=150)
close_frame.grid(row=0,column=1)	#done

#buttons setup
play_button = Button(play_frame,text="Igraj",bg="black",fg="lightblue",font="arial 54 bold")
play_button.config(width=8,height=1)
play_button.bind("<Button>",play_func)
play_button.pack()

rules_button = Button(rules_frame,text="Pravila",bg="black",fg="lightblue",font="arial 54 bold")
rules_button.config(width=8,height=1)
rules_button.bind("<Button>",rules_func)
rules_button.pack()

feedback_button = Button(feedback_frame,text="Prijedlozi i primjedbe",bg="black",fg="lightblue",font="arial 36 bold",wraplength=400)
feedback_button.config(width=12,height=2)
feedback_button.bind("<Button>",feedback_func)
feedback_button.pack()

close_button = Button(close_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 56 bold")
close_button.config(width=8,height=1)
close_button.bind("<Button>",close_func)
close_button.pack()

#label setup
title_label = Label(title_frame,text="Tko Želi Biti Milijunaš?",bg="black",fg="lightblue",font="arial 41 bold")
title_label.config(width=23,height=3)
title_label.pack()

main.mainloop()