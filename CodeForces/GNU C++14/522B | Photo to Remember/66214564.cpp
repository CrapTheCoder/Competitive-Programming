#include <iostream>
 
using namespace std;
 
void integer_input(int &number)
{
    bool negative = false;
    register int c;
 
    number = 0;
 
    c = getchar();
 
    if (c=='-')
    {
        negative = true;
        c = getchar();
    }
 
    for (; (c > 47 && c < 58); c=getchar())
        number = number * 10 + c - 48;
 
    if (negative)
        number *= -1;
}
 
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
 
    int n; integer_input(n);
 
    int sw = 0;
    int ws[n];
 
    int m1 = -1, m1i = -1;
    int m2 = -1;
 
    for(int i = 0; i < n; i++){
        int h; integer_input(ws[i]); integer_input(h);
 
        sw += ws[i];
 
        if(h >= m1){
            m2 = m1;
            m1 = h; m1i = i;
        }
 
        else if(h >= m2)
            m2 = h;
    }
 
    for(int i = 0; i < n; i++){
        int w = sw - ws[i];
 
        if(i == m1i)
            cout << m2 * w << " ";
        else
            cout << m1 * w << " ";
    }
}