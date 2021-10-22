import random

feet_in_miles = 5280
meters_in_kilometers = 1000
employess = ["1emp","2emp","3emp","4emp","5emp","6emp","7emp","8emp"]

def roll_dice(num):
    return random.randint(1,num)

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]



#print(roll_dice(10))
#print(get_file_ext("thisisafile.txt"))