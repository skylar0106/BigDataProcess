#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
genre = []
genre_cnt = []

with open(input_file) as file:
    for line in file:
        cnt = 1
        for i in line.split("::"):
            if cnt % 3 == 0:
                for g in i.split("|"):
                    genre.append(g.rstrip("\n"))
            cnt += 1
            
genre = list(set(genre))

for g in genre:
    print(g)
    with open(input_file) as file:
        genre_cnt.append(file.read().count(g))
        
with open(output_file, "w", encoding="utf-8") as file:
    for v1, v2 in zip(genre, genre_cnt):
        file.write("{} {}\n".format(v1, v2))
