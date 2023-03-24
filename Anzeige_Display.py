# This Python file uses the following encoding: utf-8

# Importieren der benötigten Bibliotheken
import socket
import sys
import os
#from bs4 import BeautifulSoup
#import openfoodfacts
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import font
import threading
import requests

#Erstellen eines Fensters
root = Tk()

# Vollbildmodus aktivieren
root.attributes("-fullscreen", True)

# Hintergrundfarbe des Fensters setzen
root.configure(background='beige')



# Schleife, die das Fenster im Fullscreen offen hält
while True:
    
    #Funktion zum neu starten des Programms, dabei wird alles auf den Ausgangszustand zurückgesetzt
    def restart_programm():
        python = sys.executable
        os.execv(python, [python] + sys.argv)
    
    #Funktion für den Button "Entfernen" eines Elements aus der oberen Listbox
    def delete_item():
        
        # Überprüfung, ob der "Einkaufsliste"-Button deaktiviert ist
        if einkaufsliste_button["state"] == "disabled":
            # Auswahl des Elements in der Liste
            selection1 = listbox.curselection()
            if selection1:
                # Überprüfung, ob Daten in der Liste vorhanden sind
                if Daten != []:
                    # Entfernen des Elements aus der Datenliste
                    zahl = selection1[0] 
                    global name_delete
                    name_delete = listbox.get(zahl)
                    print(name_delete)
                    Daten.remove(name_delete)
                    print(Daten)
                
                # Entfernen des Elements aus der Listbox
                listbox.delete(selection1[0])
                
                # Entfernen des zugehörigen Labels mit dem Bild 
                if name_delete in Obst:                
                    name_Obst = f"label_obst_{name_delete}"
                    globals()[name_Obst].grid_forget()
                elif name_delete in Suessigkeiten:
                    name_suessigkeiten = f"label_Suessigkeiten_{name_delete}"
                    globals()[name_suessigkeiten].destroy()
                elif name_delete in Konserven:
                    name_konserven = f"label_konserven_{name_delete}"
                    globals()[name_konserven].destroy()
                elif name_delete in Getraenke:
                    name_getraenke = f"label_getraenke_{name_delete}"
                    globals()[name_getraenke].destroy()
                

            else:
                # Anzeige einer Warnmeldung, wenn kein Element in der Liste ausgewählt wurde
                messagebox.showwarning("Warnung", "Bitte waehlen Sie ein Element zum Loeschen aus.")
        
        # Überprüfung, ob der "Rechnung"-Button deaktiviert ist
        elif Rechnung_button["state"] == "disabled":
            # Auswahl des Elements in der Liste
            selection2 = listboxAusgabeScanner.curselection()
            if selection2:
                # Entfernen des Elements aus der Listbox
                listboxAusgabeScanner.delete(selection2[0])
                
            else:
                # Anzeige einer Warnmeldung, wenn kein Element in der Liste ausgewählt wurde
                messagebox.showwarning("Warnung", "Bitte waehlen Sie ein Element zum Loeschen aus.")
    

   
        

    # Funktion zum Erstellen des Labels mit dem Bild des Obstes/Gemüses
    def Label_erstellen_obst(element):    
        
        #Bild auslesen, kann nicht als extra funktion ausgegliedert werden, sonst wird es nicht für alle produkte gleich erstellt
        global photo_obst
        global image_obst
    
        # Oeffne das Bild und verkleinere es
        image_obst = Image.open("/home/rc/ProgrammDisplay/kreis_rot_klein.png")
        image_obst = image_obst.resize((25, 30), resample=Image.LANCZOS)
        # Erstelle das PhotoImage-Objekt aus dem Bild
        photo_obst = ImageTk.PhotoImage(image_obst)
        # Erstelle den Namen des Labels und erstelle das Label
        name_obst = f"label_obst_{element}"
        globals()[name_obst] = Label(root, image=photo_obst)
        globals()[name_obst].grid(row=5, column=1, sticky="nw", padx=32, pady=1)

    def obst_gemuese_abgleich():
    # Ueberprüfe jedes Element in Obst
        for element in Obst:
            if element in Daten:
                print(f"Das Element {element} ist in beiden Listen vorhanden.")
                
                # Rufe die Funktion Label_erstellen auf, um das Label zu erstellen
                Label_erstellen_obst(element)
            else:
                print("Keine uebereinstimmenden Elemente gefunden.")
    
        # Ueberprüfe jedes Element in Gemuese
        for element in Gemuese:  
            if element in Daten:
                print(f"Das Element {element} ist in beiden Listen vorhanden.")
               
                # Rufe die Funktion Label_erstellen auf, um das Label zu erstellen
                Label_erstellen_obst(element)
            else:
                print("Keine uebereinstimmenden Elemente gefunden.")
    
    def Suessigkeiten_abgleich():
    # Ueberprüfe jedes Element in Süßigkeiten
        for element in Suessigkeiten:
            if element in Daten:
                print(f"Das Element {element} ist in beiden Listen vorhanden.")
                
                # Rufe die Funktion Label_erstellen auf, um das Label zu erstellen
                Label_erstellen_Suessigkeiten(element)
            else:
                print("Keine uebereinstimmenden Elemente gefunden.")
    

    def Label_erstellen_Suessigkeiten(element):

        global photo_suessigkeiten
        global image_Suessigkeiten
    
        # Oeffne das Bild und verkleinere es
        image_Suessigkeiten = Image.open("/home/rc/ProgrammDisplay/kreis_rot_klein.png")
        image_Suessigkeiten = image_Suessigkeiten.resize((25, 30), resample=Image.LANCZOS)
        # Erstelle das PhotoImage-Objekt aus dem Bild
        photo_suessigkeiten = ImageTk.PhotoImage(image_Suessigkeiten)
        
        # Erstelle den Namen des Labels und erstelle das Label
        name_suessigkeiten = f"label_Suessigkeiten_{element}"
        globals()[name_suessigkeiten] = Label(root, image=photo_suessigkeiten)
        globals()[name_suessigkeiten].place(x=460,y=350)


    def Konserven_abgleich():
    # Ueberprüfe jedes Element in Süßigkeiten
        for element in Konserven:
            if element in Daten:
                print(f"Das Element {element} ist in beiden Listen vorhanden.")
                
                # Rufe die Funktion Label_erstellen auf, um das Label zu erstellen
                Label_erstellen_Konserven(element)
            else:
                print("Keine uebereinstimmenden Elemente gefunden.")
    

    def Label_erstellen_Konserven(element):

        global photo_konserven
        global image_konserven
    
        # Oeffne das Bild und verkleinere es
        image_konserven = Image.open("/home/rc/ProgrammDisplay/kreis_rot_klein.png")
        image_konserven = image_konserven.resize((25, 30), resample=Image.LANCZOS)
        # Erstelle das PhotoImage-Objekt aus dem Bild
        photo_konserven = ImageTk.PhotoImage(image_konserven)
        
        # Erstelle den Namen des Labels und erstelle das Label
        name_konserven = f"label_konserven_{element}"
        globals()[name_konserven] = Label(root, image=photo_konserven)
        globals()[name_konserven].place(x=12,y=330)


    def Getraenke_abgleich():
    # Ueberprüfe jedes Element in Süßigkeiten
        for element in Getraenke:
            if element in Daten:
                print(f"Das Element {element} ist in beiden Listen vorhanden.")
                
                # Rufe die Funktion Label_erstellen auf, um das Label zu erstellen
                Label_erstellen_Getraenke(element)
            else:
                print("Keine uebereinstimmenden Elemente gefunden.")
    

    def Label_erstellen_Getraenke(element):

        global photo_getraenke
        global image_getraenke
    
        # Oeffne das Bild und verkleinere es
        image_getraenke = Image.open("/home/rc/ProgrammDisplay/kreis_rot_klein.png")
        image_getraenke = image_getraenke.resize((25, 30), resample=Image.LANCZOS)
        # Erstelle das PhotoImage-Objekt aus dem Bild
        photo_getraenke = ImageTk.PhotoImage(image_getraenke)
        
        # Erstelle den Namen des Labels und erstelle das Label
        name_getraenke = f"label_getraenke_{element}"
        globals()[name_getraenke] = Label(root, image=photo_getraenke)
        globals()[name_getraenke].place(x=145,y=290)


    def add_item():
        # Wenn das Eingabefeld nicht leer ist, füge das Element der Listbox hinzu und ruft verschiedene Abgleiche auf, zum hinzufügen der Bilder und Labels
        if eingabe.get() !="":
            listbox.insert(END, eingabe.get())
            Daten.append(eingabe.get())
            eingabe.delete(0, END)
            obst_gemuese_abgleich()
            Suessigkeiten_abgleich()
            Getraenke_abgleich()
            Konserven_abgleich()
            hide_keyboard()
        else:
            # Wenn das Eingabefeld leer ist, zeige eine Warnmeldung an und versteckt die Tastatur
            hide_keyboard()
            messagebox.showwarning("Warnung", "Bitte geben Sie etwas in das weisse Feld ein.")

    

        # Funktion um ein bestimmtes Produkt zu erkennen mit einer open source Datenbank für Lebensmittel
    def get_product_name_by_barcode(barcode):
        # API-URL mit Barcode erstellen
        api_url = "https://world.openfoodfacts.org/api/v0/product/{}.json".format(barcode)
    
        # GET-Anforderung an die API senden
        response = requests.get(api_url)
    
        # Wenn die Anfrage erfolgreich war, den Produktname aus den Daten extrahieren
        if response.status_code == 200:
            data = response.json()
            product_name = data["product"]["product_name"]
            return product_name
    
        # Andernfalls "None" zurückgeben
        else:
            return None


        # Funktion, um die Menge eines Produkts zu erkennen, das durch einen Barcode identifiziert wird, mit Hilfe einer open source Datenbank für Lebensmittel
    def get_quantity_by_barcode(barcode):
        # API-URL mit Barcode erstellen
        api_url = "https://world.openfoodfacts.org/api/v0/product/{}.json".format(barcode)
    
        # GET-Anforderung an die API senden
        response = requests.get(api_url)
    
        # Wenn die Anfrage erfolgreich war, die Daten in JSON-Format parsen und die Menge des Produkts extrahieren
        if response.status_code == 200:
            data = response.json()
            quantity = data["product"]["quantity"]
            return quantity
    
        # Andernfalls "None" zurückgeben
        else:
            return None
    
    
        # Funktion für eine Schleife zum Abfragen des Barcodescanners im Hintergrund
    def background_loop():
        print("Schleife faengt an")
        try:
            try:
                # Socket-Objekt erstellen
                socketObject = socket.socket()
                # Verbindung zum Server (in diesem Fall: localhost/barcodescanner) herstellen
                socketObject.connect(("192.168.0.100", 2003))
                print("Verbindung hergestellt")
            except Exception as e:
                print("Verbindung fehlgeschlagen")
        
            # Endlose Schleife, um kontinuierlich nach Barcodes zu suchen
            while True:
                # Schleifendurchlauf
                print("Schleife laeuft im Hintergrund")
                #time.sleep(0.05)

                # Barcode vom Scanner empfangen
                barcode = str(socketObject.recv(13))
                # socket.MSG_WAITALL
                print(barcode)

                # Produktname und Menge mithilfe der Barcode-Nummer abrufen
                product_name = get_product_name_by_barcode(barcode)
                quantity = get_quantity_by_barcode(barcode)
            
                # Wenn der Produktname gefunden wurde, füge ihn zur Liste der gescannten Produkte hinzu
                if product_name:
                    print("Product name:", product_name , "Quantity:",quantity)                    
                    listboxAusgabeScanner.insert(0, product_name)
                    gescannteProdukte.append(product_name)
                    zwScanProdukte.append(product_name)
                    global product_entfernen
                    product_entfernen = product_name
                    Daten.remove(product_entfernen)
                    
                             
                    # Entfernen des zugehörigen Labels mit dem Bild 
                    if product_entfernen in Obst:                
                        name_Obst = f"label_obst_{product_entfernen}"
                        globals()[name_Obst].grid_forget()                        
                        for i in range(listbox.size()):
                            if listbox.get(i) == product_entfernen:
                                listbox.delete(i)
                                break
                    elif product_entfernen in Suessigkeiten:
                        name_suessigkeiten = f"label_Suessigkeiten_{product_entfernen}"
                        globals()[name_suessigkeiten].destroy()                 
                                               
                        for i in range(listbox.size()):
                            if listbox.get(i) == product_entfernen:
                                listbox.delete(i)
                                break
                    elif product_entfernen in Konserven:
                        name_konserven = f"label_konserven_{product_entfernen}"
                        globals()[name_konserven].destroy()
                        for i in range(listbox.size()):
                            if listbox.get(i) == product_entfernen:
                                listbox.delete(i)
                                break
                    elif product_entfernen in Getraenke:
                        name_getraenke = f"label_getraenke_{product_entfernen}"
                        globals()[name_getraenke].destroy()
                        for i in range(listbox.size()):
                            if listbox.get(i) == product_entfernen:
                                listbox.delete(i)
                                break
                    break
                else:
                    print("Product not found.")
                    break

        except Exception as e:
            print(f"Error: {e}")


    #Diverse globale Listen für die Funktion
    global zwScanProdukte
    zwScanProdukte = [""]
    global gescannteProdukte
    gescannteProdukte = [""]
    
    global listboxAusgabeScanner
    listboxAusgabeScanner = Listbox(root, height=0)
    listboxAusgabeScanner.grid(row=1, column=5, columnspan=5,rowspan=7, sticky="nsw")
    listboxAusgabeScanner.config(font=("Courier", 32), justify="center")

    #Eine Funktion, die beim Aufrufen, diverse Buttons und die Einkaufsliste Ausblenden und dafür die Rechnungsliste einblendet
    def ausblenden_einkaufsliste():

        #Die Positionen von den nicht benötigten Elementen Löschen
        hinzufuegen.grid_forget()
        eingabe.grid_forget()
        listbox.grid_forget()
        listboxAusgabeScanner.config(height=10)

        #Daten aus der Einkaufsliste zwischen speichern
        
        global zwischenSpeichernEinkaufsliste
        zwischenSpeichernEinkaufsliste = [""]
        zwischenSpeichernEinkaufsliste.extend(Daten)

        #Neue Elemente erstellen        
        scrollbar_einkaufsliste.grid_forget()       
        Zahlen.grid(row=8,column=5,columnspan=2,rowspan=2,sticky="nesw")        
        kosten_label.grid(row=8,column=7,columnspan=3,rowspan=2,sticky="nesw")

        #Scrollbar an die linke Seite der Liste für die gescannten Produkte heften
        global scrollbar_Rechnung
        scrollbar_Rechnung = Scrollbar(root, orient="vertical", command=listboxAusgabeScanner.yview)
        scrollbar_Rechnung.grid(row=1, column=5,rowspan=7, sticky="nsw")
        listboxAusgabeScanner.configure(yscrollcommand=scrollbar_Rechnung.set)
                
        button_Rechnung()
 
    

    #Daten aus einer Liste der Listbox hinzufügen, gehört zu def ausblenden_einkaufsliste():
    def Daten_Rechnung_anfuegen():
    
        for i in zwScanProdukte:
             listboxAusgabeScanner.insert(0, i)

   
    #Einen Rand den Buttons hinzufügen
    global rand_button
    rand_button = 2
    
    #Optische und Programm technische Sachen für Buttons festlegen, gehört zu def ausblenden_einkaufsliste():
    def button_Rechnung():
        #Button deaktivieren
        Rechnung_button.config(state="disabled")
        #Button aktivieren
        einkaufsliste_button.config(state="active")
        #Optisch vertieft darstellen
        Rechnung_button.config(relief = "sunken")
        #optisch erhöht/normal darstellen
        einkaufsliste_button.config(relief = "raised")
        #optische Darstellungen aufrufen, sonst kommt es zu fehlerhafte Darstellungen
        entfernen.config(bd = rand_button)
        scannen_button.config(bd = rand_button)
        einkaufsliste_button.config(bd = rand_button,activebackground=hintergrundFarbe_Buttons, activeforeground=schriftFarbe_buttons)


    #Optische und Programm technische Sachen für Buttons festlegen, gehört zu def ausblenden_gescannteProdukte(); für genauere beschreibung bei def button_Rechnung(): nachschauen
    def button_Einkaufsliste():
        einkaufsliste_button.config(state="disabled")
        Rechnung_button.config(state="active")
        einkaufsliste_button.config(relief = "sunken")
        Rechnung_button.config(relief = "raised")
        entfernen.config(bd = rand_button)
        scannen_button.config(bd = rand_button)
        Rechnung_button.config(bd = rand_button,activebackground=hintergrundFarbe_Buttons, activeforeground=schriftFarbe_buttons)
    
    
    #Eine Funktion, die beim Aufrufen, diverse Buttons und die Rechnungsliste Ausblenden und dafür die Einkaufsliste einblendet; ähnlich wie die def ausblenden_einkaufsliste(): Funktion
    def ausblenden_gescannteProdukte():
        
        hinzufuegen.grid(row=8, column=5,columnspan=2,rowspan=2, sticky="nesw")
        eingabe.grid(row=8, column=7,columnspan=3,rowspan=2, sticky="nesw")
        listbox.grid(row=1, column=5, columnspan=5,rowspan=7, sticky="nsw")
        scrollbar_listbox()
        Zahlen.grid_forget()
        kosten_label.grid_forget()
        listboxAusgabeScanner.config(height=0)
        scrollbar_Rechnung.grid_forget()
        Daten_listbox_anfuegen()
        button_Einkaufsliste()
    
    #Funktion für die Scrollbar der Einkaufsliste; gehört zu def ausblenden_gescannteProdukte():
    def scrollbar_listbox():
        global scrollbar_einkaufsliste
        scrollbar_einkaufsliste = Scrollbar(root, orient="vertical", command=listbox.yview)
        scrollbar_einkaufsliste.grid(row=1, column=5,rowspan=7, sticky="nsw")
        listbox.configure(yscrollcommand=scrollbar_einkaufsliste.set)
    
    #Funktion um Produkte aus einer globalen Liste, der Einkaufsliste hinzufügen; gehört zu def ausblenden_gescannteProdukte():
    def Daten_listbox_anfuegen():
        global Daten
        Daten.sort(key=str.lower)
    
        for i in zwischenSpeichernEinkaufsliste:
            if i not in Daten and not " ":
               listbox.insert(END, i)


    #Thread von der Scanner Schleife starten
    def scannen():
        print("Scannen starten")
        thread = threading.Thread(target=background_loop)
        thread.start()
    
    
    #Oberfläche der grafik, Größe und die Rastergröße und Menge einstellen
    
    root.geometry("1024x600")
    for i in range(12):
                root.grid_rowconfigure(i, minsize=50,weight=1)

    for i in range(9):
                    root.grid_columnconfigure(i, minsize=100,weight=1)

    

    #Farben der Buttons ändern
    hintergrundFarbe_Buttons = "darkblue"
    schriftFarbe_buttons = "white"

    #Element zum aufnehmen des Bildes vom Grundriss
    canvas = Canvas(root)
    canvas.grid(row=0, column=0, rowspan=12, columnspan=5, sticky="nesw")

    #Bild hochladen und erstellen, und resizen des Bildes
    image = Image.open("/home/rc/ProgrammDisplay/Einkaufsladen_grundriss_V3.png")
    image = image.resize((500, 600), resample=Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(1, 1, anchor=NW, image=photo)

    #Einkaufsliste Listbox mit scrollbar
    listbox = Listbox(root)
    listbox.grid(row=1, column=5, columnspan=5,rowspan=7, sticky="nsw")
    scrollbar_listbox()

    #Schriftgröße für die Buttons allgemein
    Schriftgroesse = font.Font(size=20)
    #Schriftgröße für extra große Schriften
    Schriftgroesse2 = font.Font(size=30)

    #Entfernen button anlegen zum entfernen eines elements aus der oberen listbox
    entfernen = Button(root,bd = rand_button, text="Entfernen", command=delete_item, font=Schriftgroesse, bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
    entfernen.grid(row=10, column=5,columnspan=2,rowspan=2, sticky="nesw")

    #hinzufügen button anlegen zum hinzufügen eines Elements zur listbox, welches im eingabefeld enthalten ist
    hinzufuegen = Button(root,bd = rand_button, text="Hinzufuegen", command=add_item, font=Schriftgroesse,bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
    hinzufuegen.grid(row=8, column=5,columnspan=2,rowspan=2, sticky="nesw")
    
   
    #Zahlen Button anlegen, zum zahlen der Rechnung an der Kasse oder per Paypal
    Zahlen = Button(root, bd = rand_button, text="Zahlen", command=restart_programm, font=Schriftgroesse2, bg=hintergrundFarbe_Buttons, fg = schriftFarbe_buttons)
    Zahlen.grid(row=8, column=5,columnspan=2,rowspan=2, sticky="nesw")
    Zahlen.grid_forget()

    #eingabefeld 
    eingabe = Entry(root,font=("Arial",20))
    eingabe.grid(row=8, column=7,columnspan=3,rowspan=2, sticky="nesw")

    #Beispiel Liste und Produkte der Listbox hinzufügen

    Daten = ["Ice Fresh","Hanuta Minis","Lach gummi minis","Nimm2 240G","Kinder Schoko-Bons" ,"Happy Easter","Pflaume","Tomaten gehackt","Ravioli","Coca-Cola","Apfelschorle"]
    for item in Daten:
        listbox.insert(END, item)
    gescannteProdukte = [""]

    #Größe der Schrift ändern
    listbox.config(font=("Courier", 32), justify="right")
    
    #Button zum sarten des Scannvorgangs
    scannen_button = Button(root,bd = rand_button, text="Scannen", command=scannen, font=Schriftgroesse2,bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
    scannen_button.grid(row=10, column=7, columnspan=3,rowspan=2, sticky="nesw")

    #Button um die Einkaufsliste einzublenden
    einkaufsliste_button = Button(root,bd = rand_button, text="Einkaufsliste", command=ausblenden_gescannteProdukte, font=Schriftgroesse,bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
    einkaufsliste_button.grid(row=0, column=5, columnspan=2,rowspan=1, sticky="nesw")
    einkaufsliste_button.config(state="disabled")

    #Button um die Rechnungsliste einblenden
    Rechnung_button = Button(root,bd = rand_button, text="Rechnung", command=ausblenden_einkaufsliste, font=Schriftgroesse,bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
    Rechnung_button.grid(row=0, column=7, columnspan=3,rowspan=1, sticky="nesw")


    #Virtuelle Tastatur erstellen, beim "klicken" in das eingabe Feld
    class Keyboard(Frame):
        def __init__(self, master=None, target=None, font_size=16):
            Frame.__init__(self, master)
            self.grid()
            self.target = target
            self.font_size = font_size
            self.create_widgets()
        

        #Funktion zum kreieren der Buttons und der Namen
        def create_widgets(self):

            button_font = font.Font(size=self.font_size)
            buttons = [
            
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                'z', 'x', 'c', 'v', 'b', 'n', 'm', '<--','Esc'
            ]
        
            row = 0
            col = 0
            #Gestaltung wie viele Buttons in einer Reihe und wie viele zeilen
            for button in buttons:
                command = lambda x=button: self.click(x)
                Button(self, text=button, width=2, height=1, fg=schriftFarbe_buttons, command=command,bg=hintergrundFarbe_Buttons, font=button_font).grid(row=row, column=col)
                col += 1
                if col >9:
                    row += 1
                    col = 0
        

        #Funktion was beim klicken eines buttons passiert, vorallem beim zurückpfeil und ESC buttons
        def click(self, key):
            global text
            text = ""
            if key == '<--':
                text = self.target.get()[:-1]
            elif not key == 'Esc':
                text = self.target.get() + key
            else:
                hide_keyboard()
            self.target.delete(0, END)
            self.target.insert(0, text)
    
    #Tastatur auf nichts setzen
    keyboard = None


    #Funktion zum erscheinen lassen der Tastatur
    def show_keyboard(event):
        global keyboard
        if keyboard is not None and keyboard.withdraw() == True:
            # Keyboard ist bereits geöffnet
            return
        
        keyboard = Toplevel(root)
        keyboard.title("Tastatur")
        #Größe der Schrift der Buttons/Größe der Buchstaben
        Keyboard(keyboard, target=event.widget, font_size=35).pack()
        #Farbe der Tastatur festlegen
        keyboard.configure(bg=hintergrundFarbe_Buttons)
        #Erscheinungsposition und andere Features der Tastatur festlegen
        keyboard.geometry("+0+0")
        keyboard.wm_attributes("-topmost",1)
        keyboard.wm_attributes("-type","splash")
        #Tastatur vor das Hauptfenster legen
        keyboard.lift()
    
    #Funktion zum "verstecken" der Tastatur 
    def hide_keyboard():
        global keyboard
        keyboard.withdraw()
    
    #Das Eingabefeld mit der funktion zum ERscheinen lassen der Tastatur verbinden
    eingabe.bind('<Button-1>', show_keyboard)
    if keyboard is not None:
        keyboard.protocol("WM_DELETE_WINDOW",hide_keyboard())
    
    #Listen zum abgleichen mit der Einkaufsliste
    global Obst
    Obst = ["Kirsche","Pflaume","Apfel","Kiwi","Erdbeeren","Ananas","Trauben"]
    global Gemuese
    Gemuese = ["Gurke", "Tomate","Kuerbis","Blumenkohl","Karotten","Zucchini","Kolrabi"]
    global Getraenke
    Getraenke = ["Coca-Cola","Apfelschorle","Wasser"]
    global Fleisch
    Fleisch = [""]
    global Konserven
    Konserven = ["Tomaten gehackt","Ravioli","Gewuerzgurken"]
    global Nudeln
    Nudeln = ["Fusilli"]
    global Suessigkeiten 
    Suessigkeiten = ["Nutella","Hanuta Minis","Lach gummi minis","Nimm2 240G","Kinder Schoko-Bons","Pringles","Happy Easter","Ice Fresh",'Duplo']

    #Funktionen zum abgleich beim initialisieren aufrufen
    obst_gemuese_abgleich()
    Suessigkeiten_abgleich()
    Konserven_abgleich()
    Getraenke_abgleich()
    
    #Funktion die das Fenster der Erklärungen schließt
    def schliesse_Erklaerungen():
        Erklaerungen.destroy()
        root.lift()
    
    #Funktion die ein Fenster im Fullscreen erstellt, in dem verschiedene Funktionen des Programms erklärt werden.
    def zeige_Erklaerungen():

        #Erstellung des Fensters mit verscheidenen Eigenschaften z.B. Fullscreen
        global Erklaerungen
        Erklaerungen = Toplevel(root)
        Erklaerungen.title("Erklaerungen zu den Funktionen")
        Erklaerungen.attributes("-fullscreen"  , True)
        Erklaerungen.lift(root)
        Erklaerungen_schriftgroesse = font.Font(size=15)

        #Alle Bilder Variablen global machen
        global image_laden_klein
        global photo_laden_klein
        global image_kreis_rot
        global photo_kreis_rot
        global image_scannen
        global photo_scannen
        global image_fragezeichen
        global photo_fragezeichen
        global image_entfernen
        global photo_entfernen
        global image_hinzufuegen
        global photo_hinzufuegen
        global image_zahlen
        global photo_zahlen

        #Die Bilder öfnen, aufrufen und an die benötigte Größe anpassen
        image_fragezeichen = Image.open("/home/rc/ProgrammDisplay/fragezeichen2.png")
        image_fragezeichen = image_fragezeichen.resize((120, 80), resample=Image.LANCZOS)
        photo_fragezeichen = ImageTk.PhotoImage(image_fragezeichen)
        image_laden_klein = Image.open("/home/rc/ProgrammDisplay/Einkaufsladen_klein.png")
        image_laden_klein = image_laden_klein.resize((120, 60), resample=Image.LANCZOS)
        photo_laden_klein = ImageTk.PhotoImage(image_laden_klein)
        image_kreis_rot = Image.open("/home/rc/ProgrammDisplay/kreis_rot.png")
        image_kreis_rot = image_kreis_rot.resize((60, 70), resample=Image.LANCZOS)
        photo_kreis_rot= ImageTk.PhotoImage(image_kreis_rot)
        image_scannen = Image.open("/home/rc/ProgrammDisplay/Bild_Scannen.png")
        image_scannen = image_scannen.resize((120, 60), resample=Image.LANCZOS)
        photo_scannen = ImageTk.PhotoImage(image_scannen)
        image_entfernen = Image.open("/home/rc/ProgrammDisplay/Bild_Entfernen.png")
        image_entfernen = image_entfernen.resize((120, 60), resample=Image.LANCZOS)
        photo_entfernen = ImageTk.PhotoImage(image_entfernen)
        image_hinzufuegen = Image.open("/home/rc/ProgrammDisplay/Bild_Hinzufuegen.png")
        image_hinzufuegen = image_hinzufuegen.resize((120, 60), resample=Image.LANCZOS)
        photo_hinzufuegen = ImageTk.PhotoImage(image_hinzufuegen)
        image_zahlen = Image.open("/home/rc/ProgrammDisplay/Bild_Zahlen.png")
        image_zahlen = image_zahlen.resize((120, 60), resample=Image.LANCZOS)
        photo_zahlen = ImageTk.PhotoImage(image_zahlen)

        #Abstand zwischen den Zeilen
        yabstand = 5

        #Labels für die verschiedenen Erklärungen erstellen
        ueberschrift_bild = Label(Erklaerungen, image =photo_fragezeichen )
        ueberschrift_bild.grid(row = 0, column=0, pady=yabstand)
        Ueberschrift_Label = Label(Erklaerungen, font = 30, text="Erklaerungen zu den Funktionen")
        Ueberschrift_Label.grid(row = 0, column=1, pady=yabstand)
        Hintergrund_Label = Label(Erklaerungen, image=photo_laden_klein)
        Hintergrund_Label.grid(row=2,column=0,pady = yabstand)
        Text_Hintergrund_Label=Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- befindet der Grundriss des Einkaufladens in dem Sie sich befinden.")
        Text_Hintergrund_Label.grid(row=2,column=1, pady=yabstand)
        Kreis_Label = Label(Erklaerungen, image=photo_kreis_rot)
        Kreis_Label.grid(row=3,column=0, pady=yabstand)
        Text_Kreis_Label = Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- Anzeige von Produkten aus der Einkaufsliste an ihren Standorten im Einkaufsladen.")
        Text_Kreis_Label.grid(row=3,column=1, pady=yabstand)
        Scannen_Label = Label(Erklaerungen, image=photo_scannen)
        Scannen_Label.grid(row=4,column=0, pady=yabstand)
        Text_scannen_Label = Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- Starten des Scanvorgangs.")
        Text_scannen_Label.grid(row=4,column=1, pady=yabstand)
        Entfernen_Label = Label(Erklaerungen, image=photo_entfernen)
        Entfernen_Label.grid(row=5,column=0, pady=yabstand)
        Text_Entfernen_Label = Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- Entfernen von Artikeln aus der Einkaufsliste oder Rechnung.")
        Text_Entfernen_Label.grid(row=5,column=1, pady=yabstand)
        hinzufuegen_Label = Label(Erklaerungen, image=photo_hinzufuegen)
        hinzufuegen_Label.grid(row=6,column=0, pady=yabstand)
        Text_hinzufuegen_Label = Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- Artikel der Einkaufsliste hinzufuegen.")
        Text_hinzufuegen_Label.grid(row=6,column=1, pady=yabstand)
        zahlen_Label = Label(Erklaerungen, image=photo_zahlen)
        zahlen_Label.grid(row=7,column=0, pady=yabstand)
        Text_zahlen_Label = Label(Erklaerungen,font=Erklaerungen_schriftgroesse, text=" <----- Den gesammten Einkauf bezahlen.")
        Text_zahlen_Label.grid(row=7,column=1, pady=yabstand)
        Verstanden_Button = Button(Erklaerungen,bd = rand_button, font = 20, text="Verstanden", command=schliesse_Erklaerungen,bg=hintergrundFarbe_Buttons, fg=schriftFarbe_buttons)
        Verstanden_Button.grid(row=8, rowspan=2, column=1, pady=yabstand)
    
    #Die Fenster funktion aufrufen
    zeige_Erklaerungen()
    
    
    
    #Gesamt Kosten der Rechnung anzeigen
    kosten_label = Label(root, font=("Arial",20))
    #kosten_label.config(text = kosten + preis)
    kosten_label.grid(row=8,column=7,columnspan=3,rowspan=2,sticky="nesw")
    kosten_label.grid_forget()
    
    #Durchlauf des Programms
    root.mainloop()

    #Benötigt für dauerhaften Fullscreen
    pass


