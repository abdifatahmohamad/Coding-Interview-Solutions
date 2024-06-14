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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head; // Return the head as is if the list is empty or contains only one node
        }
        
        ListNode dummy = new ListNode(0); // Create a dummy node
        dummy.next = head; // Point dummy's next to the head of the list
        
        ListNode prev = dummy; // Pointer to track the previous unique node
        ListNode curr = head; // Pointer to traverse the linked list
        
        while (curr != null) {
            while (curr.next != null && curr.val == curr.next.val) {
                curr = curr.next; // Skip duplicate nodes
            }
            
            if (prev.next == curr) {
                prev = prev.next; // Move prev to the next unique node
            } else {
                prev.next = curr.next; // Remove duplicate nodes
            }
            
            curr = curr.next; // Move curr to the next node
        }
        
        return dummy.next; // Return the modified list without duplicates
        
    }
}