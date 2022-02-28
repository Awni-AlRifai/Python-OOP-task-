
class Plane:
    def __init__(self, position, fuel):
        self._position = position
        self._fuel = self.__check_fuel(fuel)
        self._distance = 0
        print(self.plane_status())

    @staticmethod
    def __check_fuel(fuel):
        if(fuel > 1000):
            return 1000
        else:
            return fuel

    def plane_status(self):

        return f'Plane is at position {self._position}, travel distance is {self._distance}km and the current fuel is {self._fuel} liter (max fuel is 1000 liter) \n '

    def get_plane_fuel(self):
        return self._fuel

    def get_plane_location(self):
        return self.__location

    def add_fuel(self, fuel):
        self._fuel += self.__check_fuel(fuel)
        print(f'added {fuel} liter')

    def __str__(self):
        return self.plane_status()

    def fly(self, desired_location):
        try:
            # update total distance
            horizontal_distance = abs(desired_location[0]-self._position[0])
            vertical_distance = abs(desired_location[1]-self._position[1])
            total_distance = vertical_distance+horizontal_distance
            fuel_needed = 4*total_distance
            if(self._fuel < fuel_needed):
                raise ValueError
            self._distance += total_distance
            self._position = desired_location
            print(
                f'The plane will fly to {desired_location} location,the total distance is {total_distance} \n')

        except:
            print(
                f'The fuel is not enough. current plane location{self._position}, new location {desired_location}, current amount of fuel {self._fuel}, minimum amount of fuel needed {fuel_needed} \n')


plane__1 = Plane((0, 0), 22)
plane__1.fly((3, 4))
plane__1.add_fuel(10)
plane__1.fly((10, 10))
plane__1.fly((3, 5))
