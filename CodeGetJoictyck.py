import pygame

def listar_joysticks():
    """Lista los joysticks disponibles."""
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for i, joystick in enumerate(joysticks):
        print(f"{i}: {joystick.get_name()}")
    return joysticks

def seleccionar_joystick(joysticks):
    """Permite seleccionar un joystick de la lista."""
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

def main():
    pygame.init()
    print("Listando joysticks...")
    joysticks = listar_joysticks()

    joystick = seleccionar_joystick(joysticks)
    if not joystick:
        pygame.quit()
        return

    print("Presiona cualquier botón o mueve los ejes. Presiona ESC para salir.")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Botón presionado: {event.button}")
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Eje {event.axis} movido a {event.value}")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return

        clock.tick(60)

if __name__ == "__main__":
    main()
