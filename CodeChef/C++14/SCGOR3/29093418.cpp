#include<bits/stdc++.h>
using namespace std;
#define o string
int t(o a,o b,o &e){int f=INT_MIN;int c=a.length();int d=b.length();for(int i=1;i<=min(c,d);i++){if(!a.compare(c-i,i,b,0,i)){if(f<i){f=i;e=a+b.substr(i);}}}for(int i=1;i<=min(c,d);i++){if(!a.compare(0,i,b,d-i,i)){if(f<i){f=i;e=b+a.substr(i);}}}return f;}

o p(o a[], int len)
{
    while(len != 1)
    {
        int m = INT_MIN;
        int l, r;

        o h;

        for(int i = 0; i < len; i++)
        {
            for(int j = i + 1; j < len; j++)
            {
                o g;

                int s = t(a[i], a[j], g);

                if (m < s)
                {
                    m = s;
                    h=g;
                    l=i,r=j;
                }
            }
        }

        len--;

        if (m == INT_MIN)
            a[0] += a[len];
        else
        {
            a[l] = h;
            a[r] = a[len];
        }
    }
    return a[0];
}

int main()
{
    int n; cin >> n;

    o a[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    cout << p(a, n) << endl;
}
