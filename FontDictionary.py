# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:07:12 2022

@author: ovdessel
"""

letters = {'A':[[0,1,0],
                [1,0,1],
                [1,1,1],
                [1,0,1],
                ],
           
           'B':[[1,1,0],
                [1,1,1],
                [1,0,1],
                [1,1,0],
                ],
           
           'C':[[0,1,1],
                [1,0,0],
                [1,0,0],
                [0,1,1],
                ],
           
           'D':[[1,1,0],
                [1,0,1],
                [1,0,1],
                [1,1,0],
                ],
           
           'E':[[1,1,1],
                [1,1,0],
                [1,0,0],
                [1,1,1],
                ],

           'F':[[1,1,1],
                [1,1,0],
                [1,0,0],
                [1,0,0],
                ],

           'G':[[0,1,1],
                [1,0,0],
                [1,0,1],
                [0,1,1],
                ],

           'H':[[1,0,1],
                [1,1,1],
                [1,0,1],
                [1,0,1],
                ],
           
           'I':[[1,1,1],
                [0,1,0],
                [0,1,0],
                [1,1,1],
                ],
           
           'J':[[1,1,1],
                [0,0,1],
                [1,0,1],
                [0,1,0],
                ],
           
           'K':[[1,0,1],
                [1,1,0],
                [1,0,1],
                [1,0,1],
                ],

           'L':[[1,0,0],
                [1,0,0],
                [1,0,0],
                [1,1,1],
                ],

           'M':[[1,1,1],
                [1,1,1],
                [1,0,1],
                [1,0,1],
                ],

           'N':[[1,1,0],
                [1,0,1],
                [1,0,1],
                [1,0,1],
                ],

           'O':[[0,1,0],
                [1,0,1],
                [1,0,1],
                [0,1,0],
                ],
           
           'P':[[1,1,1],
                [1,0,1],
                [1,1,1],
                [1,0,0],
                ],
           
           'Q':[[0,1,0],
                [1,0,1],
                [1,1,1],
                [0,1,0],
                ],
           
           'R':[[1,1,0],
                [1,0,1],
                [1,1,0],
                [1,0,1],
                ],
           
           'S':[[0,1,1],
                [1,1,0],
                [0,0,1],
                [1,1,0],
                ],

           'T':[[1,1,1],
                [0,1,0],
                [0,1,0],
                [0,1,0],
                ],
           
           'U':[[1,0,1],
                [1,0,1],
                [1,0,1],
                [0,1,0],
                ],

           'V':[[1,0,1],
                [1,0,1],
                [1,1,0],
                [1,0,0],
                ],
           
           'W':[[1,0,1],
                [1,0,1],
                [1,1,1],
                [1,1,1],
                ],
           
           'X':[[1,0,1],
                [0,1,0],
                [1,0,1],
                [1,0,1],
                ],

           'Y':[[1,0,1],
                [0,1,0],
                [0,1,0],
                [0,1,0],
                ],

           'Z':[[1,1,1],
                [0,1,0],
                [1,0,0],
                [1,1,1],
                ],
           
           '.':[[0],
                [0],
                [0],
                [1]
                ],
           
           ' ':[[0],
                [0],
                [0],
                [0],
                ],
           
           '!':[[1,0],
                [1,0],
                [0,0],
                [1,0],
                ],
           
           '?':[[1,1,1],
                [0,0,1],
                [0,0,0],
                [0,1,0],
                ],
           
           r"'":[[0,1,0],
                 [0,0,0],
                 [0,0,0],
                 [0,0,0],
                ],
           
    }


def string_to_bitmap(string):
#build bitmap list
    #string = "TEST this very long string. and hopefully everything works now that lists make sense."
    line = []
    line_length = 0
    bitmap = [[0 for _ in range(32)] for _ in range(4)]
    
    #go through each character
    for char in string.upper().split(',')[1]:
        #skip if letter not in dictionary
        if not char in letters.keys():
            continue
        
        #if its too long, go to new line and reset
        if line_length+len(letters[char][0])+1 > 32:
            line.append(bitmap)
            line_length = 0
            bitmap = [[0 for _ in range(32)] for _ in range(4)]

        #build map
        for n in range(4):
            for c in range(len(letters[char][0])):
                bitmap[n][line_length + c] = letters[char][n][c]
           
        line_length += len(letters[char][0])+1
   
    line.append(bitmap)
    ########################################################################
    
    display = [[0 for _ in range(32)] for _ in range(5*len(line))]
    for line_num in range(len(line)):
        for row_num in range(len(line[line_num])):
            for col_num in range(len(line[line_num][row_num])):
                display[row_num+line_num*5][col_num] = line[line_num][row_num][col_num]
            

    return display

# string = "pew pew. guess we need to add buffers"
# bitmap = string_to_bitmap(string)

#pixel to pixel translation
# bitmap in bitmap out display limited
def bitmap_to_display(bitmap):
    new_map = [[0 for _ in range(64)] for _ in range(8)]
    temp_map = [[0 for _ in range(32)] for _ in range(16)]
    
    #fit to full frame
    if len(bitmap)<16: row_count = len(bitmap)
    else: row_count = 16
    for row in range(row_count):
        for col in range(len(bitmap[row])):
            temp_map[row][col] = bitmap[row][col]
    
    #Transform coordinates to display     
    for row in range(8):
        #add first row normally
        for col in range(0,32):
            new_map[row][col] = temp_map[row][col]
        
        #add next 32
        for col in range(0,32):
            new_map[row][32+col] = temp_map[-row-1][-col-1]
    return new_map
    
# import numpy as np
# test = np.array(bitmap_to_display(bitmap))



    
    