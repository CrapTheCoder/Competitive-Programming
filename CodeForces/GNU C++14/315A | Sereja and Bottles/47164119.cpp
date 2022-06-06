#include <iostream>
 
using namespace std;
 
int add_digit(int n, int i){
    return n * 10 + i;
}
 
int main()
{
    int n; cin >> n;
    int e[n], v[n];
 
    int x = 0;
 
    for(int l = 0; l < n; l++)
        cin >> e[l] >> v[l];
 
    for(int i = 0; i < n; i++){
        int c = 0;
 
        for(int j = 0; j < n; j++){
            if(i != j){
                if(e[i] == v[j])
                    break;
            }
 
            c++;
        }
 
        if(c == n)
            x++;
    }
 
    cout << x << endl;
}