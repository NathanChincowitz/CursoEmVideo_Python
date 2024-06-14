'''faça um programa em python e abra e reproduza o audio de um arquivo mp3'''
import pygame
pygame.init()
pygame.mixer.music.load('teste021.mp3')
pygame.mixer.music.play()
pygame.image.load('teste021.jpg')
pygame.image.show()
input()
pygame.event.wait()