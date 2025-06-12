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
    public ListNode mergeKLists(ListNode[] lists) {
        if( lists == null || lists.length == 0){
            return null;
        }
        while(lists.length > 1){
            List<ListNode> temp = new ArrayList<>();
            for ( int i=0; i< lists.length; i= i+2){
                ListNode l1 = lists[i];
                ListNode l2;
                if( i+1 < lists.length){
                    l2 = lists[i+1];
                }
                else{
                    l2 = null;
                }
                ListNode merging = mergelist( l1, l2);
                temp.add(merging);
            }
            lists = new ListNode[temp.size()];
            for (int i = 0; i < temp.size(); i++) {
                lists[i] = temp.get(i);
            }
            
        }
        return lists[0];
    }
    public ListNode mergelist(ListNode list1, ListNode list2) {
        if(list1==null){
            return list2;
        }
        if(list2==null){
            return list1;
        }
        ListNode d = new ListNode();
        ListNode c = d;
        while(list1 !=null && list2 != null){
            if(list1.val <= list2.val){
                c.next = list1;
                list1= list1.next;
                
            }
            else{
                c.next = list2;
                list2 = list2.next;
                
            }
            c = c.next;
        }
       if( list1!= null){
        c.next = list1;
       }
       if( list2!= null){
        c.next = list2;
       }
    return d.next;
   }
}