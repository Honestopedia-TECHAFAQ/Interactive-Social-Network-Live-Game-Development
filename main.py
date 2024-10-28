import pygame
import threading
from obs_controller import OBSController
from tiktok_interaction import listen_for_chat
from game_logic import GameLogic

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Tournament")

obs_controller = OBSController(password="password")
obs_controller.connect()

game_logic = GameLogic(screen)
def on_chat_message(message):
    if "Horse 1" in message or "Red" in message:
        game_logic.horses[0].move_forward()
    elif "Horse 2" in message or "Blue" in message:
        game_logic.horses[1].move_forward()
chat_thread = threading.Thread(target=listen_for_chat, args=(on_chat_message,))
chat_thread.start()
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_logic.update_race()
    game_logic.draw()
    clock.tick(60)
obs_controller.disconnect()
pygame.quit()
