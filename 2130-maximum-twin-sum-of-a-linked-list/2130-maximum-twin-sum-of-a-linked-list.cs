/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int PairSum(ListNode head) {
        int[] array = LinkedListToArray(head);
        return FindMaxSum(array);
    }
    
    
    // Method that converts LL into an array
    private int[] LinkedListToArray(ListNode head)
    {
        List<int> array = new List<int>();
        ListNode curr = head;
        while (curr != null)
        {
            array.Add(curr.val);
            curr = curr.next;
        }

        return array.ToArray();
    }

    // Method that finds max sum using two pointers
    private int FindMaxSum(int[] nums)
    {
        int i = 0;
        int j = nums.Length - 1;
        int maxSum = int.MinValue;
        while (i < j)
        {
            int currentSum = nums[i] + nums[j];
            maxSum = Math.Max(maxSum, currentSum);
            i++;
            j--;
        }

        return maxSum;
    }
}
