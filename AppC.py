from tkinter import *
from PIL import ImageTk,Image
from main import response, wishme
from  spech_text import takecommand,speak




bot_name= "Aan"

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 16"
FONT_BOLD = "Helvetica 13 bold"
f = open('News.txt')
news = f.read()


class ChatApplication:

    def __init__(self):
        self.root = Tk()
        self._setup_main_window()

    def run(self):
        self.root.mainloop()


    def _setup_main_window(self):
        self.root.title("Intelligent Chatbot")
        self.root.geometry('1360x690+-5+0')
        self.root.configure(background='white')
        #adding images



        '''img2 = PhotoImage(file='button-green.png')
        img3 = PhotoImage(file='icon.png')
        background_image = PhotoImage(file="chatbg.png")
        img4 = PhotoImage(file='terminal.png')
        frames = [PhotoImage(file='chatgif.gif',format = 'gif -index %i' %(i)) for i in range(20)]
'''
        global img1, img2, img3, img4, background_image, frames
        img1 = ImageTk.PhotoImage(Image.open("chatbg.png"))
        #creating canvas
        canvas = Canvas(self.root, width = 884, height = 630)
        canvas.place(relheight=0.917,relwidth=0.65,rely=0.085)
        canvas.create_image(0, 0, image=img1, anchor=NW)

        # news label
        canvas.create_text(700,150, text =news, font= FONT_BOLD )

        #head label
        head_label = Label(self.root, bg=BG_COLOR, fg=TEXT_COLOR,
                           text=wishme(), font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1,relheight=0.062)

        # tiny divider
        line = Label(self.root, width=320, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.063, relheight=0.024)

        # text widget
        self.text_widget = Text(self.root, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.82, relwidth=0.35, rely=0.083,relx=0.65)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(canvas)
        scrollbar.place(relheight=0.88, relx=0.98)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.root, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.905,relx=0.6)
        # bottom line
        bottom_most = Label(self.root, bg=BG_GRAY, height=80)
        bottom_most.place(relwidth=1, rely=0.990, relx=0.6)


        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.248, relheight=0.03, rely=0.005, relx=0.05)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.30, rely=0.002, relheight=0.05, relwidth=0.05)
        # listen button
        listen_button = Button(bottom_label, text="listen", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=self._on_listen_pressed)
        listen_button.place(relx=0.35, rely=0.002, relheight=0.05, relwidth=0.05)
        # talk button
        talk_button = Button(bottom_label, text="talk", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=self._on_talk_pressed)
        talk_button.place(relx=0, rely=0.002, relheight=0.05, relwidth=0.05)

    def _on_listen_pressed(self):
        msg =takecommand()
        self._insert_message(msg, "You")
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    def _on_talk_pressed(self):
        speak(msgr)


    def _insert_message(self, msg, sender):
        if not msg:
            return



        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        global msgr
        msgr=response(msg)

        msg2 = f"{bot_name}: {msgr}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)



        self.text_widget.see(END)



if __name__ == "__main__":
    app = ChatApplication()
    app.run()
