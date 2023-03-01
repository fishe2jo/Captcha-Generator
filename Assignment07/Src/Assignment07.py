# Name: Jake Fisher    
# Email: fishe2jo@mail.uc.edu
# Assignment Title: Assignment 07
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Module that generates the string, draws the ellipses, text and rotates it and generates a captcha image
# Citations: https://stackoverflow.com/questions/62910445/watermarking-pasting-rotated-text-to-empty-image
# Anything else that's relevant: 75% Bill's brain, 10% Stack Overflow's brain, and 15% my brain
# Assignment07.py
from random import randint
'''
Created on Feb 26, 2020

@author: nicomp
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha(captchaLength, targetFileName):
    '''
    Generate a captcha
    :return: A tuple (image, captcha string encoded in the image)
    '''
    if captchaLength < 6 or captchaLength > 10:
        captchaLength = 10
    captcha_string = generate_random_string(captchaLength)
#   print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)

    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    for letter in captcha_string:
        # Select a random font from all the fonts I have
        myFonts = ["Aaargh.ttf", "Gamer.ttf", "impact.ttf", "NEUROPOL.ttf", "retro_computer_personal_use.ttf"]
        randomFont = random.choice(myFonts)
        fontStyle = ImageFont.truetype(randomFont, 48)     # font must be in the same folder as the .py file. 
#       print(letter)
        text_image = Image.new("RGBA", (400, 200), (255,255,255,0))
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((x, y), letter, (0,0,0),font=fontStyle) # Write in black
        randomDegree = randint(-15,15)
        rotated_text_image = text_image.rotate(randomDegree)
        captcha_image = Image.alpha_composite(captcha_image, rotated_text_image)
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
        
    # Save the image on the disk as targetFileName
    rgb_im = captcha_image.convert("RGB")
    rgb_im.save(targetFileName)
    return (captcha_image, captcha_string)  # return a heterogeneous tuple
