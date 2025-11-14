import pyxel

from app.components.sprites import Sprite,SpriteAnimated

class Text:
    def __init__(self, text : list[str | Sprite | SpriteAnimated], line_spacing : int = 8) -> None:
        self.line_spacing : int = line_spacing
        self.text = text
        self.wlist : list[float] = []
        i = 0
        while i < len(self.text):
            if type(self.text[i]) == str and "\n" in self.text[i] and self.text[i] != "\n": # type: ignore
                lines = self.text[i].split("\n") # type: ignore
                self.text[i] = lines[0]
                for l in lines[1:]: # type: ignore
                    self.text.insert(i+1, l) # type: ignore
                    self.text.insert(i+1, "\n")
                    i+=2
            i+=1

        self.w : int = 0
        self.h : int = 0

        current_w : int = 0
        for i in range(len(self.text)):
            if self.text[i] == "\n":
                self.wlist.append(0)
                self.h += self.line_spacing
                current_w = 0
            
            elif type(self.text[i]) == str:
                self.wlist.append(len(self.text[i])*pyxel.FONT_WIDTH) # type: ignore
                current_w += len(self.text[i])*pyxel.FONT_WIDTH # type: ignore

            elif type(self.text[i]) in [Sprite,SpriteAnimated]:
                self.wlist.append(self.text[i].w) # type: ignore
                current_w += int(self.text[i].w) # type: ignore

            if current_w > self.w:
                self.w = current_w
            i+=1


    def draw(self, x : float,y : float, col : int):
        cx = x
        cy = y
        for i in range(len(self.text)):
            if self.text[i] == "\n":
                cx = x
                cy += self.line_spacing
                continue

            if type(self.text[i]) == str:
                pyxel.text(cx,cy, self.text[i],col) # type: ignore

            elif type(self.text[i]) in [Sprite,SpriteAnimated]:
                self.text[i].draw(cx,cy-self.text[i].h/2+pyxel.FONT_HEIGHT/2) # type: ignore
            
            cx += self.wlist[i]