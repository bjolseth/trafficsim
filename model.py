SIMULATOR_STEP_SIZE = 0.02
FRICTION = 0.1
K_P = 0.2
K_I = 0.02

class Simulator:

    def __init__(self, cars):
        self.cars = cars;
        self.time = 0
        self.step = 0

    def next_step(self):
        self.time += SIMULATOR_STEP_SIZE
        self.step += 1
        for car in self.cars:
            car.update_state()

class Car:

    def __init__(self):
        self.pos = 0.0
        self.velocity = 0.0
        self.desired_velocity = 0.0
        self.controller = 0
        
    def update_state(self):
        throttle = 0
        if self.controller:
            throttle = self.controller.calculate_output()
            
        accel = throttle - FRICTION * self.velocity
        self.velocity = self.velocity + SIMULATOR_STEP_SIZE * accel
        self.pos = self.pos + SIMULATOR_STEP_SIZE * self.velocity

    def set_controller(self, controller):
        self.controller = controller

class CarController:
    def __init__(self, car):
        self.car = car    
        self.integrated_error = 0.0
        
    def calculate_output(self):
        error = self.car.desired_velocity - self.car.velocity
        self.integrated_error += SIMULATOR_STEP_SIZE * error
        u = K_P * error + K_I * self.integrated_error
        return u
