#include <iostream>
 
using namespace std;
 
int main()
{
    int n; cin >> n;
 
    int sw = 0;
    int ws[n];
 
    int m1 = -1, m1i = -1;
    int m2 = -1;
 
    for(int i = 0; i < n; i++){
        int w, h; cin >> w >> h;
 
        ws[i] = w;
 
        sw += w;
 
        if(h >= m1){
            m2 = m1;
            m1 = h; m1i = i;
        }
 
        else if(h >= m2){
            m2 = h;
        }
    }
 
    for(int i = 0; i < n; i++){
        int w = sw - ws[i];
 
        if(i == m1i)
            cout << m2 * w << " ";
        else
            cout << m1 * w << " ";
    }
}