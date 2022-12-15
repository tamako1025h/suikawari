from tkinter import messagebox
import tkinter as tk
import random
import math
import os

"""ファイルパスを指定"""
project_root = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(project_root, "image")

suika_path = os.path.join(image_dir, "suika.png")
sukawari_path = os.path.join(image_dir,"suikawari.png")

CHARACTER_IMG_PATH = sukawari_path
SUIKA_IMG_PATH = suika_path
GAME_COUNT = 0

"""スイカの座標を生成"""
ANSWER = []
while len(ANSWER) < 2:
    num = random.randrange(100,500,100)
    ANSWER.append(num)

class SuikaGame:
    """スイカ割ゲーム"""
    
    def __init__(self,master):
        self.master = master
        self.width = 500
        self.height = 570
        
        self.createCanvas()
    
    """キャンバスの作成"""
    def createCanvas(self):
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack()
        
        """5x5マスの作成"""
        for i in range(5):
            for j in range(5):
                x1 = i*100
                y1 = j*100
                x2 = x1 + 100
                y2 = y1 + 100
                
                self.canvas.create_rectangle(x1,y1,x2,y2)
        
        """キャラクターとスイカの画像の読み込み"""
        self.charImage = tk.PhotoImage(file=CHARACTER_IMG_PATH)
        self.suikaImg = tk.PhotoImage(file=SUIKA_IMG_PATH)
        
        self.image_on_canvas = self.canvas.create_image(0,0,image=self.charImage,anchor=tk.NW,)
        self.canvas.create_text(220,560,text="スイカ割りゲームを始めます。",tag="adv")
        
        # デバッグ用スイカの位置
        #self.ansewer = self.canvas.create_text(ANSWER[0]+50, ANSWER[1]+50, text="スイカ")
        
        """ボタンの作成"""
        button_up = tk.Button(self.canvas, text="上", width=10,command=lambda:self.move("up"))
        button_down = tk.Button(self.canvas, text="下",width=10,command=lambda:self.move("down"))
        button_left = tk.Button(self.canvas, text="左",width=10,command=lambda:self.move("left"))
        button_right = tk.Button(self.canvas, text="右",width=10,command=lambda:self.move("right"))
        
        button_up.place(x=50,y=520)
        button_down.place(x=150,y=520)
        button_left.place(x=250,y=520)
        button_right.place(x=350,y=520)
    
    """ボタンが押されたときの動き"""    
    def move(self,event):
        
        if event == "up":
            if self.canvas.coords(self.image_on_canvas)[1] != 0:
                self.canvas.move(self.image_on_canvas,0,-100)
                self.judge()
        if event == "down":
            if self.canvas.coords(self.image_on_canvas)[1] != 400:
                self.canvas.move(self.image_on_canvas,0,100)
                self.judge()
        if event == "left":
            if self.canvas.coords(self.image_on_canvas)[0] != 0:
                self.canvas.move(self.image_on_canvas,-100,0)
                self.judge()
        if event == "right":
            if self.canvas.coords(self.image_on_canvas)[0] != 400:
                self.canvas.move(self.image_on_canvas,100,0)
                self.judge()
    
    """スイカ判定"""
    def judge(self):
        global GAME_COUNT
        GAME_COUNT = GAME_COUNT + 1
        
        if self.canvas.coords(self.image_on_canvas) == ANSWER:
            self.canvas.delete(self.image_on_canvas)
            self.canvas.create_image(ANSWER[0],ANSWER[1],image=self.suikaImg,anchor=tk.NW)
            self.canvas.delete("adv")
            self.canvas.create_text(220,560,text=f"{GAME_COUNT}回目でスイカを割りました")
            self.Exit()
        else:
            distance = (ANSWER[0] - self.canvas.coords(self.image_on_canvas)[0]) **2 + (ANSWER[1] - self.canvas.coords(self.image_on_canvas)[1]) **2
            distance_opt = math.sqrt(distance) / 100
            self.canvas.delete("adv")
            self.canvas.create_text(220,560,text=f"スイカまでの距離:{distance_opt}",tag="adv")

    """クリアした後のメッセージボックス"""
    def Exit(self):
        self.messageboxExit = messagebox.askquestion("クリア",f"{GAME_COUNT}回でクリアしました。終了しますか？",icon="question")
        if self.messageboxExit == 'yes':
            self.master.destroy()
                            
def main():
    root = tk.Tk()
    root.title("スイカ割りゲーム")
    root.resizable(width=False, height=False)
    app = SuikaGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()