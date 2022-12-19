import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


# creating home page
def my_home():
    class homepage:
        def __init__(self, home):
            self.home = home
            self.home.title("Aragi Hospital Main Menu")
            self.home["bg"] = "light yellow"
            self.home.option_add("*Font", ('Verdana', 12))

            la1 = Label(home, text="Welcome\nAragi Hospital", bg="light yellow", font="Times 36 italic underline bold",
                        width="500", height="2").pack()

            bt1 = Button(home, text="About Us", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle",
                         command=self.about).place(x=140, y=150)
            bt2 = Button(home, text="Our Centres", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.ourcentres).place(x=140, y=210)
            bt3 = Button(home, text="Facilities", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.facility).place(x=140, y=270)
            bt4 = Button(home, text="Laboratory Services", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.lab).place(x=140, y=330)
            bt5 = Button(home, text="Pharmacy", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle",
                         command=self.pharmacy).place(x=140, y=390)
            bt6 = Button(home, text="Medical Packages", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.medical).place(x=140, y=450)
            bt7 = Button(home, text="Contact Us", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.contact).place(x=140, y=510)
            bt8 = Button(home, text="Add New Comment", width="30", height="2", bg="red", activeforeground="blue",
                         cursor="circle", command=self.comment).place(x=600, y=150)
            bt9 = Button(home, text="Exit", width="30", height="2", bg="red", activeforeground="blue", cursor="circle",
                         command=self.exit).place(x=140, y=570)
            bt10 = Button(home, text="Staff Use Only", width="30", height="2", bg="red", activeforeground="blue",
                          cursor="circle", command=self.staff_dtails).place(x=600, y=210)

        # creating about window
        def about(self):
            home.destroy()

            class five:
                def __init__(self, aboutus):
                    self.about = aboutus
                    self.about.title("About Us")
                    self.about['bg'] = 'light yellow'
                    self.about.option_add("*Font", ('Verdana', 12))

                    l1 = Label(aboutus, text="About Us", font="Times 36 italic bold underline",
                               bg="light yellow").pack()

                    T = Text(aboutus, height=8, width=30, font="Times 30", bg="light yellow")
                    T.pack(pady=30)
                    T.insert(END, "Aragi Hospital's origins date back to\n2000."
                                  "We have been providing you\nwith various "
                                  "health services from the\nbeginning."
                                  "But this hospital is now \ngiving priority "
                                  "to covid vaccination.\nOperated under the theme"
                                  " 'This is\nyour hospital',this hospital is a "
                                  "great\nhospital and is your favorite hospital.")
                    T.config(state="disabled")

                    back_button = Button(aboutus, text="Back", width="20", height="2",
                                         bg="red", activeforeground="blue", command=self.home).place(x=420, y=505)

                def home(self):
                    self.about.destroy()
                    my_home()

            about = Tk()
            obj = five(about)
            about.minsize(700, 600)
            about.maxsize(700, 600)
            about.tk.mainloop()

        # creating our centrew window
        def ourcentres(self):
            home.destroy()

            def my_our():
                class six:
                    def __init__(self, our):
                        self.our = our
                        self.our.title("Our Centres")

                        self.our['bg'] = 'light yellow'
                        self.our.option_add("*Font", ('Verdana', 12))

                        la1 = Label(our, text="Our Centres", bg="light yellow", fg="black", width="500", height="1",
                                    font="Times 36 italic underline bold").pack()

                        bt1 = Button(our, text="Covid-19 Vaccination", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.covid).place(x=90, y=100)
                        bt2 = Button(our, text="Admission Unit", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.admission).place(x=90, y=170)
                        bt3 = Button(our, text="OPD - OutPatient Department", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.opd).place(x=90, y=240)
                        bt4 = Button(our, text="Channeling Centre", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.channel).place(x=90, y=310)
                        bt5 = Button(our, text="Dental Unit", width="25", height="2", bg="red", activeforeground="blue",
                                     cursor="circle", command=self.dental).place(x=90, y=380)
                        bt6 = Button(our, text="Heart Centre", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.heart).place(x=90, y=450)
                        bt7 = Button(our, text="Physiotherapy Unit", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.phisio).place(x=90, y=520)
                        bt8 = Button(our, text="Skin Care Centre", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.skin).place(x=90, y=590)
                        bt9 = Button(our, text="Back", width="23", height="2", bg="red", activeforeground="blue",
                                     cursor="circle",
                                     command=self.exit).place(x=550, y=590)

                    # creating covid vaccination centre
                    def covid(self):
                        our.destroy()

                        class eight:
                            def __init__(self, covid):
                                self.covid = covid
                                self.covid.title("Covid-19 Vaccination Centre")

                                self.covid["bg"] = "light yellow"
                                self.covid.option_add("*Font", ('Verdana', 12))

                                Label(self.covid,
                                      text='If you want to get vaccinated,You can find some information here.',
                                      bg="light yellow", fg="black",
                                      width="500", height="1",
                                      font="Times 20 bold").pack()
                                Label(self.covid, text='Covid-19 Vaccination Centre', bg="light yellow", fg="black",
                                      width="500",
                                      height="1",
                                      font="Times 36 italic bold underline").pack()
                                Label(self.covid, text="If you want to get vaccinated , fill out the form below",
                                      font="Times 20 italic bold", width="40",
                                      bg="light yellow").place(x=0, y=515)
                                Label(self.covid, text="1.  Age", width="10", bg="light yellow",
                                      font="Times 15 bold").place(
                                    x=-16,
                                    y=550)
                                Label(self.covid, text="2.  Gender", width="10", bg="light yellow",
                                      font="Times 15 bold").place(
                                    x=0,
                                    y=580)
                                Label(self.covid, text="3.  Although previously infected\nwith Covid-19", width="24",
                                      bg="light yellow",
                                      font="Times 15 bold").place(x=5, y=610)
                                Label(covid, text="4.  Previously covid vaccinated\nor not", width="24",
                                      bg="light yellow",
                                      font="Times 15 bold").place(x=1,
                                                                  y=660)

                                T = Text(self.covid, height=13, width=70, font="Times 20", bg="light yellow")
                                T.pack(pady=10)
                                T.insert(END, "1. What is vaccination?\n"
                                              "It is a simple, safe and effective way of protecting people from harmful diseases by using\nyour"
                                              "body’s natural defenses to build resistance to specific infections and make your\nimmune "
                                              "system stronger.\n"
                                              "\n2. Why do we need a vaccine against COVID-19?\n"
                                              "• Vaccination is important in preventing illness and disease.\n"
                                              "• Sri Lanka has a long and very successful history of disease control and prevention with vaccination.\n"
                                              "• COVID -19 preventive behaviors are extremely important, but disease control with\nbehavior alone has been difficult to achieve.\n"
                                              "• A vaccine together with preventive behaviors may be the only possible exit from this\npandemic.")
                                T.config(state="disabled")

                                gendervar = StringVar()

                                # creating dropdown list
                                self.gender1 = Combobox(self.covid, width=30, textvariable=gendervar)
                                self.gender1.place(x=300, y=590)
                                self.gender1["values"] = ("Male", "Female")

                                prevvar = StringVar()
                                self.prev1 = Combobox(self.covid, width=30, textvariable=prevvar)
                                self.prev1.place(x=300, y=625)
                                self.prev1["values"] = ("Yes", "No")
                                # self.prev1.current(1)

                                vacvar = StringVar()
                                self.vac1 = Combobox(self.covid, width=30, textvariable=vacvar)
                                self.vac1.place(x=300, y=660)
                                self.vac1["values"] = ("Yes", "No")

                                agevar = StringVar()
                                self.age_entry = Entry(self.covid, textvariable=agevar, width="32")
                                self.age_entry.place(x=300, y=560)

                                submit_button = Button(self.covid, text="Submit", width="12", height="2", bg="red",
                                                       activeforeground="blue",
                                                       command=self.getTextInput).place(x=690, y=600)
                                back_button = Button(self.covid, text="Back", width="20", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=660, y=700)

                            def clear(self):
                                self.age_entry.delete(0, "end")
                                self.gender1.delete(0, "end")
                                self.prev1.delete(0, "end")
                                self.vac1.delete(0, "end")

                            # checking users input of covid vaccination centre
                            def getTextInput(self):
                                age = self.age_entry.get()
                                gender = self.gender1.get()
                                prev = self.prev1.get()
                                vac = self.vac1.get()
                                try:
                                    if age == "" and gender == "" and prev == "" and vac == "":
                                        messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.covid)
                                    else:
                                        self.clear()

                                        if prev == "Yes":
                                            messagebox.showwarning("Information", "Important\n"
                                                                                  "Sorry, you can not get the covid vaccine if you have had covid disease before.",
                                                                   parent=self.covid)

                                        elif int(age) < 30:
                                            messagebox.showwarning("Information",
                                                                   "Sorry,You cannot get the Covid vaccine if you are under 30 years of age",
                                                                   parent=self.covid)

                                        elif prev == "No":

                                            if gender == "Male" and vac == "Yes":
                                                messagebox.showinfo("Information",
                                                                    "Go to the first(1) room and see the doctor",
                                                                    parent=self.covid)
                                                Label(self.covid, text="Go to the first(1) room and see the doctor",
                                                      width="33",
                                                      fg="blue",
                                                      bg="light yellow",
                                                      font="Times 15 italic bold").place(x=120, y=720)

                                            elif gender == "Male" and vac == "No":
                                                messagebox.showinfo("Information",
                                                                    "Go to the second room(2) and see the doctor",
                                                                    parent=self.covid)
                                                Label(self.covid, text="Go to the first(2) room and see the doctor",
                                                      width="33",
                                                      fg="blue",
                                                      bg="light yellow",
                                                      font="Times 15 italic bold").place(x=120, y=720)
                                            elif gender == "Female" and vac == "Yes":
                                                messagebox.showinfo("Information",
                                                                    "Go to the third room(3) and see the doctor",
                                                                    parent=self.covid)
                                                Label(self.covid, text="Go to the first(3) room and see the doctor",
                                                      width="33",
                                                      fg="blue",
                                                      bg="light yellow",
                                                      font="Times 15 italic bold").place(x=120, y=720)

                                            elif gender == "Female" and vac == "No":
                                                messagebox.showinfo("Information",
                                                                    "Go to the fourth room(4) and see the doctor",
                                                                    parent=self.covid)
                                                Label(self.covid, text="Go to the first(4) room and see the doctor",
                                                      width="33",
                                                      fg="blue",
                                                      bg="light yellow",
                                                      font="Times 15 italic bold").place(x=120, y=720)

                                            else:
                                                messagebox.showerror("Information",
                                                                     "The data you entered is incorrect\nplease try again",
                                                                     parent=self.covid)

                                        else:
                                            messagebox.showerror("Information",
                                                                 "The data you entered is incorrect\nplease try again",
                                                                 parent=self.covid)
                                except ValueError:
                                    messagebox.showerror("Information", "Enter your age as a number",
                                                         parent=self.covid)

                                except:
                                    messagebox.showerror("Information", "Something Went wrong!!\nPlease Try Again",
                                                         parent=self.covid)

                            def exit(self):
                                self.covid.destroy()
                                my_our()

                        covid = Tk()
                        obj = eight(covid)
                        covid.minsize(1000, 780)
                        covid.maxsize(1000, 780)
                        covid.mainloop()

                    # creating admission centre window
                    def admission(self):
                        self.our.destroy()

                        class nine:
                            def __init__(self, admi):
                                self.admi = admi
                                self.admi.title("Admission Unit")
                                self.admi.option_add("*Font", ('Verdana', 12))

                                self.admi['bg'] = 'light yellow'

                                l1 = Label(self.admi, text="Admission Unit", bg="light yellow", fg="black", width="50",
                                           height="2",
                                           font="Times 36 italic bold underline").pack()

                                text1 = Text(self.admi, height=12, width=50, font="Times 17", bg="light yellow")
                                text1.pack()
                                text1.insert(END, "• We are open 24 hours a day, seven days a week.\n"
                                                  "• We have talented doctors and talented staff.\n"
                                                  "• At Aragi we understand your concerns only too"
                                                  " well.\n  Our 24-hour Admission Unit is equipped with "
                                                  "the latest\n  technology, and is manned by skilled "
                                                  "staff and medical\n  professionals, including surgeons\n"
                                                  "  and anesthetists\n"
                                                  "• We provide consultant-led around-the-clock service with\n  "
                                                  "full resuscitation facilities and designated accommodation\n"
                                                  "  for the reception of accident and emergency patients."
                                                  "\n\nEnter Age for more information")

                                text1.config(state="disabled")

                                la1 = Label(self.admi, text="Age", bg="light yellow", font="Times 20 bold", width="10",
                                            height="2").place(x=0, y=445)

                                age = StringVar()

                                self.age_entry = Entry(self.admi, textvariable=age, width="30")
                                self.age_entry.place(x=145, y=475)

                                submit_button = Button(self.admi, text="Submit", width="8", height="1", bg="red",
                                                       activeforeground="blue", command=self.admi_fun).place(x=495, y=470)
                                back_button = Button(self.admi, text="Back", width="15", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=450, y=550)

                            # checking users input of admission unit
                            def admi_fun(self):
                                age_info = self.age_entry.get()
                                try:
                                    if age_info != "":
                                        if int(age_info) > 12:
                                            Label(self.admi, text="Go to room number three for admission", bg="light yellow",
                                                  fg="blue",
                                                  width="42", height="1",
                                                  font="Times 18 italic bold").place(x=60, y=505)
                                            messagebox.showinfo("Admission Unit Information",
                                                                "Go to room number three for admission",
                                                                parent=self.admi)
                                            self.age_entry.delete(0, "end")
                                        else:
                                            self.a = Label(self.admi,
                                                           text="You go to room number 28 to admit the pediatric ward",
                                                           bg="light yellow",
                                                           fg="blue", width="40", height="1",
                                                           font="Times 18 italic bold").place(x=60, y=505)
                                            messagebox.showinfo("Admission Unit Information",
                                                                "You go to room number 28 to admit the pediatric ward",
                                                                parent=self.admi)
                                            self.age_entry.delete(0, "end")
                                    else:
                                        messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.admi)
                                except ValueError:
                                    messagebox.showerror("Information", "Enter your age as a number",
                                                         parent=self.admi)
                                except:
                                    messagebox.showerror("Information", "Something Went wrong!!\nPlease Try Again",
                                                         parent=self.admi)

                            def exit(self):
                                self.admi.destroy()
                                my_our()

                        admi = Tk()
                        obj = nine(admi)
                        admi.minsize(700, 650)
                        admi.maxsize(700, 650)
                        admi.mainloop()

                    # creating opd window
                    def opd(self):
                        self.our.destroy()

                        class ten:
                            def __init__(self, opd):
                                self.opd = opd
                                self.opd.title("OPD - OutPatient Department")

                                self.opd['bg'] = 'light yellow'
                                self.opd.option_add("*Font", ('Verdana', 12))
                                l1 = Label(opd, text="OPD - OutPatient Department", bg="light yellow", fg="black",
                                           width="500",
                                           height="1",
                                           font="Times 36 italic bold underline").pack()

                                text1 = Text(self.opd, height=23, width=53, font="Times 17", bg="light yellow")
                                text1.pack()
                                text1.insert(END, "At Aragi Hospitals we are concerned about your "
                                                  "welfare no\nmatter what your medical needs may be."
                                                  "Just as we are geared\nto handle all your residential "
                                                  "needs, should you need to stay\nwith us for medical "
                                                  "treatment or investigations, we also take\npride in "
                                                  "being a premier provider of out-patient medical\nservices.\n"
                                                  "\nHow Asiri Out-Patient Department operates\n"
                                                  "\nOur trusted family practice sees to all the day-to-day medical\nneeds of the entire family.\n"

                                                  "\n• Doctors are available 24 hours a day, seven days a week at\n  our OPD facilities\n"
                                                  "• Patients register at the Admission Office\n"
                                                  "• Urgent investigations can be performed by the OPD doctor\n"
                                                  "  • The OPD utilises a triage system that follows Australian\n    guidelines\n"
                                                  "  • Patients are categorised and urgent patients are attended to\n    immediately\n"
                                                  "  • 24-hour on-call system in place\n"
                                                  "  • Interlinked island-wide ambulance service for patient\n    evacuation")

                                text1.config(state="disabled")

                                l3 = Label(self.opd, text="Age", font="Times 16 bold", bg="light yellow", width="5",
                                           height="1").place(
                                    x=150, y=670)
                                l4 = Label(self.opd, text="Gender", font="Times 16 bold", bg="light yellow", width="5",
                                           height="1").place(x=150, y=696)
                                l5 = Label(self.opd,
                                           text="If you would like to receive treatment from us, please fill in the details below",
                                           bg="light yellow",
                                           fg="black", width="80", height="1",
                                           font="Times 14 italic bold").place(x=-40, y=725)

                                age = StringVar()
                                gender = StringVar()
                                # get data from entrybox
                                self.age_entry = Entry(self.opd, textvariable=age, width="32")
                                self.age_entry.place(x=250, y=670)

                                self.gender_entry1 = Combobox(self.opd, width=30, textvariable=gender)
                                self.gender_entry1['values'] = ("Male", "Female")
                                self.gender_entry1.place(x=250, y=700)

                                submit_button = Button(self.opd, text="Submit", width="10", height="2", bg="red",
                                                       activeforeground="blue",
                                                       command=self.admigetinfo).place(x=630, y=670)
                                back_button = Button(self.opd, text="Back", width="15", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=600, y=750)

                            def clear(self):
                                self.age_entry.delete(0, "end")
                                self.gender_entry1.delete(0, "end")

                            # get data and check and show them to information
                            def admigetinfo(self):
                                age_info = self.age_entry.get()
                                gender_info = str(self.gender_entry1.get())

                                try:
                                    if age_info == "" or gender_info == "":
                                        messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.opd)

                                    else:
                                        self.clear()
                                        if int(age_info) <= 12:
                                            if gender_info == "Male":
                                                Label(self.opd,
                                                      text="Go to room 5 to go to the pediatric ward because you are {} years old".format(
                                                          age_info),
                                                      font="Times 14 bold", bg="light yellow", fg="blue", width="52",
                                                      height="1").place(x=5,
                                                                        y=755)
                                                messagebox.showinfo("Information",
                                                                    "Go to room 5 to go to the pediatric ward because you are {} years old".format(
                                                                        age_info), parent=self.opd)

                                            elif gender_info == "Female":
                                                Label(self.opd,
                                                      text="Go to room 6 to go to the pediatric ward because you are {} years old".format(
                                                          age_info),
                                                      font="Times 14 bold", bg="light yellow", fg="blue", width="52",
                                                      height="1").place(x=5,
                                                                        y=755)
                                                messagebox.showinfo("Information",
                                                                    "Go to room 6 to go to the pediatric ward because you are {} years old".format(
                                                                        age_info), parent=self.opd)

                                            else:
                                                messagebox.showwarning("Information",
                                                                       "Please enter your gender and try again",
                                                                       parent=self.opd)

                                        else:
                                            if gender_info == "Male":
                                                Label(self.opd, text="Go to room 7 to see your doctor",
                                                      font="Times 14 bold",
                                                      bg="light yellow", fg="blue", width="52", height="1").place(x=5,
                                                                                                                  y=755)
                                                messagebox.showinfo("Information", "Go to room 7 to see your doctor",
                                                                    parent=self.opd)

                                            elif gender_info == "Female":
                                                Label(self.opd, text="Go to room 8 to see your doctor",
                                                      font="Times 14 bold",
                                                      bg="light yellow", fg="blue", width="52", height="1").place(x=5,
                                                                                                                  y=755)
                                                messagebox.showinfo("Information", "Go to room 8 to see your doctor",
                                                                    parent=self.opd)

                                            else:
                                                messagebox.showerror("Information",
                                                                     "Please enter your gender and try again",
                                                                     parent=self.opd)
                                except ValueError:
                                    messagebox.showerror("Information", "Enter your age as a number",
                                                         parent=self.opd)

                                except:
                                    messagebox.showerror("Information", "Something Went wrong!!\nPlease Try Again",
                                                         parent=self.opd)

                            def exit(self):
                                self.opd.destroy()
                                my_our()

                        opd = Tk()
                        obj = ten(opd)
                        opd.minsize(800, 800)
                        opd.maxsize(800, 800)
                        opd.mainloop()

                    # creating channeling centre window
                    def channel(self):
                        self.our.destroy()

                        class eleven:
                            def __init__(self, channel):
                                self.channel = channel
                                self.channel.title("Channeling Centre")

                                self.channel['bg'] = 'light yellow'

                                self.channel.option_add("*Font", ('Verdana', 18))
                                l1 = Label(self.channel, text="Click Here", bg="light yellow", fg="black", width="20",
                                           height="1",
                                           font="Times 30 italic bold").place(x=60, y=10)

                                l2 = Label(self.channel,
                                           text="If you want to see the doctors in the above\nunits call our phone number and make\nan appointment and get a number\nContact No : 0112500500",
                                           bg="light yellow", fg="black", width="32", height="4",
                                           font="Times 25 italic").place(
                                    x=20,
                                    y=60)
                                l3 = Label(self.channel, text="Channeling Centre", bg="light yellow", fg="black",
                                           width="20",
                                           height="1",
                                           font="Times 36 italic bold underline").place(x=42, y=215)

                                # doctors name list
                                dr_name_list = ["Dr. Aruna Munasinghe", "Dr. Kasun Perera", "Dr. Champa Jayamanna",
                                                "Dr. Chanaka Peiris",
                                                "Dr. Palitha Gunawardhana", "Dr.Lanka Adikari",
                                                "Dr. Sampath Jayathilake",
                                                "Dr. Nadeera Jayawardhana", "Dr. Wasantha Kapuwatta",
                                                "Dr. Chandrika Jayasinghe",
                                                "Mr. Amantha Silva", "Mrs. Gihani Kumarasinghe",
                                                "Dr. Dhammika Dissanayake",
                                                "Dr. Nishantha Dolawatta"]

                                centre_list = ["Consultant Physician", "Dental Surgeon", "Consultant Cardiologist",
                                               "Physiotherapist",
                                               "Consultant Plastic Surgeon", ]

                                days = ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                                        "Sunday"]

                                channel_menu = Menu(self.channel)

                                # craeting menubar
                                menu1 = Menu(channel_menu, tearoff=0, bg="cyan")
                                channel_menu.add_cascade(label=centre_list[0], menu=menu1)

                                # adding a command
                                menu1.add_command(label=dr_name_list[0],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 9 every {} at 7 am"
                                                                                      .format(centre_list[0],
                                                                                              dr_name_list[0],
                                                                                              days[0]),
                                                                                      parent=self.channel))
                                menu1.add_separator()
                                menu1.add_command(label=dr_name_list[1],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 10 every {} at 10 am"
                                                                                      .format(centre_list[0],
                                                                                              dr_name_list[1],
                                                                                              days[3]),
                                                                                      parent=self.channel))
                                menu1.add_separator()
                                menu1.add_command(label=dr_name_list[2],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 11 every {} at 7 pm"
                                                                                      .format(centre_list[0],
                                                                                              dr_name_list[2],
                                                                                              days[5]),
                                                                                      parent=self.channel))
                                menu1.add_separator()
                                menu1.add_command(label=dr_name_list[3],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 12 every {} at 9 am"
                                                                                      .format(centre_list[0],
                                                                                              dr_name_list[3],
                                                                                              days[5]),
                                                                                      parent=self.channel))
                                menu1.add_separator()
                                menu1.add_command(label=dr_name_list[4],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 13 every {} at 11 am"
                                                                                      .format(centre_list[0],
                                                                                              dr_name_list[4],
                                                                                              days[4]),
                                                                                      parent=self.channel))
                                menu1.add_separator()

                                menu2 = Menu(channel_menu, tearoff=0, bg="cyan")
                                channel_menu.add_cascade(label=centre_list[1], menu=menu2)

                                menu2.add_command(label=dr_name_list[5],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 14 every {} at 6.30 am"
                                                                                      .format(centre_list[1],
                                                                                              dr_name_list[5],
                                                                                              days[1]),
                                                                                      parent=self.channel))
                                menu2.add_separator()
                                menu2.add_command(label=dr_name_list[6],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 15 every {} at 7 pm"
                                                                                      .format(centre_list[1],
                                                                                              dr_name_list[6],
                                                                                              days[0]),
                                                                                      parent=self.channel))
                                menu2.add_separator()
                                menu2.add_command(label=dr_name_list[7],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 16 every {} at 8 pm"
                                                                                      .format(centre_list[1],
                                                                                              dr_name_list[7],
                                                                                              days[2]),
                                                                                      parent=self.channel))
                                menu2.add_separator()

                                menu3 = Menu(channel_menu, tearoff=0, bg="cyan")
                                channel_menu.add_cascade(label=centre_list[2], menu=menu3)

                                menu3.add_command(label=dr_name_list[8],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 17 every {} at 10 am"
                                                                                      .format(centre_list[2],
                                                                                              dr_name_list[8],
                                                                                              days[3]),
                                                                                      parent=self.channel))
                                menu3.add_separator()
                                menu3.add_command(label=dr_name_list[9],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 18 every {} at 7 am"
                                                                                      .format(centre_list[2],
                                                                                              dr_name_list[9],
                                                                                              days[2]),
                                                                                      parent=self.channel))
                                menu3.add_separator()

                                menu4 = Menu(channel_menu, tearoff=0, bg="cyan")
                                channel_menu.add_cascade(label=centre_list[3], menu=menu4)

                                menu4.add_command(label=dr_name_list[10],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 19 every {} at 8 am"
                                                                                      .format(centre_list[3],
                                                                                              dr_name_list[10],
                                                                                              days[1]),
                                                                                      parent=self.channel))
                                menu4.add_separator()
                                menu4.add_command(label=dr_name_list[11],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 20 every {} at 5 pm"
                                                                                      .format(centre_list[3],
                                                                                              dr_name_list[11],
                                                                                              days[4]),
                                                                                      parent=self.channel))
                                menu4.add_separator()

                                menu5 = Menu(channel_menu, tearoff=0, bg="cyan")
                                channel_menu.add_cascade(label=centre_list[4], menu=menu5)

                                menu5.add_command(label=dr_name_list[12],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 9 every {} at 1 pm"
                                                                                      .format(centre_list[4],
                                                                                              dr_name_list[12],
                                                                                              days[6]),
                                                                                      parent=self.channel))
                                menu5.add_separator()
                                menu5.add_command(label=dr_name_list[13],
                                                  command=lambda: messagebox.showinfo("Information-Channeling Centre",
                                                                                      "{} {} visits room number 9 every {} at 3 pm"
                                                                                      .format(centre_list[4],
                                                                                              dr_name_list[13],
                                                                                              days[5]),
                                                                                      parent=self.channel))
                                menu5.add_separator()

                                channel.config(menu=channel_menu)

                                back_button = Button(self.channel, text="Back", width="10", height="1", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=400, y=286)

                            def exit(self):
                                self.channel.destroy()
                                my_our()

                        channel = Tk()
                        bj = eleven(channel)
                        channel.minsize(620, 350)
                        channel.maxsize(620, 350)
                        channel.mainloop()

                    # creating dental unit window
                    def dental(self):
                        self.our.destroy()

                        class denta:
                            def __init__(self, dent):
                                self.dent = dent

                                self.dent.title("Dental Unit")
                                self.dent["bg"] = "light yellow"
                                self.dent.option_add("*Font", ('Verdana', 12))

                                l1 = Label(self.dent, text="Dental Unit", font="Times 36 italic underline bold",
                                           bg="light yellow").pack()

                                T = Text(self.dent, height=11, width=35, font="Times 22 italic bold", bg="light yellow")
                                T.pack(pady=30)
                                T.insert(END, "The Dental Unit of Aragi Hospital is\ncommitted to delivering "
                                              "a high level of care\nto all patients. A full range of oral care \nservices "
                                              "for patients off all age groups are\nthree by offered by a team "
                                              "of well experien--ced medical personnel.\n"
                                              "In line with the patient centric policy\n"
                                              "adopted by the hospital, the best and "
                                              "most\nmodern equipment has been invested on to\n"
                                              "ensure that you will have the best service\nat all times.")
                                T.config(state="disabled")

                                back_button = Button(self.dent, text="Back", width="20", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=275, y=500)

                            def exit(self):
                                self.dent.destroy()
                                my_our()

                        dent = Tk()
                        o = denta(dent)
                        dent.minsize(600, 600)
                        dent.maxsize(600, 600)
                        dent.tk.mainloop()

                    # creating heart centre window
                    def heart(self):
                        self.our.destroy()

                        class heartcen:
                            def __init__(self, heart):
                                self.heart = heart
                                self.heart.title("Heart Centre")
                                self.heart["bg"] = "light yellow"
                                self.heart.option_add("*Font", ('Verdana', 12))

                                l1 = Label(self.heart, text="Heart Centre", font="Times 36 italic bold underline",
                                           bg="light yellow").pack(pady=11)

                                T = Text(self.heart, height=7, width=30, font="Times 23 italic bold", bg="light yellow")
                                T.pack(pady=10)
                                T.insert(END, "Aragi Heart Centre is "
                                              "renowned to\nbe nmost trusted"
                                              "place for matter of\nthe heart."
                                              "We provide comprehensive\n"
                                              "cardiac care from state-of-theart\n"
                                              "Heart Screening Packages to Bypass\nSurgery."
                                              "Trust us with you heart\nand we will "
                                              "take good care of it.")
                                T.config(state="disabled")

                                back_button = Button(self.heart, text="Back", width="20", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=215, y=385)

                            def exit(self):
                                self.heart.destroy()
                                my_our()

                        heart = Tk()
                        o = heartcen(heart)
                        heart.minsize(500, 490)
                        heart.maxsize(500, 490)
                        heart.tk.mainloop()

                    # craeting phisiotherophy unit window
                    def phisio(self):
                        self.our.destroy()

                        class phisi:
                            def __init__(self, phi):
                                self.phi = phi

                                self.phi.title("Physiotherapy Unit")
                                self.phi['bg'] = 'light yellow'
                                self.phi.option_add("*Font", ('Verdana', 12))

                                l1 = Label(self.phi, text="Physiotherapy Unit", font="Times 36 italic bold",
                                           bg="light yellow").pack(
                                    pady=11)

                                T = Text(self.phi, height=8, width=27, font="Times 25 italic", bg="light yellow")
                                T.pack()
                                T.insert(END, "Physiotherapy is the "
                                              "treatment of\nany disease; "
                                              " deformity or malfu-\n-nctions, "
                                              "by distinct therapeutic "
                                              "measures like massages, "
                                              "exercises,\nheat, etc. "
                                              "Over the years this has\n"
                                              "gained vast acceptance as "
                                              "a\nsophisticated and "
                                              "essential\nmedical technology.")
                                T.config(state="disabled")

                                back_button = Button(self.phi, text="Back", width="18", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=245, y=418)

                            def exit(self):
                                self.phi.destroy()
                                my_our()

                        phi = Tk()
                        o = phisi(phi)
                        phi.minsize(500, 500)
                        phi.maxsize(500, 500)
                        phi.tk.mainloop()

                    # creating skincare centre window
                    def skin(self):
                        self.our.destroy()

                        class skincen:
                            def __init__(self, skin):
                                self.skin = skin

                                self.skin.title("Skin Care Centre")
                                self.skin['bg'] = 'light yellow'
                                self.skin.option_add("*Font", ('Verdana', 12))

                                l1 = Label(skin, text="Skin Care Centre", font="Times 36 italic underline bold",
                                           bg="light yellow").pack()

                                T = Text(skin, height=10, width=35, font="Times 20", bg="light yellow")
                                T.pack(pady=20)
                                T.insert(END, " The skin is the largest "
                                              "organ of your body.\nIt’s "
                                              "your visible health detector,"
                                              "and it’s very\nmuch a part "
                                              "of your individuality.And yet.\n"
                                              "Aragi Skin Care and Cosmetic Centre is\n"
                                              "perfectly equipped to deal with these issues.\n"
                                              "From making you look younger through skin\n"
                                              "rejuvenation, permanent hair removal, "
                                              "scar\nremoval, hair transplants, plastic surgeries\n"
                                              "and eye cosmetic treatments, coupled with\nthe "
                                              "best of medical technology.")
                                T.config(state="disabled")

                                back_button = Button(skin, text="Back", width="18", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=300, y=425)

                            def exit(self):
                                self.skin.destroy()
                                my_our()

                        skin = Tk()
                        m = skincen(skin)
                        skin.minsize(600, 500)
                        skin.maxsize(600, 500)
                        skin.tk.mainloop()

                    def exit(self):
                        self.our.destroy()
                        my_home()

                our = Tk()
                obj = six(our)
                our.minsize(900, 700)
                our.maxsize(900, 700)
                our.mainloop()

            my_our()

        # creating facility window
        def facility(self):
            home.destroy()

            class faci:
                def __init__(self, fac):
                    self.fac = fac

                    self.fac.title("Facilities")
                    self.fac["bg"] = "light yellow"
                    self.fac.option_add("*Font", ('Verdana', 12))

                    l1 = Label(fac, text="Facilities", font="Times 36 italic bold underline", bg="light yellow").pack(
                        pady=25)

                    T = Text(fac, height=15, width=50, font="Times 18", bg="light yellow")
                    T.pack()
                    T.insert(END, "  • ROOM FACILITIES\n"
                                  "To make a hospital stay more comfortable we arrange extras\n"
                                  "and cater to any special dietary requirements, so that you and\n"
                                  "your visitors feel at home.\n"
                                  "\n  • BANKING & ATM FACILITIES\n"
                                  "Easy access to money is guaranteed thanks to a branch of "
                                  "the Bank of Ceylon with an ATM that is located within the\n"
                                  "hospital premises\n"
                                  "\n  • FOOD & BEVERAGES\n"
                                  "Along with a food safety management system, modern kitchen"
                                  "and the freshest ingredients our food surpasses standard\n"
                                  "hospital food, which is why we have been rated excellent in\n"
                                  "meeting international standards in food quality and hygiene.")
                    T.config(state="disabled")

                    back_button = Button(fac, text="Back", width="20", height="2",
                                         bg="red", activeforeground="blue", command=self.exit).place(x=440, y=555)

                def exit(self):
                    self.fac.destroy()
                    my_home()

            fac = Tk()
            p = faci(fac)
            fac.minsize(700, 650)
            fac.maxsize(700, 650)
            fac.tk.mainloop()

        # creating lab services window
        def lab(self):
            home.destroy()

            class LAB:
                def __init__(self, lab):
                    self.lab = lab
                    self.lab.title("Laboratory Services")
                    self.lab["bg"] = "light yellow"
                    self.lab.option_add("*Font", ('Verdana', 12))

                    l1 = Label(lab, text="Laboratory Services", font="Times 38 italic bold underline",
                               bg="light yellow").pack()

                    T = Text(lab, height=15, width=42, font="Times 28", bg="light yellow")
                    T.pack(pady=22)
                    T.insert(END, "Over the last 20 years Aragi Laboratories"
                                  " has built a\nreputation for accuracy and"
                                  " dependability. Using the\nmost modern, "
                                  "fast and accurate analysers in the world, "
                                  "\nAragi Laboratories conducts internal quality "
                                  "control on\nall its machines daily. It also "
                                  "ensures external quality\ncontrol by working "
                                  "closely with a reputed international\nlaboratories."
                                  " All this means faster and reliable results\nfor all"
                                  " your medical tests.\n"
                                  "               Common Tests\n"
                                  "•  Blood Testing & Blood Disorders\n"
                                  "•  Allergy Testing\n"
                                  "•  Vitamin & Nutritional Tests\n"
                                  "•  Diabetes Testing\n"
                                  "•  Kidney & liver Tests\n"
                                  "•  Hormone & Adrenal Testing\n"
                                  "•  Other Tests")
                    T.config(state="disabled")

                    back_button = Button(lab, text="Back", width="20", height="2",
                                         bg="red", activeforeground="blue", command=self.exit).place(x=650, y=740)

                def exit(self):
                    self.lab.destroy()
                    my_home()

            lab = Tk()
            obj = LAB(lab)
            lab.minsize(900, 800)
            lab.maxsize(900, 800)
            lab.tk.mainloop()

        # craeting pharmacy window
        def pharmacy(self):
            home.destroy()

            class pharma:
                def __init__(self, pharm):
                    self.pharm = pharm

                    self.pharm.title("Pharmacy")
                    self.pharm["bg"] = "light yellow"
                    self.pharm.option_add("*Font", ('Verdana', 12))

                    l1 = Label(pharm, text="Pharmacy", font="Times 36 italic bold underline", bg="light yellow").pack(
                        pady=18)

                    T = Text(pharm, height=12, width=35, font="Times 28", bg="light yellow")
                    T.pack()
                    T.insert(END, "The pharmacy is the one place where all our\n"
                                  "patients converge at some point or the other\n"
                                  "during a visit to Aragi Hospitals and that is\n"
                                  "why we ensure that all Aragi Pharmacies are\n"
                                  "well stocked with products that match the\nmost "
                                  "stringent international standards, and\nmanned "
                                  "by efficient, qualified personnel.The\nAragi"
                                  "Pharmacy is open 24 hours a day, seven\ndays a"
                                  "week. It sells over-the-counter (OTC)\n"
                                  "products, prescription-only medicine (POM)\nand "
                                  "surgical products at Government\napproved prices.")
                    T.config(state="disabled")

                    back_button = Button(pharm, text="Back", width="17", height="2",
                                         bg="red", activeforeground="blue", command=self.exit).place(x=455, y=625)

                def exit(self):
                    self.pharm.destroy()
                    my_home()

            pharm = Tk()
            obj = pharma(pharm)
            pharm.minsize(700, 700)
            pharm.maxsize(700, 700)
            pharm.tk.mainloop()

        # creating medical packages main window
        def medical(self):
            home.destroy()

            def my_mrdi():
                class medical:
                    def __init__(self, medi):
                        self.medi = medi

                        medi.title("Medical Packages")

                        medi['bg'] = 'light yellow'
                        medi.option_add("*Font", ('Verdana', 12))

                        la1 = Label(medi, text="Medical Packages", bg="light yellow",
                                    font="Times 36 italic underline bold",
                                    width="500", height="2").pack()

                        bt1 = Button(medi, text="Senior Citizens Package", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.sen).place(x=100, y=130)
                        bt2 = Button(medi, text="Covid Vaccination Package", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.vac).place(x=100, y=210)
                        bt3 = Button(medi, text="Skin Care packages", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.skin).place(x=100, y=290)
                        bt4 = Button(medi, text="Other Medical Packages", width="25", height="2", bg="red",
                                     activeforeground="blue",
                                     cursor="circle", command=self.other).place(x=100, y=370)
                        bt5 = Button(medi, text="Back", width="25", height="2", bg="red", activeforeground="blue",
                                     cursor="circle",
                                     command=self.exit).place(x=475, y=370)

                    def exit(self):
                        self.medi.destroy()
                        my_home()

                    # creating senior citizen packages window
                    def sen(self):
                        self.medi.destroy()

                        class senior:
                            def __init__(self, sen):

                                self.sen = sen
                                sen.title("Senior Citizens Package")

                                sen['bg'] = 'light yellow'
                                sen.option_add("*Font", ('Verdana', 12))
                                la1 = Label(sen, text="Senior Citizens Package", bg="light yellow",
                                            font="Times 36 italic bold underline",
                                            width="50", height="2").pack()
                                la2 = Label(sen, text="Select Here", bg="light yellow", font="Times 18 bold",
                                            width="10",
                                            height="2").place(x=10,
                                                              y=350)

                                T = Text(sen, height=7, width=37, font="Times 20 bold", bg="light yellow")
                                T.pack(pady=10)
                                T.insert(END, "1.Full Blood Count\n"
                                              "2.Fasting Blood Sugar\n"
                                              "3.ECG\n"
                                              "4.Hearing Test\n"
                                              "\n"
                                              "You must select three or four services\n"
                                              "Select your Option/s Below")
                                T.config(state="disabled")

                                medical = StringVar()
                                self.medical_entry = Combobox(sen, width=27, textvariable=medical)
                                self.medical_entry.place(x=155, y=368)
                                self.medical_entry['values'] = ("1,2,3", "2,3,4", "1,3,4", "1,2,4", "1,2,3,4")

                                submit_button = Button(sen, text="Submit", width="8", height="1", bg="red",
                                                       activeforeground="blue",
                                                       command=self.senioorr).place(x=480, y=365)
                                back_button = Button(sen, text="Back", width="17", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=320, y=437)

                            def exit(self):
                                self.sen.destroy()
                                my_mrdi()

                            # claer data which user inputs
                            def clear(self):
                                self.medical_entry.delete(0, "end")

                            # shows user to informatin about senior citizen pckg
                            def senioorr(self):
                                medical_info = self.medical_entry.get()

                                self.clear()

                                packages = [1000, 300, 800, 2800]
                                pn = ["Full Blood Count", "Fasting Blood Sugar", "ECG", "Hearing Test"]

                                if medical_info == "":
                                    messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.sen)

                                else:
                                    if medical_info == "1,2,3":
                                        s = sum(packages[0:3])
                                        display1 = 'Your package includes {}'.format(pn[0:3])
                                        display2 = 'The price of your medical package is {} rupees.'.format(s)
                                        display3 = display1 + "\n" + display2
                                        Label(sen, text=display3, bg="light yellow", font="Times 10 italic bold",
                                              fg="blue",
                                              width="72",
                                              height="2").place(x=15,
                                                                y=398)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.sen)

                                    elif medical_info == "2,3,4":
                                        s = sum(packages[1:])
                                        display1 = 'Your package includes {}'.format(pn[1:])
                                        display2 = 'The price of your medical package is {} rupees.'.format(s)
                                        display3 = display1 + "\n" + display2
                                        Label(sen, text=display3, bg="light yellow", font="Times 10 italic bold",
                                              fg="blue",
                                              width="72",
                                              height="2").place(x=15,
                                                                y=398)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.sen)

                                    elif medical_info == "1,3,4":
                                        s = sum(packages[2:]) + 1000
                                        display1 = 'Your package includes {} , {} and {}'.format(pn[0], pn[2], pn[3])
                                        display2 = 'The price of your medical package is {} rupees.'.format(s)
                                        display3 = display1 + "\n" + display2
                                        Label(sen, text=display3, bg="light yellow", font="Times 10 italic bold",
                                              fg="blue",
                                              width="72",
                                              height="2").place(x=15,
                                                                y=398)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.sen)

                                    elif medical_info == "1,2,4":
                                        s = sum(packages[0:2]) + 2800
                                        display1 = 'Your package includes {} , {} and {}'.format(pn[0], pn[1], pn[3])
                                        display2 = 'The price of your medical package is {} rupees.'.format(s)
                                        display3 = display1 + "\n" + display2
                                        Label(sen, text=display3, bg="light yellow", font="Times 10 italic bold",
                                              fg="blue",
                                              width="72",
                                              height="2").place(x=15,
                                                                y=398)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.sen)

                                    elif medical_info == "1,2,3,4":
                                        s = sum(packages)
                                        display1 = 'Your package includes {}'.format(pn[0:])
                                        display2 = 'The price of your medical package is {} rupees.'.format(s)
                                        display3 = display1 + "\n" + display2
                                        Label(sen, text=display3, bg="light yellow", font="Times 10 italic bold",
                                              fg="blue",
                                              width="72",
                                              height="2").place(x=15,
                                                                y=398)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.sen)

                                    else:
                                        messagebox.showerror("Your Package Details",
                                                             "The {} data you entered is incorrect".format(
                                                                 medical_info),
                                                             parent=self.sen)

                        sen = Tk()
                        org = senior(sen)
                        sen.minsize(600, 500)
                        sen.maxsize(600, 500)
                        sen.tk.mainloop()

                    # covid vaccination centre
                    def vac(self):
                        self.medi.destroy()

                        class covid_med:
                            def __init__(self, comed):
                                self.comed = comed
                                self.comed.title("Covid-19 Vaccination Package")
                                self.comed['bg'] = "light yellow"
                                self.comed.option_add("*Font", ('Verdana', 12))
                                la1 = Label(comed, text="Covid-19 Vaccination Package", bg="light yellow",
                                            font="Times 30 italic bold underline",
                                            width="50",
                                            height="2").pack()
                                la2 = Label(comed, text="Do you pay for both injections\nat once? (Yes / No)",
                                            bg="light yellow",
                                            font="Times 12 bold", width="22", height="3").place(x=12, y=369)
                                la3 = Label(comed,
                                            text="What vaccine would you like\nto get vaccinated?\nEnter the vaccine number you prefer",
                                            bg="light yellow", font="Times 10 bold", width="29", height="3").place(x=10,
                                                                                                                   y=420)

                                T = Text(comed, height=9, width=45, font="Times 18 bold", bg="light yellow")
                                T.pack(pady=10)
                                T.insert(END, "The following are the types of Covid-19 vaccines\n"
                                              "\n1. Sputnik-V Vaccine - Russia\n"
                                              "2. Pfizer Vaccine - America\n"
                                              "3. AstraZeneca Vaccine - India\n"
                                              "4. Sinopharm Vaccine - China\n"
                                              "\nFill out the form below to find out more about the"
                                              "\ncovid-19 package")
                                T.config(state="disabled")

                                both_vacc = StringVar()
                                name = StringVar()

                                self.vac1 = Combobox(comed, width=30, textvariable=both_vacc)
                                self.vac1.place(x=230, y=390)
                                self.vac1["values"] = ("Yes", "No")

                                self.name_entry = Combobox(comed, width=30, textvariable=name)
                                self.name_entry.place(x=230, y=440)
                                self.name_entry["values"] = (
                                    "Sputnik-V Vaccine - Russia", "Pfizer Vaccine - America",
                                    "AstraZeneca Vaccine - India",
                                    "Sinopharm Vaccine - China")

                                submit_button = Button(comed, text="Submit", width="15", height="2", bg="red",
                                                       activeforeground="blue",
                                                       command=self.covid_medi).place(x=265, y=475)
                                back_button = Button(comed, text="Back", width="15", height="2", bg="red",
                                                     activeforeground="blue",
                                                     command=self.exit).place(x=480, y=530)

                            def exit(self):
                                self.comed.destroy()
                                my_mrdi()

                            # claer user's inputs
                            def clear(self):
                                self.vac1.delete(0, "end")
                                self.name_entry.delete(0, "end")

                            # calculate covid vaccine package
                            def covid_medi(self):
                                medlist = {"Sputnik-V Vaccine - Russia": 6000, "Pfizer Vaccine - America": 6500,
                                           "AstraZeneca Vaccine - India": 7000, "Sinopharm Vaccine - China": 4500}

                                vacc_info = str(self.vac1.get())
                                name_info = str(self.name_entry.get())

                                self.clear()
                                if vacc_info == "" or name_info == "":
                                    messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.comed)
                                else:
                                    if vacc_info == "Yes":
                                        if name_info == "Sputnik-V Vaccine - Russia":
                                            p = lambda a, b, c, d: (a * b) - (c * d)
                                            display = p(medlist["Sputnik-V Vaccine - Russia"], 2,
                                                        medlist["Sputnik-V Vaccine - Russia"],
                                                        0.05)
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package\nis only {} rupees"
                                                  .format(format(display, ".2f")), bg="light yellow", fg="blue",
                                                  font="Times 13 ",
                                                  width="27",
                                                  height="4").place(x=10,
                                                                    y=470)

                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly {} rupees"
                                                                .format(format(display, ".2f")), parent=self.comed)

                                        elif name_info == "Pfizer Vaccine - America":
                                            p = lambda a, b, c, d: (a * b) - (c * d)
                                            display2 = p(medlist["Pfizer Vaccine - America"], 2,
                                                         medlist["Pfizer Vaccine - America"],
                                                         0.05)
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package\nis only {} rupees"
                                                  .format(format(display2, ".2f")), bg="light yellow", fg="blue",
                                                  font="Times 13 ",
                                                  width="27",
                                                  height="4").place(x=10,
                                                                    y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly {} rupees"
                                                                .format(format(display2, ".2f")), parent=self.comed)

                                        elif name_info == "AstraZeneca Vaccine - India":
                                            p = lambda a, b, c, d: (a * b) - (c * d)
                                            display3 = p(medlist["AstraZeneca Vaccine - India"], 2,
                                                         medlist["AstraZeneca Vaccine - India"],
                                                         0.05)
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package\nis only {} rupees"
                                                  .format(format(display3, ".2f")), bg="light yellow", fg="blue",
                                                  font="Times 13 ",
                                                  width="27",
                                                  height="4").place(x=10,
                                                                    y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly {} rupees"
                                                                .format(format(display3, ".2f")), parent=self.comed)

                                        elif name_info == "Sinopharm Vaccine - China":
                                            p = lambda a, b, c, d: (a * b) - (c * d)
                                            display4 = p(medlist["Sinopharm Vaccine - China"], 2,
                                                         medlist["Sinopharm Vaccine - China"],
                                                         0.05)
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package\nis only {} rupees"
                                                  .format(format(display4, ".2f")), bg="light yellow", fg="blue",
                                                  font="Times 13 ",
                                                  width="27",
                                                  height="4").place(x=10,
                                                                    y=470)

                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly {} rupees"
                                                                .format(format(display4, ".2f")), parent=self.comed)

                                        else:
                                            messagebox.showerror("Your Package Details",
                                                                 "Sorry!!\nThe vaccine name entered is incorrect\nPlease try again",
                                                                 parent=self.comed)

                                    elif vacc_info == "No":
                                        if name_info == "Sputnik-V Vaccine - Russia":
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 6000 rupees",
                                                  bg="light yellow", fg="blue"
                                                  , font="Times 12", width="27", height="4").place(x=10, y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 6000 rupees",
                                                                parent=self.comed)

                                        elif name_info == "Pfizer Vaccine - America":
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 6500 rupees",
                                                  bg="light yellow", fg="blue"
                                                  , font="Times 12", width="27", height="4").place(x=10, y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 6500 rupees",
                                                                parent=self.comed)

                                        elif name_info == "AstraZeneca Vaccine - India":
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 7000 rupees",
                                                  bg="light yellow", fg="blue", font="Times 12", width="27",
                                                  height="4").place(x=10, y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 7000 rupees",
                                                                parent=self.comed)

                                        elif name_info == "Sinopharm Vaccine - China":
                                            Label(comed,
                                                  text="Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 4500 rupees",
                                                  bg="light yellow", fg="blue", font="Times 12", width="27",
                                                  height="4").place(x=10, y=470)
                                            messagebox.showinfo("Your Package Details",
                                                                "Congratulations!!\nYour Covid-19 Vaccination Package is\nonly 4500 rupees",
                                                                parent=self.comed)

                                        else:
                                            messagebox.showerror("Your Package Details",
                                                                 "Sorry!!\nThe vaccine name entered is incorrect.\nPlease try again",
                                                                 parent=self.comed)

                                    else:
                                        messagebox.showerror("Your Package Details",
                                                             "Sorry!!\nThe data entered is incorrect.\nPlease try again",
                                                             parent=self.comed)

                        comed = Tk()
                        org = covid_med(comed)
                        comed.minsize(700, 600)
                        comed.maxsize(700, 600)
                        comed.tk.mainloop()

                    # creating skin care package
                    def skin(self):
                        self.medi.destroy()

                        class skin_care:
                            def __init__(self, health):

                                self.health = health
                                self.health.title("Skin Care Package")

                                self.health['bg'] = 'light yellow'
                                self.health.option_add("*Font", ('Verdana', 12))

                                la1 = Label(health, text="Skin Care Package", bg="light yellow",
                                            font="Times 36 italic bold underline",
                                            width="30",
                                            height="1").pack()
                                la2 = Label(health, text="Select the number of products you like below",
                                            bg="light yellow",
                                            font="Times 26 bold", width="33",
                                            height="2").pack()
                                la3 = Label(health, text="Serum & Essence", bg="light yellow",
                                            font="Times 20 bold italic",
                                            width="33",
                                            height="1").place(x=75,
                                                              y=190)
                                la4 = Label(health, text="Face mask & Packs", bg="light yellow",
                                            font="Times 20 bold italic",
                                            width="33", height="1").place(
                                    x=75, y=290)
                                la5 = Label(health, text="Facial Cleansers", bg="light yellow",
                                            font="Times 20 bold italic",
                                            width="33",
                                            height="1").place(x=75,
                                                              y=390)
                                la6 = Label(health, text="Toner & Mists", bg="light yellow",
                                            font="Times 20 bold italic",
                                            width="33",
                                            height="1").place(x=75,
                                                              y=490)

                                # crating scale
                                self.scale1 = Scale(health, from_=0, to=100, orient=HORIZONTAL, bg="#ffff9d", fg="black", length=500, activebackground="red", cursor="dot")
                                self.scale1.place(x=100, y=150)
                                self.scale2 = Scale(health, from_=0, to=100, orient=HORIZONTAL, bg="#ffff9d", fg="black", length=500, activebackground="red", cursor="dot")
                                self.scale2.place(x=100, y=250)
                                self.scale3 = Scale(health, from_=0, to=100, orient=HORIZONTAL, bg="#ffff9d", fg="black", length=500, activebackground="red", cursor="dot")
                                self.scale3.place(x=100, y=350)
                                self.scale4 = Scale(health, from_=0, to=100, orient=HORIZONTAL, bg="#ffff9d", fg="black", length=500, activebackground="red", cursor="dot")
                                self.scale4.place(x=100, y=450)

                                bt1 = Button(health, text="Submit", width="15", height="2", bg="red",
                                             activeforeground="blue",
                                             cursor="circle",
                                             command=self.hcare_pkg).place(x=260, y=550)
                                bt2 = Button(health, text="Back", width="15", height="2", bg="red",
                                             activeforeground="blue",
                                             cursor="circle", command=self.exit).place(x=490,
                                                                                       y=615)

                            def exit(self):
                                self.health.destroy()
                                my_mrdi()

                            # calculation of skin care medical package
                            def hcare_pkg(self):
                                s1 = self.scale1.get()
                                s2 = self.scale2.get()
                                s3 = self.scale3.get()
                                s4 = self.scale4.get()

                                name_prices = {"S1 Serum": 1200, "S2 Face Mask": 990, "S3 Cleansers": 2100,
                                               "S4 Toner": 2600}

                                p1 = s1 * name_prices["S1 Serum"]
                                p2 = s2 * name_prices["S2 Face Mask"]
                                p3 = s3 * name_prices["S3 Cleansers"]
                                p4 = s4 * name_prices["S4 Toner"]

                                x = lambda a, b, c, d: a + b + c + d
                                itemsum = x(p1, p2, p3, p4)
                                if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
                                    messagebox.showwarning("Information", "Blank Not Allowed!!", parent=self.health)

                                else:
                                    if itemsum >= 20000:
                                        totblnc = lambda x, y, z: x - (y * z)
                                        finalsum = totblnc(itemsum, itemsum, 0.02)
                                        display = "Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                            format(finalsum, ".2f"))
                                        Label(self.health, text=display, bg="light yellow", font="Times 15 bold ",
                                              fg="blue",
                                              width="20", height="4").place(x=0, y=520)
                                        messagebox.showinfo("Your Package Details", display, parent=self.health)

                                    elif itemsum >= 50000:
                                        totblnc2 = lambda x, y, z: x - (y * z)
                                        finalsum = totblnc2(itemsum, itemsum, 0.02)
                                        display2 = "Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                            format(finalsum, ".2f"))

                                        Label(self.health, text=display2, bg="light yellow", font="Times 15 bold ",
                                              fg="blue",
                                              width="20", height="4").place(x=0, y=520)
                                        messagebox.showinfo("Your Package Details", display2, parent=self.health)

                                    elif itemsum >= 250000:
                                        totblnc3 = lambda x, y, z: x - (y * z)
                                        finalsum = totblnc3(itemsum, itemsum, 0.02)
                                        display3 = "Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                            format(finalsum, ".2f"))
                                        Label(self.health, text=display3, bg="light yellow", font="Times 15 bold ",
                                              fg="blue",
                                              width="20", height="4").place(x=0, y=520)
                                        messagebox.showinfo("Your Package Details", display3, parent=self.health)

                                    elif itemsum >= 500000:
                                        totblnc4 = lambda x, y, z: x - (y * z)
                                        finalsum = totblnc4(itemsum, itemsum, 0.02)
                                        display4 = "Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                            format(finalsum, ".2f"))
                                        Label(self.health, text=display4, bg="light yellow", font="Times 15 bold ",
                                              fg="blue",
                                              width="20", height="4").place(x=0, y=520)
                                        messagebox.showinfo("Your Package Details", display4, parent=self.health)

                                    else:
                                        Label(self.health,
                                              text="Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                                  itemsum),
                                              fg="blue", bg="light yellow", font="Times 15 bold ", width="20", height="4").place(x=0, y=520)
                                        messagebox.showinfo("Your Package Details",
                                                            "Congratulations!!\nyour skincare package is\nonly {} rupees".format(
                                                                itemsum), parent=self.health)

                        health = Tk()
                        org = skin_care(health)
                        health.minsize(700, 700)
                        health.maxsize(700, 700)
                        health.mainloop()

                    # creating other packages window
                    def other(self):
                        self.medi.destroy()

                        class package:
                            def __init__(self, pkg):
                                self.pkg = pkg

                                self.pkg.title("Other Medical Packages")

                                self.pkg['bg'] = "light yellow"
                                self.pkg.option_add("*Font", ('Verdana', 12))

                                la1 = Label(pkg, text="Other Medical Packages", bg="light yellow",
                                            font="Times 36 italic bold underline", width="500", height="2").pack()

                                T = Text(pkg, height=7, width=33, font="Times 20 bold", bg="light yellow")
                                T.pack()
                                T.insert(END, " •  Physiotherapy Medical Package\n"
                                              " •  Heart Disease Package\n"
                                              " •  Dental Surgery Package\n"
                                              " •  Basic Checkup Package\n"
                                              " •  Annual Checkup Package\n"
                                              " •  Well Man Screening Package\n"
                                              " •  Well Woman Screening Package ")
                                T.config(state="disabled")

                                medical = StringVar()

                                back_button = Button(pkg, text="Back", width="20", height="2", bg="red",
                                                     activeforeground="blue", command=self.exit).place(x=350, y=365)

                            def exit(self):
                                self.pkg.destroy()
                                my_mrdi()

                        pkg = Tk()
                        org = package(pkg)
                        pkg.minsize(600, 450)
                        pkg.maxsize(600, 450)
                        pkg.tk.mainloop()

                medi = Tk()
                obj = medical(medi)
                medi.minsize(800, 500)
                medi.maxsize(800, 500)
                mainloop()

            my_mrdi()

        # craeting contact us window
        def contact(self):
            home.destroy()

            class conta:
                def __init__(self, cont):
                    self.cont = cont
                    self.cont.title("Contact Us")
                    self.cont["bg"] = "light yellow"
                    self.cont.option_add("*Font", ('Verdana', 12))

                    l1 = Label(cont, text="Contcat Us", font="Times 36 italic underline bold", bg="light yellow").pack(
                        pady=11)

                    T = Text(cont, height=7, width=33, font="Times 20 italic bold", bg="light yellow")
                    T.pack(pady=50)
                    T.insert(END, "General Line : 0112666666\n"
                                  "Channeling Hotline : 0112666667\n"
                                  "Fax : 0112666668\n"
                                  "Email : aragihos@hospital.lk\n"
                                  "Address : Aragi Hospital's (PVT) LTD,\n"
                                  "               Colombo Road,"
                                  "\n               Colombo 07.")
                    T.config(state="disabled")

                    back_button = Button(cont, text="Back", width="20", height="2", bg="red", activeforeground="blue",
                                         command=self.exit).place(x=300, y=400)

                def exit(self):
                    self.cont.destroy()
                    my_home()

            cont = Tk()
            org = conta(cont)
            cont.minsize(600, 500)
            cont.maxsize(600, 500)
            cont.tk.mainloop()

        # creating comment window
        def comment(self):
            home.destroy()

            def my_comment():
                class comment:
                    def __init__(self, comm):
                        self.comm = comm

                        self.comm.title("Comment Here")

                        self.comm['bg'] = 'light yellow'
                        self.comm.option_add("*Font", ('Verdana', 12))

                        la1 = Label(self.comm, text="Comment Here", bg="light yellow",
                                    font="Times 36 italic bold underline",
                                    width="500",
                                    height="2").pack()

                        self.mycom = Text(self.comm, height=10, width=33, font="Times 20 italic bold", bg="#FEF7C1")
                        self.mycom.pack(pady=10)
                        self.mycom.insert(END, "")

                        submit_button = Button(self.comm, text="Submit", width="10", height="2", bg="red",
                                               activeforeground="blue",
                                               command=self.new_comment).place(x=65, y=500)
                        see_comment = Button(self.comm, text="Show Your Comment", width="18", height="2", bg="red",
                                             activeforeground="blue",
                                             command=self.show_comment).place(x=200, y=500)
                        back_button = Button(self.comm, text="Back", width="10", height="2", bg="red",
                                             activeforeground="blue",
                                             command=self.exit).place(x=420, y=500)

                    def new_comment(self):
                        comment_info = self.mycom.get("1.0", "end")
                        if comment_info == "\n":
                            Label(self.comm, text="Please say something about us!!", fg="red", bg="light yellow",
                                  width=30).place(x=140, y=455)
                            messagebox.showinfo("Information", "Please say something about us!!", parent=self.comm)

                        else:
                            save_comment_file = open("Comment_Details.txt", "a")

                            save_comment_file.write("Customer Comment : " + comment_info + "\n")
                            save_comment_file.write(("** " + "Next Comment " + "** ") * 3 + "\n")
                            save_comment_file.write("" + "\n")
                            Label(self.comm, text="Thanks for your comment", fg="red", bg="light yellow",
                                  width=30).place(x=140,
                                                  y=455)
                            messagebox.showinfo("Thank You", "Thanks for your comment", parent=self.comm)

                            # save_comment_file.colse()
                            self.mycom.delete(0.0, "end")

                            show_comment_file = open("Show_Comment_Details.txt", "w")
                            show_comment_file.write(comment_info)
                            show_comment_file.close()

                    def exit(self):
                        self.comm.destroy()
                        my_home()

                    def show_comment(self):
                        a = pathlib.Path("Show_Comment_Details.txt")
                        if a.exists():
                            self.comm.destroy()

                            class show_comm:
                                def __init__(self, show):
                                    self.show = show
                                    self.show.title("Your Comment")
                                    self.show['bg'] = 'light yellow'
                                    self.show.option_add("*Font", ('Verdana', 12))

                                    l1 = Label(self.show, text="Your Comment", font="Times 36 italic bold underline",
                                               bg="light yellow").pack()
                                    text_file = open("Show_Comment_Details.txt", "r")
                                    x = text_file.read()
                                    text_file.close()

                                    self.T = Text(self.show, height=8, width=30, font="Times 30", bg="light yellow")
                                    self.T.pack(pady=30)
                                    self.T.insert(END, x)
                                    self.T.config(state="disabled")
                                    self.T.delete(0.0, "end")
                                    back_button = Button(self.show, text="Back", width="20", height="2", bg="red",
                                                         activeforeground="blue", command=self.exit).place(x=420, y=505)

                                def exit(self):
                                    self.show.destroy()
                                    my_comment()

                            show = Tk()
                            a = show_comm(show)
                            show.minsize(700, 600)
                            show.maxsize(700, 600)
                            show.mainloop()

                        else:
                            messagebox.showinfo("Information",
                                                "If you want to see your comment,Firstly say something about us in Comment Box",
                                                parent=self.mycom)

                comm = Tk()
                org = comment(comm)
                comm.minsize(600, 600)
                comm.maxsize(600, 600)
                comm.mainloop()

            my_comment()

        def staff_dtails(self):
            home.destroy()

            class admin_login:
                def __init__(self, log):

                    self.log = log

                    self.log.title("Login")

                    self.log['bg'] = 'light yellow'
                    self.log.option_add("*Font", ('Verdana', 12))

                    la1 = Label(self.log, text="Enter Your Admin\nUser Name and Password\n for logging Staff Use Only",
                                bg="light yellow",
                                font="Times 30 italic bold",
                                width="50").pack()
                    la2 = Label(self.log, text="Username : ", bg="light yellow", font="calibre 20 bold").place(x=35,
                                                                                                               y=160)
                    la3 = Label(self.log, text="Password : ", bg="light yellow", font="calibre 20 bold").place(x=40,
                                                                                                               y=200)
                    la4 = Label(self.log, text="Secret Code : ", bg="light yellow", font="calibre 20 bold").place(x=10,
                                                                                                                  y=240)

                    name_var = StringVar()
                    passw_var = StringVar()
                    sc_var = StringVar()

                    self.name_entry = Entry(self.log, textvariable=name_var, font=('calibre', 10, 'normal'), width=35)
                    self.name_entry.place(x=205, y=172)
                    self.passw_entry = Entry(self.log, textvariable=passw_var, font=('calibre', 10, 'normal'), width=35,
                                             show='*')
                    self.passw_entry.place(x=205, y=211)
                    self.sc_entry = Entry(self.log, textvariable=sc_var, font=('calibre', 10, 'normal'), width=35,
                                          show='*')
                    self.sc_entry.place(x=205, y=250)

                    btn1 = Button(self.log, text="Login", width="15", height="2", bg="red", activeforeground="blue",
                                  cursor="dot",
                                  command=self.login).place(x=50, y=305)
                    btn2 = Button(self.log, text="Back", width="15", height="2", bg="red", activeforeground="blue",
                                  cursor="dot",
                                  command=self.exit).place(x=290, y=305)

                def exit(self):
                    self.log.destroy()
                    my_home()

                def clear(self):
                    self.name_entry.delete(0, "end")
                    self.passw_entry.delete(0, "end")
                    self.sc_entry.delete(0, "end")

                def login(self):
                    username = self.name_entry.get()
                    password = self.passw_entry.get()
                    secret_code = self.sc_entry.get()
                    if username == "" or password == "" or secret_code == "":
                        messagebox.showwarning("Information", "Blank Not Allowed", parent=self.log)

                    self.clear()
                    a = pathlib.Path("Admin_Login_Details.txt")
                    if a.exists():
                        # checking username & pw are correct
                        for x in open("Admin_Login_Details.txt", "r").readlines():
                            login_info = x.split()  # Split on the space, and store the results in a list of two strings

                            if username == login_info[0] and password == login_info[1] and secret_code == "210abc#":
                                Label(self.log, text="   Successfully Login!!", bg="light yellow", fg="blue",
                                      width="40",
                                      height="1",
                                      font="calibre 15").place(x=25, y=270)
                                messagebox.showinfo("Successfully Login!!", "Successfully Login!!", parent=self.log)
                                self.log.destroy()

                                def my_staff():
                                    class staff:
                                        def __init__(self, stf):
                                            self.stf = stf

                                            stf.title("Details")

                                            stf['bg'] = 'light yellow'
                                            stf.option_add("*Font", ('Verdana', 12))

                                            la1 = Label(self.stf, text="Details", bg="light yellow",
                                                        font="Times 36 italic underline bold", width="500",
                                                        height="2").pack()

                                            bt1 = Button(self.stf, text="Patients Registration Details", width="30",
                                                         height="2",
                                                         bg="red", activeforeground="blue", cursor="circle",
                                                         command=self.pat_reg).place(x=100, y=130)
                                            bt2 = Button(self.stf, text="Health Sector Registration Details",
                                                         width="30",
                                                         height="2", bg="red", activeforeground="blue", cursor="circle",
                                                         command=self.health).place(x=100, y=210)
                                            bt3 = Button(self.stf, text="Admin Registration Details", width="30",
                                                         height="2",
                                                         bg="red", activeforeground="blue", cursor="circle",
                                                         command=self.admin).place(x=100, y=290)
                                            bt4 = Button(self.stf, text="Users Comment", width="30", height="2",
                                                         bg="red",
                                                         activeforeground="blue", cursor="circle",
                                                         command=self.u_com).place(
                                                x=100, y=370)
                                            bt5 = Button(self.stf, text="Back", width="20", height="2", bg="red",
                                                         activeforeground="blue", cursor="circle",
                                                         command=self.exit).place(x=520, y=370)

                                        def exit(self):
                                            self.stf.destroy()
                                            my_home()

                                        def pat_reg(self):
                                            a = pathlib.Path("Patients_Register_Details.txt")
                                            if a.exists():
                                                self.stf.destroy()

                                                class Patients:
                                                    def __init__(self, show):
                                                        self.show = show
                                                        self.show.title("Patients Details")
                                                        self.show['bg'] = 'light yellow'
                                                        self.show.option_add("*Font", ('Verdana', 12))

                                                        l1 = Label(self.show, text="Patients Details",
                                                                   font="Times 36 italic bold underline",
                                                                   bg="light yellow").pack()
                                                        text_file = open("Patients_Register_Details.txt", "r")
                                                        x = text_file.read()
                                                        text_file.close()

                                                        self.T = Text(self.show, height=27, width=80, font="Times 15",
                                                                      bg="light yellow")
                                                        self.T.pack(pady=30)
                                                        self.T.insert(END, x)
                                                        self.T.config(state="disabled")
                                                        self.T.delete(0.0, "end")
                                                        back_button = Button(self.show, text="Back", width="20",
                                                                             height="2",
                                                                             bg="red", activeforeground="blue",
                                                                             command=self.exit).place(x=640, y=720)

                                                    def exit(self):
                                                        self.show.destroy()
                                                        my_staff()

                                                show = Tk()
                                                a = Patients(show)
                                                show.minsize(900, 800)
                                                show.maxsize(900, 800)
                                                show.mainloop()

                                            else:
                                                messagebox.showinfo("Information",
                                                                    "No patients have been registered yet",
                                                                    parent=self.stf)

                                        def health(self):
                                            a = pathlib.Path("Medical_Register_Details.txt")
                                            if a.exists():
                                                self.stf.destroy()

                                                class heal:
                                                    def __init__(self, show):
                                                        self.show = show
                                                        self.show.title("Health Sector Details")
                                                        self.show['bg'] = 'light yellow'
                                                        self.show.option_add("*Font", ('Verdana', 12))

                                                        l1 = Label(self.show, text="Health Sector Details",
                                                                   font="Times 36 italic bold underline",
                                                                   bg="light yellow").pack()
                                                        text_file = open("Medical_Register_Details.txt", "r")
                                                        x = text_file.read()
                                                        text_file.close()

                                                        self.T = Text(self.show, height=27, width=80, font="Times 15",
                                                                      bg="light yellow")
                                                        self.T.pack(pady=30)
                                                        self.T.insert(END, x)
                                                        self.T.config(state="disabled")
                                                        self.T.delete(0.0, "end")
                                                        back_button = Button(self.show, text="Back", width="20",
                                                                             height="2",
                                                                             bg="red",
                                                                             activeforeground="blue",
                                                                             command=self.exit).place(x=640, y=720)

                                                    def exit(self):
                                                        self.show.destroy()
                                                        my_staff()

                                                show = Tk()
                                                a = heal(show)
                                                show.minsize(900, 800)
                                                show.maxsize(900, 800)
                                                show.mainloop()
                                            else:
                                                messagebox.showinfo("Information",
                                                                    "No one is registered with the health sector yet",
                                                                    parent=self.stf)

                                        def admin(self):
                                            a = pathlib.Path("Admin_Register_Details.txt")
                                            if a.exists():
                                                self.stf.destroy()

                                                class admin_dep:
                                                    def __init__(self, show):
                                                        self.show = show
                                                        self.show.title("Admin Sector Details")
                                                        self.show['bg'] = 'light yellow'
                                                        self.show.option_add("*Font", ('Verdana', 12))

                                                        l1 = Label(self.show, text="Admin Sector Details",
                                                                   font="Times 36 italic bold underline",
                                                                   bg="light yellow").pack()
                                                        text_file = open("Admin_Register_Details.txt", "r")
                                                        x = text_file.read()
                                                        text_file.close()

                                                        self.T = Text(self.show, height=27, width=86, font="Times 15",
                                                                      bg="light yellow")
                                                        self.T.pack(pady=30)
                                                        self.T.insert(END, x)
                                                        self.T.config(state="disabled")
                                                        self.T.delete(0.0, "end")
                                                        back_button = Button(self.show, text="Back", width="20",
                                                                             height="2",
                                                                             bg="red",
                                                                             activeforeground="blue",
                                                                             command=self.exit).place(x=640, y=720)

                                                    def exit(self):
                                                        self.show.destroy()
                                                        my_staff()

                                                show = Tk()
                                                a = admin_dep(show)
                                                show.minsize(900, 800)
                                                show.maxsize(900, 800)
                                                show.mainloop()
                                            else:
                                                messagebox.showinfo("Information",
                                                                    "No one is registered with the Administration yet",
                                                                    parent=self.stf)

                                        def u_com(self):
                                            a = pathlib.Path("Comment_Details.txt")
                                            if a.exists():
                                                self.stf.destroy()

                                                class user_com:
                                                    def __init__(self, show):
                                                        self.show = show
                                                        self.show.title("User's Comment")
                                                        self.show['bg'] = 'light yellow'
                                                        self.show.option_add("*Font", ('Verdana', 12))

                                                        l1 = Label(self.show, text="User's Comment",
                                                                   font="Times 36 italic bold underline",
                                                                   bg="light yellow").pack()
                                                        text_file = open("Comment_Details.txt", "r")
                                                        x = text_file.read()
                                                        text_file.close()

                                                        self.T = Text(self.show, height=27, width=80, font="Times 15",
                                                                      bg="light yellow")
                                                        self.T.pack(pady=30)
                                                        self.T.insert(END, x)
                                                        self.T.config(state="disabled")
                                                        self.T.delete(0.0, "end")
                                                        back_button = Button(self.show, text="Back", width="20",
                                                                             height="2",
                                                                             bg="red",
                                                                             activeforeground="blue",
                                                                             command=self.exit).place(x=640, y=720)

                                                    def exit(self):
                                                        self.show.destroy()
                                                        my_staff()

                                                show = Tk()
                                                a = user_com(show)
                                                show.minsize(900, 800)
                                                show.maxsize(900, 800)
                                                show.mainloop()
                                            else:
                                                messagebox.showinfo("Information", "No users Comment", parent=self.stf)

                                    stf = Tk()
                                    obj = staff(stf)
                                    stf.minsize(800, 500)
                                    stf.maxsize(800, 500)
                                    stf.mainloop()

                                my_staff()

                                return True

                        Label(self.log, text="Invalid Username or Password or Secret Code", bg="light yellow", fg="red",
                              width="40",
                              height="1",
                              font="calibre 15").place(x=25, y=270)
                        messagebox.showwarning("Invalid Username or Password or Secret Code",
                                               "Invalid Username or Password or Secret Code\nPlease Try Again!!",
                                               parent=self.log)

                        return False

                    else:
                        messagebox.showwarning("Information", "This can only be accessed by the administrative section",
                                               parent=self.log)

            log = Tk()
            obj = admin_login(log)
            log.minsize(500, 380)
            log.maxsize(500, 380)
            log.mainloop()

        def exit(self):
            messagebox.showinfo("Thank You", "Thank You for joining us")
            self.home.destroy()

            a = pathlib.Path("Show_Comment_Details.txt")
            # if file is exists, remove the file
            if a.exists():
                os.remove("Show_Comment_Details.txt")
                print("ok")

    home = Tk()
    obj = homepage(home)
    home.minsize(1000, 700)
    home.maxsize(1000, 700)
    home.mainloop()


my_home()
