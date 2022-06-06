#include <bits/stdc++.h>
using namespace std;
 
typedef int integer;
typedef long long int ll;
 
#define int ll
 
int power(int n, int b){
    if(b == 0)
        return 1;
 
    int res = power(n, b / 2); res *= res;
 
    if(b & 1)
        res *= n;
 
    return res;
}
 
int sum_digits(int n){
    int res = 0;
 
    while(n > 0){
        res += n % 10;
        n /= 10;
    }
 
    return res;
}
 
integer main()
{
    int n; cin >> n;
 
    int m = 0;
 
    int c = 0;
 
    while(true){
        int x = 9 * power(10, c);
 
        if(m + x > n)
            break;
 
        m += x; c++;
    }
 
    cout << sum_digits(m) + sum_digits(n - m) << endl;
}