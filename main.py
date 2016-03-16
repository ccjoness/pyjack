import random
import animation


class Card:
    def __init__(self, name, suit, value, art):
        self.name = name
        self.suit = suit
        self.value = value
        self.art = art
        self.a = art[0]
        self.b = art[1]
        self.c = art[2]
        self.d = art[3]
        self.e = art[4]
        self.f = art[5]
        self.g = art[6]

    @staticmethod
    def arts(s, v):
        if s == "Clubs":
            a = ".-------."
            b = "|   _   |"
            c = "| _( )_ |"
            d = "|(_ . _)|"
            e = "|   I   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Diamonds":
            a = ".-------."
            b = "|  / \\  |"
            c = "| /   \\ |"
            d = "| \\   / |"
            e = "|  \\ /  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Hearts":
            a = ".-------."
            b = "| ** ** |"
            c = "|*  *  *|"
            d = "| *   * |"
            e = "|   *   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Spades":
            a = ".-------."
            b = "|   *   |"
            c = "| *   * |"
            d = "|*     *|"
            e = "|  *I*  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g

    def card_art(self):
        return self.a + '\n' + self.b + '\n' + self.c + '\n' + self.d + '\n' + self.e + '\n' + self.f + '\n' + self.g

    def __str__(self):
        return "{name} of {suit}".format(name=self.name, suit=self.suit)

    def __repr__(self):
        return "{name} of {suit}".format(name=self.name, suit=self.suit)


class BlackJack:
    NAME_VALUE = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }
    SUIT = [
        "Clubs",
        "Diamonds",
        "Hearts",
        "Spades"
    ]

    def __init__(self):
        self.deck = self.create_decks()
        self.players = self.create_players()
        self.dealer = self.create_dealer()

    def first_deal(self):
        random.shuffle(self.deck)
        for pl in self.players:
            pl.hand.append(self.deck.pop())
            pl.hand.append(self.deck.pop())
        self.dealer.hand.append(self.deck.pop())
        self.dealer.hand.append(self.deck.pop())

    def hit(self, pl):
        if pl.hand_value() > 21:
            pass
        else:
            pl.hand.append(self.deck.pop())

    @staticmethod
    def create_players():
        how_many_players = int(input("How many players are there? "))
        x = 1
        p = []
        while x <= how_many_players:
            name = input("What is Player {} name? ".format(x))
            p.append(name)
            x += 1
        players = [Player(name=prop) for prop in p]
        return players

    @staticmethod
    def create_dealer():
        return Dealer()

    @staticmethod
    def arts(s, v):
        if s == "Clubs":
            a = ".-------."
            b = "|   _   |"
            c = "| _( )_ |"
            d = "|(_ . _)|"
            e = "|   I   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Diamonds":
            a = ".-------."
            b = "|  / \\  |"
            c = "| /   \\ |"
            d = "| \\   / |"
            e = "|  \\ /  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Hearts":
            a = ".-------."
            b = "| ** ** |"
            c = "|*  *  *|"
            d = "| *   * |"
            e = "|   *   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Spades":
            a = ".-------."
            b = "|   *   |"
            c = "| *   * |"
            d = "|*     *|"
            e = "|  *I*  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g

    def create_decks(self):
        deck = []
        for dks in range(6):
            for su in self.SUIT:
                for name, value in self.NAME_VALUE.items():
                    art = [a, b, c, d, e, f, g] = self.arts(su, str(value))
                    deck.append(Card(name, su, value, art))
        return deck


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name.capitalize()

    def hand_value(self):
        tot = 0
        ace = []
        for crd in self.hand:
            if crd.value == 11:
                ace.append('ace')
            else:
                tot += crd.value
        for a in ace:
            if tot + 11 > 21:
                tot += 1
            else:
                tot += 11
        return tot

    def __repr__(self):
        return self.name


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, "Dealer")

    def render_cards(self, hidden):
        hidden_card = hidden
        a = ''
        b = ''
        c = ''
        d = ''
        e = ''
        f = ''
        g = ''
        if hidden_card:
            a = ".-------." + self.hand[1].a
            b = "|*******|" + self.hand[1].b
            c = "|0000000|" + self.hand[1].c
            d = "|*******|" + self.hand[1].d
            e = "|0000000|" + self.hand[1].e
            f = "|*******|" + self.hand[1].f
            g = "'-------'" + self.hand[1].g
        else:
            for crd in self.hand:
                a += crd.a
                b += crd.b
                c += crd.c
                d += crd.d
                e += crd.e
                f += crd.f
                g += crd.g
        return [a, b, c, d, e, f, g]


def table(players, dealer, render):
    animation.cls()
    dlr = dealer.render_cards(render)
    spacer = '  |**|  '
    spst = '********'
    line = ''
    bar = ''
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    f = ''
    g = ''
    player_stats = ''
    player_name = ''
    pn_test = ''
    for plr in players:
        line += spst
        bar += spacer
        a += spacer
        b += spacer
        c += spacer
        d += spacer
        e += spacer
        f += spacer
        g += spacer

        # temp to test out score placement
        score = 0
        for sc in plr.hand:
            score += sc.value

        score_txt = 'Hand Value: ' + str(score)
        stats_spaces = ' ' * ((9 * len(plr.hand)) - len(score_txt))
        player_stats += spacer + score_txt + stats_spaces

        # player_spaces = ' ' * ((9 * len(plr.hand)) - len(plr.name))
        # player_name += spacer + plr.name + player_spaces
        pn_spacer = '*' * int(((9 * len(plr.hand)) - len(plr.name)) / 2)
        pn_middle = spacer + pn_spacer + plr.name + pn_spacer
        pn_middle_a = pn_middle[:]
        if len(pn_middle) < (len(plr.hand) * 9) + 8:
            while len(pn_middle_a) < (len(plr.hand) * 9) + 8:
                pn_middle_a += '*'
        player_name += pn_middle_a
        for car in plr.hand:
            line += "*" * 9
            bar += "*" * 9
            a += car.a
            b += car.b
            c += car.c
            d += car.d
            e += car.e
            f += car.f
            g += car.g
    line += spst
    bar += spacer
    a += spacer
    b += spacer
    c += spacer
    d += spacer
    e += spacer
    f += spacer
    g += spacer
    player_stats += spacer
    player_name += spacer
    solid_line = '  |' + line[3:-3] + '|  '
    # Half minus rendered cards
    hmrc = ((len(solid_line) - len(dlr[0])) / 2) - 4
    left_side = '  |' + '*' * (int(hmrc) - 2) + '  '
    right_side = '  ' + '*' * (int(hmrc)) + '|  '

    if len(left_side + dlr[0] + right_side) > len(solid_line):
        size_fix = len(left_side + dlr[0] + right_side) - len(solid_line)
        right_side = '  ' + '*' * ((int(hmrc) - 2) - size_fix) + '|  '

    print(solid_line)
    print(left_side + dlr[0] + right_side)
    print(left_side + dlr[1] + right_side)
    print(left_side + dlr[2] + right_side)
    print(left_side + dlr[3] + right_side)
    print(left_side + dlr[4] + right_side)
    print(left_side + dlr[5] + right_side)
    print(left_side + dlr[6] + right_side)
    print(solid_line)
    print(solid_line)
    print(solid_line)
    print(bar)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(player_stats)
    print(player_name)
    print('  ' + line[2:-2] + '  ')


def rounds(gm):
    for pl in gm.players:
        turn = True
        while turn:
            choice = input("{player}, would you like to (H)it or (S)tay?: ".format(player=pl.name)).lower()
            if choice == "hit" or choice == 'h':
                gm.hit(pl)
                table(gm.players, gm.dealer, True)
                if pl.hand_value() > 21:
                    turn = False
            elif choice == 'stay' or choice == 's':
                turn = False
                table(gm.players, gm.dealer, True)
            else:
                print("I did not understand that. Please try again.")
    table(gm.players, gm.dealer, False)

if __name__ == "__main__":
    game = BlackJack()
    game.first_deal()
    table(game.players, game.dealer, True)
    while True:
        rounds(game)

