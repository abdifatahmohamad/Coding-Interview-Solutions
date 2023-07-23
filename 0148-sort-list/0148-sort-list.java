class Solution {
    public ListNode sortList(ListNode head) {
        // Base case: if head is null or head is the only one node
        if (head == null || head.next == null) {
            return head;
        }
        
        // Call get mid
        ListNode middle = getMid(head);
        ListNode leftList = head;
        ListNode rightList = middle.next;
        middle.next = null; // Split the linked list into two halves
        
        // Recursively sort both halves
        leftList = sortList(leftList);
        rightList = sortList(rightList);
        
        // Merge both leftList and rightList portions
        return merge(leftList, rightList);
    }
    
    // Helper method that gets the middle of the linked list
    private ListNode getMid(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }
    
    private ListNode merge(ListNode list1, ListNode list2) {
        // Create a dummy node with value -1
        ListNode dummy = new ListNode(-1);
        // Create a tail variable that is gonna be the position we insert
        // the merged node at
        ListNode tail = dummy;
        
        while (list1 != null && list2 != null) {
            // Find the smaller value
            if (list1.val < list2.val) {
                tail.next = list1;
                // Shift list1
                list1 = list1.next;
            } else {
                tail.next = list2;
                // Shift list2
                list2 = list2.next;
            }
            
            // Shift tail pointer
            tail = tail.next;
        }
        
        // Handle leftover nodes in list1 and list2
        if (list1 != null) {
            tail.next = list1;
        }
        
        if (list2 != null) {
            tail.next = list2;
        }
        
        return dummy.next;
    }
}
