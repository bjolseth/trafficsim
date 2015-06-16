#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import *
import sys   
import unittest

MS_2_KMH = 3.6

class TestSimpleSpeedControl(unittest.TestCase):

    def test_that_simple_pid_speedcontrol_reaches_desired_speed(self):
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
        self.assertTrue(abs(car.desired_velocity - car.velocity) < tolerance)


if __name__ == '__main__':
    unittest.main()


