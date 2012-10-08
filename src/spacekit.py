"""The SpaceKit astrodynamics toolkit.

This module imports the following classes:
Axes - A set of axes.
CoordinateSystem - A coordinate system (origin and axes).
Point - A point in space.
Spacecraft - A physical spacecraft.
State - The state (position and velocity) of a point.

"""

# Physical things

class Point:
    """A point in space.

    name - The name of the point.
    state - The position and velocity of the point.

    """
    
    def __init__(self, name=''):
        self.state = State()

class Universe:
    """A universe."""

    def __init__(self):
        self._participants = []

    def add(self, participant):
        self._participants.append(participant)

class State:
    """The state (position and velocity of a point.

    cartstate - The Cartesian position and velocity.
    cs - The coordinate system in which the state is defined.
    
    """
    
    def __init__(self):
        self.cartstate = [0, 0, 0, 0, 0, 0]

class CoordinateSystem:
    """A coordinate system (origin and axes).

    origin - The origin of the system.
    axes - The axes of the system.

    """

    def __init__(self):
        pass

class Axes:
    """A set of axes."""

    def __init__(self):
        pass

# Set up default objects

universe = Universe()
universe.add(Point(name='Sun'))
universe.add(Point(name='Earth'))
