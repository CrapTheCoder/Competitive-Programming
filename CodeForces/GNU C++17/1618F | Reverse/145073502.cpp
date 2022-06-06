bits/stdc++.h>
<ext/pb_ds/assoc_container.hpp>
<ext/pb_ds/tree_policy.hpp>

namespace std;
namespace __gnu_pbds;

get_rand() {
long a = rand();
long b = rand();
a * (RAND_MAX + 1ll) + b;


int long long
ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
ordered_multiset tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update>
intmin -100000000000000000LL
intmax 100000000000000000LL

string itob(int n) {
== 0)
return "0";

string s;
(n) {
+= (n & 1) + '0';
>>= 1;


reverse(s.begin(), s.end());
s;


string s) {
= 0;
int i = 0, j = s.size() - 1; i < (int)s.size(); i++, j--)
(s[i] == '1')
n += 1LL << j;

return n;
}

set<int> visited;

int32_t main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);

int x, y;
cin >> x >> y;

string ans = "NO\n";
if(x == y){
cout << "YES\n";
return 0;
}

queue<string> q;
q.push(itob(x));

while(!q.empty()){
string s = q.front();
q.pop();

if(s.size() > 60)
break;

string a = s + '1';
reverse(a.begin(), a.end());

string b = s + '0';
reverse(b.begin(), b.end());

int num = btoi(b);
b = itob(num);

int aNum = btoi(a), bNum = btoi(b);
if(visited.find(aNum) == visited.end()){
visited.insert(aNum);
q.push(a);
}
if(visited.find(bNum) == visited.end()){
visited.insert(bNum);
q.push(b);
}

if(aNum == y || bNum == y){
ans = "YES\n";
break;
}
}

cout << ans;
}