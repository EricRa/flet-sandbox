import flet as ft

def main(page: ft.Page):
    greeting = ft.Text(value="Welcome!", color ="blue")
    page.controls.append(greeting)
    page.update()

    greeting2 = ft.Text(value="This is apparently a Flet app.", color="red")
    page.add(greeting2) #this is a shortcut for the page.controls.append + page.update syntax above
    

ft.app(target=main)