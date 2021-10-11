def fill_the_box(height, width, length, *args):
    volume = height * width * length
    for x in args:
        if x == 'Finish':
            break
        volume -= x

    if volume > 0:
        return f'There is free space in the box. You could put {volume} more cubes.'
    if volume < 0:
        return f'No more free space! You have {abs(volume)} more cubes.'
