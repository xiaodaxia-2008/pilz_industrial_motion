#! /usr/bin/python

# Copyright (c) 2018 Pilz GmbH & Co. KG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class RobotVersionError(Exception):
    pass


class RobotMultiInstancesError(Exception):
    pass


class RobotMoveAlreadyRunningError(Exception):
    pass


class RobotMoveFailed(Exception):
    pass


class RobotMoveInvalidState(Exception):
    pass


class RobotUnknownCommandType(Exception):
    pass


class RobotCurrentStateError(Exception):
    pass