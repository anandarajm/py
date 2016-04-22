__author__ = 'anandraj'
import texttable
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

tt = texttable.Texttable()
r1 = [1, 4, 15, 7]
r2 = [8,10,2,11]
r3 = [14,3,6,13]
r4 = [12,9,5, None]

tt.add_row(r1)
tt.add_row(r2)
tt.add_row(r3)
tt.add_row(r4)

print tt.draw()

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
        elif k=='\x1b[B':
                print "down"
        elif k=='\x1b[C':
                print "right"
        elif k=='\x1b[D':
                print "left"
        else:
                print "not an arrow key!"

def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()