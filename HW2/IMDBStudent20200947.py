#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
genre = []

with open(input_file) as file:
    for line in file:
        cnt = 1
        for i in line.split("::"):
            if cnt % 3 == 0:
                for g in i.split("|"):
                    genre.append(g.rstrip("\n"))
            cnt += 1
            
genre = list(set(genre))
genre_dict = {}

for g in genre:
    genre_dict[g] = 0
print(genre_dict)
    
for g in genre_dict:
    with open(input_file) as file:
        for line in file:
            if g in line:
                genre_dict[g] += int(line.split("::")[0])
                        
with open(output_file, "w", encoding="utf-8") as file:
    for g in genre_dict:
        file.write("{} {}\n".format(g, genre_dict[g]))
