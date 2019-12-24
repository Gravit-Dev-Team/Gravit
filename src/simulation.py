#coding: utf-8
#!/usr/bin/env python3

import pygame
from pygame.locals import *

from random import randint as r
from threading import Thread

class Simulation(Thread):

    def do_play(self):
        self.play = True
        self.stop = False

    def do_pause(self):
        self.play = False

    def do_stop(self):
        self.play = False
        self.stop = True

    def rcolor(self):
        return r(0, 255), r(0, 255), r(0, 255)

    def gen(self, gravit):
        pass

    def __init__(self, FPS=60, win_size=(640, 480)):
        super().__init__()

        self.FPS = FPS
        self.win_size = win_size

    def run(self):

        pygame.init()

        self.spacetime = pygame.display.set_mode(self.win_size)

        self.fps_limiter = pygame.time.Clock()
        pygame.key.set_repeat(400, 30)

        self.obj1_color = self.rcolor()
        self.obj1 = pygame.draw.circle(self.spacetime, self.obj1_color, (320, 240), 50)

        self.fond = pygame.Surface(self.win_size).convert()
        self.do_play()

        while not self.stop:
            print("avant")
            while self.play:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        self.do_stop()

                    if event.type == KEYDOWN:

                        if event.key == K_RIGHT:
                            self.obj1.move_ip(2, 0)

                        if event.key == K_LEFT:
                            self.obj1.move_ip(-2, 0)

                        if event.key == K_DOWN:
                            self.obj1.move_ip(0 ,2)

                        if event.key == K_UP:
                            self.obj1.move_ip(0, -2)

            self.spacetime.blit(self.fond, (0, 0))

            self.obj1 = pygame.draw.circle(self.spacetime, self.obj1_color, self.obj1.center, 50)

            pygame.display.update(self.obj1)

            self.fps_limiter.tick(self.FPS)
