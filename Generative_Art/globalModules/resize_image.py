def get_size(image_path, max_width, max_height):
    """
    loads image from the path
    resizes it and out puts width and height
    """

    out_w, out_h = max_width, max_height

    image_fullsize = loadImage(image_path)
    w, h = image_fullsize.width, image_fullsize.height
    aspect_ratio = float(w)/float(h)

    if max_height * aspect_ratio <= max_width:
        out_w, out_h = int(max_height * aspect_ratio), int(max_height)

    else:
        out_w, out_h = int(max_width), int(max_width/aspect_ratio)

    return out_w, out_h
