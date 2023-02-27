class MyQueue {
public:
    int top;
    vector<int>a;
    MyQueue() {
        top=-1;
    }
    
    void push(int x) {
        top++;
        a.push_back(x);
    }

    int pop() {
            int t=a[0];
            top--;
            for (int i = 0; i <=top; i++)
                a[i]=a[i+1];
            a.erase(a.begin()+top+1);
            return t;
    }
    
    int peek() {
        return a[0];
    }
    
    bool empty() {
        if (top==-1)
            return true;
        else
            return false;
    }
};
