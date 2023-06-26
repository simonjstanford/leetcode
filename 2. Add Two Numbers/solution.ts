/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let node1 = l1;
    let node2 = l2;
    let answers: number[] = [];
    let carry = 0;
    let previous: ListNode | null = null;
    
    while (node1 !== null || node2 !== null) {
        let val1:number = node1 !== null ? node1.val : 0
        let val2:number = node2 !== null ? node2.val : 0
        let x: number = val1 + val2 + carry;
        
        if (x >= 10) {
            let temp = x % 10;
            carry = 1;
            x = temp;
        } else {
            carry = 0;
        }
        
        answers.push(x);     
        node1 = node1 !== null ? node1.next : null;
        node2 = node2 !== null ? node2.next : null;
    }
    
    if (carry > 0) {
        answers.push(carry);
    }
    
    let answer: ListNode | null = null;
    
    for (let i = answers.length -1; i >= 0; i--) {
        answer = new ListNode(answers[i], answer);
    }
    
    return answer;
};
