# Create a program that reads data from https://www.w3schools.com/xml/plant_catalog.xml and builds parallel arrays for the plant items, with each array containing the plant's full name, zone, light, and price, respectively. Availability will be ignored. After reading the data and building the arrays, display the plant items similar to the following:
#    common name (botanical name) - zone - light - price

# At the bottom, display the total number of items in the catalog and the average price per item similar to:

#    0 items - $0.00 average price

# https://en.wikiversity.org/wiki/Python_Programming/Internet_Data
# The xml.etree.ElementTree.iter() method returns an iterator that
# loops over all elements in the tree, in section order
# https://www.w3schools.com/xml/xml_examples.asp
# https://www.w3schools.com/xml/plant_catalog.xml
# https://en.wikiversity.org/wiki/Python_Programming/RegEx
# https://regex101.com/
# https://snakify.org/en/lessons/strings_str/
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# https://snakify.org/en/lessons/strings_str/
# http://interactivepython.org/runestone/static/CS152f17/Lists/Listsandforloops.html
# https://www.tutorialspoint.com/python/python_if_else.htm
# https://www.techbeamers.com/use-try-except-python/
# http://gestaltrevision.be/wiki/python/errors


import os
import sys
import re

def get_group(tag):
	pattern = "<" + str(tag) + ">(.*)<\/" + str(tag) + ">"  
	return pattern


def collect_arrays(file_string):
	array = []
	tags = ["COMMON", "BOTANICAL", "ZONE", "LIGHT", "PRICE"]
	for tag in tags:
		pattern = get_group(tag)
		match = re.findall(pattern, file_string)
		array.append(match)
	return array

	
def display_average_item(array):
  temp_array = []
  average = 0
  for item in array:
    item = float(item[1:])
    temp_array.append(item)
    average = sum(temp_array)/len(array)
  try:
    average = sum(temp_array)/len(array)
  except ZeroDivisionError:
    average = float('Inf')
  print("%s items - $%.2f average price" % (len(array), average))
   

def get_file(filename):
  try:
    file = open(filename, "r")
    file_string = file.read()
    file.close()
    return file_string 
  except:
    print("Error Reading", filename)
    print(sys.exc_info()[1])


def display_output(array):
    for i in range(len(array[0])):
        temp_string = array[0][i] + " ( " + array[1][i] + " ) - " 
        temp_string += array[2][i] + " - " + array[3][i] + " - " + array[4][i]
        print(temp_string) 

def handle_error(filename):
	try:
		file = open(filename, "r")
		file_string = file.read()
	except:
		if not file_string:
			print("Error Opening", filename)
			print(sys.exc_info()[1])
		elif ValueError:
			print("Error Missing", filename)
			print(sys.exc_info()[1])
		elif ValueError:
			print("Error Invalid", filename)
			print(sys.exc_info()[1])
		else: 
			file.close()

def main():
  filename = "plant_catalog.xml"
  if os.path.isfile(filename):
    handle_error(filename)
    file_string = get_file(filename)
    array = collect_arrays(file_string)
    display_output(array)
    display_average_item(array[4])
  else:
    print("File doesn't exists.")

main()	

 
 