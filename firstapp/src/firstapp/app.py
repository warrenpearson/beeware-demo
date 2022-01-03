"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import requests


class FirstApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.url_input = toga.TextInput(style=Pack(flex=1))

        url_button = toga.Button(
            "Go!",
            on_press=self.say_hello,
            style=Pack(padding=(5,3), width=50, alignment="right"),
        )

        loc_box = toga.Box(style=Pack(direction=ROW, padding=15))
        loc_box.add(self.url_input)
        loc_box.add(url_button)

        self.webview = toga.WebView(
            url="https://apple.com",
            style=Pack(padding=(10, 10), width=1024, height=780),
        )

        main_box.add(loc_box)
        main_box.add(self.webview)

        self.main_window = toga.MainWindow(
            title="My great web browser!",
            position=(200, 400),
            size=(1044, 800),
            toolbar=None,
            resizeable=True,
        )
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print("Loading", self.url_input.value)
        content = requests.get(self.url_input.value)
        self.webview.set_content(self.url_input.value, content.text)


def main():
    return FirstApp()
