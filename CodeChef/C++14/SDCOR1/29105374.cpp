#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long t=1;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int p;
        vector<int> edge[n+1];
        int depth[n+1]={-1};
        vector<int> oe[n+1];
        queue<int> q;
         for(int i=1;i<n;i++)
    {
        int x,y;
        cin>>x>>y;
        edge[y].push_back(x);
        oe[x].push_back(x);
    }
    int root=-1;
    for(int i=1;i<n+1;i++)
    {
        if(oe[i].size()==0)
            root=i;
    }
    q.push(root);
    depth[root]=0;

        while(q.empty()==false)
        {
            int n1=q.front();q.pop();
            for(auto i=edge[n1].begin();i!=edge[n1].end();i++)
            {
                depth[*i]=depth[n1]+1;
                q.push(*i);
            }
        }
        int ans=0;
        for(int i=0;i<n+1;i++)
            if(depth[i]>ans)
                ans=depth[i];
        cout<<ans<<'\n';
    }
    return 0;
}
