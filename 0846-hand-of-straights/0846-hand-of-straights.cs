public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {
        if (hand.Length % groupSize != 0)
            return false;

        // Step 1: Count the frequency of each card using a hashmap
        Dictionary<int, int> cardCount = new();
        foreach (int card in hand)
        {
            cardCount[card] = cardCount.GetValueOrDefault(card, 0) + 1;
        }

        // Step 2: Use a min heap to always get the smallest available card
        SortedSet<int> minHeap = new SortedSet<int>(cardCount.Keys);

        while (minHeap.Count > 0)
        {
            int firstCard = minHeap.Min;
            for (int i = 0; i < groupSize; i++)
            {
                int currentCard = firstCard + i;
                if (!cardCount.ContainsKey(currentCard) || cardCount[currentCard] == 0)
                    return false;

                cardCount[currentCard]--;
                if (cardCount[currentCard] == 0)
                {
                    if (minHeap.Contains(currentCard))
                        minHeap.Remove(currentCard);
                }
            }
        }

        return true;
    }
}