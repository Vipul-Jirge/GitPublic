_max_fps = 0
_min_fps = 1000000


def show_fps(text_size=15, x=10, y=10, details=True):
    """
    shows fps at (x,y) location
    text style can be decided
    details shows min and max fps values achieved
    """
    global _max_fps, _min_fps

    pushStyle()
    y += text_size
    text_size_small = text_size*0.8
    fps = frameRate
    _min_fps = min(_min_fps, fps)
    _max_fps = max(_max_fps, fps)
    textSize(text_size)
    text(str(round(fps, 4)), x, y)
    if details:
        textSize(text_size_small)
        s = "Min fps : "+str(round(_min_fps, 2)) + \
            "\nMax fps : "+str(round(_max_fps, 2))
        text(s, x, y+text_size*1.2)
    popStyle()
