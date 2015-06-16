#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import *
import sys   

MS_2_KMH = 3.6

def test_that_simple_pid_speedcontrol_reaches_desired_speed():
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
        
    tolerance = 0.1
    print "Desired speed: {:.2f}, actual speed: {:.2f}".format(car.desired_velocity, car.velocity)
    return abs(car.desired_velocity - car.velocity) < tolerance


sys.exit(0 if test_that_simple_pid_speedcontrol_reaches_desired_speed() else 1)
