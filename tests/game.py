import sys
sys.path.append("../")

from xiangqi.XiangqiGame import XiangqiGame


if __name__ == "__main__":
    game = XiangqiGame()

    print(game.make_move("c1", "e3"))  # red
    print(game.make_move("a10", "a8"))  # black
    print(game.make_move("a4", "a5"))  # red
    print(game.make_move("a7", "a6"))  # black
    print(game.make_move("a5", "a6"))  # red
    print(game.make_move("a8", "a6"))  # black
    print(game.make_move("a1", "a6"))  # red
    print(game.make_move("c10", "a8"))  # black
    print(game.make_move("a6", "a7"))  # red
    print(game.make_move("g7", "g6"))  # black
    print(game.make_move("a7", "a8"))  # red
    print(game.make_move("b10", "a8"))  # black

    print(game)
    sys.exit()

    # test progression of a soldier
    print(game.make_move("c1", "e3"))  # red
    print(game.make_move("i10", "i8")) # black
    print(game.make_move("e3", "i4"))  # red; elephants can't cross the river!
    print(game.make_move("d1", "e2")) # still red; advisor
    print(game.make_move("b10", "c8")) # black; horse
    # march some soldiers across the river!
    print(game.make_move("i4", "i5")) # red
    print(game.make_move("i7", "i6")) # black
    print(game.make_move("i5", "i6"))# red  simulate capture

    # print(game._board.get_army_of("black")._personnel["soldiers"])
    # print(game._board.get_army_of("red")._personnel["soldiers"])

    print(game.make_move("g7", "g6")) # black
    print(game.make_move("i6", "h6"))# red
    print(game.make_move("i8", "i1")) # black
    # print(game.make_move("a10", "a6"))# red
    # ... still red's turn since above is impossible
    # print(game.make_move("h1", "g3"))  # red

    print(game.make_move("h3", "f3"))# red
    print(game.make_move("h8", "f8"))# black

    print(game.make_move("f3", "f10"))# red
    print(game.make_move("c10", "e8"))# black

    print(game)
    sys.exit()

    print(game.make_move("h8", "h3")) # black Cannon
    print(game.make_move("b3", "b9")) # red Cannon == false

    # print(repr(game._board.get_contents_of(("i", 5))))

    # S = Soldier("red")
    # S._has_crossed_river = True
    # print(S.is_move_legal(game._board, ("i", 5), ("h", 5)))

    # black
    # red
    # black

    print(game)
    sys.exit()

    # print(game.make_move("c1", "e3"))
    # game._current_turn_is_for = "black"
    # print(game.make_move("a10", "a8"))

    # print(game.make_move("a1", "a3"))
    # print(game._board)
    # print(game)

    # S = Soldier("red")
    # print(repr(S))
    # print(S.is_move_legal(game._board, ("a", 3), ("a", 4)))  # basic test
    # print(S.is_move_legal(game._board, ("a", 3), ("a", 2)))  # test for backward

    # test for capture
    # S._has_crossed_river = True
    # print(S.is_move_legal(game._board, ("e", 5), ("e", 6)))

    # print(S.is_move_legal(game._board, ("a", 3), ("g", 2)))  # test for across river
    # sys.exit()

    # C = Cannon("red")
    # print(repr(C))
    # print(C.is_move_legal(game._board, ("b", 2), ("b", 7)))
    # print(C.is_move_legal(game._board, ("c", 2), ("c", 6)))  # test for jumpability
    # print(C.is_move_legal(game._board, ("a", 1), ("i", 1)))
    # print(C.is_move_legal(game._board, ("b", 2), ("g", 2)))


    # R = Chariot("red")
    # print(repr(R))
    # print(R.is_move_legal(game._board, ("a", 0), ("a", 2)))
    # print(R.is_move_legal(game._board, ("a", 0), ("a", 9)))
    # print(R.is_move_legal(game._board, ("a", 1), ("i", 1)))


    # H = Horse("red")
    # print(repr(H))
    # print(E.is_move_legal(game._board, ("c", 0), ("e", 2)))
    # print(E.is_move_legal(game._board, ("c", 0), ("a", 2)))
    # print(H.is_move_legal(game._board, ("b", 0), ("c", 2)))

    # E = Elephant("red")
    # print(repr(E))
    # print(E.is_move_legal(game._board, ("c", 0), ("e", 2)))
    # print(E.is_move_legal(game._board, ("c", 0), ("a", 2)))
    # print(E.is_move_legal(game._board, ("c", 0), ("c", 2)))

    # A = Advisor("red")
    # print(repr(A))
    # print(A.is_move_legal(game._board, ("d", 0), ("e", 1)))
    # print(A.is_move_legal(game._board, ("e", 1), ("f", 2)))
    # sys.exit()


    move_result = game.make_move('c1', 'e3')
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()

    # --------

    # Test game - Red should win.
    game.make_move('h3', 'e3')
    game.make_move('h8', 'e8')
    game.make_move('e3', 'e7')
    game.make_move('e8', 'c8')
    game.make_move('b3', 'b5')
    game.make_move('h10', 'g8')
    game.make_move('b5', 'e5')
    # Test game - Black should win.
    game.make_move('b3', 'e3')
    game.make_move('b8', 'b7')
    game.make_move('h3', 'g3')
    game.make_move('h8', 'e8')
    game.make_move('g3', 'g7')
    game.make_move('e8', 'e4')
    game.make_move('e3', 'e7')
    game.make_move('b7', 'e7')
