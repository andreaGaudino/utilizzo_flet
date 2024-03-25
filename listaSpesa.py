import flet as ft

def main(page: ft.Page):
    #Riga 1

    def addCheckBox(e):
        strToAdd = txtIn.value
        txtIn.value = ""
        if strToAdd == "":
            return
        page.add(ft.Checkbox(label=strToAdd, value=False))


    txtIn = ft.TextField(label="Aggiungi un elemento")
    btnAdd = ft.CupertinoButton(text="Add", on_click=addCheckBox)
    row1 = ft.Row([txtIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

    pass

ft.app(target=main, view = ft.AppView.FLET_APP)