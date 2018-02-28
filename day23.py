import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.create_labels()
        self.idx_create()
        compute(self)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def create_labels(self):
        self.groupreg = tk.LabelFrame(self, text="registers", padx=5, pady=5)
        self.groupreg.pack()

        self.labels = list()
        for x in range(8):
            self.labels.append(tk.Label(self.groupreg))
            self.labels[x]['text'] = chr(ord('a') + x) + ': ' + str(0)
            self.labels[x].pack(side='bottom')

    def fill_labels(self, d):
        for x in range(8):
            self.labels[x]['text'] = chr(ord('a') + x) + ': ' + str(d[chr(ord('a') + x)])
            self.labels[x].pack()

    def idx_create(self):
        self.idx = tk.Label(self)
        self.idx['text'] = 'idx: ' + str(0)
        self.idx.pack(side='bottom')

    def idx_label(self, val):
        self.idx['text'] = 'idx: ' + str(val)
        self.idx.pack(side='bottom')


def getVal(a, registers):
    if a.islower():
        val = registers[a]
    else:
        val = int(a)
    return val


def compute(app):
    instructions = open("day23.txt").read().split("\n")
    registers = dict()

    for x in range(8):
        registers[chr(ord('a') + x)] = 0

    registers['a'] = 1

    idx = 0
    add = 0
    show = [21, 22, 23, 24]

    l = list()

    prevd = 0

    while True:
        i = instructions[idx].split(" ")

        l.append(idx)

        a = getVal(i[1], registers)
        b = getVal(i[2], registers)

        if i[0] == 'set':
            registers[i[1]] = b
        elif i[0] == 'jnz':
            if a != 0:
                idx += b
                if idx >= len(instructions):
                    break
                idx -= 1
        elif i[0] == 'sub':
            registers[i[1]] -= b
        elif i[0] == 'mul':
            registers[i[1]] = a * b
            add += 1
        idx += 1

        if idx in show:
            app.fill_labels(registers)
            app.idx_label(idx)
            app.update()
            prevd = registers['d']

    print('part1:', add)
    print(registers['h'])


def main():
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
