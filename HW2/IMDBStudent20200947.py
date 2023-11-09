#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

genre = []
genre_dict = dict()

with open(input_file) as file:
    for line in file:
        l = line.split("::")
        l[2] = l[2].rstrip("\n")
        genre = l[2].split("|")
        for i in genre:
            if i in genre_dict:
                genre_dict[i] += 1
            else:
                genre_dict[i] = 1
                        
with open(output_file, "wt") as file:
    for g in genre_dict:
        file.write("{} {}\n".format(g, genre_dict[g]))
