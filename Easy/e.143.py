bralpha = ["O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..",
       "O.OO..",".OO...",".OOO..","O...O.","O.O.O.", "OO..O.","OO.OO.",
       "O..OO.","OOO.O.","OOOOO.", "O.OOO.",".OO.O.",".OOOO.","O...OO",
       "O.O.OO",".OOO.O","OO..OO","OO.OOO","O..OOO"]
braille = {bra: eng for bra, eng in zip(bralpha, 'abcdefghijklmnopqrstuvwxyz')}
br_input = [(list(raw_input().split(" "))) for i in range(3)]
print ''.join([braille[k] for k in [''.join(i) for i in zip(*br_input)]])
