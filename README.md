# How to download
1. Only the `engine.py` file is needed
2. Make a file called `main.py` or whatever (if you choose to name it something else you need to edit the code in the `engine.py` file at lines 2, 52, 60, and 61)
3. PLEASE DOWNLOAD THE LIBRARY
4. PLEASE ADD A FONT IF YOU PLAN ON USING THE `text()` FUNCTION
5. Thats it on downloading :D


# How to use
This is all the functions and what they do

## init_engine()
`image_import()` goes here NOT variables

## update()
This updates every frame at 60 FPS

Here you put variables to be updated every frame

## draw()
Draws on the screen

### image_import(image, object_name)
`image` is the file path to the image you want to load

`object_name` is the name you want to reference in the `draw()` function

### draw(object_name, x, y)
`object_name` is the name of the image you imported

`x` is the horizontal position you want to draw the image at

`y` is the vertical position you want to draw the image at

### text(text_to_display, x, y, colour)
`text_to_display` is the text you want to write onto the screen

`x` is the horizontal position you want to write the text at

`y` is the vertical position you want to write the text at

(optional) `colour` is the colour you want the text to be, it is set to white by default
