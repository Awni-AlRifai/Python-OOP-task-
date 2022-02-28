
from exc__1 import Plane
import math


class Concorde(Plane):
    def __init__(self, position, fuel):
        self._number_of_passengers = 0
        super().__init__(position, fuel)

    def __valid_number_of_passengers(self, number_of_passengers):
        if(number_of_passengers > 15):
            self._number_of_passengers = 15
            print('The maximum number of Passengers is 15 you cannot add more \n')
        else:
            self._number_of_passengers = number_of_passengers

    def __fuel_based_on_passengers(self):

        if(self._number_of_passengers == 0):
            return 4
        elif(1 <= self._number_of_passengers <= 7):
            return 7
        return 9

    def fly(self, desired_location, number_of_passengers):

        self.__valid_number_of_passengers(number_of_passengers)
        fuel_per_distance = self.__fuel_based_on_passengers()
        super().fly(desired_location, fuel_per_distance)


plane__2 = Concorde((1, 0), 20)
plane__2.fly((10, 10), 5)
plane__2.fly((4, 3), 3)
plane__2.add_fuel(10)


def furthest_plane(planes, desired_location):
    planes.sort(
        key=lambda plane: plane.get_total_distance(desired_location), reverse=True)
    return planes[0]


plane__3 = Concorde((1, 40), 20)
plane__4 = Concorde((1, 50), 20)
plane__5 = Concorde((1, 80), 20)


furthest_plane([plane__3, plane__4, plane__5], (0, 0))
