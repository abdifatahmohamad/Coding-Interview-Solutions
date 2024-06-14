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
        if (head == null || head.next == null) {
            return null; // No middle node to delete
        }

        ListNode middle = findMiddleNode(head);

        // If the middle node is the head, update the head to the next node
        if (head == middle) {
            head = head.next;
            return head;
        }

        // Find the node before the middle node
        ListNode prev = head;
        while (prev.next != middle) {
            prev = prev.next;
        }

        // Remove the middle node by adjusting the previous pointer
        prev.next = middle.next;

        return head; // Return the modified head of the linked list
        
    }
    
    // Method to find the middle node of the linked list
    private ListNode findMiddleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}