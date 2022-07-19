from itertools import permutations
from math import cos, sin, pi
from functools import partial
from numpy import interp
from time import sleep
from math import perm
import mouse

mid_of_plate = [962, 724]
plate_r = 125

translateToScreen = partial(interp, xp=[-1, 1], fp=[-plate_r, plate_r])

def get_roots_of_unity_ish(n):
    # Solves the equation z^n = cis(90n)
    # Returns the complex numbers z1, z2, ...
    # Based on De Moivre’s Theorem
    for k in range(n):
        yield complex(cos(pi/2+2*pi*k/n), sin(pi/2+2*pi*k/n))

def get_all_letter_pos(n):
    points = [[z.real, z.imag] for z in get_roots_of_unity_ish(n)]
    for dx, dy in points:
        dx, dy = translateToScreen(dx), translateToScreen(dy)
        x = mid_of_plate[0] + dx
        y = mid_of_plate[1] - dy
        yield x, y

def play_perm(perm):
    [x1, y1] = perm[0]
    mouse.move(x1, y1)
    sleep(0.05)
    mouse.press()
    sleep(0.05)

    for x, y in perm[1:]:
        mouse.move(x, y)
        sleep(0.05)
    mouse.release()

n = int(input("n="))
print("The amount of permutations is exactly", sum(perm(n, k) for k in range(2, n+1)))

letters_positions = list(get_all_letter_pos(n))
for k in range(2, n+1):
    for perm in permutations(letters_positions, k):
        play_perm(perm)
        if mouse.get_position()[0] > mid_of_plate[0]+plate_r:
            raise StopIteration("Stopped Playing")
