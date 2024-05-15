import os

from talon import Context, Module, screen, ui, ctrl, actions

mod = Module()

@mod.action_class
class Actions:
    def mouse_to_screen_edge(hnd_pos: str, ms: int = 350):
        """moved mouse to one of eight positions on edge of the screen"""
        screen = ui.main_screen()
        left = 0
        right = screen.width - 1
        hz_center = int(screen.width / 2)
        top = 0
        bottom = screen.height - 1
        vrt_center = int(screen.height / 2)
        pos = {
            'center': (hz_center,vrt_center),
            'left': (left,vrt_center),
            'right': (right,vrt_center),
            'top': (hz_center,top),
            'bottom': (hz_center,bottom),
            'lower left': (left,bottom),
            'upper left': (left,top),
            'lower right': (right,bottom),
            'upper right': (right,top)
        }
        x = pos[hnd_pos][0]
        y = pos[hnd_pos][1]
        actions.user.slow_mouse(x,y)
#
ctx = Context()
