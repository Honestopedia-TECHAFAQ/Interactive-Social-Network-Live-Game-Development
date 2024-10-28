import pygame
from horse import Horse

class GameLogic:
    def __init__(self, screen):
        self.screen = screen
        self.horses = [
            Horse((255, 0, 0), 100, "Horse 1"),  
            Horse((0, 0, 255), 200, "Horse 2"),  
        ]
        self.finished = False
        self.winner = None

    def update_race(self):
        if self.finished:
            return

        for horse in self.horses:
            horse.move_forward()
            if horse.x_position >= 700:  
                self.finished = True
                self.winner = horse.name
                print(f"{self.winner} wins the race!")

    def reset_race(self):
        self.finished = False
        self.winner = None
import random
import time
import pygame
from horse import Horse

class GameLogic:
    def __init__(self, screen):
        self.screen = screen
        self.horses = [
            Horse((255, 0, 0), 100, "Horse 1"),
            Horse((0, 0, 255), 200, "Horse 2"),
        ]
        self.finished = False
        self.winner = None
        self.background_color = (255, 255, 255)
        self.special_event_time = 0
        self.leaderboard = {}

    def trigger_special_event(self):
        self.background_color = (255, 255, 0)
        self.special_event_time = time.time()

    def update_leaderboard(self, user):
        if user in self.leaderboard:
            self.leaderboard[user] += 1
        else:
            self.leaderboard[user] = 1

    def update_race(self):
        if self.finished:
            return

        if time.time() - self.special_event_time > 5:
            self.background_color = (255, 255, 255)

        for horse in self.horses:
            horse.move_forward()
            if horse.x_position >= 700:
                self.finished = True
                self.winner = horse.name
                print(f"{self.winner} wins the race!")

    def draw_leaderboard(self):
        font = pygame.font.Font(None, 36)
        y_offset = 10
        for user, score in sorted(self.leaderboard.items(), key=lambda item: -item[1])[:5]:
            text = font.render(f"{user}: {score}", True, (0, 0, 0))
            self.screen.blit(text, (600, y_offset))
            y_offset += 40

    def draw(self):
        self.screen.fill(self.background_color)

        for horse in self.horses:
            horse.draw(self.screen)

        if self.finished:
            font = pygame.font.Font(None, 74)
            text = font.render(f"{self.winner} wins!", True, (0, 255, 0))
            self.screen.blit(text, (200, 50))

        self.draw_leaderboard()

        pygame.display.flip()

        for horse in self.horses:
            horse.reset_position()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for horse in self.horses:
            horse.draw(self.screen)
        if self.finished:
            font = pygame.font.Font(None, 74)
            text = font.render(f"{self.winner} wins!", True, (0, 255, 0))
            self.screen.blit(text, (200, 50))
        pygame.display.flip()
