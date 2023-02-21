import random
card = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"K":10,"J":10,"Q":10,"A":[1,11]}
face = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
class cards:

    drawn = []

    def display(self):
        pass


    def drawn_cards(self):
        num = random.randint(0,12)

        self.drawn.append(face[num])

        return self.drawn
    def check_numbers(self,hand):

        self.sum = 0
        for i in hand:
            if i == "A" and self.sum <= 10:
                self.sum += 11
            
            elif i =="A" and self.sum > 10:
                self.sum += 1
            else: 
                self.sum += card[i]

        return self.sum
     



    
        


symbols = {"A":"""
                *********
                * A     *
                *       *
                *   A   *
                *       *
                *     A *
                *********
            """,
            "2":"""
                *********
                *   2   *
                *       *
                *       *
                *       *
                *   2   *
                *********
            """,
            "3":"""
                *********
                *   3   *
                *       *
                *   3   *
                *       *
                *   3   *
                *********
            """,
            "4":"""
                *********
                * 4   4 *
                *       *
                *       *
                *       *
                * 4   4 *
                *********
            """,
            "5":"""
                *********
                * 5   5 *
                *       *
                *   5   *
                *       *
                * 5   5 *
                *********
            """,
            "6":"""
                *********
                * 6   6 *
                *       *
                * 6   6 *
                *       *
                * 6   6 *
                *********
            """,
            "7":"""
                *********
                * 7   7 *
                *   7   *
                * 7   7 *
                *       *
                * 7   7 *
                *********
            """,
            "8":"""
                *********
                * 8   8 *
                *   8   *
                * 8   8 *
                *   8   *
                * 8   8 *
                *********
            """,
            "9":"""
                *********
                * 9 9 9 *
                *       *
                * 9 9 9 *
                *       *
                * 9 9 9 *
                *********
            """,
            "10":"""
                *********
                * 1  0  *
                * 1 0 0 *
                * 1 0 0 *
                * 1 0 0 *
                * 1  0  *
                *********
            """,
            "J":"""
                *********
                * JJJJJ *
                *     J *
                *     J *
                *     J *
                * JJJJ  *
                *********
            """,
            "Q":"""
                *********
                *  QQQ  *
                * Q   Q *
                * Q   Q *
                *  QQQ  *
                *     QQ *
                *********
            """,
            "K":"""
                *********
                *  K  K *
                *  K K  *
                *  KK   *
                *  K K  *
                *  K  K *
                *********
            """
            }

def action(i):
    hand = []

    print("Player", str(int(i)+1) ,":")

    hand = Cards.drawn_cards()

    print(hand)
    
    sum = 0

    while input("Hit or pass ? (Write hit or pass\n)") != "pass" and sum <= 21:
        hand = Cards.drawn_cards()
        for i in hand:
            own = symbols[i]
            print(own +"\t")
        sum = Cards.check_numbers(hand)
    return hand,sum







print("""
    ****    *         *       ***   *   *   *****     *       ***   *   *
    *   *   *        * *     *      *  *        *    * *     *      *  *
    *   *   *       *   *   *       * *         *   *   *   *       * *
    ****    *       *   *   *       **          *   *   *   *       **
    *   *   *       *****   *       * *         *   *****   *       * *
    *   *   *       *   *    *      *  *       *    *   *    *      *  *
    *****   *****   *   *     ***   *   *   ***     *   *     ***   *   *

    --------------------------------------------------------------------------
    """)

#Wie viele Spieler ?
#Hit oder aufhören
#karten ausgeben (als Karte)
#wenn Karte 4 mal gezogen aus stapel löschen

#Klasse für Darstellung, Gezogene Karten (Spieler + Dealer)

player_num = input("How many players are playing against the dealer ?\n")
print("There will be " + str(player_num) + " players.")
print("________________________________________________")
Cards = cards()
for i in range(player_num):
    print(range(len(player_num)))
    player ={i:action(i)}
    print(player)