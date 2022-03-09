

if __name__ == '__main__':

    import pygame
    import time



    # variables

    width = 960
    height = 960
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
    pygame.init()

    screen = pygame.display.set_mode((width, height))






    class square:
        def __init__(self, x, y, state):
            self.x = x
            self.y = y
            self.state = state
            self.clicked = False
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
        if x > 7:
            x = 7
        if y < 0:
            y = 0
        if y > 7:
            y = 7
        for items in squares_list:
            if items.x == x and items.y == y:
                items.state = piece


    def setupboard():  # sets up the chess board in a conventional way

        for x in range(columns):
            addpiece("BP", x, 1)
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
        addpiece("WR", 0, 7)
        addpiece("WN", 1, 7)
        addpiece("WB", 2, 7)
        addpiece("WQ", 3, 7)
        addpiece("WK", 4, 7)
        addpiece("WB", 5, 7)
        addpiece("WN", 6, 7)
        addpiece("WR", 7, 7)
    def move_piece(square_1, square_2,):
        global turn
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

        pygame.display.flip()

