from model import *
import pylab

def test_simple_pid_speedcontrol():
    car = Car()
    controller = CarController(car)
    car.set_controller(controller)
    car.desired_velocity = 80./3.6
    sim = Simulator([car])
    
    v = []
    r = []
    t = []
    
    while sim.time < 60:
        sim.next_step()
        if (sim.time > 30):
            car.desired_velocity = 70./3.6
        v.append(car.velocity)
        r.append(car.desired_velocity)
        t.append(sim.time)
        

    pylab.plot(t, r, 'r', t, v, 'b')

    pylab.xlabel('time (s)')
    pylab.ylabel('velocity (m/s)')
    pylab.grid(True)
    pylab.show()


test_simple_pid_speedcontrol()


