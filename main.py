"""
    ImageFinder
    A program to find (and open) all the images saved in the current computer user.
"""
import os
import webbrowser

img_list = []       # Contains the path of all found images


def find_imgs(ff_dir):
    """
    Find images recursively
    :param ff_dir: str - Current directory
    :return: none
    """
    print('Looking in', ff_dir)
    try:
        files = os.listdir(ff_dir)
        if len(files) != 0:
            for f in files:
                if f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.jpg'):
                    img_list.append(ff_dir + '/' + f)
                    print('\t\tFound', f)
            for f in files:
                find_imgs(ff_dir + '/' + f)     # Recursion
    except:
        # print('\n\tDEAD\n')
        return


def open_imgs():
    """
    Will open all images found
    :return: none
    """
    for p in img_list:
        webbrowser.open(p)


try:
    user = os.getlogin()    # Get the user currently logged in the computer
    loc = os.getcwd()       # Get the current directory
    f_dir = (loc.split(user))[0]+user       # Generate the user directory (will be used as the starting directory

    find_imgs(f_dir)        # Begin search

    print('\nFound ', len(img_list), 'images within', f_dir+'/...')

    # open_pics()       # Remove comment to open images

except():
    print('nope')




