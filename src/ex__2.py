
import math


class LOWFUELERROR(Exception):
    def __init__(self, position, desired_location, fuel, fuel_needed):

        self.message = f'The fuel is not enough. current plane location{position}, new location {desired_location}, current amount of fuel {fuel}, minimum amount of fuel needed {fuel_needed} \n'
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Plane:
    MAX_FUEL = 1000

    def __init__(self, position, fuel):
        self._position = position
        self._fuel = self.__check_fuel(fuel)
        self._distance = 0
        print(self.plane_status())

    @ staticmethod
    def __check_fuel(fuel):
        if(fuel > M):
            return 1000
        else:
            return fuel

    def plane_status(self):

        return f'Plane is at position {self._position}, travel distance is {self._distance}km and the current fuel is {self._fuel} liter (max fuel is 1000 liter) \n '

    def get_plane_fuel(self):
        return self._fuel

    def get_plane_location(self):
        return self._position

    def add_fuel(self, fuel):
        self._fuel += self.__check_fuel(fuel+self._fuel)
        print(f'added {fuel} liter')

    def __str__(self):
        return self.plane_status()

    def get_total_distance(self, desired_location):
        horizontal_distance = abs(desired_location[0]-self._position[0])
        vertical_distance = abs(desired_location[1]-self._position[1])
        return math.ceil(math.sqrt(
            vertical_distance**2+horizontal_distance**2))

    def fly(self, desired_location, fuel_per_distance=4):
        try:
            # update total distance
            total_distance = self.get_total_distance(desired_location)
            fuel_needed = int(fuel_per_distance*total_distance)
            if(self._fuel < fuel_needed):
                raise LOWFUELERROR(
                    self._position, desired_location, self._fuel, fuel_needed)

            self._distance += total_distance
            self._position = desired_location

            print(
                f'The plane will fly to {desired_location} location,the total distance is {total_distance} \n')

        except LOWFUELERROR as error:
            print(error.args[0])


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
