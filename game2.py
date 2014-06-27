def print_game(game):
	for row in game:
		print " | ".join(row)

def game_over():
    for i in range(0,3):
        if game[i][0] == game[i][1] == game[i][2] != " " \
        or game[0][i] == game[1][i] == game[2][i] != " ":
            print 'O' if xs_turn else 'X' + " won!!!"
            return True
        
    if game[0][0] == game[1][1] == game[2][2] != " " \
    or game[0][2] == game[1][1] == game[2][0] != " ":
    	print 'O' if xs_turn else 'X' + " won!!!"
        return True

    if " " not in game[0] and " " not in game[1] and " " not in game[2]:
        print "Draw"
        return True
        

    return False

game = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "]
]
print_game(game)
xs_turn = True
moved = False
while moved != True:
	print 'Please select your position by typing in a number between 1 and 9. Look at the chart below as an example: '
	print '5|6|4'
	print '2|3|1'
	print '8|9|7'
	print_game(game)

	try:
		pos = raw_input('Select: ')
		if pos <=9 and pos >=1:
			Y = pos/3
			X = pos%3
			if X != 0:
				X -=1
			else:
				X = 2
				Y -= 1
	except:
		print 'You need to add a numeric value'
	if pos == '9':
		x = 0
		y = 2
	elif pos == '8':
		x = 0
		y = 1
	elif pos == '7':
		x = 0
		y = 0
	elif pos == '6':
		x = 1
		y = 2
	elif pos == '5':
		x = 1
		y = 1
	elif pos == '4':
		x = 1
		y = 0
	elif pos == '3':
		x = 2
		y = 2
	elif pos == '2':
		x = 2
		y = 1
	elif pos == '1':
		x = 2
		y = 0
 
	xs_turn = not xs_turn	
	if xs_turn:
		game[x-1][y-1] = "x"
	else:
		game[x-1][y-1] = "o"