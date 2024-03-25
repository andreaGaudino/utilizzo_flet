import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def handleRemove(e):
        currentVal = txtOut.value
        txtOut.value = currentVal - 1
        txtOut.update()
        pass
    def handleAdd(e):
        currentVal = txtOut.value
        txtOut.value = currentVal+1
        txtOut.update()
        pass


    btnMinus = ft.IconButton(icon=ft.icons.REMOVE, icon_color="green", icon_size=24, on_click=handleRemove)
    btnAdd= ft.IconButton(icon=ft.icons.ADD,
                          icon_color="green",
                          icon_size=24,
                          on_click=handleAdd)
    txtOut = ft.TextField(width=200, disabled=True, border_color="green",
                          value=0,
                          text_align=ft.TextAlign.CENTER)

    row1 = ft.Row([btnMinus, txtOut, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

ft.app(target=main, view = ft.AppView.FLET_APP)