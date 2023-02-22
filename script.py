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
     
    def action(self,j):
        self.hand = []
        self.count = 0
        
        self.drawn = self.clear_list()

        print("Player", str(int(j)+1) ,":")
        self.hand = self.drawn_cards()
        print(symbols[self.hand[0]])

        while input("Hit or pass ? (Write hit or pass\n)") != "pass":
            
            self.hand = self.drawn_cards()

            for i in self.hand:

                if self.count <= 21:

                    own = symbols[i]
                    print(own +"\t")
                    self.count = self.check_numbers(self.hand)

                elif self.count > 21:

                    print("Player", str(int(j)+1),"lost.")

                    return self.hand,self.count
            
        
        return self.hand,self.count
    
    def clear_list(self):

        if len(self.drawn) > 0:
            for i in range(len(self.drawn)):
                self.drawn.pop()

        return self.drawn


    def dealer(self):
        self.deal = []
        self.amount = 0
        self.deal = self.drawn_cards()
        print(symbols[self.deal[0]])
        while self.amount <= 21:
            for i in self.deal:

                self.deal = self.drawn_cards()

                face = symbols[i]
                print(face)
                self.amount = self.check_numbers(self.deal)
                if self.amount <= 21 and self.amount >=18: 
                    
                    return self.deal, self.amount
                elif self.amount > 21:

                    return "The Dealer lost!" 

        


symbols = {"A":"""
                *********
                * A     *
                *       *
                *   A   *
                *       *
                *      A*
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
                *    QQ *
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
for i in range(int(player_num)):
    Cards = cards()
    player ={i:Cards.action(i)}
    print(player)

dealer = Cards.dealer()
print(dealer)