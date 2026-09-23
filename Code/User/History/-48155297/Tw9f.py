# Write code here
knight_position = input()
number_of_pieces = int(input())

# knight position
(k_col,k_row) = knight_position.split(" ")
knight_colums= ord(k_col) - ord("a") +1
knight_row = int(k_row) 

chess_piece_of_opponent=[]

for i in range(number_of_pieces):
    (x,y)= input().split(" ")
    chess_piece_of_opponent.append((x,y))

#print(chess_piece_of_opponent)

knight_attack_moves=[(2,1),(2,-1),(-2,-1),(-2,1),(-1,-2),(1,-2),(1,2),(-1,2)]

print((kc,kr))