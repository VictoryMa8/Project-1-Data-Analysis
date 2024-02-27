import string

def findName(name,outputFile): # Popular names
    infile = open("allNames.csv","r")
    outfile = open(outputFile,"w")
    aline = infile.readline() # Skips over first line
    outfile.write("Artist \tSong \tYear\n") # Creates descriptors
    while aline:
      bline = infile.readline()
      if aline != bline:
        items = aline.strip().split("\t") # Seperates data
        if items[5] == name:
            dataline = items[0]+"\t"+items[1]+"\t"+items[3] # Dataline is "Artist, Song, Year"
            outfile.write(dataline + '\n') # Writes data
        aline = bline

    infile.close() # Closes file
    outfile.close()
    return outputFile


def findRepeatedNameSongs(threshold, outputfile): # Repeat names
  file = open("allNames.csv") 
  file.readline() # Skips first line
  outfile = open(outputfile, "w") # Readies the outputfile
  outfile.write("Name \tTimes \tArtist \tSong\n") # Writes descriptors
  dict = {}
  
  for line in file:
    items = line.strip().split("\t")
    if items[5]+':'+items[0]+':'+items[1] in dict: # If a unique name (from one song by an artist) is in the dictionary
      dict[items[5]+':'+items[0]+':'+items[1]] += 1 # Add occurence
    else:         
      dict[items[5]+':'+items[0]+':'+items[1]] = 1 # If not, initialize it

  for i in dict:
    if dict[i] >= threshold: # If number of occurences meets certain point, write it
      x = i.split(':')
      times = str(dict[i]) # Number of times
      data = x[0]+','+times+','+x[1]+','+x[2] # Data is "Artist, Times, Artist, Song"
      outfile.write(data + '\n') # Writes data
      
  file.close() # Closes file
  outfile.close()
  return outputfile


def findUniqueNameSongs(threshold, outputfile): # Unique names
  file = open("allNames.csv") # Opens file
  file.readline() # Reads the first line (descriptors of each column)
  outfile = open(outputfile, "w") # Prepare the outputfile to write
  outfile.write("Number \tArtist \tSong\n") # First line says Number, Artist, and Song
  
  dict_of_songs = {} # Dictionary of every song
  
  for line in file:
    items = line.strip().split("\t") # Split items
    
    key = items[0]+':'+items[1] # Key is an artist and song
    name = items[5] # Name in the line
    
    if key not in dict_of_songs: # If a song is not already in the dictionary..
      dict_of_songs[key] = {} # Put the song in the dictionary
    else:
      if name not in dict_of_songs[key]: # If a name is not in the song's dictionary
        dict_of_songs[key][name] = 1 # Initialize the name
      else:
        dict_of_songs[key][name] += 1 # Add to the occurence total

  for key in dict_of_songs: # For every song
    length = len(dict_of_songs[key]) # Number of unique names in a song
    if length >= threshold: # If number of unique names
      x = key.split(':') # Split the key into artist and song
      artist = x[0]
      song = x[1]
      data = str(length)+','+artist+','+song  # Length, artist, song
      outfile.write(data + '\n') # Write the data

  file.close() # Closes file
  outfile.close()
  return outputfile 

def countNameDecades(name, outputfile): # Timeless names
  infile = open("allNames.csv","r") # Opens file
  outfile = open(outputfile,"w")
  aline = infile.readline() # Reads first line
  outfile.write("Number \tDecade\n") # Writes descriptors
  count0 = set()
  count1 = set()
  count2 = set()
  count3 = set()
  count4 = set()
  while aline:
    items = aline.strip().split("\t")
    if items[5] == name:
      if int(items[3]) >= 1970 and int(items[3]) < 1980:
        count0.add(items[0] + items[1] + items[2] + items[3] + items[4] + items[5])
      if int(items[3]) >= 1980 and int(items[3]) < 1990:
        count1.add(items[0] + items[1] + items[2] + items[3] + items[4] + items[5])
      if int(items[3]) >= 1990 and int(items[3]) < 2000:
        count2.add(items[0] + items[1] + items[2] + items[3] + items[4] + items[5])
      if int(items[3]) >= 2000 and int(items[3]) < 2010:
        count3.add(items[0] + items[1] + items[2] + items[3] + items[4] + items[5])
      if int(items[3]) >= 2010 and int(items[3]) < 2020:
        count4.add(items[0] + items[1] + items[2] + items[3] + items[4] + items[5])
    aline = infile.readline()

  outfile.write(str(len(count0))+"\t"+"1970"+"\n")
  outfile.write(str(len(count1))+"\t"+"1980"+"\n")
  outfile.write(str(len(count2))+"\t"+"1990"+"\n")
  outfile.write(str((len(count3)))+"\t"+"2000"+"\n")
  outfile.write(str(len(count4))+"\t"+"2010"+"\n")
  infile.close() # Closes file
  outfile.close()
  return outputfile


def countStartLetter(outputfile): #Names that start with...
    infile1 = open("allNames.csv","r")
    infile2 = open("onlyNames.csv","r")
    outfile = open(outputfile,"w")
    aline = infile1.readline()
    aline = infile1.readline() #Skip first line
    bline = infile2.readline()
    bline = infile2.readline() #Skip first line
    dict0 = {}
    dict1 = {}
    dictprop1 = {}
    total1 = 0
    dict2 = {}
    dictprop2 = {}
    total2 = 0
    for char in string.ascii_uppercase:
        dict1[char] = 0
        dictprop1[char] = 0
        dict2[char] = 0
        dictprop2[char] = 0

    outfile.write("letter \tproportion\n")

    while aline:
        items = aline.strip().split("\t")
        keys = items[0] + items[1]
        name = items[5]
        firstLetter = name[0].upper()
        if keys not in dict0:
            dict0[keys] = name
            dict1[firstLetter] += 1
            total1 += 1
        aline = infile1.readline()

    while bline:
        items = bline.strip().split("\t")
        name = items[0]
        firstLetter = name[0].upper()
        dict2[firstLetter] += int(items[1])
        total2 += int(items[1])
        bline = infile2.readline()

    for keys in dict1:
        dictprop1[keys] = (dict1[keys] / total1) * 100

    for keys in dict2:
        dictprop2[keys] = (dict2[keys] / total2) * 100

    for keys in dictprop1:
        outfile.write(keys + "\t" + str(dictprop1[keys] - dictprop2[keys]) + "%\n")

    return outputfile

def countEndLetter(outputfile): #Names that end with...
    infile1 = open("allNames.csv","r")
    infile2 = open("onlyNames.csv","r")
    outfile = open(outputfile,"w")
    aline = infile1.readline()
    aline = infile1.readline() #Skip first line
    bline = infile2.readline()
    bline = infile2.readline() #Skip first line
    dict0 = {}
    dict1 = {}
    dictprop1 = {}
    total1 = 0
    dict2 = {}
    dictprop2 = {}
    total2 = 0
    for char in string.ascii_uppercase:
        dict1[char] = 0
        dictprop1[char] = 0
        dict2[char] = 0
        dictprop2[char] = 0

    outfile.write("letter \tproportion\n")

    while aline:
        items = aline.strip().split("\t")
        keys = items[0] + items[1]
        name = items[5]
        firstLetter = name[-1].upper()
        if keys not in dict0:
            dict0[keys] = name
            dict1[firstLetter] += 1
            total1 += 1
        aline = infile1.readline()

    while bline:
        items = bline.strip().split("\t")
        name = items[0]
        firstLetter = name[-1].upper()
        dict2[firstLetter] += int(items[1])
        total2 += int(items[1])
        bline = infile2.readline()

    for keys in dict1:
        dictprop1[keys] = (dict1[keys] / total1) * 100

    for keys in dict2:
        dictprop2[keys] = (dict2[keys] / total2) * 100

    for keys in dictprop1:
        outfile.write(keys + "\t" + str(dictprop1[keys] - dictprop2[keys]) + "%\n")

    return outputfile

def main(): # Tests
  findName("Jack","tests/jack.csv")
  findName("Peter","tests/peter.csv")
  findName("Mary","tests/mary.csv")
  countNameDecades("Mary", "tests/mary.decades.csv")
  countNameDecades("Joe", "tests/joe.decades.csv")
  countNameDecades("Madison", "tests/madison.decades.csv")
  findRepeatedNameSongs(20, "tests/repeat.20.csv")
  findRepeatedNameSongs(30, "tests/repeat.30.csv")
  findRepeatedNameSongs(40, "tests/repeat.40.csv")
  findUniqueNameSongs(15, "tests/unique.15.csv")
  findUniqueNameSongs(20, "tests/unique.20.csv")
  countStartLetter("tests/names.start.csv")
  countEndLetter("tests/names.end.csv")
  
main() # Main function

# Created by Yiming Zhang & Victory Ma




