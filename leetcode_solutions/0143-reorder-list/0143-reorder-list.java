/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
       if (head == null || head.next == null) {
            return; // Empty list or single node, no need to reorder
        }
        
        // Find the middle node of the list
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next; // Move slow pointer by one node
            fast = fast.next.next; // Move fast pointer by two nodes
        }
        
        // Reverse the second half of the list
        ListNode prev = null; 
        ListNode curr = slow.next; 
        while (curr != null) {
            ListNode next = curr.next; // Store the next node
            curr.next = prev; // Reverse the link
            prev = curr; // Update the previous node
            curr = next; // Move to the next node
        }
        slow.next = null; // Break the original list into two halves
        
        // Merge the two halves alternatively
        ListNode first = head; // Pointer to the first half
        ListNode second = prev; // Pointer to the reversed second half
        while (second != null) {
            ListNode nextFirst = first.next; // Store the next node in the first half
            ListNode nextSecond = second.next; // Store the next node in the second half
            // Link the current node in the first half to the current node in the second half
            first.next = second; 
            // Link the current node in the second half to the next node in the first half
            second.next = nextFirst; 
            first = nextFirst; // Move the first pointer to the next node in the first half
            second = nextSecond; // Move the second pointer to the next node in the second half
        }
    }
}
