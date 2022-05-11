from finalgui import *


def main():
    """
    - Window for rock paper scissor game
    - Window will stay the same size and will not change
    """
    window = Tk()
    window.title('Final project Section 1')
    window.geometry('635x350')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
