# Write code here
knight_position = input()
number_of_pieces = int(input())


chess_piece_of_opponent=[]

for i in range(number_of_pieces):
    (x,y)= input().split(" ")
    chess_piece_of_opponent.append((x,y))

#print(chess_piece_of_opponent)

knight_attack_moves=[()]