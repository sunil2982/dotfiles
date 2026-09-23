# Write code here
knight_position = input()
number_of_pieces = int(input())

chess_piece_of_opponent=[]

for i in range(number_of_pieces):
    pieces_place= input()
    chess_piece_of_opponent.append(pieces_place)

print(chess_piece_of_opponent)