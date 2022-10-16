# I'm actually proud of this module - made by andrew

import asyncio
import os
import time

from src.helper.asian import clamp


class Page:
    border = ""

    def __init__(self, border=True, title=None, text=None, custom_border="-", border_size=None, border_min=None,
                 border_max=None, center_title=True, center_title_character=" "):
        add_border = border

        self.buffer = []

        if text is None:
            text = []

        if border_size is None:
            border_size = len(max([title] + text, key=len))

        if center_title:
            title = title.center(border_size, center_title_character)

        border = custom_border * clamp(border_size, border_min, border_max)

        if add_border:
            self.buffer.append(border)

        if title is not None:
            self.buffer.append(title)
            if text is not None:
                self.buffer.append("")

        self.buffer += text

        if add_border:
            self.buffer.append(border)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class __Renderer:

    def __init__(self, splash=None):
        self.buffer = []
        if splash is not None:
            self.set_page(splash)

    def refresh(self):
        clear()
        for i in self.buffer:
            if isinstance(i, str):
                print(i)
            else:
                i()

    def set_buffer(self, buffer, refresh=True):
        self.buffer = buffer

        if refresh:
            self.refresh()

    def set_page(self, page: Page):
        self.buffer = [page.border] + page.buffer + [page.border]
        self.buffer += []
        self.refresh()

    def input(self, prompt):
        print(prompt, end="")

        def buffer_func():
            print(prompt, end="")

        self.buffer.append(buffer_func)
        i = input()
        self.buffer.remove(buffer_func)
        return i

    def print(self, text):
        print(text)

        self.buffer.append(
            text
        )

    def animate(self, callback, interval=0.1):
        async def loop():
            # end the loop if the callback returns false
            while callback(self) is None:
                time.sleep(interval)
                clear()
                self.refresh()

        asyncio.run(loop())


class Animation:
    def __init__(self, frames=[], interval=.5, length=5000):
        self.interval = interval
        self.frames = frames
        self.length = length

    def compile(self):
        i=0
        while True:
            yield self.frames[i % len(self.frames)]
            i+=1