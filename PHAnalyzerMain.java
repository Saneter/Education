package PokerHandAnalyzer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;


public class PHAnalyzerMain
{
    public class Card
    {
        private int value;
        private int suit;
        
        public Card(int value, int suit)
        {
            this.value = value;
            this.suit = suit;
        }
        
        public int getCardValue()
        {
            return value;
        }
        
        public int getCardSuit()
        {
            return suit;
        }
        
        public String getCard()
        {
            String value = Integer.toString(getCardValue());
            String suit = Integer.toString(getCardSuit());
            
            String card = value + suit;
            
            return card;
        }
    }
    
    public class Player
    {
        
        private ArrayList<Card> hand = new ArrayList<Card>();
        private Map<Integer, Integer> freqMapValue = new HashMap<>();
        private Map<Integer, Integer> freqMapSuit = new HashMap<>();
        
        public Player()
        {
            for(int i = 1; i < 14; ++i)
            {
                freqMapValue.put(i, 0);
            }
            
            for(int i = 1; i < 5; ++i)
            {
                freqMapSuit.put(i, 0);
            }
        }
        
        public void addCard(Card card)
        {
            hand.add(card);
        }
        public void calculateFrequency()
        {
            // use (p1 or p2.)freqMapTYPE.entry.getKey()
            // use (p1 or p2.)freqMapTYPE.entry.getValue()
            
            for(int i = 0;i<5;++i)
            {   
                Integer count = freqMapValue.get(hand.get(i).getCardValue());
                freqMapValue.put(hand.get(i).getCardValue(), count + 1);
            }
            for(int i = 0;i<5;++i)
            {   
                Integer count = freqMapSuit.get(hand.get(i).getCardSuit());
                freqMapSuit.put(hand.get(i).getCardSuit(), count + 1);
            }
        }
        public int determineHand()
        {   
            if(isRoyalFlush() != 0)
                return isRoyalFlush();
            else if(isStraightFlush() !=0)
                return isStraightFlush();
            else if(isFourOfaKind() != 0)
                return isFourOfaKind();
            else if(isFullHouse() != 0)
                return isFullHouse();
            else if(isFlush() != 0)
                return isFlush();
            else if(isStraight() != 0)
                return isStraight();
            else if(isThreeOfaKind() != 0)
                return isThreeOfaKind();
            else if(isTwoPair() !=0)
                return isTwoPair();
            else if(isPair() != 0)
                return isPair();
            return 0;
        }
        
        public int isHighCard()
        {
            int temp = 0;
            int count = 0;

            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 4)
                {
                    temp = entry.getKey();
                    return temp;
                }
                
                if(entry.getValue() == 3)
                {
                    temp = entry.getKey();
                    return temp;
                }
                
                if(entry.getValue() == 2)
                    ++count;
                
                if(count == 2)
                {
                    if(entry.getKey() > temp)
                    {
                        temp = entry.getKey();
                        return temp;
                    }
                }
                else if(count == 1)
                {
                    temp = entry.getKey();
                        return temp;
                }
            }
            return temp;
        }
        
        public int isHighSingleCard()
        {
            int temp = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
            if(entry.getValue() == 1)
                if(entry.getKey() > temp)
                    temp = entry.getKey();
            }
            return temp;
        }
        
        public int isPair()
        {
            int twoOfcount = 0;
            int threeOfcount = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 2)
                {
                    ++twoOfcount;
                }
                if(entry.getValue() == 3)
                {
                    ++threeOfcount;
                }
            }
            
            if(twoOfcount == 1 && threeOfcount == 0)
            {
                return 15;
            }
            else
                return 0;     
        }
        
        public int isTwoPair()
        {
            int twoPaircount = 0;

            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 2)
                {
                    ++twoPaircount;
                }
            }
            
            if(twoPaircount == 2)
            {
                return 20;
            }
            else
                return 0; 
        }
        
        public int isThreeOfaKind()
        {
            int threeOfcount = 0;
            int twoOfcount = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 3)
                {
                    ++threeOfcount;
                }
                if(entry.getValue() == 2)
                {
                    ++twoOfcount;
                }
            }
            
            if(threeOfcount == 1 && twoOfcount == 0)
            {
                return 25;
            }
            else
                return 0;   
        }
        
        public int isStraight()
        {
            int i = 0;
            int [] temp = new int[5];
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() != 0)
                {
                    temp[i] = entry.getKey();
                    ++i;
                }
            }
            Arrays.sort(temp);
            
            
            for(int j =0; j < 4; ++j)
            {
                if(temp[j] + 1 != temp[j+1])
                    return 0;
            }
            if(isFlush() != 0)
                return 0;
            else
                return 30;
        }
        
        public int isFlush()
        {
            int fiveOfcount = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapSuit.entrySet())
            {
                if(entry.getValue() == 5)
                {
                    ++fiveOfcount;
                }
            }
            
            if(fiveOfcount == 1)
            {
                return 35;
            }
            else
                return 0;   
        }
        
        public int isFullHouse()
        {
            int threeOfcount = 0;
            int twoOfcount = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 3)
                {
                    ++threeOfcount;
                }
                if(entry.getValue() == 2)
                {
                    ++twoOfcount;
                }
            }
            
            if(threeOfcount == 1 && twoOfcount == 1)
            {
                return 40;
            }
            else
                return 0; 
        }
        
        public int isFourOfaKind()
        {
            int count = 0;
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() == 4)
                {
                    ++count;
                }
            }
            
            if(count == 1)
            {
                return 45;
            }
            else
                return 0; 
        }
        
        public int isStraightFlush()
        {
            int i = 0;
            int sum = 0;
            int [] temp = new int[5];
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() != 0)
                {
                    temp[i] = entry.getKey();
                    ++i;
                }
            }
            Arrays.sort(temp);
            
            for(int n =0; n < 5; ++n)
            {
                sum += temp[n];
            }
            
            for(int j =0; j < 4; ++j)
            {
                if(temp[j] + 1 != temp[j+1])
                    return 0;
            }
            if(isFlush() != 0 && sum < 55)
                return 50;
            else
                return 0; 
        }
        
        public int isRoyalFlush()
        {
            int i = 0;
            int sum = 0;
            int [] temp = new int[5];
            for(Map.Entry<Integer, Integer> entry : freqMapValue.entrySet())
            {
                if(entry.getValue() != 0)
                {
                    temp[i] = entry.getKey();
                    ++i;
                }
            }
            Arrays.sort(temp);
            
            for(int n =0; n < 5; ++n)
            {
                sum += temp[n];
            }

            for(int j =0; j < 4; ++j)
            {
                if(temp[j] + 1 != temp[j+1])
                    return 0;
            }
            
            if(isFlush() != 0 && sum == 55)
                return 100;
            else
                return 0; 
        }
        
    }
    
    public static void main(String[] args)
    {
        PHAnalyzerMain outerClass = new PHAnalyzerMain();
        Path path = Paths.get("C:\\Users\\Travis\\Desktop\\poker.txt");
        InputStream input = null;
        String hands = null;
        int player1Count = 0;
        int player2Count = 0;
        int tie = 0;
        int gamesPlayed = 0;
        try
        {
            input = Files.newInputStream(path);
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            
            while((hands = reader.readLine()) != null)
            {
               String[] temp = hands.split(" ");


                Player p1 = outerClass.new Player();
                for(int i=0; i<5; ++i)
                {
                    int value = getValue(temp[i].charAt(0));
                    int suit = getSuit(temp[i].charAt(1));
                    Card card1 = outerClass.new Card(value,suit);
                    p1.addCard(card1);
                }
                p1.calculateFrequency();
                Player p2 = outerClass.new Player();
                for(int i=5; i<10; ++i)
                {
                    int value = getValue(temp[i].charAt(0));
                    int suit = getSuit(temp[i].charAt(1));   
                    Card card2 = outerClass.new Card(value,suit);
                    p2.addCard(card2);
                }
                p2.calculateFrequency();
                //Compare Value of p1 to p2 here. Add to player count.
                ++gamesPlayed;
                if(p1.determineHand() > p2.determineHand())
                {
                    ++player1Count;
                }
                    
                else if(p1.determineHand() < p2.determineHand())
                {
                    ++player2Count;
                }

                else if(p1.determineHand() == p2.determineHand())
                {
                    if(p1.isHighCard() > p2.isHighCard())
                    {
                        ++player1Count;
                    }
                    else if(p1.isHighCard() < p2.isHighCard())
                    {
                        ++player2Count;
                    }
                    else if(p1.isHighCard() == p2.isHighCard())
                    {
                        if(p1.isHighSingleCard() > p2.isHighSingleCard())
                        {
                            ++player1Count;
                        }
                        else if(p1.isHighSingleCard() < p2.isHighSingleCard())
                        {
                            ++player2Count;
                        }
                        else
                        {    
                            System.out.println(gamesPlayed);
                            ++tie;
                        }
                    }
                        
                }
                
            }
        }
        catch(IOException e)
        {
            System.out.println(e);
        }
        
        System.out.println(" Player 1 won: " + player1Count + " games.");
        System.out.println(" Player 2 won: " + player2Count + " games.");
        System.out.println(" Players tied: " + tie + " games.");
    }
    
    public static int getValue(char cv)
    {
        int value = 0;
        switch(cv)
        {
        case'2':
            value = 1;
            break;
        case'3':
            value = 2;
            break;
        case'4':
            value = 3;
            break;
        case'5':
            value = 4;
            break;
        case'6':
            value = 5;
            break;
        case'7':
            value = 6;
            break;
        case'8':
            value = 7;
            break;
        case'9':
            value = 8;
            break;
        case'T':
            value = 9;
            break;
        case'J':
            value = 10;
            break;
        case'Q':
            value = 11;
            break;
        case'K':
            value = 12;
            break;
        case'A':
            value = 13;
            break;
        }
        
        return value;
    }
    
    public static int getSuit(char cs)
    {
        int cardSuit = 0;
        switch(cs)
        {
        case'H':
            cardSuit = 1;
            break;
        case'D':
            cardSuit = 2;
            break;
        case'C':
            cardSuit = 3;
            break;
        case'S':
            cardSuit = 4;
            break;
        }
        
        return cardSuit;
    }
}
