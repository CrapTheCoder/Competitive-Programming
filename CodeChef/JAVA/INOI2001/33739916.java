import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.*;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        new Solver().solve();
    }
}

class Solver {
    final Helper hp;

    Solver() {
        hp = new Helper();
        hp.initIO(System.in, System.out);
    }

    public void solve() throws Exception {
        int tcs = TESTCASES ? hp.nextInt() : 1;

        for(int tcn = 0; tcn < tcs; tcn++)
            solve(tcn);

        hp.flush();
    }

    boolean TESTCASES = true;

    ArrayList<ArrayList<Long>> adj;
    boolean[] visited;

    public void solve(int tcn) throws Exception {
        long n = hp.nextInt(), m = hp.nextInt();

        adj = new ArrayList<>((int) n);
        visited = new boolean[(int) n];

        for (long i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (long i = 0; i < m; i++){
            long u = hp.nextInt(), v = hp.nextInt();
            u--; v--;

            adj.get((int) u).add((long) v);
            adj.get((int) v).add((long) u);
        }

        ArrayList<Long> odd = new ArrayList<>();
        ArrayList<Long> even = new ArrayList<>();

        for(long u = 0; u < n; u++){
            if(visited[(int) u])
                continue;

            minimum = Long.MAX_VALUE;
            maximum = Long.MIN_VALUE;
            size = 0;

            dfs(u);

            if (size % 2 == 1)
                odd.add(maximum);
            else
                even.add(minimum);
        }

        visited = new boolean[(int) n];

        long oddSum = 0, evenSum = 0;

        for (long u : odd) oddSum += sumLevels(u, 1);
        for (long u : even) evenSum += sumLevels(u, 1);

        hp.println(evenSum + " " + oddSum);
    }

    long minimum;
    long maximum;
    long size;

    public void dfs(long u){
        if (visited[(int) u])
            return;

        visited[(int) u] = true;

        minimum = Math.min(minimum, u);
        maximum = Math.max(maximum, u);
        size++;

        for (long v : adj.get((int) u))
            dfs(v);
    }

    public long sumLevels(long u, long cur_level){
        if (visited[(int) u])
            return 0;

        visited[(int) u] = true;

        long sum = cur_level;

        for (long v : adj.get((int) u))
            sum += sumLevels(v, cur_level + 1);

        return sum;
    }
}

class Helper {
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

    public long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }

    public int lcm(int a, int b) {
        return a * b / gcd(a, b);
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


    static final int BUFFER_SIZE = 1 << 20;
    static byte[] buf;
    static int index, total;
    static InputStream in;
    static BufferedWriter bw;


    public void initIO(InputStream is, OutputStream os) {
        try {
            in = is;
            bw = new BufferedWriter(new OutputStreamWriter(os));
            buf = new byte[BUFFER_SIZE];
        } catch (Exception ignored) {
        }
    }

    public void initIO(String inputFile, String outputFile) {
        try {
            in = new FileInputStream(inputFile);
            bw = new BufferedWriter(new OutputStreamWriter(
                    new FileOutputStream(outputFile)));
            buf = new byte[BUFFER_SIZE];
        } catch (Exception ignored) {
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
        int c = scan();
        while (c <= 32) c = scan();
        StringBuilder sb = new StringBuilder();
        for (; c > 32; c = scan())
            sb.append((char) c);
        return sb.toString();
    }

    public int nextInt() throws Exception {
        int c = scan(), val = 0;
        while (c <= 32) c = scan();
        boolean neg = c == '-';
        if (c == '-' || c == '+')
            c = scan();
        for (; c >= '0' && c <= '9'; c = scan())
            val = (val << 3) + (val << 1) + (c & 15);
        return neg ? -val : val;
    }

    public long nextLong() throws Exception {
        int c = scan(), val = 0;
        while (c <= 32) c = scan();
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

    public void flush() throws Exception {
        bw.flush();
    }
}
