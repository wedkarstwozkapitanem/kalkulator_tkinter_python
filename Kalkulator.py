from tkinter import Tk, PhotoImage, Frame, Label, Button,PhotoImage


class Kalkulator:
    def poczotkoweUstawienia(self):
        self.dzialanie = str("0")
        self.okno.resizable(False,False)

        self.ikonka = PhotoImage(file="icon.png")
        self.okno.iconphoto(False, self.ikonka)

        self.okno.title("Kalkulator kapitana")
        self.okno.geometry(f"{self.dlugosc}x{self.wysokosc}")
        self.okno.config(bg="black")
        self.renderuj()

    def nowyPrzycisk(self, x, row, col,czyZnak=False):
        color = "#2b2e2c"
        if x != "C":
            funkcja = lambda:  self.ustawWynik(str(x),czyZnak)
        else:
            funkcja = self.wyczysc
            color = "red"

        przycisk = Button(self.akcje, text=x, fg="green", bg=color,
                          command= funkcja, font=("Arial", int(self.dlugosc / 10)), width=3)
        przycisk.grid(row=row, column=col, padx=3, pady=1)

    def renderuj(self):
        self.l = 0
        self.oknoKalkulatora = Frame(self.okno).grid(row=0, column=0)
        self.wynik = Label(self.oknoKalkulatora, bg="#141414", fg="white",text=self.dzialanie,
                           font=("Arial", 68), width=8,takefocus=1)
        self.wynik.grid(row=0, column=0, columnspan=5)

        # Przyciski liczbowe
        self.przyciski = list(range(9))
        k = 1
        self.liczby = Frame(self.oknoKalkulatora)
        for i in self.przyciski:
            Button(self.liczby, bg="#2b2e2c", fg="white", text=i + 1,
                   font=("Arial", int(self.dlugosc / 8)), takefocus=1, activebackground="green",
                   command=lambda i=i + 1: self.ustawWynik(str(i))
                   ).grid(row=k + 3, column=i % 3, padx=3, pady=3)
            if i % 3 == 2:
                k += 1
        Button(self.liczby, bg="#2b2e2c", fg="white", text=0,
               font=("Arial", int(self.dlugosc / 8)), takefocus=1, activebackground="green",
               command=lambda i=i + 1: self.ustawWynik(str(0))
               ).grid(row=7, column=0, padx=1, pady=3)
        self.liczby.grid(column=0, row=1, columnspan=3)
        Button(self.liczby, bg="#2b2e2c", fg="white", text=".",width=2,
               font=("Arial", int(self.dlugosc / 8)), takefocus=1, activebackground="green",
               command=lambda: self.ustawWynik(str("."))
               ).grid(row=7, column=1, padx=1, pady=3)
        self.liczby.grid(column=0, row=1, columnspan=3)
        # Przyciski operacyjne
        Button(self.liczby, bg="blue", fg="white", text="=",
               font=("Arial", int(self.dlugosc / 8)), takefocus=1, activebackground="green",
               command=self.wynikDzialania
               ).grid(row=7, column=2, padx=1, pady=3)

        self.akcje = Frame(self.oknoKalkulatora)
        przyciski_akcje = ["C", "+", "-", "*", "/"]
        for idx, val in enumerate(przyciski_akcje):
            self.nowyPrzycisk(val, idx, 0,True)
        self.akcje.grid(column=3, row=1, rowspan=5)

        self.czyZnak = bool(False)

    def wyczysc(self):
        global dzialanie
        self.czyZnak = False
        self.wynik.config(fg="white")
       # self.dzialanie = ""
        if(len(str(self.dzialanie))>1):
            self.dzialanie = str(self.dzialanie)
            self.dzialanie = self.dzialanie[:-1]
        else:
            self.dzialanie = 0
        self.wynik.config(text=self.dzialanie)

    def ustawWynik(self,x,czyZnak=False):
        global dzialanie
        self.wynik.config(fg="white")
        if x != "":
            self.dzialanie = str(self.dzialanie)
            if not self.czyZnak and czyZnak:
                if czyZnak:
                    self.czyZnak = True
                self.dzialanie += str(x)
            elif not czyZnak:
                self.dzialanie += str(x)
                self.czyZnak = False
            else:
                self.dzialanie = self.dzialanie[:-1] + str(x)
        if len(str(self.dzialanie)) >= 1:
            if self.dzialanie[0] == "0" and x != ".":
                self.dzialanie = self.dzialanie[1:]

            self.wynik.config(text=str(self.dzialanie))

        else:
            self.wynik.config(text=str(self.dzialanie))

    def wynikDzialania(self):
        global dzialanie
        self.blod = False
        try:
            self.dzialanie = str(eval(str(self.dzialanie)))
        except ZeroDivisionError:
            self.blod = True
            self.dzialanie = ""
            self.wynik.config(text=str("Nie dziel przez 0!"), fg="red")
        except ArithmeticError:
            self.blod = True
            self.dzialanie = ""
            self.wynik.config(text=str("błąd artymetryczny!"), fg="red")
        except RuntimeError:
            self.blod = True
            self.dzialanie = ""
            self.wynik.config(text=str("błąd!"), fg="red")
        except SyntaxError:
            self.blod = True
            self.dzialanie = ""
            self.wynik.config(text=str("błąd składniowy!"), fg="red")
        finally:
            if not self.blod:
                if len(self.dzialanie) <= 5:
                    self.wynik.config(text=str(self.dzialanie))
                else:
                    self.dzialanie = round(float(self.dzialanie), 5)
                    self.wynik.config(text=str(self.dzialanie) + "...")
                self.wynik.config(font=("Arial", 68), width=8,height=1)
            else:
                self.wynik.config(font=("Arial",40),width=14,height=2)
    def __init__(self, wysokosc, dlugosc):
        self.wysokosc = wysokosc
        self.dlugosc = dlugosc
        self.okno = Tk()
        self.poczotkoweUstawienia()
        self.okno.mainloop()


if __name__ == "__main__":
    kalkulator = Kalkulator(690, 428)
