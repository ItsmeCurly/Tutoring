def triangle(width, height):
    for i in range(height):
        for j in range(width):
            char = computeChar(height, width, i, j)
            print(char, end = '')
        print()
   
def computeChar(height, width, i, j):
    if (i == 0 or i == height -1)and j == int(width/2):
        return 'o'
    elif j == int(width/2):
        return 'e'
    elif i == height - 1:
        return 'o'
    elif j == int(width/2 + (width/height) * ((i+1)/2))-1 or j == int(width/2 - (width/height) * ((i+1)/2))+1:
        return 'o'
    elif j < int(width/2 + (width/height) * ((i+1)/2)) and j > int(width/2 - (width/height) * ((i+1)/2)):
        return 'e'
    else:
        return ' '
     
if __name__ == "__main__":
    triangle(23, 1)
