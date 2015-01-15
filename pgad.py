import pygame
import serial
from pygame.locals import *
 
def main():
        "Opens a window and prints events to the terminal. Closes on ESC or QUIT."
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("JOYTEST")
        clock = pygame.time.Clock()
        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()
                print "Detected joystick '",joysticks[-1].get_name(),"'"
        ser = serial.Serial('/dev/ttyACM0',9600)
        while 1:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                print "Received event 'Quit', exiting."
                                return
                        elif event.type == JOYAXISMOTION:
                                print "Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion."
                                if event.axis == 4:
                                        print ' axis 4', event.value
                                elif event.axis == 3:
                                        print ' axis 3', event.value
                                elif event.axis == 5 or event.axis == 2:
                                    ser.write('w')
                                    ser.write(str(int(((event.value+1.0)/2.0)*100))+'d')
                        elif event.type == JOYBUTTONDOWN:
                                print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
                                if event.button == 0:
                                    ser.write('g')
                                elif event.button == 2:
                                    ser.write('b')
                                elif event.button == 1:
                                    ser.write('r')
                        elif event.type == JOYBUTTONUP:
                                print "Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up."
                                if event.button == 0:
                                    ser.write('G')
                                elif event.button == 2:
                                    ser.write('B')
                                elif event.button == 1:
                                    ser.write('R')
                        elif event.type == JOYHATMOTION:
                                print "Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved."
 
if __name__ == "__main__":
        main()
