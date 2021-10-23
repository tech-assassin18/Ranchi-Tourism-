from tkinter import *
import tkinter as tk
import webbrowser
from PIL import ImageTk,Image

#function to display the distance
def distance():
    filewin=Toplevel(win)
    button=Button(filewin,text="Click to know the distance from the city centre")
    button.pack()
    
#function for displaying pictures
def imgjgg():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Jagannath-Temple-Ranchi.jpg')
    load1=Image.open('Jaganath_Temple,_Ranchi.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)


    tk.Label(filewin,text="THE JAGGANATH TEMPLE ",font=('TimesNewRoman', 15),background='yellow', foreground='red').pack() 
    button=Button(filewin,text=" 4 Kilometres away from city centre", font=('calibri',13),width=50,background='darkblue',foreground='white').pack()
    tk.Message(filewin,text="Perched up on a hilltop the \
                        Jagannath Temple is the most popular historical landmark in Ranchi dating back to 1691.\n \
                        As smaller replica of the Jagannath Temple in Puri,the temple is decked \
                        with intricate carvings and a unique blend of coloured stones. \
                        The Rath Yatra is a festival of joyous celebration that sees a \
                        footfall of thousands of tourists each year.", font=('calibri', 13),background='lightgreen').pack()

def imgphr():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('pahari-mandir 1.jpg')
    load1=Image.open('pahari-mandir.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    
    tk.Label(filewin,text=" THE PAHARI MANDIR ",font=('TimesNewRoman', 16),background='yellow', foreground='red').pack()
    button=Button(filewin,text="3 Kilometres away from city centre",font=('calibri',13),width=50,background='darkblue',foreground='white').pack()
    tk.Message(filewin,text=" Dedicated to Lord Shiva, the Pahari Mandir in Rachi soars \
                              at an altitude of 2140 feet and offers a mind-stirring bird's eye view of the entire city. \
                              You have to climb about 300 steps to reach here, \
                              but the beauty of the temple and the stunning view is absolutely worth it. \
                        The Shravan season is a pompous affair here and sees a footfall of\
               hundreds of devotees each year.",font=('calibri', 13),background='lightgreen').pack()
def imgdeo():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('deori-temple.jpg')
    load1=Image.open('deori-temple (1).jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" THE DEORI MANDIR ",font=('TimesNewRoman', 16),background='yellow',foreground='red').pack()
    button=Button(filewin,text="51 Kilometres away from city centre", font=('calibri',13),width=50,background='darkblue',foreground='white').pack()
    tk.Message(filewin,text=" Dedicated to the ferocious 16-armed Goddess Kali,\
                              the Deori Mandir was originally built by a tribal devotee of the goddess \
                              with nothing but sandstone.Holding tremendous religious significance, thousands of devotees \
                              pray to the goddess and tie a thread around a bamboo as a ritual.\
                              The temple gained popularity when news broke out that \
                              famous cricketer MS Dhoni visits the temple on a regular basis..",font=('calibri', 13),background='lightgreen').pack()
def imgrajj():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('rajrappa images.jpg')
    load1=Image.open('rajrappa 2.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)


    tk.Label(filewin,text=" THE RAJJRAPPA MANDIR ",font=('TimesNewRoman',16),background='yellow',foreground='red').pack()
    button=Button(filewin,text="52 Kilometres away from city centre",font=('calibri',13),width=50,background='darkblue',foreground='white').pack()
    tk.Message(filewin,text="Rajrappa is a Hindu pilgrimage centre attracting an estimated 2,500-3,000 persons daily.\
                             The main attraction of the Chhinnamasta (also known as Chinnamastika) temple located\
                             here is the headless deity of goddess Chinnamasta which stands on the body of Kamdev and Rati \
                             in the lotus bed. The Chhinnamasta temple is very popular for its Tantrik style \
                             of architectural design. The temple is very old but has that essence of enchantment.\
                             Apart from the main temple, there are ten temples of various gods and goddesses such as the\
                             Sun God and Lord Shiva. Animal sacrifice is still practised in the temple. \
                             The sacrifice is offered on Tuesdays and Saturdays \
                             and during Kali puja", font=('calibri', 13),background='lightgreen').pack()

#function for displaying distance of falls from city centre
def df():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Dasam_fall.jpg')
    load1=Image.open('Dassam_falls.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)

    tk.Label(filewin,text=" DASSAM FALLS ",font=('Algerian', 16),background='blue', foreground='white').pack()
    button=Button(filewin,text="26 Kilometres away from city centre",font=('calibri',13),width=50,background='pink',foreground='black').pack()
    tk.Message(filewin,text="Located near the Taimara village in Ranchi,\
                             Dassam Falls, is a spectacular waterfall cascading down a height of 144 feet\
                             The area surrounding the spot is engulfed in rich greenery, \
                             that makes it an ideal picnic place in the region.", font=('calibri', 13),background='orange').pack()
def jf():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Jonha_falls.jpg')
    load1=Image.open('jonha.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" JONHA FALLS ",font=('Algerian', 16),background='blue',foreground='white').pack()
    button=Button(filewin,text="31 Kilometres away from city centre",font=('calibri',13),width=50,background='pink',foreground='black').pack()
    tk.Message(filewin,text="Plunging from a height of about 45 meters, \
                             the Jonha Falls are surrounded in a canopy of plush dense trees and thick shrubbery. \
                             The holy waters of River Ganga and River Raru come together to form these giant roaring falls.\
                             They are also known as the Gautamdhara Falls because of a Buddhist \
                             shrine that lies in proximity to the falls.",font=('calibri', 13),background='orange').pack()
def hf():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Hundru_falls.jpg')
    load1=Image.open('hudru.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" HUDRU FALLS ",font=('Algerian', 16),background='blue',foreground='white').pack()
    button=Button(filewin,text="37 Kilometres away from city centre",font=('calibri',13),width=50,background='pink',foreground='black').pack()
    tk.Message(filewin,text="The river Subarnekha while flowing through Ranchi forms a lot of waterfalls, \
                             but the most beautiful of them is Hudru Falls. \
                             Falling from a height of 320 feet, the Hudru Falls create a spectacular \
                             landscape and is extremely popular with tourists.",font=('calibri', 13),background='orange').pack()
def pgf():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Panch-Gagh-Falls.jpg')
    load1=Image.open('panch gagh.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" PANCH GAGH FALLS ",font=('Algerian', 16),background='blue', foreground='white').pack()
    button=Button(filewin,text="3 Kilometres away from city centre",font=('calibri',13),width=50,background='pink',foreground='black').pack()
    tk.Message(filewin,text="Panch (means five) Gagh Falls is a stunning tourist destination \
                             which has five waterfalls cascading through tall and steep hills\
                             near the scenic village of Khunti. \
                             The foot of the waterfalls has a very calm and serene atmosphere and is \
                             an ideal location for picnics and weekend getaways.",font=('calibri', 13),background='orange').pack()
#function for displaying the distance of parks from city centre
def rg():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('rock garden.jpg')
    load1=Image.open('Rock-Garden-1.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
   
    tk.Label(filewin,text=" ROCK GARDEN ",font=('calibri', 16),background='lightgreen', foreground='green').pack()
    button=Button(filewin,text="7 Kilometres away from city centre",font=('calibri',13),width=50,background='orange',foreground='blue').pack()
    tk.Message(filewin,text="Complete with waterfalls, sculptures, art and unparalleled scenic beauty, \
                             the Rock Garden in Ranchi is the perfect weekend excursion destination. \
                             The major attraction here is an iron footbridge that stands on only two poles. \
                             Since the garden is situated on a hillock by the Kanke Dam and is surrounded by lush environs, \
                             you can relax peacefully while enjoying a stunning view of the city.",font=('calibri', 13)).pack()
def bzp():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Birsa-Zoological-Park.jpg')
    load1=Image.open('biirsa.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" BIRSA ZOOLOGICAL PARK ",font=('calibri', 16),background='lightgreen', foreground='green').pack()
    button=Button(filewin,text="20 Kilometres away from city centre",font=('calibri',13),width=50,background='orange',foreground='blue').pack()
    tk.Message(filewin,text="The Birsa Zoological Park, also known as Birsa Jaivik Udyan \
                             houses a wide variety of wild animals like lions, tigers, various kinds of deer etc. \
                             It is located on the Ranchi-Patna National Highway near Ormanjhi \
                             and is a must-visit for all wildlife enthusiasts.",font=('calibri', 13)).pack()
def bp():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('biodiversity.jpg')
    load1=Image.open('bio.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
   
    tk.Label(filewin,text=" BIODIVERSITY PARK ",font=('calibri', 16),background='lightgreen', foreground='green').pack()
    button=Button(filewin,text="11 Kilometres away from city centre",font=('calibri',13),width=50,background='orange',foreground='blue').pack()
    tk.Message(filewin,text="Biodiversity Park is one of the most loved picnic spots in Ranchi.\
                             Replete with plenteous vegetation and lush greenery, \
                             the park is popular among the adults and kids alike. \
                             The park strives to preserve and protect medicinal plants and herbs.",font=('calibri', 13)).pack()
def nv():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('nak.png')
    load1=Image.open('nakvan.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" NAKSHATRA VAN ", font=('calibri', 16),background='lightgreen', foreground='green').pack()
    button=Button(filewin,text="4 Kilometres away from city centre",font=('calibri',13),width=50,background='orange',foreground='blue').pack()
    tk.Message(filewin,text="Nakshatra Van is a park is in front of \
                             the Jharkhand Raj Bhawan (Governor's Residence) in Ranchi.\
                             A nakshatra or lunar mansion is one of the 27 or 28 divisions of the sky,\
                             identified by the prominent star(s) in them, that the Moon passes\
                             through during its monthly cycle, as used in Hindu astronomy and astrology. \
                             Each Nakshatra is associated with a Zodiac, which is related to celestial bodies\
                             and their movements in sky. Hindu Astrologers believe that each constellation\
                             of the zodiac is associated with a tree. \
                            Those trees are of medicinal, social, aesthetic or economic value.",font=('calibri', 13)).pack()

#functions for dipalying the distance of dayouts from city centre
def pv():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Patratu-Valley.jpg')
    load1=Image.open('Patratu.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
   
    tk.Label(filewin,text=" PATRATU VALLEY ",font=('calibri', 16),background='orange', foreground='blue').pack()
    button=Button(filewin,text="26 Kilometres away from city centre",font=('calibri',13),width=50,background='yellow',foreground='black').pack()
    tk.Message(filewin,text="Forty kilometres outside Ranchi lies the scintillating Patratu Valley.\
                             With sparkling waters of the Patratu Dam on one side and lush green trees flanked along the other,\
                             driving along the Ghat of the Patratu Valley is truly a stupendous experience. \
                             However, do not venture into these roads after dark \
                             because of the rampant Naxalite influence in the area.",font=('calibri', 13),background='pink').pack()
def th():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('Tagore-Hill.jpg')
    load1=Image.open('tagore hills.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" TAGORE HILLS ", font=('calibri', 16),background='orange', foreground='blue').pack()
    button=Button(filewin,text="7 Kilometres away from city centre",font=('calibri',13),width=50,background='yellow',foreground='black').pack()
    tk.Message(filewin, text="Tagore Hill is situated at an altitude of 200 feet in \
                              an isolated location where one find spend time in some peace and quiet.\
                              It is named after the famous poet, Nobel Laureate Rabindra Nath Tagore.",font=('calibri', 13),background='pink').pack()
def fc():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('fun-castle.jpg')
    load1=Image.open('fun castle.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" FUN CASTLE WATER PARK ",font=('calibri', 16),background='orange', foreground='blue').pack()
    button=Button(filewin,text="12 Kilometres away from city centre", font=('calibri',13),width=50,background='yellow',foreground='black').pack()
    tk.Message(filewin,text="Located in Ratu in Ranchi, Fun Castle Water Park is one of the most popular water parks in the city.\
                             Replete with a number of fun options, the park has water draughting, thrilling water, \
                             Playground etc in addition changing and locker rooms, food options etc.",font=('calibri', 13),background='pink').pack()
def nm():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('nucleus mall.jpg')
    load1=Image.open('nucleus-mall.jpg')

    load=load.resize((450,450))
    load1=load1.resize((450,450))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    
    tk.Label(filewin,text=" NUCLEUS MALL ",font=('calibri', 16),background='orange', foreground='blue').pack()
    button=Button(filewin,text="4 Kilometres away from city centre",font=('calibri',13),width=50,background='yellow',foreground='black').pack()
    tk.Message(filewin,text="The biggest mall in Ranchi, the Nucleus Mall is the up and coming hangout place for the new generations.\
                            Housing big brand stores, a huge food court with various cuisine options,\
                            an advanced gym, an arcade, a FUN zone for kids and the luxurious PVR theatres- this place has it all. \
                            The mall is equipped with all premium modern amenities.",font=('calibri', 13),background='pink').pack()
    
def about():
    filewin=Toplevel(win)
    filewin.resizable(False,False)
    filewin.config(background='black')

    load=Image.open('me.png')
    load1=Image.open('dandin sir.jpg')

    load=load.resize((250,500))
    load1=load1.resize((300,500))

    render=ImageTk.PhotoImage(load)
    render1=ImageTk.PhotoImage(load1)

    img=Label(filewin,image=render)
    img1=Label(filewin,image=render1)

    img.image=render
    img1.image=render1

    img.pack(side=LEFT)
    img1.pack(side=LEFT)
    button=Button(filewin,text=" RANCHI TOURISM PROJECT DEVELOPED BY SHIWANGINI SHREYA ",font=('algerian', 16),background='lightgreen').pack()
    tk.Message(filewin,text="I'm really blessed to have such an amazing teacher who \
                             not only just guided us but also supported and motivated and also\
                             helped our completion of project on time.Thank you for so much of inspiration\
                             Hat's off to you sir for always being such a great mentor\n \
                             Thank you so much SHRIDHAR B. DANDIN SIR.",font=('clalibri',13),background='yellow').pack() 
win=Tk()
win.title("RANCHI TOURISM PROJECT")
menu=Menu(win)
win.config(menu=menu,bg="lime")
filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Sacred and religious",menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Jagganth temple",command=imgjgg)
filemenu.add_separator()
filemenu.add_command(label="Pahari Mandir",command=imgphr)
filemenu.add_separator()
filemenu.add_command(label="Deori mandir",command=imgdeo)
filemenu.add_separator()
filemenu.add_command(label="Rajrappa mandir",command=imgrajj)
filemenu.add_separator()


helpmenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Water falls",menu=helpmenu)
helpmenu.add_separator()
helpmenu.add_command(label="Dasham falls",command=df)
helpmenu.add_separator()
helpmenu.add_command(label="Jonha falls",command=jf)
helpmenu.add_separator()
helpmenu.add_command(label="Hudru falls",command=hf)
helpmenu.add_separator()
helpmenu.add_command(label="Panch gagh falls",command=pgf)
helpmenu.add_separator()

filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Parks ",menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Rock garden",command=rg)
filemenu.add_separator()
filemenu.add_command(label="Birsa zoological park",command=bzp)
filemenu.add_separator()
filemenu.add_command(label="Biodiversity park",command=bp)
filemenu.add_separator()
filemenu.add_command(label="Nakshatra Van",command=nv)
filemenu.add_separator()


filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Dayouts",menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Patratu valley",command=pv)
filemenu.add_separator()
filemenu.add_command(label="Tagore hills",command=th)
filemenu.add_separator()
filemenu.add_command(label="Fun castle",command=fc)
filemenu.add_separator()
filemenu.add_command(label="Nucleus mall",command=nm)
filemenu.add_separator()


exitmenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Exit",menu=exitmenu)
exitmenu.add_separator()
exitmenu.add_command(label="About",command=about)
exitmenu.add_separator()
exitmenu.add_command(label="Quit",command=win.destroy)
exitmenu.add_separator()

win.mainloop()
