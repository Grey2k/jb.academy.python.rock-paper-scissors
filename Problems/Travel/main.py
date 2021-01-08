# add Turkey to countries.txt
from os import linesep

countries = open('countries.txt', 'a')

countries.write('Turkey' + linesep)
countries.close()
