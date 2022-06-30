import time
import itertools


class TrafficLight():
    color = [['red', 7], ['yellow', 2], ['green', 5]]

    def running(self):
        color = TrafficLight.color
        for light in itertools.cycle(color):
            print(f'Traffic Light is {light[0]}')
            time.sleep(light[1])


lenina_mira = TrafficLight()
lenina_mira.running()
