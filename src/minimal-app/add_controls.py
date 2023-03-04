import flet as ft
import time

def main(page: ft.Page):
    greeting = ft.Text(value="Welcome!", color ="blue")
    page.controls.append(greeting)
    page.update()

    greeting2 = ft.Text(value="This is apparently a Flet app.", color="red")
    page.add(greeting2) #this is a shortcut for the page.controls.append + page.update syntax above

    step_text = ft.Text()
    page.add(step_text)

    for i in range(2):
        step_text.value = f"Step {i}"
        page.update()
        time.sleep(1)

    # Row is another container control (like page).  It allows arranging other controls in a row one-by-one.
    page.add(
        ft.Row(controls=[
            ft.Text("I'm row 1."),
            ft.Text("I'm row 2."),
            ft.Text("I'm row 3.")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name here"),
            ft.ElevatedButton(text="What's my name?")
        ])
    )

    # You can batch in new elements to the page by waiting to call page.update()
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

ft.app(target=main)