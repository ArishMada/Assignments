# calculate the height the image must be in order to preserve the aspect ratio
def calc_new_height():
    current_width = float(input('Enter the current width: '))
    current_height = float(input('Enter the current height: '))
    desired_width = float(input('Enter the desired width: '))
    # the ratio should be the same so current width/current height should equal to desired width/desired height
    # desired height therefore equals to desired width*current height/current width
    corresponding_height = desired_width * current_height / current_width

    print(f'The corresponding height is: {corresponding_height}')
    print(corresponding_height)


calc_new_height()
