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
    public ListNode deleteMiddle(ListNode head) {
        // Check if head is null or has no next node
        if (head == null || head.next == null) {
            return null; // No middle node to delete
        }

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        // Move the pointers until the fast pointer reaches the end of the list
        while (fast != null && fast.next != null) {
            fast = fast.next.next; // Move fast pointer by two nodes
            prev = slow; // Update previous pointer to be one step behind slow pointer
            slow = slow.next; // Move slow pointer by one node
        }

        // Remove the middle node by adjusting the previous pointer
        if (prev != null) {
            prev.next = slow.next;
        } else {
            head = slow.next; // Update head if the middle node is the head
        }

        return head; // Return the modified head of the linked list
    }
}