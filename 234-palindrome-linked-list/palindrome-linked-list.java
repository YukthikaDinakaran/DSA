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
        while(fast!=null && fast.next!= null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode prev = null;
        ListNode cur = slow;
        while(cur!= null){
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        ListNode fh = head;
        ListNode sh = prev;
        while(sh!= null){
            if(fh.val!= sh.val){
                return false;
            }
            fh = fh.next;
            sh = sh.next;
        }
        return true;        
    }
}