// https://csacademy.com/submission/370681/
#include <bits/stdc++.h>
using namespace std;

int n;

char kol[1000007];
int tab[1000007];

int k;

int p1, p2;
vector <int> graf[1000007];

long long inf=(long long)1000000000*1000000000;
long long wyn=inf;

int parz[1000007];
int jest[2];

long long aktu;

int licz[1000007];

int mabyc[1000007];

void dfs1(int v, int oj)
{
    jest[parz[v]]++;
    licz[v]=tab[v];
    for (int i=0; i<graf[v].size(); i++)
    {
        if (graf[v][i]==oj)
            continue;
        parz[graf[v][i]]=(parz[v]^1);
        dfs1(graf[v][i], v);
        licz[v]+=licz[graf[v][i]];
    }
}

void dfs2(int v, int oj)
{
    for (int i=0; i<graf[v].size(); i++)
    {
        if (graf[v][i]==oj)
            continue;
        dfs2(graf[v][i], v);
        mabyc[v]+=mabyc[graf[v][i]];
    }
    aktu+=abs(mabyc[v]-licz[v]);
}

int main()
{
    int tcs; cin >> tcs;
    
    while(tcs--) {
        scanf("%d", &n);
        for (int i=1; i<n; i++)
        {
            scanf("%d%d", &p1, &p2);
            graf[p1].push_back(p2);
            graf[p2].push_back(p1);
        }
        scanf("%s", kol+1);
        for (int i=1; i<=n; i++)
        {
            tab[i]=kol[i] - '0';
            k+=tab[i];
        }
        dfs1(1, 0);
        for (int h=0; h<2; h++)
        {
            if (jest[h]==k)
            {
                for (int i=1; i<=n; i++)
                {
                    mabyc[i]=(parz[i]==h);
                }
                aktu=0;
                dfs2(1, 0);
                wyn=min(wyn, aktu);
            }
        }
        if (wyn<inf)
            printf("%lld\n", wyn);
        else
            printf("-1\n");

        memset(kol, (sizeof kol[0]) * n, 0);
        memset(tab, (sizeof tab[0]) * n, 0);
        
        k = 0;
        p1 = p2 = 0;
        
        for (int i = 0; i < n + 1; i++)
            graf[i].clear();
        
        inf=(long long)1000000000*1000000000;
        wyn=inf;
        
        memset(parz, (sizeof parz[0]) * n, 0);
        jest[0] = jest[1] = 0;
        
        aktu = 0;
        
        memset(licz, (sizeof licz[0]) * n, 0);
        memset(mabyc, (sizeof mabyc[0]) * n, 0);
    }
}