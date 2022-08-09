# Opis tkinter (Znajomość Tk mile widziana)
# https://docs.python.org/3/library/tkinter.html
# http://www.tcl.tk/man/tcl8.5/TkCmd/contents.htm
# https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# https://docs.python.org/3/library/index.html
# canvas: https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas-methods.html

# Wpisz polecenie w wierszu poleceń systemu:
# python -m tkinter
# Jeżeli pojawi się okienko, wszystko jest OK. Zaczynamy!

# uwaga! nie skupiam się na wyłapywaniu błędów, tylko na pokazaniu jak uruchomić
# prostą aplikację okienkową 


from tkinter import * # podstawy do utworzenia okna
from tkinter import messagebox # okno komunikatu

import mysql.connector
import time
from collections import deque

# nasza aplikacja będzie czerpać dane z MySQL'owej bazy (lekcja 14)
mydb = mysql.connector.connect(host="localhost",user="user",passwd="1234",database="baza")

root = Tk()  # okno główne aplikacji, Tk() - konstruktor okna
root.resizable(width=False, height=True) # okno główne rozciągalność

# FUNKCJE OBSŁUGI OKNA
def klikniętoPrzycisk() :
  print('click!')
  print(ent.get())
  t = txt.get('1.0',END) # pobiera wszystko od pierwszego wiersza do końca
  t2 = txt.get('1.3','2.0') # pierwsze dwa wiersze ale nie od pierwzego znaku (1.3 - 3 znak)  
  #txt.delete('1.0',END) # kasuję wszystko od pierwszego wiersza do końca
  query="SELECT id,regNr FROM cars"
  f = ""
  cursor = mydb.cursor()
  cursor.execute(query)
  for (id,regNr) in cursor:
    f = f + "{} = {}\n".format(id,regNr);  
  cursor.close()  
  messagebox.showerror('Wpisane dane',ent.get() + t + '\n' + t2) # messagebox.showerror/showwarrning
  txt.insert('2.0',f) #wstawiam na początek

def mouse_move(event):
  # współrzędne myszy na płótnie
  print(event.x,event.y)
  # rysuję kwadracik
  c.create_rectangle(event.x+5,event.y+5,event.x-5,event.y-5,outline='pink',fill='blue')
def clear_canvas(event):  
  print(c.find_all())
  list(map(lambda i : c.delete(i), c.find_all())) # dlaczego list ??
  # bo map - zwraca iterator do wywołań, czyli tak, jakby jeszcze się nie wykonały te funkcje
  # zatem trzeba je wykonać (list wymusza wywołanie, ale zwraca też listę, co może nie być
  # potrzebne, dlatego można zrobić to tak
  # deque(map(lambda i : c.delete(i), c.find_all()))
  deque(map(lambda i : c.delete(i), c.find_all()))
  
def on_select(event):
  # wyświetlam tekst 
  libox = event.widget
  index = int(libox.curselection()[0])
  print(libox.get(index),index)  
  

################ PROGRAM GŁÓWNY #######################

#NAPIS
haj = Label(root, text='Witaj świecie') # napis
haj.grid(row=0,column=0) # wpakowanie do "niewidzialnej tabeli" (umiejscowienie w oknie)

#RAMKA
frame = Frame(root,borderwidth=4) # ramka 
frame.grid(row=0, column=1 )
frame.config(background='black')

#NAPIS W RAMCE
lab1 = Label(frame,text='Ramka1') # do ramki dodaję napis
lab1.grid(sticky=E, row=0, column=0, padx=5, pady=5) # określam sposób przyklejania, odstępy

#POLE INPUT JEDNOLINIOWE (upchane do ramki)
ent = Entry(frame, width=50)  # pole tekstowe jednoliniowe 
ent.grid(sticky=W,row=1,column=0,padx=5, pady=5) # określam ponownie sposób umiejscowienia

#PRZYCISK czyli ukochany Baton, przepraszam BUTTON (też wpycham go do ramki)
  # + powiązanie akcji kliknięcia przycisku
przycisk = Button(frame,text='Kliknij proszę we mnie teraz!', command=klikniętoPrzycisk)
przycisk.grid(row=2,column=0)
przycisk.config(background='red', foreground='#FFFF00') # pobawimy się batonem
#PŁÓTNO. A, no to wiadomo - wszystko jasne. Płótno ... to płótno. Płótno też w ramce
c = Canvas(frame,width=500, height=150)
# obsługa sytuacji, gdy nad płótnem rusza się myszka
c.bind('<B1-Motion>',mouse_move) 
c.bind('<Button-3>',clear_canvas)
'''
  B1/2/3/4-Motion ruch z trzymanym przyciskiem
  Button-1/2/3/4 klik
  ButtonPress-1/2/3/4 wciśk
  ButtonRelease-1/2/3/4  wycisk
  Double-Button-1/2/3/4
  Enter (wjazd myszy na płótno)
  Leave (zjazd myszy z płótna)
  Return,Shift_L,BackSpace,Tab, F1, Control_R itd.
  FocusIn - klawiatura fokusuje płótno lub jego zawartość
  FocusOut
'''
c.grid(sticky=S, row=3,column=0, padx=5, pady=5) # umiejscowienie płótna w ramce
c.config(background='green') # manipulacja płótnem
#POLE TEKSTOWE WIELOLINIOWE (też do ramki wstawię)
txt = Text(frame,width=120, height=10)
txt.grid(sticky=E+N, row=4,column=0, padx=5, pady=5) # tu pozycjonuję
#POLE ROZWIJANE tzw. skrzynkolista (ok, wymyśliłem to tłumaczenie...) może... pudłolist ?
libox = Listbox(root) # lista w oknie głównym a nie ramce
libox.grid(row=4,column=1) # pozycjonuję
# pozycja gdzie wstawiam, i jaki napis (END zawsze na koniec)
libox.insert(0,'witajcie uczniowie') 
libox.insert(1,'żegnajcie lenie')
libox.insert(END,'jestem ostatni')
libox.insert(0,'zawsze pierwszy...') 
libox.bind('<<ListboxSelect>>',on_select) # powiąż zdarzenie z metodą
# libox.delete(0,END) # czyści od .. do


# ODPALAM OKNO (ciągle sięwyświetla, ciągle jest generowane)
root.mainloop() # czeka na zakończenie - program nie idzie dalej
print ('\nNo i po roocie!')

mydb.close() # zamykam bazę danych
'''
ĆWICZENIE:
  1) kliknięcie na listę ustawia napis do pól tekstowych
  2) kliknięcie w przycisk rysuje na płótnie prostokąt o losowym rozmiarze i losowym położeniu
'''
