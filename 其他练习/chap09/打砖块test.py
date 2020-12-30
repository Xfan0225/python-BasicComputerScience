#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:29:09 2019

@author: xie
"""

# Block Breaker Game
# Chapter 9

import sys, time, random, math, pygame
from pygame.locals import *
#from MyLibrary.py import *

# MyLibrary.py

import sys, time, random, math, pygame
from pygame.locals import *


# prints text using the supplied font
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface() #req'd when function moved into MyLibrary
    screen.blit(imgText, (x,y))

# MySprite class extends pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0,0.0)

    #X property
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)

    #Y property
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)


    def load(self, filename, width=0, height=0, columns=1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)

    def set_image(self, image, width=0, height=0, columns=1):
        self.master_image = image
        if width==0 and height==0:
            self.frame_width = image.get_width()
            self.frame_height = image.get_height()
        else:
            self.frame_width = width
            self.frame_height = height
            rect = self.master_image.get_rect()
            self.last_frame = (rect.width//width) * (rect.height//height) - 1
        self.rect = Rect(0,0,self.frame_width,self.frame_height)
        self.columns = columns

    def update(self, current_time, rate=30):
        if self.last_frame > self.first_frame:
            #update animation frame number
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
        else:
            self.frame = self.first_frame

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)

#Point class
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"

levels = (
(1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,0,0,1,1,1,1,1,
 1,1,1,1,1,0,0,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1),

(2,2,2,2,2,2,2,2,2,2,2,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,2,2,2,2,2,2,2,2,2,2,2),

(3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3),
)

#this function increments the level
def goto_next_level():
    global level, levels
    level += 1
    if level > len(levels)-1: level = 0
    load_level()

#this function updates the blocks in play
def update_blocks():
    global block_group, waiting
    if len(block_group) == 0: #all blocks gone?
        goto_next_level()
        waiting = True
    block_group.update(ticks, 50)

#this function sets up the blocks for the level
def load_level():
    global level, block, block_image, block_group, levels

    block_image = pygame.image.load("/Users/xie/Desktop/python源代码/chap09/blocks.png").convert_alpha()

    block_group.empty() #reset block group

    for bx in range(0, 12):
        for by in range(0,10):
            block = MySprite()
            block.set_image(block_image, 58, 28, 4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x,y

            #read blocks from level data
            num = levels[level][by*12+bx]
            block.first_frame = num-1
            block.last_frame = num-1
            if num > 0: #0 is blank
                block_group.add(block)

    print(len(block_group))


#this function initializes the game
def game_init():
    global screen, font, timer
    global paddle_group, block_group, ball_group
    global paddle, block_image, block, ball

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Block Breaker Game")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()

    #create sprite groups
    paddle_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()

    #create the paddle sprite
    paddle = MySprite()
    paddle.load("/Users/xie/Desktop/python源代码/chap09/paddle.png")
    paddle.position = 400, 540
    paddle_group.add(paddle)

    #create ball sprite
    ball = MySprite()
    ball.load("/Users/xie/Desktop/python源代码/chap09/ball.png")
    ball.position = 400,300
    ball_group.add(ball)



#this function moves the paddle
def move_paddle():
    global movex,movey,keys,waiting

    paddle_group.update(ticks, 50)

    if keys[K_SPACE]:
        if waiting:
            waiting = False
            reset_ball()
    elif keys[K_LEFT]: paddle.velocity.x = -10.0
    elif keys[K_RIGHT]: paddle.velocity.x = 10.0
    else:
        if movex < -2: paddle.velocity.x = movex
        elif movex > 2: paddle.velocity.x = movex
        else: paddle.velocity.x = 0

    paddle.X += paddle.velocity.x
    if paddle.X < 0: paddle.X = 0
    elif paddle.X > 710: paddle.X = 710

#this function resets the ball's velocity
def reset_ball():
    ball.velocity = Point(4.5, -7.0)

#this function moves the ball
def move_ball():
    global waiting, ball, game_over, lives

    #move the ball
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + 40
        ball.Y = paddle.Y - 20
    ball.X += ball.velocity.x
    ball.Y += ball.velocity.y
    if ball.X < 0:
        ball.X = 0
        ball.velocity.x *= -1
    elif ball.X > 780:
        ball.X = 780
        ball.velocity.x *= -1
    if ball.Y < 0:
        ball.Y = 0
        ball.velocity.y *= -1
    elif ball.Y > 580: #missed paddle
        waiting = True
        lives -= 1
        if lives < 1: game_over = True

#this function test for collision between ball and paddle
def collision_ball_paddle():
    if pygame.sprite.collide_rect(ball, paddle):
        ball.velocity.y = -abs(ball.velocity.y)
        bx = ball.X + 8
        by = ball.Y + 8
        px = paddle.X + paddle.frame_width/2
        py = paddle.Y + paddle.frame_height/2
        if bx < px: #left side of paddle?
            ball.velocity.x = -abs(ball.velocity.x)
        else: #right side of paddle?
            ball.velocity.x = abs(ball.velocity.x)

#this function tests for collision between ball and blocks
def collision_ball_blocks():
    global score, block_group, ball

    hit_block = pygame.sprite.spritecollideany(ball, block_group)
    if hit_block != None:
        score += 10
        block_group.remove(hit_block)
        bx = ball.X + 8
        by = ball.Y + 8

        #hit middle of block from above or below?
        if bx > hit_block.X+5 and bx < hit_block.X + hit_block.frame_width-5:
            if by < hit_block.Y + hit_block.frame_height/2: #above?
                ball.velocity.y = -abs(ball.velocity.y)
            else: #below?
                ball.velocity.y = abs(ball.velocity.y)

        #hit left side of block?
        elif bx < hit_block.X + 5:
            ball.velocity.x = -abs(ball.velocity.x)
        #hit right side of block?
        elif bx > hit_block.X + hit_block.frame_width - 5:
            ball.velocity.x = abs(ball.velocity.x)

        #handle any other situation
        else:
            ball.velocity.y *= -1


#main program begins
game_init()
game_over = False
waiting = True
score = 0
lives = 3
level = 0
load_level()

#repeating loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    #handle events
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == MOUSEMOTION:
            movex,movey = event.rel
        elif event.type == MOUSEBUTTONUP:
            if waiting:
                waiting = False
                reset_ball()
        elif event.type == KEYUP:
            if event.key == K_RETURN: goto_next_level()

    #handle key presses
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()

    #do updates
    if not game_over:
        update_blocks()
        move_paddle()
        move_ball()
        collision_ball_paddle()
        collision_ball_blocks()

    #do drawing
    screen.fill((50,50,100))
    block_group.draw(screen)
    ball_group.draw(screen)
    paddle_group.draw(screen)
    print_text(font, 0, 0, "SCORE " + str(score))
    print_text(font, 200, 0, "LEVEL " + str(level+1))
    print_text(font, 400, 0, "BLOCKS " + str(len(block_group)))
    print_text(font, 670, 0, "BALLS " + str(lives))
    if game_over:
        print_text(font, 300, 380, "G A M E   O V E R")
    pygame.display.update()

