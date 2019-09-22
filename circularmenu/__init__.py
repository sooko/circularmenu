import math
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.app import App
Builder.load_string('''
#:import math math
<CircularMenu>:
    mbok:mbok
    len_wg:180
    FloatLayout:
        id:mbok
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: 1*min(root.size), 1*min(root.size)
        Label:
            pos_hint:{"center_x": 0.5+0.42*math.sin(math.pi/root.len_wg*(360-root.angle)), "center_y": 0.5+0.42*math.cos(math.pi/root.len_wg*(360-root.angle))}
            text:"1"
''')
class BtnMenu(Button):
    data=StringProperty("")

class CircularMenu(FloatLayout):
    angle = NumericProperty(10)
    listsource=ListProperty(["","","","","","","","","","","",""])
    listdata=ListProperty(["a","b","c","d","e","f","g","f","i","j","k","l"])
    listtext=ListProperty(["a","b","c","d","e","f","g","f","i","j","k","l"])

    len_wg=NumericProperty(180)
    count=NumericProperty(0)
    def __init__(self, *args, **kwargs):
        super(CircularMenu, self).__init__(*args,**kwargs)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            y = (touch.y - self.center[1])
            x = (touch.x - self.center[0])
            calc = math.degrees(math.atan2(y, x))
            self.prev_angle = calc if calc > 0 else 360 + calc
            self.tmp = self.angle
            return super(CircularMenu, self).on_touch_down(touch)
    def on_touch_move(self, touch):
        self.ids["mbok"].clear_widgets()
        if self.collide_point(*touch.pos):
            y = (touch.y - self.center[1])
            x = (touch.x - self.center[0])
            calc = math.degrees(math.atan2(y, x))
            new_angle = calc if calc > 0 else 360 + calc
            self.angle = self.tmp + (new_angle - self.prev_angle) % 360
            for i in range(len(self.listsource)):
                self.ids["mbok"].add_widget(BtnMenu(text=self.listtext[i],
                                                    data=self.listdata[i],
                                                    on_press=self.on_menu_press,
                                                    size_hint=(.1,.1),
                                                    pos_hint={"center_x": 0.5+0.42*math.sin(math.pi/self.len_wg*(360-i*30-self.angle)),
                                                                          "center_y": 0.5+0.42*math.cos(math.pi/self.len_wg*(360-i*30-self.angle))}))



    def on_angle(self, a, b):
        pass
    def on_menu_press(self,a):
        print(a.data)
class MyApp(App):
    def build(self):
        return CircularMenu()
if __name__=="__main__":
    MyApp().run()
