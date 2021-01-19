import pygame
import wx
import time
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


class App(wx.App):
    def __init__(self):
        super(App, self).__init__()

    def OnInit(self):
        Frame(None, title="Piano Sound Generator", size=(800, 600)).Show()

        return True


class Frame(wx.Frame):
    def __init__(self, parent, title, size):
        super(Frame, self).__init__(parent=parent, title=title, size=size)
        self.OnInit()

    def OnInit(self):
        Panel(parent=self)


class Panel(wx.Panel):
    def __init__(self, parent):
        super(Panel, self).__init__(parent=parent)
        self.piano_player = PianoPlayer()

        self.value_lbl = wx.StaticText(parent=self, label="Note Value:", pos=(10, 12))
        self.noteValue_sCtrl = wx.SpinCtrl(parent=self, value="60", min=60, max=72, pos=(90, 10))
        self.play_btn = wx.Button(parent=self, label="Play", pos=(25, 70))
        self.play_btn.Bind(wx.EVT_BUTTON, self._on_play_btn_click)

    def _on_play_btn_click(self, e):
        self.piano_player.PlayNote(int(self.noteValue_sCtrl.GetValue()))



if __name__ == "__main__":
    App().MainLoop()

    piano = PianoPlayer()





