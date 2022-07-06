import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'back'

def main():
    money = 5000
    while True:
        if money <= 0:
            print('You are broke')
            sys.exit()
        print('Budget: ', money)
        bet = getBet(money)

        deck = getDeck()    # tylko raz jest pobierana przetasowana talia kart
        dealerHand = [deck.pop(), deck.pop()]   # pop() pobiera z tablicy (tali kart) ostatni element
        playerHand = [deck.pop(), deck.pop()]   # i kasuje go z tablicy (tali kart)

        print('Bet: ', bet)

        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'P':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet: ', bet)

            if move in ('D', 'P'):
                newCard = deck.pop()
                rank, suite = newCard
                print('You get {} {}.'.format(rank, suite))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ('S', 'P'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('the dealer draws a card...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                print(getHandValue(playerHand))
                print(playerHand)
                input('Please press any key to continue...')
                print('\n\n')

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('Dealer have more than 21. You are won {}: '.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You have lost')
            money -= bet
        elif playerValue > dealerValue:
            print('You are won {} '.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("There is tie")

        input('Press any key')
        print('\n\n')



def getBet(maxBet):
    while True:
        print('for how much do you want to play? (1-{} or q-Exit)'.format(maxBet))
        bet = input('> ').lower().strip()
        if bet == 'q':
            print('Thanks for You game')
            sys.exit()
        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('KRUPIER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('KRUPIER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ____  '
        if card == BACKSIDE:
            rows[1] += '|##  | '
            rows[2] += '|### | '
            rows[3] += '|__##| '
        else:
            rank, suit = card
            rows[1] += '|{}  | '.format(rank.ljust(2))
            rows[2] += '| {}  | '.format(suit)
            rows[3] += '|__{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(P)ick', '(S)top']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('P', 'S'):
            return move
        if move == 'P' and '(D)ouble' in moves:
            return move



if __name__ == '__main__':
    main()
