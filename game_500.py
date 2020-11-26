from tkinter import *
from random import choice as pick
from random import randint as r
from sys import exit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import game_1000


def run():
	global jok_50_used

	#question base
	qs = ["Koji gol ima najmanji volumen?",
			"Koji je maksimalan broj poena što se može postići jednim šutem u košarci?",
			"Dužina 1 kruga na atletskoj stazi je...?",
			"Wimbeldon, Roland Garros, US Open, Australian Open jednim se imenom nazivaju..."]

	#wrong answers base
	wanss = [["nogometni","rukometni","vaterpolski"],
			["1","2","5"],
			["100m","200m","300m"],
			["Davis Cup","Masters","ITF"]]

	#correct answers base
	canss = ["hokejaški",
			"3",
			"400m",
			"Grand Slam"]

	#functions
	def ansA_func(event):
		def quit_func(event):
			exit()

		def send_func(event):
			email = "antoniosalov.tzbm@gmail.com"
			password = "TZBMtzbm"
			send_to_email = "antoniosalov.tzbm@gmail.com"

			ime = textbox.get("1.0",END)
			if ime == "":
				ime = "Anonimno"

			subject = "[Rezultat - " + ime + " ]"

			message = "Osvojen iznos: " + money_won

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

		global money_500_button

		ansB_button.destroy()
		ansC_button.destroy()
		ansD_button.destroy()

		give_up_button.destroy()
		title_label = Label(title_frame,text="Tko želi biti Milijunaš?",bg="lightblue",fg="black",font="arial 27 bold")
		title_label.config(width=27,height=1)
		title_label.pack()

		if ansA_button.cget("text")[3:] in canss[qs.index(q)]:
			ansA_button.config(fg="green")
		else:
			ansA_button.config(fg="red")

		qs.remove(q)

		if ansA_button.cget("fg") == "green":
			q_label.config(text="VAŠ ODGOVOR JE TOČAN. PRITISNITE 'DALJE' ZA SLIJEDEĆE PITANJE")

			money_500_label.destroy()
		
			money_500_button = Button(money_500_frame,text="DALJE !!",bg="lightblue",fg="red",font="arial 10 bold")
			money_500_button.config(width=24,height=1)
			money_500_button.bind("<Button>",next_1000)
			money_500_button.pack()

		else:
			q_label.config(text="VAŠ ODGOVOR JE NETOČAN. OSVOJILI STE 0 KN")
			money_won = "0"

			end = Toplevel(main)
			end.title("Tko Želi Biti Milijunaš?")
			end.geometry("400x200+810+200")
			end.resizable(False,False)
			end.config(bg="black")

			result_frame = Frame(end,bg="black",width=200,height=200)
			result_frame.grid(row=0,column=0)	#done

			quit_frame = Frame(end,bg="black",width=200,height=200)
			quit_frame.grid(row=0,column=1)	#done

			name_frame = Frame(result_frame,bg="black",width=200,height=100)
			name_frame.grid(row=0,column=0)	#done

			send_frame = Frame(result_frame,bg="black",width=200,height=100)
			send_frame.grid(row=1,column=0)	#done

			name_label = Label(name_frame,text="Ime:",bg="black",fg="lightblue",font="arial 25 bold")
			name_label.config(width=10,height=1)
			name_label.grid(row=0,column=0)

			textbox = Text(name_frame,width=25,height=3)
			textbox.grid(row=1,column=0)

			quit_button = Button(quit_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 34 bold")
			quit_button.config(width=7,height=3)
			quit_button.bind("<Button>",quit_func)
			quit_button.pack()

			send_button = Button(send_frame,text="Pošalji rezultat",bg="black",fg="lightblue",font="arial 17 bold")
			send_button.config(width=14,height=3)
			send_button.bind("<Button>",send_func)
			send_button.pack()

	def ansB_func(event):
		def quit_func(event):
			exit()

		def send_func(event):
			email = "antoniosalov.tzbm@gmail.com"
			password = "TZBMtzbm"
			send_to_email = "antoniosalov.tzbm@gmail.com"

			ime = textbox.get("1.0",END)
			if ime == "":
				ime = "Anonimno"

			subject = "[Rezultat - " + ime + " ]"

			message = "Osvojen iznos: " + money_won

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

		global money_500_button

		ansA_button.destroy()
		ansC_button.destroy()
		ansD_button.destroy()

		give_up_button.destroy()
		title_label = Label(title_frame,text="Tko želi biti Milijunaš?",bg="lightblue",fg="black",font="arial 27 bold")
		title_label.config(width=27,height=1)
		title_label.pack()

		if ansB_button.cget("text")[3:] in canss[qs.index(q)]:
			ansB_button.config(fg="green")
		else:
			ansB_button.config(fg="red")

		qs.remove(q)

		if ansB_button.cget("fg") == "green":
			q_label.config(text="VAŠ ODGOVOR JE TOČAN. PRITISNITE 'DALJE' ZA SLIJEDEĆE PITANJE")

			money_500_label.destroy()
		
			money_500_button = Button(money_500_frame,text="DALJE !!",bg="lightblue",fg="red",font="arial 10 bold")
			money_500_button.config(width=24,height=1)
			money_500_button.bind("<Button>",next_1000)
			money_500_button.pack()

		else:
			q_label.config(text="VAŠ ODGOVOR JE NETOČAN. OSVOJILI STE 0 KN")
			money_won = "0"

			end = Toplevel(main)
			end.title("Tko Želi Biti Milijunaš?")
			end.geometry("400x200+810+200")
			end.resizable(False,False)
			end.config(bg="black")

			result_frame = Frame(end,bg="black",width=200,height=200)
			result_frame.grid(row=0,column=0)	#done

			quit_frame = Frame(end,bg="black",width=200,height=200)
			quit_frame.grid(row=0,column=1)	#done

			name_frame = Frame(result_frame,bg="black",width=200,height=100)
			name_frame.grid(row=0,column=0)	#done

			send_frame = Frame(result_frame,bg="black",width=200,height=100)
			send_frame.grid(row=1,column=0)	#done

			name_label = Label(name_frame,text="Ime:",bg="black",fg="lightblue",font="arial 25 bold")
			name_label.config(width=10,height=1)
			name_label.grid(row=0,column=0)

			textbox = Text(name_frame,width=25,height=3)
			textbox.grid(row=1,column=0)

			quit_button = Button(quit_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 34 bold")
			quit_button.config(width=7,height=3)
			quit_button.bind("<Button>",quit_func)
			quit_button.pack()

			send_button = Button(send_frame,text="Pošalji rezultat",bg="black",fg="lightblue",font="arial 17 bold")
			send_button.config(width=14,height=3)
			send_button.bind("<Button>",send_func)
			send_button.pack()

	def ansC_func(event):
		def quit_func(event):
			exit()

		def send_func(event):
			email = "antoniosalov.tzbm@gmail.com"
			password = "TZBMtzbm"
			send_to_email = "antoniosalov.tzbm@gmail.com"

			ime = textbox.get("1.0",END)
			if ime == "":
				ime = "Anonimno"

			subject = "[Rezultat - " + ime + " ]"

			message = "Osvojen iznos: " + money_won

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

		global money_500_button

		ansA_button.destroy()
		ansB_button.destroy()
		ansD_button.destroy()

		give_up_button.destroy()
		title_label = Label(title_frame,text="Tko želi biti Milijunaš?",bg="lightblue",fg="black",font="arial 27 bold")
		title_label.config(width=27,height=1)
		title_label.pack()

		if ansC_button.cget("text")[3:] in canss[qs.index(q)]:
			ansC_button.config(fg="green")
		else:
			ansC_button.config(fg="red")

		qs.remove(q)

		if ansC_button.cget("fg") == "green":
			q_label.config(text="VAŠ ODGOVOR JE TOČAN. PRITISNITE 'DALJE' ZA SLIJEDEĆE PITANJE")

			money_500_label.destroy()
		
			money_500_button = Button(money_500_frame,text="DALJE !!",bg="lightblue",fg="red",font="arial 10 bold")
			money_500_button.config(width=24,height=1)
			money_500_button.bind("<Button>",next_1000)
			money_500_button.pack()

		else:
			q_label.config(text="VAŠ ODGOVOR JE NETOČAN. OSVOJILI STE 0 KN")
			money_won = "0"

			end = Toplevel(main)
			end.title("Tko Želi Biti Milijunaš?")
			end.geometry("400x200+810+200")
			end.resizable(False,False)
			end.config(bg="black")

			result_frame = Frame(end,bg="black",width=200,height=200)
			result_frame.grid(row=0,column=0)	#done

			quit_frame = Frame(end,bg="black",width=200,height=200)
			quit_frame.grid(row=0,column=1)	#done

			name_frame = Frame(result_frame,bg="black",width=200,height=100)
			name_frame.grid(row=0,column=0)	#done

			send_frame = Frame(result_frame,bg="black",width=200,height=100)
			send_frame.grid(row=1,column=0)	#done

			name_label = Label(name_frame,text="Ime:",bg="black",fg="lightblue",font="arial 25 bold")
			name_label.config(width=10,height=1)
			name_label.grid(row=0,column=0)

			textbox = Text(name_frame,width=25,height=3)
			textbox.grid(row=1,column=0)

			quit_button = Button(quit_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 34 bold")
			quit_button.config(width=7,height=3)
			quit_button.bind("<Button>",quit_func)
			quit_button.pack()

			send_button = Button(send_frame,text="Pošalji rezultat",bg="black",fg="lightblue",font="arial 17 bold")
			send_button.config(width=14,height=3)
			send_button.bind("<Button>",send_func)
			send_button.pack()

	def ansD_func(event):
		def quit_func(event):
			exit()

		def send_func(event):
			email = "antoniosalov.tzbm@gmail.com"
			password = "TZBMtzbm"
			send_to_email = "antoniosalov.tzbm@gmail.com"

			ime = textbox.get("1.0",END)
			if ime == "":
				ime = "Anonimno"

			subject = "[Rezultat - " + ime + " ]"

			message = "Osvojen iznos: " + money_won

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

		global money_500_button

		ansA_button.destroy()
		ansB_button.destroy()
		ansC_button.destroy()

		give_up_button.destroy()
		title_label = Label(title_frame,text="Tko želi biti Milijunaš?",bg="lightblue",fg="black",font="arial 27 bold")
		title_label.config(width=27,height=1)
		title_label.pack()

		if ansD_button.cget("text")[3:] in canss[qs.index(q)]:
			ansD_button.config(fg="green")
		else:
			ansD_button.config(fg="red")
		
		qs.remove(q)

		if ansD_button.cget("fg") == "green":
			q_label.config(text="VAŠ ODGOVOR JE TOČAN. PRITISNITE 'DALJE' ZA SLIJEDEĆE PITANJE")

			money_500_label.destroy()
		
			money_500_button = Button(money_500_frame,text="DALJE !!",bg="lightblue",fg="red",font="arial 10 bold")
			money_500_button.config(width=24,height=1)
			money_500_button.bind("<Button>",next_1000)
			money_500_button.pack()

		else:
			q_label.config(text="VAŠ ODGOVOR JE NETOČAN. OSVOJILI STE 0 KN")
			money_won = "0"

			end = Toplevel(main)
			end.title("Tko Želi Biti Milijunaš?")
			end.geometry("400x200+810+200")
			end.resizable(False,False)
			end.config(bg="black")

			result_frame = Frame(end,bg="black",width=200,height=200)
			result_frame.grid(row=0,column=0)	#done

			quit_frame = Frame(end,bg="black",width=200,height=200)
			quit_frame.grid(row=0,column=1)	#done

			name_frame = Frame(result_frame,bg="black",width=200,height=100)
			name_frame.grid(row=0,column=0)	#done

			send_frame = Frame(result_frame,bg="black",width=200,height=100)
			send_frame.grid(row=1,column=0)	#done

			name_label = Label(name_frame,text="Ime:",bg="black",fg="lightblue",font="arial 25 bold")
			name_label.config(width=10,height=1)
			name_label.grid(row=0,column=0)

			textbox = Text(name_frame,width=25,height=3)
			textbox.grid(row=1,column=0)

			quit_button = Button(quit_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 34 bold")
			quit_button.config(width=7,height=3)
			quit_button.bind("<Button>",quit_func)
			quit_button.pack()

			send_button = Button(send_frame,text="Pošalji rezultat",bg="black",fg="lightblue",font="arial 17 bold")
			send_button.config(width=14,height=3)
			send_button.bind("<Button>",send_func)
			send_button.pack()

	def give_up_func(event):
		def quit_func(event):
			exit()

		def send_func(event):
			email = "antoniosalov.tzbm@gmail.com"
			password = "TZBMtzbm"
			send_to_email = "antoniosalov.tzbm@gmail.com"

			ime = textbox.get("1.0",END)
			if ime == "":
				ime = "Anonimno"

			subject = "[Rezultat - " + ime + " ]"

			message = "Osvojen iznos: " + money_won

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

		ansA_button.destroy()
		ansB_button.destroy()
		ansC_button.destroy()
		ansD_button.destroy()

		q_label.config(text="ODUSTALI STE. OSVOJILI STE 300 KN")
		money_won = "300"

		end = Toplevel(main)
		end.title("Tko Želi Biti Milijunaš?")
		end.geometry("400x200+810+200")
		end.resizable(False,False)
		end.config(bg="black")

		result_frame = Frame(end,bg="black",width=200,height=200)
		result_frame.grid(row=0,column=0)	#done

		quit_frame = Frame(end,bg="black",width=200,height=200)
		quit_frame.grid(row=0,column=1)	#done

		name_frame = Frame(result_frame,bg="black",width=200,height=100)
		name_frame.grid(row=0,column=0)	#done

		send_frame = Frame(result_frame,bg="black",width=200,height=100)
		send_frame.grid(row=1,column=0)	#done

		name_label = Label(name_frame,text="Ime:",bg="black",fg="lightblue",font="arial 25 bold")
		name_label.config(width=10,height=1)
		name_label.grid(row=0,column=0)

		textbox = Text(name_frame,width=25,height=3)
		textbox.grid(row=1,column=0)

		quit_button = Button(quit_frame,text="Izlaz",bg="black",fg="lightblue",font="arial 34 bold")
		quit_button.config(width=7,height=3)
		quit_button.bind("<Button>",quit_func)
		quit_button.pack()

		send_button = Button(send_frame,text="Pošalji rezultat",bg="black",fg="lightblue",font="arial 17 bold")
		send_button.config(width=14,height=3)
		send_button.bind("<Button>",send_func)
		send_button.pack()

	def jok_50_func(event):
		global jok_50_used
		jok_50_used = True

		jok_test_file = open("jok_test.txt","a")
		jok_test_file.write("50")
		jok_test_file.close()

		jok_50_button.config(fg="red")

		ans_options = ["A","B","C","D"]
		dels = 0
		ans_del = pick(ans_options)
		ans_options.remove(ans_del)

		if ans_del == "A":
			if not ansA_button.cget("text")[3:] in canss[qs.index(q)]:
				ansA_button.destroy()
				dels +=1
		if ans_del == "B":
			if not ansB_button.cget("text")[3:] in canss[qs.index(q)]:
				ansB_button.destroy()
				dels += 1
		if ans_del == "C":
			if not ansC_button.cget("text")[3:] in canss[qs.index(q)]:
				ansC_button.destroy()
				dels += 1
		if ans_del == "D":
			if not ansD_button.cget("text")[3:] in canss[qs.index(q)]:
				ansD_button.destroy()
				dels += 1

		ans_del = pick(ans_options)
		ans_options.remove(ans_del)

		if ans_del == "A":
			if not ansA_button.cget("text")[3:] in canss[qs.index(q)]:
				ansA_button.destroy()
				dels +=1
		if ans_del == "B":
			if not ansB_button.cget("text")[3:] in canss[qs.index(q)]:
				ansB_button.destroy()
				dels += 1
		if ans_del == "C":
			if not ansC_button.cget("text")[3:] in canss[qs.index(q)]:
				ansC_button.destroy()
				dels += 1
		if ans_del == "D":
			if not ansD_button.cget("text")[3:] in canss[qs.index(q)]:
				ansD_button.destroy()
				dels += 1

		if dels == 1:
			ans_del = pick(ans_options)
			ans_options.remove(ans_del)

			if ans_del == "A":
				if not ansA_button.cget("text")[3:] in canss[qs.index(q)]:
					ansA_button.destroy()
					dels +=1
			if ans_del == "B":
				if not ansB_button.cget("text")[3:] in canss[qs.index(q)]:
					ansB_button.destroy()
					dels += 1
			if ans_del == "C":
				if not ansC_button.cget("text")[3:] in canss[qs.index(q)]:
					ansC_button.destroy()
					dels += 1
			if ans_del == "D":
				if not ansD_button.cget("text")[3:] in canss[qs.index(q)]:
					ansD_button.destroy()
					dels += 1

		jok_50_button.bind("<Button>",jok_50_func_false)

	def jok_50_func_false(event):
		pass

	def jok_friend_func(event):
		def areyousure_func(event):
			prec_label.config(text=ch)

		jok_test_file = open("jok_test.txt","a")
		jok_test_file.write("call")
		jok_test_file.close()

		jok_friend_button.bind("<Button>",jok_friend_func_false)
		jok_friend_button.config(fg="red")

		call = Toplevel(main)
		call.title("Joker Zovi")
		call.geometry("800x500+0+0")
		call.config(bg="black")
		call.resizable(False,False)

		cans_frame = Frame(call,bg="black",width=800,height=170)
		cans_frame.grid(row=0,column=0)	#done

		areyousure_frame = Frame(call,bg="pink",width=800,height=160)
		areyousure_frame.grid(row=1,column=0)

		prec_frame = Frame(call,bg="red",width=800,height=170)
		prec_frame.grid(row=2,column=0)

		ch = "85%"
		ans_options=["A","B","C","D"]
		if r(1,20) in range(1,18):
			try:
				if ansA_button.cget("text")[3:] in canss[qs.index(q)]:
					cans_text = "A"
			except:
				pass
			try:
				if ansB_button.cget("text")[3:] in canss[qs.index(q)]:
					cans_text = "B"
			except:
				pass
			try:
				if ansC_button.cget("text")[3:] in canss[qs.index(q)]:
					cans_text = "C"
			except:
				pass
			try:
				if ansD_button.cget("text")[3:] in canss[qs.index(q)]:
					cans_text = "D"
			except:
				pass
		else:
			try:
				if not ansA_button.cget("text"):
					ans_options.remove("A")
			except:
				ans_options.remove("A")
			try:
				if not ansB_button.cget("text"):
					ans_options.remove("B")
			except:
				ans_options.remove("B")
			try:
				if not ansC_button.cget("text"):
					ans_options.remove("C")
			except:
				ans_options.remove("C")
			try:
				if not ansD_button.cget("text"):
					ans_options.remove("D")
			except:
				ans_options.remove("D")
			cans_text=pick(ans_options)

		cans_label = Label(cans_frame,text="Točan odgovor je: "+cans_text,bg="black",fg="lightblue",font="arial 54 bold")
		cans_label.config(width=18,height=2)
		cans_label.pack()

		areyousure_button = Button(areyousure_frame,text="Koliko si siguran?",bg="black",fg="lightblue",font="arial 36 bold")
		areyousure_button.config(width=26,height=2)
		areyousure_button.bind("<Button>",areyousure_func)
		areyousure_button.pack()

		prec_label = Label(prec_frame,text="",bg="black",fg="lightblue",font="arial 54 bold")
		prec_label.config(width=18,height=2)
		prec_label.pack()

	def jok_friend_func_false(event):
		pass

	def jok_audience_func(event):
		global A_ch_valid
		global B_ch_valid
		global C_ch_valid
		global D_ch_valid

		A_ch_valid = False
		B_ch_valid = False
		C_ch_valid = False
		D_ch_valid = False

		jok_test_file = open("jok_test.txt","a")
		jok_test_file.write("ask")
		jok_test_file.close()

		jok_audience_button.bind("<Button>",jok_audience_func_false)
		jok_audience_button.config(fg="red")

		ask = Toplevel(main)
		ask.title("Joker Publika")
		ask.geometry("800x500+0+0")
		ask.config(bg="black")
		ask.resizable(False,False)

		layerA_frame = Frame(ask,bg="black",width=800,height=125)
		layerA_frame.grid(row=0,column=0)

		layerB_frame = Frame(ask,bg="black",width=800,height=125)
		layerB_frame.grid(row=1,column=0)

		layerC_frame = Frame(ask,bg="black",width=800,height=125)
		layerC_frame.grid(row=2,column=0)

		layerD_frame = Frame(ask,bg="black",width=800,height=125)
		layerD_frame.grid(row=3,column=0)

		A_frame = Frame(layerA_frame,bg="green",width=200,height=125)
		A_frame.grid(row=0,column=0)

		A_prec_frame = Frame(layerA_frame,bg="black",width=200,height=125)
		A_prec_frame.grid(row=0,column=1)

		A_color_frame = Frame(layerA_frame,bg="black",width=400,height=125)
		A_color_frame.grid(row=0,column=2)

		B_frame = Frame(layerB_frame,bg="lightgreen",width=200,height=125)
		B_frame.grid(row=0,column=0)

		B_prec_frame = Frame(layerB_frame,bg="black",width=200,height=125)
		B_prec_frame.grid(row=0,column=1)

		B_color_frame = Frame(layerB_frame,bg="black",width=400,height=125)
		B_color_frame.grid(row=0,column=2)

		C_frame = Frame(layerC_frame,bg="green",width=200,height=125)
		C_frame.grid(row=0,column=0)

		C_prec_frame = Frame(layerC_frame,bg="black",width=200,height=125)
		C_prec_frame.grid(row=0,column=1)

		C_color_frame = Frame(layerC_frame,bg="black",width=400,height=125)
		C_color_frame.grid(row=0,column=2)

		D_frame = Frame(layerD_frame,bg="lightgreen",width=200,height=125)
		D_frame.grid(row=0,column=0)

		D_prec_frame = Frame(layerD_frame,bg="black",width=200,height=125)
		D_prec_frame.grid(row=0,column=1)

		D_color_frame = Frame(layerD_frame,bg="black",width=400,height=125)
		D_color_frame.grid(row=0,column=2)

		ch = "85%"
		if jok_50_used:
			if r(1,20) in range(1,18):
				try:
					test = ansA_button.cget("text")
					if test[3:] in canss[qs.index(q)]:
						A_ch = r(80,85)
						A_ch_valid = True
						try:
							test = ansB_button.cget("text")
							B_ch = 100-A_ch
							B_ch_valid = True
						except:
							pass
						try:
							test = ansC_button.cget("text")
							C_ch = 100-A_ch
							C_ch_valid = True
						except:
							pass
						try:
							test = ansD_button.cget("text")
							D_ch = 100-A_ch
							D_ch_valid = True
						except:
							pass
				except:
					pass
				try:
					test = ansB_button.cget("text")
					if test[3:] in canss[qs.index(q)]:
						B_ch = r(80,85)
						B_ch_valid = True
						try:
							test = ansA_button.cget("text")
							A_ch = 100-B_ch
							A_ch_valid = True
						except:
							pass
						try:
							test = ansC_button.cget("text")
							C_ch = 100-B_ch
							C_ch_valid = True
						except:
							pass
						try:
							test = ansD_button.cget("text")
							D_ch = 100-B_ch
							D_ch_valid = True
						except:
							pass
				except:
					pass
				try:
					test = ansC_button.cget("text")
					if test[3:] in canss[qs.index(q)]:
						C_ch = r(80,85)
						C_ch_valid = True
						try:
							test = ansB_button.cget("text")
							B_ch = 100-C_ch
							B_ch_valid = True
						except:
							pass
						try:
							test = ansA_button.cget("text")
							A_ch = 100-C_ch
							A_ch_valid = True
						except:
							pass
						try:
							test = ansD_button.cget("text")
							D_ch = 100-C_ch
							D_ch_valid = True
						except:
							pass
				except:
					pass
				try:
					test = ansD_button.cget("text")
					if test[3:] in canss[qs.index(q)]:
						D_ch = r(80,85)
						D_ch_valid = True
						try:
							test = ansB_button.cget("text")
							B_ch = 100-D_ch
							B_ch_valid = True
						except:
							pass
						try:
							test = ansC_button.cget("text")
							C_ch = 100-D_ch
							C_ch_valid = True
						except:
							pass
						try:
							test = ansA_button.cget("text")
							A_ch = 100-D_ch
							A_ch_valid = True
						except:
							pass
				except:
					pass

			else:
				try:
					test = ansA_button.cget("text")
					A_ch = r(0,99)
					A_ch_valid = True

					try:
						test = ansB_button.cget("text")
						B_ch = 100-A_ch
						B_ch_valid = True

					except:
						try:
							test = ansC_button.cget("text")
							C_ch = 100-A_ch
							C_ch_valid = True

						except:
							try:
								test = ansD_button.cget("text")
								D_ch = 100-A_ch
								D_ch_valid = True

							except:
								pass
				except:
					pass

				try:
					test = ansB_button.cget("text")
					B_ch = r(0,99)
					B_ch_valid = True

					try:
						test = ansA_button.cget("text")
						A_ch = 100-B_ch
						A_ch_valid = True

					except:
						try:
							test = ansC_button.cget("text")
							C_ch = 100-B_ch
							C_ch_valid = True

						except:
							try:
								test = ansD_button.cget("text")
								D_ch = 100-B_ch
								D_ch_valid = True

							except:
								pass
				except:
					pass

				try:
					test = ansC_button.cget("text")
					C_ch = r(0,99)
					C_ch_valid = True

					try:
						test = ansB_button.cget("text")
						B_ch = 100-C_ch
						B_ch_valid = True

					except:
						try:
							test = ansA_button.cget("text")
							A_ch = 100-C_ch
							A_ch_valid = True

						except:
							try:
								test = ansD_button.cget("text")
								D_ch = 100-C_ch
								D_ch_valid = True

							except:
								pass
				except:
					pass

				try:
					test = ansD_button.cget("text")
					D_ch = r(0,99)
					D_ch_valid = True

					try:
						test = ansB_button.cget("text")
						B_ch = 100-D_ch
						B_ch_valid = True

					except:
						try:
							test = ansC_button.cget("text")
							C_ch = 100-D_ch
							C_ch_valid = True

						except:
							try:
								test = ansA_button.cget("text")
								A_ch = 100-D_ch
								A_ch_valid = True

							except:
								pass
				except:
					pass

		else:
			A_ch_valid = True
			B_ch_valid = True
			C_ch_valid = True
			D_ch_valid = True

			if r(1,20) in range(1,18):
				if ansA_button.cget("text")[3:] in canss[qs.index(q)]:
					A_ch = r(80,85)
			 
					B_ch = r(0,100-A_ch)

					C_ch = r(0,100-A_ch-B_ch)

					D_ch = 100-A_ch-B_ch-C_ch

				if ansB_button.cget("text")[3:] in canss[qs.index(q)]:
					B_ch = r(80,85)

					A_ch = r(0,100-B_ch)

					C_ch = r(0,100-B_ch-A_ch)

					D_ch = 100-B_ch-A_ch-C_ch

				if ansC_button.cget("text")[3:] in canss[qs.index(q)]:
					C_ch = r(80,85)

					A_ch = r(0,100-C_ch)

					B_ch = r(0,100-C_ch-A_ch)

					D_ch = 100-C_ch-A_ch-B_ch

				if ansD_button.cget("text")[3:] in canss[qs.index(q)]:
					D_ch = r(80,85)

					A_ch = r(0,100-D_ch)

					B_ch = r(0,100-D_ch-A_ch)

					C_ch = 100-D_ch-A_ch-B_ch

			else:
					C_ch = r(0,99)

					B_ch = r(0,100-C_ch)

					D_ch = r(0,100-C_ch-B_ch)

					A_ch = 100-C_ch-B_ch-D_ch

		A_label = Label(A_frame,text="A:",bg="black",fg="lightblue",font="arial 79 bold")
		A_label.config(width=3,height=1)
		A_label.pack()

		B_label = Label(B_frame,text="B:",bg="black",fg="lightblue",font="arial 79 bold")
		B_label.config(width=3,height=1)
		B_label.pack()

		C_label = Label(C_frame,text="C:",bg="black",fg="lightblue",font="arial 79 bold")
		C_label.config(width=3,height=1)
		C_label.pack()

		D_label = Label(D_frame,text="D:",bg="black",fg="lightblue",font="arial 79 bold")
		D_label.config(width=3,height=1)
		D_label.pack()

		if A_ch_valid:
			A_prec_label = Label(A_prec_frame,text=str(A_ch)+"%",bg="black",fg="lightblue",font="arial 79 bold")
			A_prec_label.config(width=3,height=1)
			A_prec_label.pack()

			A_colored_frame = Frame(A_color_frame,bg="red",width=4*A_ch,height=125)
			A_colored_frame.grid(row=0,column=0)
			A_uncolored_frame = Frame(A_color_frame,bg="black",width=400-4*A_ch,height=125)
			A_uncolored_frame.grid(row=0,column=1)

		if B_ch_valid:
			B_prec_label = Label(B_prec_frame,text=str(B_ch)+"%",bg="black",fg="lightblue",font="arial 79 bold")
			B_prec_label.config(width=3,height=1)
			B_prec_label.pack()

			B_colored_frame = Frame(B_color_frame,bg="red",width=4*B_ch,height=125)
			B_colored_frame.grid(row=0,column=0)
			B_uncolored_frame = Frame(B_color_frame,bg="black",width=400-4*B_ch,height=125)
			B_uncolored_frame.grid(row=0,column=1)

		if C_ch_valid:
			C_prec_label = Label(C_prec_frame,text=str(C_ch)+"%",bg="black",fg="lightblue",font="arial 79 bold")
			C_prec_label.config(width=3,height=1)
			C_prec_label.pack()

			C_colored_frame = Frame(C_color_frame,bg="red",width=4*C_ch,height=125)
			C_colored_frame.grid(row=0,column=0)
			C_uncolored_frame = Frame(C_color_frame,bg="black",width=400-4*C_ch,height=125)
			C_uncolored_frame.grid(row=0,column=1)

		if D_ch_valid:
			D_prec_label = Label(D_prec_frame,text=str(D_ch)+"%",bg="black",fg="lightblue",font="arial 79 bold")
			D_prec_label.config(width=3,height=1)
			D_prec_label.pack()

			D_colored_frame = Frame(D_color_frame,bg="red",width=4*D_ch,height=125)
			D_colored_frame.grid(row=0,column=0)
			D_uncolored_frame = Frame(D_color_frame,bg="black",width=400-4*D_ch,height=125)
			D_uncolored_frame.grid(row=0,column=1)

	def jok_audience_func_false(event):
		pass

	def next_1000(event):
		money_500_button.bind("<Button>",next_1000_false)
		game_1000.run()

	def next_1000_false(event):
		pass


	main = Tk()

	#main setup
	main.title("Tko Želi Biti Milijunaš?")
	main.geometry("800x500+0+0")
	main.config(bg="black") #done
	main.resizable(False,False)

	#frame setup
	left_frame = Frame(main,bg="black",width=600,height=500)
	left_frame.grid(row=0,column=0) #done

	up_frame = Frame(left_frame,bg="black",width=600,height=300)
	up_frame.grid(row=0,column=0) #done

	ans_frame = Frame(left_frame,bg="black",width=600,height=200)
	ans_frame.grid(row=1,column=0) #done

	title_frame = Frame(up_frame,bg="lightblue",width=600,height=50)
	title_frame.grid(row=0,column=0)

	q_frame = Frame(up_frame,bg="black",width=600,height=250)
	q_frame.grid(row=1,column=0)

	ansA_frame = Frame(ans_frame,bg="black",width=300,height=100)
	ansA_frame.grid(row=0,column=0)

	ansB_frame = Frame(ans_frame,bg="black",width=300,height=100)
	ansB_frame.grid(row=0,column=1)

	ansC_frame = Frame(ans_frame,bg="black",width=300,height=100)
	ansC_frame.grid(row=1,column=0)

	ansD_frame = Frame(ans_frame,bg="black",width=300,height=100)
	ansD_frame.grid(row=1,column=1)

	right_frame = Frame(main,bg="black",width=200,height=500)
	right_frame.grid(row=0,column=1) #done

	jok_frame = Frame(right_frame,bg="black",width=200,height=50)
	jok_frame.grid(row=0,column=0) #done

	money_frame = Frame(right_frame,bg="black",width=200,height=450)
	money_frame.grid(row=1,column=0) #done

	jok_50_frame = Frame(jok_frame,bg="black",width=67,height=50)
	jok_50_frame.grid(row=0,column=0)

	jok_friend_frame = Frame(jok_frame,bg="black",width=66,height=50)
	jok_friend_frame.grid(row=0,column=1)

	jok_audience_frame = Frame(jok_frame,bg="black",width=67,height=50)
	jok_audience_frame.grid(row=0,column=2)

	money_1000000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_1000000_frame.grid(row=0,column=0)

	money_500000_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_500000_frame.grid(row=1,column=0)

	money_250000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_250000_frame.grid(row=2,column=0)

	money_125000_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_125000_frame.grid(row=3,column=0)

	money_64000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_64000_frame.grid(row=4,column=0)

	money_32000_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_32000_frame.grid(row=5,column=0)

	money_16000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_16000_frame.grid(row=6,column=0)

	money_8000_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_8000_frame.grid(row=7,column=0)

	money_4000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_4000_frame.grid(row=8,column=0)

	money_2000_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_2000_frame.grid(row=9,column=0)

	money_1000_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_1000_frame.grid(row=10,column=0)

	money_500_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_500_frame.grid(row=11,column=0)

	money_300_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_300_frame.grid(row=12,column=0)

	money_200_frame = Frame(money_frame,bg="lightblue",width=200,height=30)
	money_200_frame.grid(row=13,column=0)

	money_100_frame = Frame(money_frame,bg="black",width=200,height=30)
	money_100_frame.grid(row=14,column=0)

	#label setup
	title_label = Label(title_frame,text="Tko želi biti Milijunaš?",bg="lightblue",fg="black",font="arial 27 bold")
	title_label.config(width=27,height=1)
	title_label.pack()

	money_1000000_label = Label(money_1000000_frame,text="1 000 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_1000000_label.config(width=15,height=1)
	money_1000000_label.pack()

	money_500000_label = Label(money_500000_frame,text="500 000",bg="lightblue",fg="black",font="arial 16 bold")
	money_500000_label.config(width=15,height=1)
	money_500000_label.pack()

	money_250000_label = Label(money_250000_frame,text="250 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_250000_label.config(width=15,height=1)
	money_250000_label.pack()

	money_125000_label = Label(money_125000_frame,text="125 000",bg="lightblue",fg="black",font="arial 16 bold")
	money_125000_label.config(width=15,height=1)
	money_125000_label.pack()

	money_64000_label = Label(money_64000_frame,text="64 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_64000_label.config(width=15,height=1)
	money_64000_label.pack()

	money_32000_label = Label(money_32000_frame,text="32 000",bg="lightblue",fg="black",font="arial 16 bold")
	money_32000_label.config(width=15,height=1)
	money_32000_label.pack()

	money_16000_label = Label(money_16000_frame,text="16 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_16000_label.config(width=15,height=1)
	money_16000_label.pack()

	money_8000_label = Label(money_8000_frame,text="8 000",bg="lightblue",fg="black",font="arial 16 bold")
	money_8000_label.config(width=15,height=1)
	money_8000_label.pack()

	money_4000_label = Label(money_4000_frame,text="4 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_4000_label.config(width=15,height=1)
	money_4000_label.pack()

	money_2000_label = Label(money_2000_frame,text="2 000",bg="lightblue",fg="black",font="arial 16 bold")
	money_2000_label.config(width=15,height=1)
	money_2000_label.pack()

	money_1000_label = Label(money_1000_frame,text="1 000",bg="black",fg="lightblue",font="arial 16 bold")
	money_1000_label.config(width=15,height=1)
	money_1000_label.pack()

	money_500_label = Label(money_500_frame,text="500",bg="lightblue",fg="black",font="arial 16 bold")
	money_500_label.config(width=15,height=1)
	money_500_label.pack()

	money_300_label = Label(money_300_frame,text="300",bg="black",fg="lightblue",font="arial 16 bold")
	money_300_label.config(width=15,height=1)
	money_300_label.pack()

	money_200_label = Label(money_200_frame,text="200",bg="lightblue",fg="black",font="arial 16 bold")
	money_200_label.config(width=15,height=1)
	money_200_label.pack()

	money_100_label = Label(money_100_frame,text="100",bg="black",fg="lightblue",font="arial 16 bold")
	money_100_label.config(width=15,height=1)
	money_100_label.pack()

	#joker buttons setup
	jok_50_button = Button(jok_50_frame,text="50/50",bg="black",fg="lightblue",font="arial 11 bold")
	jok_50_button.config(width=6,height=2)
	jok_50_button.bind("<Button>",jok_50_func)
	jok_50_button.pack()

	jok_audience_button = Button(jok_audience_frame,text="Publika",bg="black",fg="lightblue",font="arial 11 bold")
	jok_audience_button.config(width=7,height=2)
	jok_audience_button.bind("<Button>",jok_audience_func)
	jok_audience_button.pack()

	jok_friend_button = Button(jok_friend_frame,text="Zovi",bg="black",fg="lightblue",font="arial 11 bold")
	jok_friend_button.config(width=6,height=2)
	jok_friend_button.bind("<Button>",jok_friend_func)
	jok_friend_button.pack()

	#game system
	money_500_label.config(fg="red")
	jok_50_used = False

	jok_test_file = open("jok_test.txt","r")
	used_joks = jok_test_file.readlines()
	try:
		if "50" in used_joks[0]:
			jok_50_button.bind("<Button>",jok_50_func_false)
			jok_50_button.config(fg="red")
		if "call" in used_joks[0]:
			jok_friend_button.bind("<Button>",jok_friend_func_false)
			jok_friend_button.config(fg="red")
		if "ask" in used_joks[0]:
			jok_audience_button.bind("<Button>",jok_audience_func_false)
			jok_audience_button.config(fg="red")
	except:
		pass
	jok_test_file.close()

	q = pick(qs)

	ans = []
	wans = wanss[qs.index(q)]
	cans = canss[qs.index(q)]
	for i in wans:
		ans.append(i)
	ans.append(cans)

	ansA = pick(ans)
	ans.remove(ansA)

	ansB = pick(ans)
	ans.remove(ansB)

	ansC = pick(ans)
	ans.remove(ansC)

	ansD = pick(ans)
	ans.remove(ansD)

	q_label = Label(q_frame,text=q,bg="black",fg="lightblue",font="arial 32 bold",wraplength=600)
	q_label.config(width=23,height=5)
	q_label.pack()

	ansA_button = Button(ansA_frame,text="A: "+ansA,bg="black",fg="lightblue",font="arial 22 bold")
	ansA_button.config(width=16,height=2)
	ansA_button.bind("<Button>",ansA_func)
	ansA_button.pack()

	ansB_button = Button(ansB_frame,text="B: "+ansB,bg="black",fg="lightblue",font="arial 22 bold")
	ansB_button.config(width=16,height=2)
	ansB_button.bind("<Button>",ansB_func)
	ansB_button.pack()

	ansC_button = Button(ansC_frame,text="C: "+ansC,bg="black",fg="lightblue",font="arial 22 bold")
	ansC_button.config(width=16,height=2)
	ansC_button.bind("<Button>",ansC_func)
	ansC_button.pack()

	ansD_button = Button(ansD_frame,text="D: "+ansD,bg="black",fg="lightblue",font="arial 22 bold")
	ansD_button.config(width=16,height=2)
	ansD_button.bind("<Button>",ansD_func)
	ansD_button.pack()

	title_label.destroy()

	give_up_button = Button(title_frame,text="Odustani !!",bg="lightblue",fg="black",font="arial 18 bold")
	give_up_button.config(width=39,height=1)
	give_up_button.bind("<Button>",give_up_func)
	give_up_button.pack()

	main.mainloop()