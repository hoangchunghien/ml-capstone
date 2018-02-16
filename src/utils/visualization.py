from IPython.display import Image
from IPython.core.display import HTML, display


def display_image_from_urls(urls, display_len=12):
    img_style = "width: 180px; margin: 0px; float: left; border: 1px solid black;"
    images_list = ''.join(['<img style="{}" src="{}" />'.format(img_style, u) for _, u in urls.head(display_len).iteritems()])

    display(HTML(images_list))
