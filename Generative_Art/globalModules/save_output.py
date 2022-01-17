import datetime
import re


def unique_name():
    """
    generates new name with date and time
    """
    return re.sub(r"\D", '', str(datetime.datetime.now())[:-4])


def save_img(ext=".png"):
    """saves image in the save folder of the package
        NOTE : save doesnt work when noLoop() is in draw function

    Args:
        ext (str, optional): extension of the saved file. Defaults to ".png".
    """
    img_path = "save/"+unique_name()+ext
    save(img_path)
    print("image saved : "+img_path)


_counter = 0
_newrun = True
_img_path = ''


def save_img_seq(max_frames=30000, ext=".png"):
    """saves image sequence in unique folder in the save folder of the package

    Args:
        max_frames (int, optional):maximum number of frames to be saved. Defaults to  30,000.
        ext (str, optional): extension of the saved file. Defaults to ".png".
    """
    global _counter, _newrun, _img_path

    if _newrun:
        _img_path = "save/"+unique_name() + "/######"+ext
        _newrun = False

    if _counter > max_frames:
        print("Max frame count reached")
        print("image sequence saved : "+_img_path)
        return

    saveFrame(_img_path)
    _counter += 1
