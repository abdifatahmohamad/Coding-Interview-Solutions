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
    public ListNode rotateRight(ListNode head, int k) {
        // Handle edge cases
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        
        // Convert linked list to array
        List<Integer> list = linkedListToArray(head);
        int n = list.size();
        int rotateCount = k % n;
        
        // If effective rotation count is zero, return the original list
        if(rotateCount == 0){
            return head;
        }
        
        // Rotate the array
        reverseArray(list, 0, n - 1); // Reverse the whole array
        reverseArray(list, 0, rotateCount - 1); // Reverse the first part
        reverseArray(list, rotateCount, n - 1); // Reverse the second part
        
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
    
    // Helper method that reverses array
    private void reverseArray(List<Integer> arr, int start, int end) {
        while (start < end) {
            int temp = arr.get(start);
            arr.set(start, arr.get(end));
            arr.set(end, temp);
            start++;
            end--;
        }
    }
    
    // Helper method that converts array back to linked list
    private ListNode arrayToLinkedList(List<Integer> list) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int num : list) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }
}