#
#    Copyright (C) 2016 Dang Duong
#
#    This file is part of Open Tux World.
#
#    Open Tux World is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Open Tux World is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Open Tux World.  If not, see <http://www.gnu.org/licenses/>.
#
def check_item_previous(own, item_number):
    if item_number == 0:
        return 0
    elif item_number == 3 or item_number < 0:
        if own["fish"] > 0:
            return 3
        else:
            return check_item_previous(own, 2)
    elif item_number == 2:
        if own["ice"] > 0:
            return 2
        else:
            return check_item_previous(own, 1)
    else:
        if own["snow"] > 0:
            return 1
        else:
            return 0

def check_item_next(own, item_number):
    if item_number == 0 or item_number > 3:
        return 0
    elif item_number == 1:
        if own["snow"] > 0:
            return 1
        else:
            return check_item_next(own, 2)
    elif item_number == 2:
        if own["ice"] > 0:
            return 2
        else:
            return 0
    else:
        if own["fish"] > 0:
            return 3
        else:
            return 0

def main(own, previous, next):
    item = own["item"]
    if previous:
        item = check_item_previous(own, item-1)
    elif next:
        item = check_item_next(own, item+1)
    else:
        item = check_item_previous(own, item)
    own["item"] = item
