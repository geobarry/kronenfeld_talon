# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:29:11 2023

@author: Administrator
"""

from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def pan_arcgis_pro_map(direction: str, duration: int):
        """Pans the map for duration expressed relative to the default duration 
        which is 0.5 seconds."""
        if direction == 'west':
            key = 'left'
        elif direction == 'east':
            key = 'right'
        elif direction == 'north':
            key = 'up'
        elif direction == 'south':
            key = 'down'
        else:
            return None
        actions.key("{}:down".format(key))
        print("pan_arcgis_pro_map duration: {}".format(duration))
        actions.sleep(duration * 0.5)
        actions.key("{}:up".format(key))