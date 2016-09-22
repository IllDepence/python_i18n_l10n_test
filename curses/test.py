# -*- coding: utf-8 -*-

import gettext
import curses
import sys

NAV_U = 'k'
NAV_D = 'j'
NAV_L = 'h'
NAV_R = 'l'

lang = {}
lang['en_US'] = gettext.translation('test', languages=['en_US'], localedir='translations', fallback='false')
lang['de_DE'] = gettext.translation('test', languages=['de_DE'], localedir='translations', fallback='false')
lang['ja_JA'] = gettext.translation('test', languages=['ja_JA'], localedir='translations', fallback='false')
lang['en_US'].install()

class Screen():
    def set(scr):
        Screen.scr = scr
        Screen.update()
    def update():
        (y_max,x_max) = Screen.scr.getmaxyx()
        end_screen = y_max-2
        Screen.y_max = y_max
        Screen.x_max = x_max
        Screen.end_screen = end_screen
    def get():
        return Screen.scr

class Menu():
    def __init__(self):
        self.y_offset = 5
        self.cursor = self.y_offset
        self.x_offset = 10
        self.menu_items = []
    def draw(self):
        scr = Screen.get()
        scr.addstr(self.y_offset-1, self.x_offset, _('### L A N G U A G E ###'))
        for row in range(self.y_offset, self.y_offset+len(self.menu_items)):
            if self.cursor == row: scr.standout()
            scr.addstr(row, self.x_offset, _(self.menu_items[self.y_offset-row]['label']))
            if self.cursor == row: scr.standend()
    def add(self, itm):
        self.menu_items.append(itm)
    def nav(self, delta):
        self.cursor = self.cursor + delta
    def getUnderCursor(self):
        return self.menu_items[self.y_offset-self.cursor]

class Border():
    def draw(self):
        scr = Screen.get()
        for row in range(Screen.end_screen):
            for col in range(Screen.x_max):
                char = ' '
                if row == 0 or row == Screen.end_screen-1:
                    if col == 0 or col == Screen.x_max-1:
                        char = '+'
                    else:
                        char = '-'
                else:
                    if col == 0 or col == Screen.x_max-1:
                        char = '|'
                scr.addstr(row, col, char)

def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.clear()

    Screen.set(stdscr)
    border = Border()
    menu = Menu()
    menu.add({'label':_('English'),'locale':'en_US'})
    menu.add({'label':_('German'),'locale':'de_DE'})
    menu.add({'label':_('Japanese'),'locale':'ja_JA'})

    c=None

    while c != 'q':
        stdscr.move(0,0)

        border.draw()
        menu.draw()

        c = stdscr.getkey()
        if c=='KEY_RESIZE':
            stdscr.clear() # to prevent "residual" bottom lines
            Screen.update()
        if c==NAV_U:
            menu.nav(-1)
        if c==NAV_D:
            menu.nav(1)
        if c=='\n':
            locale = menu.getUnderCursor()['locale']
            lang[locale].install()

if __name__ == '__main__':
    curses.wrapper(main)
