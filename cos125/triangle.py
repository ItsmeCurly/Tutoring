def triangle(width, height):
    for i in range(height):
        spacing = int((height-i)/2)
        space_str = spacing * "-"
        inner_space_str = (width - spacing*2 - 2) * "-"
        print(f"{space_str}*{inner_space_str}*{space_str}")
    
if __name__ == "__main__":
    triangle(5, 19)