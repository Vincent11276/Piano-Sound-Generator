import pygame
pygame.init()

POLYPHONY = 64
pygame.mixer.set_num_channels(POLYPHONY)
channels = [pygame.mixer.Channel(i) for i in range(POLYPHONY)]


class PianoPlayer:
    def __init__(self, sound_pack_path='Resources/Piano Samples'):
        self.min_value = 60
        self.max_value = 72

        self.sounds = []
        for i in range(60, 73):
            self.sounds.append(pygame.mixer.Sound(f'{sound_pack_path}/Piano {i}.mp3'))

    def PlayNote(self, value):
        if value < self.min_value or value > self.max_value:
            return

        for channel in channels:
            if not channel.get_busy():
                channel.play(self.sounds[value - self.min_value])
                return

        # If the code manages to get here, it means that all of the channels are occupied
        global POLYPHONY
        POLYPHONY += 1
        pygame.mixer.set_num_channels(POLYPHONY)
        channels.append(pygame.mixer.Channel(POLYPHONY - 1))
        channels[-1].play(self.sounds[value])