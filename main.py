import PianoPlayer as Piano
import wx


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
        self.piano_player = Piano.PianoPlayer()

        self.value_lbl = wx.StaticText(parent=self, label="Note Value:", pos=(10, 12))
        self.noteValue_sCtrl = wx.SpinCtrl(parent=self, value="60", min=60, max=72, pos=(90, 10))
        self.play_btn = wx.Button(parent=self, label="Play", pos=(25, 70))
        self.play_btn.Bind(wx.EVT_BUTTON, self._on_play_btn_click)

    def _on_play_btn_click(self, e):
        self.piano_player.PlayNote(int(self.noteValue_sCtrl.GetValue()))



if __name__ == "__main__":
    App().MainLoop()

    piano = PianoPlayer()
