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
    public ListNode reverseList(ListNode head) {
        ListNode c = head;//c is current
        ListNode prev = null; // p is prev
        while(c!=null){
            ListNode next = c.next;
            c.next = prev;
            prev = c;
            c = next;
        }
        return prev;  
    }
}