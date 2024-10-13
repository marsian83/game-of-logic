# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from config import state_colors, font

class Trilateral():
    def __init__(self, x, y, w=None, h=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        self.state = [0, 1, 1, 2, 2, 3, 3, 0]
        self.rects = []
        self.tips = [
                    "x, not m, y", 
                    "x, m, y",
                    "x, not m, not y", 
                    "x, m, not y",
                    "not x, not m, y", 
                    "not x, m, y",
                    "not x, not m, not y", 
                    "not x, m, not y",
                    ]

        side = 0
        if h is None and w is not None:
            side = w // 2
        if w is None and h is not None:
            side = h // 2
        if w is not None and h is not None:
            if w > h:
                side = h // 2
            else:
                side = w // 2

        mid_side = side // 2
        
        self.rects.append(pygame.Rect((x, y), (side, side)))
        self.rects.append(pygame.Rect((x + mid_side, y + mid_side), (mid_side, mid_side)))

        self.rects.append(pygame.Rect((x + side, y), (side, side)))
        self.rects.append(pygame.Rect((x + side, y + mid_side), (mid_side, mid_side)))
        
        self.rects.append(pygame.Rect((x, y + side), (side, side)))
        self.rects.append(pygame.Rect((x + mid_side, y + side), (mid_side, mid_side)))
        
        self.rects.append(pygame.Rect((x + side, y + side), (side, side)))
        self.rects.append(pygame.Rect((x + side, y + side), (mid_side, mid_side)))


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        tooltip = ""
        for i, rect in enumerate(self.rects):
            pygame.draw.rect(self.gameDisplay, state_colors[self.state[i]], rect)
            if rect.collidepoint(mouse_pos):
                tooltip = self.tips[i]
        
        tooltip = font.render(tooltip, True, (0, 0, 0))
        pygame.Surface.blit(tooltip, mouse_pos)

        # for event in game.events:
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         for i, rect in enumerate(self.rects):
                    
