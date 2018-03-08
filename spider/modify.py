import os

def tt(file):
    movie_name = os.listdir(file)
    for temp in movie_name:
        print(temp)
        if os.path.isdir("./cfile/"+temp):
            print(11111)
            tt("./cfile/"+temp)
        else:
            new_name = '[111]' + temp
            os.rename('./cfile/' + temp, 'cfile/' + new_name)

tt('./cfile')