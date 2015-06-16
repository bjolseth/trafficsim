from model import *
import pylab

MS_2_KMH = 3.6


def test_cars_following():

    create_cars(3, 80./MS_2_KMH)
    
    sim = Simulator([car1, car2])
    while sim.time < 100:
        sim.next_step()


def create_cars(n, speed):
    cars = []
        
    leader = Car()
    leader.velocity = speed
    leader.desired_velocity = speed
    cars.append(leader)
    
    previous = leader    
    for i in range(2, n):
        car = Car()
        car.velocity = speed
        c = SpeedController(previous)
        c = FollowCarController(previous, car)
        c.pos = c.set_desired_time_difference(speed)
        cars.append(car)
        
   return cars

def test_simple_pid_speedcontrol():
    car = Car()
    controller = SpeedController(car)
    car.set_controller(controller)
    car.desired_velocity = 80./MS_2_KMH
    sim = Simulator([car])
    
    v = []
    r = []
    t = []
    
    while sim.time < 40:
        sim.next_step()
        if (sim.time > 20):
            car.desired_velocity = 70./MS_2_KMH
        v.append(car.velocity*MS_2_KMH)
        r.append(car.desired_velocity*MS_2_KMH)
        t.append(sim.time)
        

    pylab.plot(t, r, 'r', t, v, 'b')

    pylab.xlabel('time (s)')
    pylab.ylabel('velocity (m/s)')
    pylab.grid(True)
    pylab.show()

test_simple_pid_speedcontrol()

