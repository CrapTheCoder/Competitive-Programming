#include <iostream>

using namespace std;

typedef int in;
typedef long long int ll;

#define int ll

int gcd(int a, int b){
    int temp;

    while(a != 0){
        temp = a;
        a = b % a;
        b = temp;
    }

    return b;
}

in main()
{
    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int v, s = 0, g = -1;

        for(int i = 0; i < n; i++){
            cin >> v;

            if(g == -1)
                g = v;
            else
                g = gcd(g, v);

            s += v;
        }

        cout << g << " " << s / g << endl;
    }
}
