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

import config

from components.Bilateral import Bilateral


def view(game):
    vw = game.vw
    vh = game.vh

    buttons = []
    bilateral = Bilateral(vw(50) - vh(30), vh(50) - vh(25), h = vh(60))

    def update():
        bilateral.update()
        
        for btn in buttons:
            btn.update()

    game.update_function = update