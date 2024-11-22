import pygame
import serial
import time

pygame.init()
pygame.joystick.init()

def listar_joysticks():
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for i, joystick in enumerate(joysticks):
        print(f"{i}: {joystick.get_name()}")
    return joysticks

def seleccionar_joystick(joysticks):
    if not joysticks:
        print("No hay joysticks disponibles.")
        return None
    while True:
        try:
            seleccion = int(input("Selecciona el joystick (número): "))
            if 0 <= seleccion < len(joysticks):
                joysticks[seleccion].init()
                print(f"Joystick '{joysticks[seleccion].get_name()}' seleccionado.")
                return joysticks[seleccion]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

port = 'COM15'
baudrate = 115200
ser = serial.Serial(port, baudrate)
port2 = 'COM16'
baudrate2 = 9600
ser2 = serial.Serial(port2, baudrate2)
time.sleep(2)
stateBomba=2

print("Listando joysticks...")
joysticks = listar_joysticks()
joystick = seleccionar_joystick(joysticks)

if not joystick:
    print("No se seleccionó ningún joystick. Saliendo...")
    pygame.quit()
    exit()

servo_x_position = 90
servo_y_position = 90
servo_z_position = 90
servo_r_position = 90
servo_5_position = 90

servo_speed = 5

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                button_up = joystick.get_button(3)
                button_down = joystick.get_button(1)
                button_left = joystick.get_button(0)
                button_right = joystick.get_button(4)
                button_z_up = joystick.get_button(7)
                button_z_down = joystick.get_button(6)
                button_r_up = joystick.get_button(8)
                button_r_down = joystick.get_button(9)
                button_reset = joystick.get_button(14)
                button_Bomba = joystick.get_button(13)
                if button_up:
                    servo_x_position = min(servo_x_position + servo_speed, 180)
                if button_down:
                    servo_x_position = max(servo_x_position - servo_speed, 0)
                if button_left:
                    servo_y_position = max(servo_y_position - servo_speed, 0)
                if button_right:
                    servo_y_position = min(servo_y_position + servo_speed, 180)
                if button_z_up:
                    servo_z_position = min(servo_z_position + servo_speed, 180)
                if button_z_down:
                    servo_z_position = max(servo_z_position - servo_speed, 0)
                if button_r_up:
                    servo_r_position = min(servo_r_position + servo_speed, 180)
                if button_r_down:
                    servo_r_position = max(servo_r_position - servo_speed, 0)
                if button_reset:
                    servo_x_position = 90
                    servo_y_position = 90
                    servo_z_position = 90
                    servo_r_position = 90
                    servo_5_position = 90
                if button_Bomba:
                    if stateBomba==1:
                        stateBomba=2
                    else:
                        stateBomba=1
                    ser2.write(str(stateBomba).encode())
                    print(f"Estado de la bomba: {stateBomba}")
                command = f"{servo_x_position},{servo_y_position},{servo_z_position},{servo_r_position},{servo_5_position}\n"
                ser.write(command.encode())
                print(f"X: {servo_x_position}, Y: {servo_y_position}, Z: {servo_z_position}, R: {servo_r_position}, 5: {servo_5_position}")

except KeyboardInterrupt:
    print("Saliendo...")
finally:
    ser.close()
    pygame.quit()
