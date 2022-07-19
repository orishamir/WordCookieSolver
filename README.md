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
![eq](data:image/png;base64,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)   
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
