from random import Random
CANVAS_HEIGHT, CANVAS_WIDTH = 800, 800

def main():
    file = open('file.html', 'w')
    file.write(f"""<html>
               <head></head>
               <body>
               <svg width=\"{CANVAS_WIDTH}\" height=\"{CANVAS_HEIGHT}\">\n""")
    file.close()
    rect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
    file = open('file.html', 'a')
    file.write('</svg></body></html>')
    file.close()

def rect(x, y, width, height):
    rand = Random()
    if width < 120 and height < 120:
        write_html(x, y, width, height)
    elif width > 120 and height > 120:
        rand_width = rand.randrange(120, int(width * 1.5))
        rand_height = rand.randrange(120, int(height * 1.5))
        if width > CANVAS_WIDTH/2 and height > CANVAS_HEIGHT/2:
            split_two(x, y, width, height)
        elif width > CANVAS_WIDTH/2:
            split_vert(x, y, width, height)
        elif height > CANVAS_HEIGHT/2:
            split_hor(x, y, width, height)
        elif width > rand_width and height > rand_height:
            split_two(x, y, width, height)
        elif width > rand_width:
            split_vert(x, y, width, height)
        elif height > rand_height:
            split_hor(x, y, width, height)
        else:
            write_html(x, y, width, height)
    elif width > 120:
        rand_width = rand.randrange(120, int(width * 1.5))
        if width > CANVAS_WIDTH/2 or width > rand_width:
            split_vert(x, y, width, height)
        else:
            write_html(x, y, width, height)
    elif height > 120:
        rand_height = rand.randrange(120, int(height * 1.5))
        if height > CANVAS_HEIGHT / 2 or height > rand_height:
            split_hor(x, y, width, height)
        else:
            write_html(x, y, width, height)


def split_two(x, y, width, height):
    rand = Random()
    v_split_pt = rand.randrange(33, 68)/100
    h_split_pt = rand.randrange(33, 68)/100
    rect(x, y, width * v_split_pt, height * h_split_pt)
    rect(x + width * v_split_pt, y, width * (1-v_split_pt), height * h_split_pt)
    rect(x, y + height * h_split_pt, width * v_split_pt, height * (1- h_split_pt))
    rect(x + width * v_split_pt, y + height * h_split_pt, width * (1 - v_split_pt), height * (1 - h_split_pt))

def split_vert(x, y, width, height):
    rand = Random()
    v_split_pt = rand.randrange(33, 68) / 100
    rect(x, y, width * v_split_pt, height)
    rect(x + width * v_split_pt, y, width * (1- v_split_pt), height)

def split_hor(x, y, width, height):
    rand = Random()
    h_split_pt = rand.randrange(33, 68) / 100
    rect(x, y, width, height * h_split_pt)
    rect(x, y + height * h_split_pt, width, height * (1-h_split_pt))

def write_html(x, y, width, height):
    file = open('file.html', 'a')
    file.write(f"""<rect x=\"{x}\" y=\"{y}\" width=\"{width}\" height=\"{height}\" style=\"fill:white;stroke-width:3;stroke:black\"/>\n""")
    file.close()
main()