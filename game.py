class Card:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana
    
    def __str__(self):
        return self.name

class MinionCard(Card):
    def __init__(self, name, mana, attack, health, hasEffect = False, effect = None):
        super(MinionCard, self).__init__(name, mana)
        self.attack = attack
        self.health = health

        if (hasEffect == True):
            self.effect = effect
            self.hasEffect = True

    def __str__(self):
        try:
            return super(MinionCard, self).__str__() + '({}/{}/{})'.format(self.mana, self.attack, self.health) + ', Effect: ' + self.effect
        except:
            return super(MinionCard, self).__str__() + '({}/{}/{})'.format(self.mana, self.attack, self.health)

def MinionBattle(Minioncard obj1, Minioncard obj2):
    if obj1.attack >= obj2.health:
        obj2.health = 0
    if    
class SpellCard(Card):
    def __init__(self, name, mana, damage, hasEffect = False, effect = None):
        super(SpellCard, self).__init__(name, mana)
        self.damage = damage
        
        if (hasEffect == True): 
            self.effect = effect
            self.hasEffect = True

    def __str__(self):
        try:
            return super(SpellCard, self).__str__() + '({}/{})'.format(self.mana, self.damage) + ', Effect: ' + self.effect
        except:
            return super(SpellCard, self).__str__() + '({}/{})'.format(self.mana, self.damage)

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.board = []
        self.health = 30
        self.healtLossPerInvalidDraw = 0

    def draw(self):
        try:
            self.hand.append(self.deck.pop())
        except:
            self.healtLossPerInvalidDraw += 1
            self.health -= self.healtLossPerInvalidDraw
            print('Deck is empty, can\'t draw. You lose ' + str(self.healtLossPerInvalidDraw) + ' health.')
            print(self)

    def __str__(self):
        return self.name + ' has ' + str(self.health) + ' health left.'

    def printDeck(self):
        if (len(self.deck) == 0):
            print('Deck is empty.')
        for card in self.deck:
            print(card)
    
    def printHand(self):
        if (len(self.hand) == 0):
            print('Hand is empty.')
        for card in self.hand:
            print(card)
    

def main():
    minionCardObj = MinionCard('Ogre', 1, 2, 3, True, 'Taunt')
    spellCardObj = SpellCard('Fireball', 2, 4, True, 'Deal 4 damage')

    deck = []
    deck.append(minionCardObj)
    deck.append(spellCardObj)
        
    player1 = Player('John', deck)

    player1.printHand()
    print("~" * 20)
    player1.printDeck()
    print("\n")

    player1.draw()
    player1.printHand()
    print("~" * 20)
    player1.printDeck()
    print("\n")

    player1.draw()
    player1.printHand()
    print("~" * 20)
    player1.printDeck()
    print("\n")

    player1.draw()

    #print(player1)

if __name__ == '__main__':
    main()