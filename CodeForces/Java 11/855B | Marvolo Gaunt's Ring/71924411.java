import java.io.OutputStream;
import java.util.*;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.LinkedHashSet;
import java.io.Writer;
import java.io.OutputStreamWriter;
 
/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Egor Kulikov (egor@egork.net)
 */
 
public class Main {
 
    public static void main(String[] args) {
 
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        Solutio solver = new Solutio();
        int testCount = 1;//Integer.parseInt(in.next());
        int sum=0,te=0;
 
        for (int i = 1; i <= testCount; i++) 
        {
            solver.solve(i, in, out);
        }
        out.close();
    }
//**********************SOLVE    HERE     EVERYTHING******************************
 
 
 
    //1 2 3 4 5 
    static class Solutio {
 
        public void solve(int testNumber, InputReader in, OutputWriter out) {
      int n=in.readInt();
      int p=in.readInt(),q=in.readInt(),r=in.readInt();
      long arr[]=new long[n];
      for(int i=0;i<n;i++)
       arr[i]=in.readInt();
      
      long dpp[]=new long[n+1];
      long dpq[]=new long[n+1];
      long dpr[]=new long[n+1];
      
      dpp[0]=dpq[0]=dpr[0]=Long.MIN_VALUE;
      for(int i=1;i<=n;i++)
      {
       dpp[i]=Math.max(p*arr[i-1],dpp[i-1]);
       dpq[i]=Math.max(q*arr[i-1]+dpp[i],dpq[i-1]);
       dpr[i]=Math.max(r*arr[i-1]+dpq[i],dpr[i-1]);
      }
      
      System.out.println(dpr[n]);
      
//      System.out.println(Arrays.toString(pa));
//      System.out.println(Arrays.toString(qa));
//      System.out.println(Arrays.toString(ra));
//      System.out.println(Arrays.toString(dpp));
//      System.out.println(Arrays.toString(dpq));
//      System.out.println(Arrays.toString(dpr));
//      System.out.println(Arrays.toString(s));
      
      
      
      }
      
      
    }
 
 
//*********************END        HERE       EVERYTHING*******************************    
 
    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;
 
        public InputReader(InputStream stream) {
            this.stream = stream;
        }
 
        public void readIntArrays(int[]... arrays) {
            for (int i = 0; i < arrays[0].length; i++) {
                for (int j = 0; j < arrays.length; j++) {
                    arrays[j][i] = readInt();
                }
            }
        }
 
        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }
 
        public int readInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
 
        public String readString() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
                if (Character.isValidCodePoint(c)) {
                    res.appendCodePoint(c);
                }
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }
 
        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }
 
        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
 
        public String next() {
            return readString();
        }
 
        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
 
        }
 
    }
 
    static class OutputWriter {
        private final PrintWriter writer;
 
        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }
 
        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }
 
        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }
 
        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }
 
        public void close() {
            writer.close();
        }
 
    }
 
 
}