#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long double dl;
typedef long long int ll;
typedef unsigned long long int ull;

typedef set<int> sti;
typedef unordered_set<int> usti;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef unordered_map<int, int> umii;

#define int ll
#define double dl

#define endl '\n'
#define INF LLONG_MAX
#define INFN LLONG_MIN

#define MOD 1000000007

#define flush cout.flush();

#define speed ios::sync_with_stdio(false); cin.tie(NULL);

#define gcd(m, n) __gcd(m, n)
#define lcm(m, n) ((m * n) / gcd(m, n))

#define t_times int no_of_t; cin >> no_of_t; while(no_of_t--)
#define q_times int no_of_q; cin >> no_of_q; while(no_of_q--)

#define ain(a, n) for(int i = 0; i < n; i++) cin >> a[i];
#define aout(a, n) for(int i = 0; i < n; i++){cout << a[i] << " ";} cout << endl;

#define gin(a, n, m) for(int i = 0; i < n; i++){for(int j = 0; j < m; j++){cin >> a[i][j];}}
#define gout(a, n, m) for(int i = 0; i < n; i++){for(int j = 0; j < m; j++){cout << a[i][j] << " ";} cout << endl;}

#define pb push_back
#define ins insert

#define uset unordered_set
#define umap unordered_map

#define PI 3.1415926535

#define is_odd(n) ((n & 1) == 1)
#define is_even(n) ((n & 1) == 0)

#define fir first
#define sec second

void int_input(int &n){
char c;
int val = 0;

for(c = getchar(); c <= 32; c = getchar()) ;

bool neg = (c == '-');

if (c == '-' || c == '+')
c = getchar();

for (; c >= '0' && c <= '9'; c = getchar())
val = (val << 3) + (val << 1) + (c & 15);

n = (neg ? -val : val);
}

int sum(int a[], int n, int st = 0){
int s = 0;

for(int i = s; i < n; i++)
s += a[i];

return s;
}

bool is_prime_basic(int n){
if(n == 2) return true;
if(n <= 2 || is_even(n)) return false;

for(int i = 3; i <= sqrt(n); i += 2){
if(!(n % i))
return false;
}

return true;
}

int modulo(int n, int mod){
n %= mod;

if(n < 0)
n += mod;

return n;
}

int power(int x, int y, int mod=0){
if(mod != 0) x = modulo(x, mod);

int z = 1;

while(y > 0) {
if(is_odd(y)){
z *= x;

if(mod != 0) z = modulo(z, mod);
}

y /= 2; x *= x;

if(mod != 0) x = modulo(x, mod);
}

if(mod != 0) z = modulo(z, mod);

return z;
}

umap<char, int> Counter(string str){
umap<char, int> counter;

for(auto i: str)
counter[i]++;

return counter;
}

#define PMAX 1000005
bool prime[PMAX + 5];
int prime_factor[PMAX + 5];

#define FMAX 1000005
#define FMOD MOD
int fact[FMAX + 5];

void factorial_init(){
fact[0] = 1;

for(int i = 1; i <= FMAX; i++)
fact[i] = (fact[i - 1] * i) % FMOD;
}

void sieve(){
int n = PMAX;

fill(prime, prime + n, true);

prime[0] = prime[1] = false;

for(int p = 4; p <= n; p += 2)
prime[p] = false;

for(int p = 3; p * p <= n; p += 2){
if(!prime[p])
continue;

for(int i = p * p; i <= n; i += p)
prime[i] = false;
}
}

bool is_prime(int n){
if(!prime[2])
sieve();

return prime[n];
}

void factors_sieve(){
int n = PMAX;

fill(prime_factor, prime_factor + n, -1);

prime_factor[1] = 1;

for(int p = 2; p <= n; p += 2)
prime_factor[p] = 2;

for(int p = 3; p <= n; p += 2){
if(prime_factor[p] != -1)
continue;

prime_factor[p] = p;

for(int i = p; i <= n; i += p){
if(prime_factor[i] == -1)
prime_factor[i] = p;
}
}
}

vector<int> prime_factors(int n){
if(prime_factor[1] != 1)
factors_sieve();

vector<int> factors;

if(n == 0)
return factors;

while(n != 1){
factors.push_back(prime_factor[n]);

n /= prime_factor[n];
}

return factors;
}

int int_len(int n){
if(n == 0)
return 1;

int c = 0;

while(n > 0){
n /= 10;
c++;
}

return c;
}

vector<int> primeFactors(int n)
{
vector<int> facts;

while(n % 2 == 0){
facts.pb(2);
n /= 2;
}

for(int i = 3; i <= sqrt(n); i += 2){
while(n % i == 0){
facts.pb(i);
n /= i;
}
}

if (n > 2)
facts.pb(n);

return facts;
}

string int_to_str(int n){
int len = int_len(n);

if(n == 0)
return "0";

string str(len, 'X');

while(n > 0){
str[--len] = (n % 10) + '0';
n /= 10;
}

return str;
}

int str_to_int(string str){
int n = 0;

for(auto i: str)
n = n * 10 + (i - '0');

return n;
}

void testcase();

/** ----------------------------------------------- **/

// #define FILE_I "input.txt"
// #define FILE_O "output.txt"

#define MOD 1000000007

void init(){
#ifdef FILE_I
freopen(FILE_I, "r", stdin);
#endif

#ifdef FILE_O
freopen(FILE_O, "w", stdout);
#endif

speed; // Comment this line for input-output synchronization
}

integer main()
{
init();

t_times
testcase();
}

void testcase(){
int n; cin >> n;

vector<int> v = primeFactors(n);

if(v.size() < 3){
cout << "NO" << endl;
return;
}

int m = v.size();

int a = v[0];
int b = v[1];
int c = 1;

int x = 2;

if(a == b){
b *= v[2];
x++;
}

for(int i = x; i < m; i++)
c *= v[i];

if(a != b && b != c && a != c && c != 1){
cout << "YES" << endl;
cout << a << " " << b << " " << c << endl;
}

else
cout << "NO" << endl;
}