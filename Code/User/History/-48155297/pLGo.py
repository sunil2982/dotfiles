# Write code here
knight_position = input()
number_of_pieces = int(input())

chess_piece_of_opponent=[]
chess_piece=[]
for i in range(number_of_pieces):
    pieces_place= input()
    chess_piece_of_opponent.append(pieces_place)

for  sp in chess_piece_of_opponent:
    (x,y) = sp.split(" ")
    chess_piece.append((x,y))

print(chess_piece)