import flet as ft
import requests

def main (page):
    page.title = "Погода"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label="Введите город", width=400)
    weather_data = ft.Text("")

    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = "47dcbb1b2db7e3ea32bb1ede4150205d"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric"
        res = requests.get(URL).json()
        temp = res["main"]["temp"]
        weather_data.value = "Погода: " + str(temp)
        page.update()

    def change_theme(e):
        page.theme_mode = "Light" if page.theme_mode == "Dark" else "Dark"
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text("Weather")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Получить", on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)

    )




ft.app(target=main)