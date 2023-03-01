# Name: Jake Fisher    
# Email: fishe2jo@mail.uc.edu
# Assignment Title: Assignment 07
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Main module for testing the captcha function in the Assignment07 package
# Citations: Literally 100% Bill's brain for this one
# Anything else that's relevant: Captcha is very annoying in real life
# Main.py
'''
Created on Feb 26, 2020

@author: nicomp
'''

from Src.Assignment07 import generate_captcha

result = generate_captcha(6, "test.jpg")
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

