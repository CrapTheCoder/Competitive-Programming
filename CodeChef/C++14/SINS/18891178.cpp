#include <bits/stdc++.h>
#include <algorithm>
 
using namespace std;
 
#define gc getchar_unlocked
 
typedef unsigned long long ull;
 
void scanint(int &x);
void scanlong(ull &x);
ull greatestCDivisor(ull first, ull second);
 
int main()
{
    int noOfTestCase;
    scanint(noOfTestCase);
    for(int i=0; i<noOfTestCase; ++i)
    {
        ull a,b;
        scanlong(a);
        scanlong(b);
        if(a == 0 || b == 0)
        {
            if(a == 0)
                printf("%llu\n",b);
            else
                printf("%llu\n",a);
        }
        else printf("%llu\n",2*greatestCDivisor(a,b));
    } 
    return 0;
}
 
 
ull greatestCDivisor(ull first, ull second)
{
    if(second==0)return first;
    else
    return greatestCDivisor(second,first%second);
}
 
void scanint(int &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
 
void scanlong(ull &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}