import pygame
import json


class StoryNode:
    def __init__(self, description, choices, effects=None, image=None):
        self.description = description
        self.choices = choices
        self.effects = effects
        self.image = image


class Character:
    def __init__(self):
        self.stats = {"health": 100, "strength": 10, "intelligence": 10}
        self.inventory = []

    def update_stats(self, effects):
        if effects:
            for stat, effect in effects.items():
                self.stats[stat] += effect

    def add_item(self, item):
        self.inventory.append(item)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Interactive Story Game")
        self.font = pygame.font.Font(None, 36)
        self.story = self.load_story()
        self.character = Character()
        self.current_node = "start"

        pygame.mixer.music.load('background_music.wav')
        pygame.mixer.music.play(-1)

        self.click_sound = pygame.mixer.Sound('sound_effect.mp3')

        self.welcome_image = pygame.image.load('welcome.jfif').convert()
        self.welcome_image = pygame.transform.scale(self.welcome_image, (800, 600))

    def load_story(self):
        with open('story.json', 'r') as f:
            story_data = json.load(f)

        story = {}
        for key, value in story_data.items():
            story[key] = StoryNode(value['description'], value['choices'], value.get('effects'), value.get('image'))

        return story

    def display_text(self, text, y):
        lines = text.split('\n')
        max_width = max(self.font.size(line)[0] for line in lines)
        padding = 10
        background_width = max_width + padding * 2
        background_height = (self.font.get_height() + 10) * len(lines) + padding * 2

        for line in lines:
            background = pygame.Surface((background_width, background_height))
            background.fill((255, 255, 255))
            text_y = y + padding

            for line in lines:
                rendered_text = self.font.render(line, True, (0, 0, 0))
                text_rect = rendered_text.get_rect(center=(self.screen.get_width() // 2, text_y))
                background_rect = background.get_rect(center=(self.screen.get_width() // 2, text_y))
                self.screen.blit(background, background_rect.topleft)
                self.screen.blit(rendered_text, text_rect)
                text_y += self.font.get_height() + 10

            y += background_height + padding

        return y

    def play_sound_effect(self, effect):
        if effect == "click":
            self.click_sound.play()

    def show_welcome_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.welcome_image, (0, 0))

        welcome_text = "Welcome to the Interactive Story Game!"
        text_rendered = self.font.render(welcome_text, True, (255, 255, 255))
        text_rect = text_rendered.get_rect(center=(400, 50))
        self.screen.blit(text_rendered, text_rect)

        pygame.display.flip()
        pygame.time.wait(3000)

    def run(self):
        self.show_welcome_screen()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.play_sound_effect("click")
                        self.current_node = self.story[self.current_node].choices['1']['next']
                    elif event.key == pygame.K_2:
                        self.play_sound_effect("click")
                        self.current_node = self.story[self.current_node].choices['2']['next']

            self.screen.fill((0, 0, 0))

            node = self.story[self.current_node]
            if node.image:
                image = pygame.image.load(node.image).convert()
                image = pygame.transform.scale(image, (800, 600))
                self.screen.blit(image, (0, 0))

            y = 20
            y = self.display_text(node.description, y)
            for key, choice in node.choices.items():
                y = self.display_text(f"{key}: {choice['text']}", y)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
