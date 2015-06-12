from model import *
import pylab

MS_2_KMH = 3.6

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

