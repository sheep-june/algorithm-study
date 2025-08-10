import java.io.*;

public class Main {
    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream is) { this.in = is; }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c, sign = 1, val = 0;
            do { c = read(); } while (c <= 32); 
            if (c == '-') { sign = -1; c = read(); }
            while (c > 32) {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        int suNo = fs.nextInt();
        int quizNo = fs.nextInt();

        long[] S = new long[suNo + 1];
        for (int i = 1; i <= suNo; i++) {
            S[i] = S[i - 1] + fs.nextInt(); 
        }

        StringBuilder sb = new StringBuilder(quizNo * 3); 
        for (int q = 0; q < quizNo; q++) {
            int i = fs.nextInt();
            int j = fs.nextInt();
            sb.append(S[j] - S[i - 1]).append('\n');
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sb.toString());
        bw.flush();
    }
}
