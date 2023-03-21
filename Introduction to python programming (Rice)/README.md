# Python
An Introduction to Interactive Programming in Python (Part 1)
# Mini - project for Week 3
import simplegui

# Define global variables
counter = 0
x = 0
y = 0
stop = False
# Define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global counter
    d = str(counter)[len(str(counter))-1:]
    c = int(((counter/600.0)-(counter/600))*60%10)
    b = int(((counter/600.0)-(counter/600))*60//10)
    a = counter/600
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# Define event handlers for button: "Start", "Stop", "Reset"
def start():
    global counter
    counter += 1
    timer.start()
    global stop
    stop = True
def stop():
    global counter
    timer.stop()
    global stop
    global x
    
    if stop:
        x += 1
        global y
        stop = False
        if (counter%10) == 0:
            global y
            y += 1
            stop = False
        
    
def reset():
    global counter
    counter = 0
    global x
    x = 0 
    global y
    y = 0
    timer.stop()
    
# Define event handler for timer for 0.1 sec interval
def timer_handler():
    start()

# Define draw handler
def draw(canvas):
    global counter
    canvas.draw_text(format(),(100,120),34,"White")
    canvas.draw_text((str(y)+"/"+str(x)),(240,20),24,"Green")

# Create frame
frame = simplegui.create_frame("Stopwatch:The Game", 300, 200)

# Register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# Start frame
frame.start()
