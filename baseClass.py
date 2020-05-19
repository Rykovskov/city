#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Human:
    """This class ia a base human class"""
    human_count = 0
    age = 0
    weight = 0
    temperature = 36.6
    state_of_health = 5

    def __init__(self):
        """Constructor"""
        Human.human_count += 1
        self.age = Human.age
        self.weight = Human.weight
        self.temperature = Human.temperature
        self.state_of_health = Human.state_of_health
        pass

    def save_state(self):
        #Save state to base
        pass

    def __str__(self):
        return "Human class Object"
