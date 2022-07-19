### About the Game
The game [Word Cookies](https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies) 
is a game where you are given `n` letters and are instructed to produce varying words of varying lengths from the given letters.   
For example:   

![Example](https://play-lh.googleusercontent.com/S1Bauc7lX4YRMXConNIRDeY0ICvVpXVviHeE66BS3bhcE9PjQhvVyQeUtLbDekb_iA)
       
In this example, `n=5` and you need to construct different words, like in the image.

### My solution
I simply try every possible combination of letters.   
After I have a list of coordinates of the letters, I can use permutate that list.   
So for example, say I have:
```python
letters_positions = [
    (962, 599), 
    (853, 786), 
    (1070, 786),
] 
```   
That means I need to try:
```python
[
    ((962, 599), (853, 786)),
    ((962, 599), (1070, 786)),
    ((853, 786), (962, 599)),
    ((853, 786), (1070, 786)),
    ((1070, 786), (962, 599)),
    ((1070, 786), (853, 786)),
    ((962, 599), (853, 786), (1070, 786)),
    ((962, 599), (1070, 786), (853, 786)),
    ((853, 786), (962, 599), (1070, 786)),
    ((853, 786), (1070, 786), (962, 599)),
    ((1070, 786), (962, 599), (853, 786)),
    ((1070, 786), (853, 786), (962, 599)),
]
```    

But that begs the question: How do I get the position of the letters?   
My solution: Notice that the pattern of where each letter is located is exactly the solution to the complex equation:   
![eq](https://i.imgur.com/Zo6yBgW.png)   
And so all that's left is to scale from `[-1, 1]` to our screen.   
After we have the postion of all the letters, we just need to iterate over every permutation.
### How to use my bot
First you need to mirror your android's screen to your PC.
You must set your monitor's resolution to 1920x1080.
To mirror your android to your screen, download [Scrcpy](https://github.com/Genymobile/scrcpy)
to mirror your phone.

You need to [Enable USB Debugging](https://www.google.com/search?q=how+to+enable+usb+debugging)
and then connect your phone to your PC via a USB cable.

Then, start the screen mirroring by issuing the command:
```shell
./scrcpy --fullscreen 
```
You must open Scrcpy in full screen mode because otherwise the location
would be off.

After you have mirrored your phone, then you can use `Main.py`.
I suggest editing the code a bit to your liking.

### Note
This project is not complete, the algorithms aren't the most optimized yet.
This project uses brute force.
