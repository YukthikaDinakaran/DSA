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
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null && fast.next.next != null){
            fast= fast.next.next;
            slow = slow.next;
        }
        ListNode half = slow.next;
        ListNode newhead = reversell(slow.next);
        ListNode front = head;
        while( newhead != null){
            if(front.val!= newhead.val){
                reversell(newhead);
                return false;
                
            }
            newhead = newhead.next;
            front = front.next;
        }
        reversell(newhead);
        return true;
        
        
    }
    public ListNode reversell(ListNode head){
        if( head== null || head.next == null){
            return head;
        }
        ListNode prev = null;
        while(head != null){
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }
}