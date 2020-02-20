#include<iostream>
#include<vector>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* creat_link_list(vector<int> &v) {
    ListNode preHead(0), *pre=&preHead;
    for(int i=0; i<v.size(); i++) {
        ListNode *cur = new ListNode(v[i]);
        pre->next = cur;
        pre = pre->next;
    }
    return preHead.next;
}

void print_link_list(ListNode* head) {
    while(head) {
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}

ListNode* reverse_link_list_for_mid(ListNode* head) {
    // 1->2->3->4->5  ->   1->2->3<-4<-5
    ListNode *low=head, *fast=head;
    // 快慢指针找中间位置
    while(fast && fast->next) {
        fast = fast->next->next;
        low = low->next;
    }
    ListNode *cur = low->next;
    low->next = nullptr;
    while(cur) {
        ListNode* nxt = cur->next;
        cur->next = low;
        low = cur;
        cur = nxt;
    }
    return low; //最后一个节点
}

void reorderList(ListNode* head, ListNode* tail) {
    //1->2->3->4->5, 重新排列为 1->5->2->4->3.
    ListNode *cur = head;
    while(cur != tail && tail != cur->next) {
        ListNode* tmp1 = cur->next;
        ListNode* tmp2 = tail->next;
        cur->next = tail;
        tail->next = tmp1;
        cur = tmp1;
        tail = tmp2;
    }
}

int main() {
    vector<int> v{1,2,3,4};
    ListNode* head = creat_link_list(v);
    print_link_list(head);
    ListNode* tail = reverse_link_list_for_mid(head);
    print_link_list(head);
    print_link_list(tail);
    reorderList(head, tail);
    print_link_list(head);
    

}
