import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
import java.math.*;
import java.awt.*;

public class Main implements Runnable {
    @Override
    public void run() {
        try {
            new Solver().solve();
            System.exit(0);
        } catch (Exception | Error e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public static void main(String[] args) throws Exception {
        //new Thread(null, new Main(), "Solver", 1l << 25).start();
        new Main().run();
    }
}


class Solver {
    final Helper hp;
    final int MAXN = 1000_006;
    final long MOD = 1000000007;

    final Timer timer;
    final TimerTask task;
    final static boolean DEBUG = false; //System.getenv("DEBUG") != null;

    Solver() {
        hp = new Helper(MOD, MAXN);
        if (DEBUG) {
            hp.initIO(System.getProperty("user.home") + "/Desktop/input.txt",
                    System.getProperty("user.home") + "/Desktop/output.txt");
        } else {
            hp.initIO(System.in, System.out);
        }

        timer = new Timer();
        task = new TimerTask() {
            @Override
            public void run() {
                try {
                    hp.flush();
                    System.exit(0);
                } catch (Exception e) {
                }
            }
        };
        //timer.schedule(task, 4700);
    }

    void solve() throws Exception {
        int tc = TESTCASES ? hp.nextInt() : 1;
        for (int tce = 1; tce <= tc; ++tce) solve(tce);
        timer.cancel();
        hp.flush();
    }

    static final boolean TESTCASES = true;

    void solve(int tc) throws Exception {
        int n = hp.nextInt();
        int q = hp.nextInt();

        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = 1;

        long d = 1;

        for (int asd = 0; asd < q; asd++) {
            int x = hp.nextInt(), y = hp.nextInt();
            d *= 2;

            long mini = Long.MAX_VALUE;
            for (int i = x; i <= y; i++) mini = Long.min(mini, a[i]);
            for (int i = x; i <= y; i++) a[i] = a[i] + (mini % MOD);
        }

        long mini = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) mini = Long.min(mini, a[i]);
        hp.println(mini % MOD);
    }

    int N, K;
    int[] C;
    ArrayList<Integer>[] graph;
    boolean[] vis;

    void dfs(int node, Map<Integer, Integer> freq) {
        if (vis[node] || C[node] == 0) return;
        vis[node] = true;
        freq.put(C[node], freq.getOrDefault(C[node], 0) + 1);
        for (int itr : graph[node]) dfs(itr, freq);
    }
}

class Helper {
    final long MOD;
    final int MAXN;
    final Random rnd;

    public Helper(long mod, int maxn) {
        MOD = mod;
        MAXN = maxn;
        rnd = new Random();
    }

    public static int[] sieve;
    public static ArrayList<Integer> primes;

    public void setSieve() {
        if (sieve == null || sieve.length < MAXN) {
            primes = new ArrayList<>();
            sieve = new int[MAXN];
            int i, j;
            for (i = 2; i < MAXN; ++i)
                if (sieve[i] == 0) {
                    primes.add(i);
                    for (j = i; j < MAXN; j += i) {
                        sieve[j] = i;
                    }
                }
        }
    }

    public boolean isPrime(int number) {
        setSieve();
        return number <= 1 ? false : sieve[number] == number;
    }

    // https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    public boolean isProbablePrime(int number, int certainty) {
        if (number < MAXN) return isPrime(number);
        else if ((number & 1) == 0) return false;

        long d = number - 1;
        int r = 0;
        while ((d & 1) == 0) {
            ++r;
            d >>= 1;
        }
        while (--certainty >= 0) { // witness loop
            long a = getRandomInRange(2, Math.min(Integer.MAX_VALUE - 7, number - 2));
            long x = pow(a, d, number);

            if (x == 1 || x == number - 1) {
                continue;
            } else {
                boolean witnessFound = false;
                for (int i = 1; i < r && x > 1; ++i) { // loop runs r - 1 times atmost
                    x = x * x % number;
                    if (x == number - 1) {
                        witnessFound = true;
                        break;
                    }
                }
                if (!witnessFound) return false;
            }
        }
        return true;
    }

    public static long[] factorial;

    public void setFactorial() {
        factorial = new long[MAXN];
        factorial[0] = 1;
        for (int i = 1; i < MAXN; ++i) factorial[i] = factorial[i - 1] * i % MOD;
    }

    public long getFactorial(int n) {
        if (factorial == null) setFactorial();
        return factorial[n];
    }

    public long ncr(int n, int r) {
        if (r > n) return 0;
        if (factorial == null) setFactorial();
        long numerator = factorial[n];
        long denominator = factorial[r] * factorial[n - r] % MOD;
        return numerator * pow(denominator, MOD - 2, MOD) % MOD;
    }


    public long[] getLongArray(int size) throws Exception {
        long[] ar = new long[size];
        for (int i = 0; i < size; ++i) ar[i] = nextLong();
        return ar;
    }

    public int[] getIntArray(int size) throws Exception {
        int[] ar = new int[size];
        for (int i = 0; i < size; ++i) ar[i] = nextInt();
        return ar;
    }

    public String[] getStringArray(int size) throws Exception {
        String[] ar = new String[size];
        for (int i = 0; i < size; ++i) ar[i] = next();
        return ar;
    }

    public String joinElements(long... ar) {
        StringBuilder sb = new StringBuilder();
        for (long itr : ar) sb.append(itr).append(" ");
        return sb.toString().trim();
    }

    public String joinElements(int... ar) {
        StringBuilder sb = new StringBuilder();
        for (int itr : ar) sb.append(itr).append(" ");
        return sb.toString().trim();
    }

    public String joinElements(String... ar) {
        StringBuilder sb = new StringBuilder();
        for (String itr : ar) sb.append(itr).append(" ");
        return sb.toString().trim();
    }

    public String joinElements(Object... ar) {
        StringBuilder sb = new StringBuilder();
        for (Object itr : ar) sb.append(itr).append(" ");
        return sb.toString().trim();
    }

    public long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public long max(long... ar) {
        long ret = ar[0];
        for (long itr : ar) ret = Math.max(ret, itr);
        return ret;
    }

    public int max(int... ar) {
        int ret = ar[0];
        for (int itr : ar) ret = Math.max(ret, itr);
        return ret;
    }

    public long min(long... ar) {
        long ret = ar[0];
        for (long itr : ar) ret = Math.min(ret, itr);
        return ret;
    }

    public int min(int... ar) {
        int ret = ar[0];
        for (int itr : ar) ret = Math.min(ret, itr);
        return ret;
    }

    public long sum(long... ar) {
        long sum = 0;
        for (long itr : ar) sum += itr;
        return sum;
    }

    public long sum(int... ar) {
        long sum = 0;
        for (int itr : ar) sum += itr;
        return sum;
    }

    public void shuffle(int[] ar) {
        int r;
        for (int i = 0; i < ar.length; ++i) {
            r = rnd.nextInt(ar.length);
            if (r != i) {
                ar[i] ^= ar[r];
                ar[r] ^= ar[i];
                ar[i] ^= ar[r];
            }
        }
    }

    public void shuffle(long[] ar) {
        int r;
        for (int i = 0; i < ar.length; ++i) {
            r = rnd.nextInt(ar.length);
            if (r != i) {
                ar[i] ^= ar[r];
                ar[r] ^= ar[i];
                ar[i] ^= ar[r];
            }
        }
    }

    public void reverse(int[] ar) {
        int r;
        for (int i = 0; i < ar.length; ++i) {
            r = ar.length - 1 - i;
            if (r > i) {
                ar[i] ^= ar[r];
                ar[r] ^= ar[i];
                ar[i] ^= ar[r];
            }
        }
    }

    public void reverse(long[] ar) {
        int r;
        for (int i = 0; i < ar.length; ++i) {
            r = ar.length - 1 - i;
            if (r > i) {
                ar[i] ^= ar[r];
                ar[r] ^= ar[i];
                ar[i] ^= ar[r];
            }
        }
    }

    public long pow(long base, long exp, long MOD) {
        base %= MOD;
        long ret = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) ret = ret * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return ret;
    }

    public int getRandomInRange(int l, int r) {
        return rnd.nextInt(r - l + 1) + l;
    }


    static final int BUFSIZE = 1 << 20;
    static byte[] buf;
    static int index, total;
    static InputStream in;
    static BufferedWriter bw;

    public void initIO(InputStream is, OutputStream os) {
        try {
            in = is;
            bw = new BufferedWriter(new OutputStreamWriter(os));
            buf = new byte[BUFSIZE];
        } catch (Exception e) {
        }
    }

    public void initIO(String inputFile, String outputFile) {
        try {
            in = new FileInputStream(inputFile);
            bw = new BufferedWriter(new OutputStreamWriter(
                    new FileOutputStream(outputFile)));
            buf = new byte[BUFSIZE];
        } catch (Exception e) {
        }
    }

    private int scan() throws Exception {
        if (index >= total) {
            index = 0;
            total = in.read(buf);
            if (total <= 0)
                return -1;
        }
        return buf[index++];
    }

    public String next() throws Exception {
        int c;
        for (c = scan(); c <= 32; c = scan()) ;
        StringBuilder sb = new StringBuilder();
        for (; c > 32; c = scan())
            sb.append((char) c);
        return sb.toString();
    }

    public int nextInt() throws Exception {
        int c, val = 0;
        for (c = scan(); c <= 32; c = scan()) ;
        boolean neg = c == '-';
        if (c == '-' || c == '+')
            c = scan();
        for (; c >= '0' && c <= '9'; c = scan())
            val = (val << 3) + (val << 1) + (c & 15);
        return neg ? -val : val;
    }

    public long nextLong() throws Exception {
        int c;
        long val = 0;
        for (c = scan(); c <= 32; c = scan()) ;
        boolean neg = c == '-';
        if (c == '-' || c == '+')
            c = scan();
        for (; c >= '0' && c <= '9'; c = scan())
            val = (val << 3) + (val << 1) + (c & 15);
        return neg ? -val : val;
    }

    public void print(Object a) throws Exception {
        bw.write(a.toString());
    }

    public void printsp(Object a) throws Exception {
        print(a);
        print(" ");
    }

    public void println() throws Exception {
        bw.write("\n");
    }

    public void println(Object a) throws Exception {
        print(a);
        println();
    }

    public void errprint(Object a) {
        if (Solver.DEBUG) {
            System.err.print(a);
        }
    }

    public void errprintsp(Object a) {
        errprint(a);
        errprint(" ");
    }

    public void errprintln() {
        errprint("\n");
    }

    public void errprintln(Object a) {
        errprint(a);
        errprintln();
    }

    public void flush() throws Exception {
        bw.flush();
    }
}
