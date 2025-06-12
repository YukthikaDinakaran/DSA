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
    public ListNode reverseKGroup(ListNode head, int k) {
        if( head == null || k==1){
            return head;
        }
        ListNode temp = head;
        ListNode prev = null;
        while(temp != null){
            ListNode kgroup = kthnode(temp, k);
            if( kgroup == null){
                if(prev != null){
                    prev.next = temp;
                }
                break;
            }
            ListNode next = kgroup.next;
            kgroup.next = null;
            reverselist(temp);
            if( temp == head){
                head = kgroup;
            }
            else{
                prev.next = kgroup;
            }
            prev = temp;
            temp = next;
        }
        return head;
    }
        static ListNode kthnode( ListNode temp , int k){
            k = k - 1;
            while(temp != null && k>0){
                k-- ;
                temp = temp.next;
            }
            return temp;
        }
        static ListNode reverselist(ListNode head){
            ListNode temp = head;
            ListNode prev = null;
            while( temp != null){
                ListNode front = temp.next;
                temp.next = prev;
                prev = temp;
                temp = front;
            }
            return prev;
        }
    
    }
