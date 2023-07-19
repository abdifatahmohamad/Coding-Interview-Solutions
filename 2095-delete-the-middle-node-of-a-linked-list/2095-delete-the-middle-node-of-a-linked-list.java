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
        // Convert linked list to array
        List<Integer> list = linkedListToArray(head);
        // int mid = list.get(list.size() / 2);
        int n = list.size();
        int midIndex = n / 2;
        
        // Remove the middle element from the list
        list.remove(midIndex);
        // Convert the modified list back to a linked list
        return arrayToLinkedList(list);
    }
    
     // Helper method that converts linkedlist into an array
    private List<Integer> linkedListToArray(ListNode head) {
        List<Integer> list = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            list.add(curr.val);
            curr = curr.next;
        }
        return list;
    }
    
    // Helper method that converts an array to a linked list
    private ListNode arrayToLinkedList(List<Integer> list) {
        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;
        for (int num : list) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }
}