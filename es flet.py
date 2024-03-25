import flet as ft
from time import sleep

def main(page:ft.Page):
    textIn = ft.Text(value="Bella", color="red") #così creo l'oggetto che inserirò nella pagina di visualizzazioen
    page.controls.append(textIn)
    page.update()
    #txtOut = ft.Text(value="Counter:", color="red")
    #page.add(txtOut) #istruzione equivalente alle due sopra(appende e aggiorna)

    """"for i in range(1,100):
        txtOut.value = "Counter: "+str(i)
        txtOut.update()
        sleep(1)
    """""


    def handleBottone(e):
        lv.controls.append(ft.Text("Tasto cliccato!"))
        lv.update()

    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleBottone) #bottone che funziona con la funzione handleBottone
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="blue", size=24)
    page.add(row1, txtOut)

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)

ft.app(target=main, view = ft.AppView.FLET_APP)