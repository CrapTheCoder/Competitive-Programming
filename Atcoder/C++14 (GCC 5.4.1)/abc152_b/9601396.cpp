#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long double dl;
typedef long long int ll;
typedef unsigned long long int ull;

typedef set<int, int> sii;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef unordered_map<int, int> umii;
typedef unordered_set<int, int> usii;

#define int ll
#define double dl

#define endl '\n'
#define INF LONG_MAX

#define flush cout.flush();

#define speed ios::sync_with_stdio(false); cin.tie(NULL);

#define gcd(m, n) __gcd(m, n)
#define lcm(m, n) (m * n) / gcd(m, n)

#define t_times int no_of_t; cin >> no_of_t; while(no_of_t--)
#define q_times int no_of_q; cin >> no_of_q; while(no_of_q--)

#define sorted(a, n) sort(a, a + n);
#define rsorted(a, n) sort(a, a + n, greater<int>());
#define reversed(a, n) reverse(a, a + n);

#define ain(a, n) for(int i = 0; i < n; i++) cin >> a[i];
#define aout(a, n) for(int i = 0; i < n; i++){cout << a[i] << " ";} cout << endl;

#define gin(a, n, m) for(int i = 0; i < n; i++){for(int j = 0; j < m; j++){cin >> a[i][j];}}
#define gout(a, n, m) for(int i = 0; i < n; i++){for(int j = 0; j < m; j++){cout << a[i][j] << " ";} cout << endl;}

#define pb push_back
#define ins insert

#define uset unordered_set
#define umap unordered_map

#define PI 3.1415926535

#define is_odd(n) (n & 1) == 1
#define is_even(n) (n & 1) == 0

int sum(int a[], int n){
    int s = 0;

    for(int i = 0; i < n; i++)
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

bool prime[1000005];
int prime_factor[1000005];

void sieve(int n){
    fill(prime, prime + n + 1, true);

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

void factor_sieve(int n){
    cout << "YES" << endl;

    fill(prime_factor, prime_factor + n + 1, -1);

    prime_factor[1] = 1;

    for(int p = 4; p <= n; p += 2)
        prime_factor[p] = 2;

    for(int p = 3; p * p <= n; p += 2){
        if(prime_factor[p] != -1)
            continue;

        prime_factor[p] = p;

        for(int i = p * p; i <= n; i += p){
            if(prime_factor[i] == -1)
                prime_factor[i] = p;
        }
    }
}

vector<int> prime_factors(int n){
    if(prime_factor[0] != -1)
        factor_sieve(1000000);

    vector<int> facts;

    while(true){
        cout << n << " " << prime_factor[n] << endl;

        facts.push_back(prime_factor[n]);

        if(n == prime_factor[n])
            break;

        n /= prime_factor[n];
    }

    return facts;
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

    // speed; // Comment this line for input-output synchronization
}

integer main()
{
    init();

    testcase();
}

void testcase(){
    int m, n; cin >> m >> n;

    if(m < n){
        for(int i = 0; i < n; i++)
            cout << m;
    }

    else {
        for(int i = 0; i < m; i++)
            cout << n;
    }

    cout << endl;
}
