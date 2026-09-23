# Write code here
knight_position = input()
number_of_pieces = int(input())

# knight position
(k_col,k_row) = knight_position.split(" ")
print(type(k_col))

chess_piece_of_opponent=[]

for i in range(number_of_pieces):
    (x,int(y))= input().split(" ")
    chess_piece_of_opponent.append((x,y))

print(chess_piece_of_opponent)

knight_attack_moves=[(2,1),(2,-1),(-2,-1),(-2,1),(-1,-2),(1,-2),(1,2),(-1,2)]

attack_positions= set()
for dc, dr in knight_attack_moves:
    target_col_ascii = int(ord(k_col)) +dc
    target_row = int(k_row) + dr
    if ord("a")<= target_col_ascii<=ord("h") and 1<= target_row<=8:
        target_col = chr(target_col_ascii)
        attack_positions.add((target_col,target_row))
attack_count = 0
attack_positions=list(attack_positions)
print(attack_positions)

for  i in range(number_of_pieces):
    if chess_piece_of_opponent[i] in attack_positions:
        attack_count = attack_count +1
print(attack_count)




