#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long double dl;
typedef long long int ll;
typedef unsigned long long int ull;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef set<int> sti;
typedef unordered_set<int> usti;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef unordered_map<int, int> uii;
typedef unordered_map<char, int> uci;

#define int ll
#define double dl

#define endl '\n'
#define INF LLONG_MAX
#define INFN LLONG_MIN

#define MOD 1000000007

#define flush cout.flush();

#define speed ios::sync_with_stdio(false); cin.tie(NULL);

int gcd(int m, int n){return __gcd(m, n);}
int lcm(int m, int n){return (m * n) / gcd(m, n);}

#define t_times int no_of_t; cin >> no_of_t; while(no_of_t--)
#define q_times int no_of_q; cin >> no_of_q; while(no_of_q--)

#define amin(a) (*min_element(a))
#define amax(a) (*max_element(a))

#define ain(a, n) for(int i = 0; i < n; ++i) cin >> a[i];
#define aout(a, n) for(int i = 0; i < n; ++i){cout << a[i] << " ";} cout << endl;

#define gin(a, n, m) for(int i = 0; i < n; ++i){for(int j = 0; j < m; ++j){cin >> a[i][j];}}
#define gout(a, n, m) for(int i = 0; i < n; ++i){for(int j = 0; j < m; ++j){cout << a[i][j] << " ";} cout << endl;}

#define push_back emplace_back
#define pb emplace_back
#define ins insert

#define uset unordered_set
#define umap unordered_map

#define PI 3.1415926535

#define is_odd(n) ((n & 1) == 1)
#define is_even(n) ((n & 1) == 0)

#define fst first
#define snd second

#define swapi(a, b) a ^= b; b ^= a; a ^= b;

#define mul2(n) (n << 1)
#define div2(n) (n >> 1)

#define mulp2(n, x) (n << x)
#define divp2(n, x) (n >> x)

void int_input(int &n){
    char c;
    int val = 0;

    for(c = getchar(); c <= 32; c = getchar());

    bool neg = (c == '-');

    if (c == '-' || c == '+')
        c = getchar();

    for (; c >= '0' && c <= '9'; c = getchar())
        val = (val << 3) + (val << 1) + (c & 15);

    n = (neg ? -val : val);
}

int sum(int a[], int n, int st = 0){
    int s = 0;

    for(int i = s; i < n; ++i)
        s += a[i];

    return s;
}

bool is_prime(int n){
    if(n == 2) return true;
    if(n <= 2 || is_even(n)) return false;

    for(int i = 3; i <= sqrt(n); i += 2){
        if(!(n % i))
            return false;
    }

    return true;
}

bool is_pow2(int x){
  return x && (!(x & (x - 1)));
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

#define pow power

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

    for(int i = 1; i <= FMAX; ++i)
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

bool is_prime_sieve(int n){
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

vector<int> prime_facts_sieve(int n){
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
        ++c;
    }

    return c;
}

vector<int> prime_facts(int n){
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

void z_array(string s, int n, int z[]){
    int i = 1, j = 0, k = 1;

    while(i < n){
        if(s[i] == s[j]){
            z[i++] = z[j++];
            z[k]++;
        }

        else {
            j = 0;

            if(s[i] != s[j])
                i++;

            k = i;
        }
    }
}

vector<int> z_match(string s, string p){
    int n = s.size(), m = p.size();
    int z[n + m + 1] = {0};

    z_array(p + '~' + s, m + 1 + n, z);

    vector<int> res;

    for(int i = 0; i <= n + m; i++){
        if(z[i] == m)
            res.pb(i - m - 1);
    }

    return res;
}

#define ppc __builtin_popcount
#define ffs __builtin_ffs
#define ctz __builtin_ctz

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

    // t_times
        testcase();
}

void testcase(){
    int n; cin >> n;

    int c = 0;

    for(int i = 1; i <= n; i++){
        string x = int_to_str(i);

        bool flag = false;

        for(int j = 1; x[j]; j++){
            if(x[j-1] > x[j]){
                flag = true;
                break;
            }
        }

        if(!flag)
            c++;
    }

    cout << c << endl;
}
