#!/usr/bin/env python

# just a random list generator
def get_random_cell(h: int, w: int) -> [int,int]:
  from random import randint
  return [randint(0,h-1),randint(0,w-1)]

# place mines and return a grid
def place_mines(height: int, width: int, nmines:int) -> list:
  mines=[]
  grid=[ ['S'] * height for _ in range(width) ]
  while len(mines) < nmines:
    random_mine_location = get_random_cell(height,width)
    if random_mine_location not in mines:
      mines.append(random_mine_location)
      grid[random_mine_location[0]][random_mine_location[1]] = '*'
      #print(random_mine_location)
      for i in range(random_mine_location[0]-1,random_mine_location[0]+2):
        if i < height and i >= 0:
          for j in range(random_mine_location[1]-1,random_mine_location[1]+2):
            if j < width and j >= 0:
              if grid[i][j] == 'S':
                grid[i][j] = 'A'

  return grid

# naive step by step traversal
def play_minesweeper(grid: list) -> list:
  for height in range(0,len(grid)):
    for width in range(0,len(grid[height])):
      if grid[height][width] == '*':
        return [height,width]
      else:
        print(grid[height][width])
  return 100

battle_field = place_mines(10,10,10)
for row in battle_field:
  print(row)


print(play_minesweeper(battle_field))
#print(place_mines(10,10,10))
