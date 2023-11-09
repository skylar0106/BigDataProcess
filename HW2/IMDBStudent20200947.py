#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

genre = []

with open(input_file) as file:
    for line in file:
        i = line.split("::")
        i[2] = i[2].rstrip("\n")
        
        for g in i[2].split("|"):
            genre.append(g)
            
genre_dict = {}

for g in genre:
    genre_dict[g] = 0
    
with open(input_file) as file:
    for line in file:
        for g in genre_dict:
            if g in line:
                genre_dict[g] += 1
                        
with open(output_file, "wt") as file:
    for g in genre_dict:
        file.write("{} {}\n".format(g, genre_dict[g]))
