public class Solution
{
    public int PairSum(ListNode head)
    {
        // Find the mid-point
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode head2 = slow.next;
        slow.next = null; // Cut the pointer/connection after mid-point
        
        // Reverse from mid point
        ListNode prev = null;
        ListNode curr = head2;
        while (curr != null)
        {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        
        // Compute maximum twin sum 
        int res = int.MinValue;
        while(prev != null){
            res = Math.Max(res, head.val + prev.val);
            head = head.next;
            prev = prev.next;
        }
        
        return res;
    }
    

}
