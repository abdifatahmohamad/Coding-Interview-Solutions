public class Solution
{
    public int PairSum(ListNode head)
    {
        ListNode head1 = head;
        ListNode head2 = ReverseLinkedList(head);
        int res = int.MinValue;
        
        while(head1 != null){
            int currentSum = head1.val + head2.val;
            res = Math.Max(res, currentSum);
            head1 = head1.next;
            head2 = head2.next;
            
        }

        return res;
    }

    // Reverse LinkedList
    private ListNode ReverseLinkedList(ListNode head)
    {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null)
        {
            ListNode temp = new ListNode(curr.val);
            temp.next = prev;
            prev = temp;
            curr = curr.next;
        }

        return prev;
    }
}
