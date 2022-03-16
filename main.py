if __name__ == '__main__':

    import pygame
    import time

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 80)
    textsurface = myfont.render('Chess', False, (0, 0, 0))



    # variables

    #width = 1560 #960
    #height = 960 #960
    fps = 60
    delay = 1000 / fps
    background_color = (0, 0, 20)

    square_color_black = (105, 57, 3)
    square_color_black_clicked = (75, 27, 0)
    square_color_white = (250, 225, 197)
    square_color_white_clicked = (200, 175, 147)
    square_size = 120

    clicked = 0

    turn = "White"

    DEFAULT_IMAGE_SIZE = (120, 120)
    # images
    # sample: carImg = pygame.image.load('racecar.png')
    Black_Pawn = pygame.image.load('Pieces/Black_Pawn.png')
    Black_Knight = pygame.image.load('Pieces/Black_Knight.png')
    Black_Bishop = pygame.image.load('Pieces/Black_Bishop.png')
    Black_King = pygame.image.load('Pieces/Black_King.png')
    Black_Queen = pygame.image.load('Pieces/Black_Queen.png')
    Black_Rook = pygame.image.load('Pieces/Black_Rook.png')

    White_Pawn = pygame.image.load('Pieces/White_Pawn.png')
    White_Knight = pygame.image.load('Pieces/White_Knight.png')
    White_Bishop = pygame.image.load('Pieces/White_Bishop.png')
    White_King = pygame.image.load('Pieces/White_King.png')
    White_Queen = pygame.image.load('Pieces/White_Queen.png')
    White_Rook = pygame.image.load('Pieces/White_Rook.png')

    Black_Pawn = pygame.transform.scale(Black_Pawn, DEFAULT_IMAGE_SIZE)
    Black_Knight = pygame.transform.scale(Black_Knight, DEFAULT_IMAGE_SIZE)
    Black_Bishop = pygame.transform.scale(Black_Bishop, DEFAULT_IMAGE_SIZE)
    Black_King = pygame.transform.scale(Black_King, DEFAULT_IMAGE_SIZE)
    Black_Queen = pygame.transform.scale(Black_Queen, DEFAULT_IMAGE_SIZE)
    Black_Rook = pygame.transform.scale(Black_Rook, DEFAULT_IMAGE_SIZE)

    White_Pawn = pygame.transform.scale(White_Pawn, DEFAULT_IMAGE_SIZE)
    White_Knight = pygame.transform.scale(White_Knight, DEFAULT_IMAGE_SIZE)
    White_Bishop = pygame.transform.scale(White_Bishop, DEFAULT_IMAGE_SIZE)
    White_King = pygame.transform.scale(White_King, DEFAULT_IMAGE_SIZE)
    White_Queen = pygame.transform.scale(White_Queen, DEFAULT_IMAGE_SIZE)
    White_Rook = pygame.transform.scale(White_Rook, DEFAULT_IMAGE_SIZE)

    rows = 8
    columns = 8
    squares_list = []
    # start pygame
    width = columns * 120 + 350
    height = rows * 120

    pygame.init()

    screen = pygame.display.set_mode((width, height))


    class square:
        def __init__(self, x, y, state):
            self.x = x
            self.y = y
            self.state = state
            self.clicked = False
            self.moved = False
            # black/white chess board pattern
            if (self.x + self.y) % 2 == 0:  # if square (x + y)/2 remainder = 0(even) set square color to white
                if self.clicked == True:
                    self.color = square_color_white_clicked
                else:
                    self.color = square_color_white


            elif (self.x + self.y) % 2 == 1:  # else set it to black
                if self.clicked == True:
                    self.color = square_color_black_clicked
                else:
                    self.color = square_color_black



    # creates board
    for y in range(rows):
        for x in range(columns):
            squares_list.append(square(x, y, "-"))


    def printboard():
        for items in squares_list:
            pygame.draw.rect(screen, items.color,
                             pygame.Rect(items.x * square_size, items.y * square_size, square_size, square_size))
            if items.state != "-":
                if items.state == "BP":
                    screen.blit(Black_Pawn, (items.x * square_size - 3, items.y * square_size + 3))
                if items.state == "BN":
                    screen.blit(Black_Knight, (items.x * square_size - 3, items.y * square_size + 3))
                if items.state == "BB":
                    screen.blit(Black_Bishop, (items.x * square_size, items.y * square_size))
                if items.state == "BK":
                    screen.blit(Black_King, (items.x * square_size, items.y * square_size))
                if items.state == "BQ":
                    screen.blit(Black_Queen, (items.x * square_size, items.y * square_size))
                if items.state == "BR":
                    screen.blit(Black_Rook, (items.x * square_size - 3, items.y * square_size + 3))

                if items.state == "WP":
                    screen.blit(White_Pawn, (items.x * square_size - 3, items.y * square_size + 3))
                if items.state == "WN":
                    screen.blit(White_Knight, (items.x * square_size - 3, items.y * square_size + 3))
                if items.state == "WB":
                    screen.blit(White_Bishop, (items.x * square_size, items.y * square_size))
                if items.state == "WK":
                    screen.blit(White_King, (items.x * square_size, items.y * square_size))
                if items.state == "WQ":
                    screen.blit(White_Queen, (items.x * square_size, items.y * square_size))
                if items.state == "WR":
                    screen.blit(White_Rook, (items.x * square_size - 3, items.y * square_size + 3))


    def addpiece(piece, x, y):
        if x < 0:
            x = 0
        if x > columns-1:
            x = columns
        if y < 0:
            y = 0
        if y > rows:
            y = rows
        for items in squares_list:
            if items.x == x and items.y == y:
                items.state = piece


    def setupboard():  # sets up the chess board in a conventional way

        for x in range(columns):
            addpiece("BP", x, 1)
            if x > 7:
                addpiece("BR", x, 0)
        addpiece("BR", 0, 0)
        addpiece("BN", 1, 0)
        addpiece("BB", 2, 0)
        addpiece("BQ", 3, 0)
        addpiece("BK", 4, 0)
        addpiece("BB", 5, 0)
        addpiece("BN", 6, 0)
        addpiece("BR", 7, 0)


        for x in range(columns):
            addpiece("WP", x, 6)
            if x > 7:
                addpiece("WR", x, 7)
        addpiece("WR", 0, 7)
        addpiece("WN", 1, 7)
        addpiece("WB", 2, 7)
        addpiece("WQ", 3, 7)
        addpiece("WK", 4, 7)
        addpiece("WB", 5, 7)
        addpiece("WN", 6, 7)
        addpiece("WR", 7, 7)

    def check_bishop_diagonal(pos_1, pos_2, x_direction, y_direction):
        succeeded = True
        for x in range(abs(pos_2.x - pos_1.x) - 1):  # correct
            for items in squares_list:
                if items.x == pos_1.x + x*x_direction + x_direction and items.y == pos_1.y + x*y_direction + y_direction:
                    if items.state != "-":
                        succeeded = False
                        print("blocked", items.x, " ", items.y)
        return succeeded


    def check_piece_inbetween(pos_1, pos_2):

        print("-------------------")
        if pos_1.state[1] == "B" or pos_1.state[1] == "Q":
            #+x +y
            if abs(pos_1.x - pos_2.x) == abs(pos_1.y - pos_2.y):


                if pos_1.x < pos_2.x and pos_1.y < pos_2.y and check_bishop_diagonal(pos_1, pos_2, 1, 1): #correct
                    return True
                if pos_1.x > pos_2.x and pos_1.y > pos_2.y and check_bishop_diagonal(pos_1, pos_2, -1, -1): #correct
                    return True
                if pos_1.x < pos_2.x and pos_1.y > pos_2.y and check_bishop_diagonal(pos_1, pos_2, 1, -1): #correct
                    return True
                if pos_1.x > pos_2.x and pos_1.y < pos_2.y and check_bishop_diagonal(pos_1, pos_2, -1, 1): #correct
                    return True
                else:
                    return False

            else:
                print("i am being stuck here")
                return False







        for items in squares_list:
            if items.x < pos_1.x and items.x > pos_2.x  and pos_1.y == items.y or items.x > pos_1.x and items.x < pos_2.x and pos_1.y == items.y:
                if items.state != "-":


                    return False

        for items in squares_list:
            if items.y < pos_1.y and items.y > pos_2.y  and pos_1.x == items.x or items.y > pos_1.y and items.y < pos_2.y and pos_1.x == items.x:
                if items.state != "-":
                    return False


        return True


    def legal_move(pos_1, pos_2, piece):
        if piece[1] == "R": #if piece is a rook
            if pos_2.x - pos_1.x == 0 and check_piece_inbetween(pos_1, pos_2): #if its x position doesn't change

                return True #move is legal
            if pos_2.y - pos_1.y == 0 and check_piece_inbetween(pos_1, pos_2):

                return True #move is legal
            else:
                return False


        if piece[1] == "P": #if piece = pawn
            if pos_2.x - pos_1.x == 0 and check_piece_inbetween(pos_1, pos_2) and pos_2.state == "-": #if the x value is different then the move is illegal and calls check_piece_inbetween function
                if piece[0] == "B" and pos_2.y - pos_1.y == 1: #if piece black and it moves downwards

                    return True #move is legal

                elif piece[0] == "B" and pos_2.y - pos_1.y == 2 and pos_1.moved == False: #if the pawn hasn't moved yet then it can move 2 spaces foward

                    return True#move is legal

                if piece[0] == "W" and pos_2.y - pos_1.y == -1: #if piece black and it moves upwards

                    return True #move is legal

                elif piece[0] == "W" and pos_2.y - pos_1.y == -2 and pos_1.moved == False: #if the pawn hasn't moved yet then it can move 2 spaces foward

                    return True #move is legal

                else:
                    return False #move is legal
            elif piece[0] == "B" and pos_1.x + 1 == pos_2.x and pos_1.y + 1 == pos_2.y and pos_2.state[0] == "W" or piece[0] == "B" and pos_1.x - 1 == pos_2.x and pos_1.y + 1 == pos_2.y and pos_2.state[0] == "W":
                return True #move is legal
            elif piece[0] == "W" and pos_1.x + 1 == pos_2.x and pos_1.y - 1 == pos_2.y and pos_2.state[0] == "B" or piece[0] == "W" and pos_1.x - 1 == pos_2.x and pos_1.y - 1 == pos_2.y and pos_2.state[0] == "B":
                return True #move is legal
            else:
                return False

        if piece[1] == "N": #knight
            if pos_1.x + 1 == pos_2.x and pos_1.y + 2 == pos_2.y or  pos_1.x - 1 == pos_2.x and pos_1.y + 2 == pos_2.y or pos_1.x + 1 == pos_2.x and pos_1.y - 2 == pos_2.y or  pos_1.x - 1 == pos_2.x and pos_1.y - 2 == pos_2.y:
                return True
            elif pos_1.x + 2 == pos_2.x and pos_1.y + 1 == pos_2.y or  pos_1.x - 2 == pos_2.x and pos_1.y + 1 == pos_2.y or pos_1.x + 2 == pos_2.x and pos_1.y - 1 == pos_2.y or  pos_1.x - 2 == pos_2.x and pos_1.y - 1 == pos_2.y:
                return True


            else:
                return False #move is not legal

        if piece[1] == "K": #king
            if pos_1.x+1 == pos_2.x and pos_1.y+1 == pos_2.y or pos_1.x-1 == pos_2.x and pos_1.y+1 == pos_2.y or pos_1.x+1 == pos_2.x and pos_1.y-1 == pos_2.y or pos_1.x-1 == pos_2.x and pos_1.y-1 == pos_2.y:
                return True
            elif pos_1.x+1 == pos_2.x and pos_2.y - pos_1.y == 0 or pos_1.x-1 == pos_2.x and pos_2.y - pos_1.y == 0:
                return True
            elif pos_1.y+1 == pos_2.y and pos_2.x - pos_1.x == 0 or pos_1.y-1 == pos_2.y and pos_2.x - pos_1.x == 0:
                return True
            else:
                return False

        if piece[1] == "B": #Bishop:
            if check_piece_inbetween(pos_1, pos_2):

                return True #move is legal
            else:
                return False

        else:
            return True #move is legal


    def move_piece(square_1, square_2,):
        global turn

        if legal_move(square_1, square_2, square_1.state):
            square_2.moved = True #needs to set the new position to have moved because pieces have no memory only squares do
            if square_1.state[0] == "B" and turn == "Black" and square_2.state[0] != "B":

                addpiece(square_1.state, square_2.x, square_2.y)
                addpiece("-", square_1.x, square_1.y)


                turn = "White"
            if square_1.state[0] == "W" and turn == "White" and square_2.state[0] != "W":


                addpiece(square_1.state, square_2.x, square_2.y)
                addpiece("-", square_1.x, square_1.y)

                turn = "Black"


    def mouse_inputs(x, y):
        global square_1
        global square_2


        global clicked

        for items in squares_list:
            if items.x*square_size + 120 > x and items.x*square_size < x and items.y*square_size + 120 > y and items.y*square_size < y:
                posx = items.x
                posy = items.y


                if clicked < 1 and items.state != "-":
                    if items.clicked == False:
                        if (items.x + items.y) % 2 == 0:  # if square (x + y)/2 remainder = 0(even) set square color to white

                            items.color = square_color_white_clicked

                        elif (items.x + items.y) % 2 == 1:
                            items.color = square_color_black_clicked

                        square_1 = items
                        items.clicked = True
                        clicked = 1

                elif items.clicked: #true
                    if (items.x + items.y) % 2 == 0:
                        items.color = square_color_white

                    elif (items.x + items.y) % 2 == 1:
                        items.color = square_color_black

                    items.clicked = False
                    clicked = 0
                elif clicked == 1:
                    square_2 = items
                    move_piece(square_1, square_2)




                    for i in squares_list: #reset board
                        if (i.x + i.y) % 2 == 0:
                            i.color = square_color_white

                        elif (i.x + i.y) % 2 == 1:
                            i.color = square_color_black

                        i.clicked = False
                        clicked = 0



    setupboard()
    if input("do you want to use the pre-determined opening?(y/n): ").lower() == "y":
        addpiece("-", 4, 7)
        addpiece("WK", 4, 6)
        addpiece("WP", 4, 4)

        addpiece("BP", 4, 3)
        addpiece("BK", 4, 1)
        addpiece("-", 4, 0)


    else:
        print("----")

    running = True
    while running:
        time.sleep(delay / 1000)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                mouse_inputs(x, y)
        keys = pygame.key.get_pressed()



        screen.fill(background_color)
        printboard()
        pygame.draw.rect(screen, (207, 154, 84), pygame.Rect(width - 350, 0, width, height))
        pygame.draw.rect(screen, (237, 184, 114), pygame.Rect(width - 350, 0, width, 160))
        screen.blit(textsurface, (width-300, 20))
        pygame.display.flip()