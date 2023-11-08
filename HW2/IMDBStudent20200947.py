#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
genre = []

with open(input_file) as file:
    for line in file:
        i = line.split("::")
        for g in i[2].split("|"):
            genre.append(g.rstrip("\n"))
            
genre_dict = {}

for g in genre:
    genre_dict[g] = 0
    
for g in genre_dict:
    with open(input_file) as file:
        for line in file:
            if g in line:
                genre_dict[g] += 1
                        
with open(output_file, "w", encoding="utf-8") as file:
    for g in genre_dict:
        file.write("{} {}\n".format(g, genre_dict[g]))
