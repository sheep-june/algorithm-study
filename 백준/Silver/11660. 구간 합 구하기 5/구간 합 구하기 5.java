import java.io.*;

public class Main {
    static class FastScanner {
        private final InputStream in; private final byte[] buf = new byte[1<<16];
        private int ptr=0,len=0;
        FastScanner(InputStream is){ in=is; }
        private int read() throws IOException {
            if (ptr>=len){ len=in.read(buf); ptr=0; if (len<=0) return -1; }
            return buf[ptr++];
        }
        int nextInt() throws IOException {
            int c, s=1, v=0;
            do{ c=read(); } while (c<=32);
            if (c=='-'){ s=-1; c=read(); }
            while (c>32){ v=v*10 + (c-'0'); c=read(); }
            return v*s;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);
        int N = fs.nextInt(), M = fs.nextInt();

        int[][] D = new int[N+1][N+1];
        for (int i=1;i<=N;i++){
            for (int j=1;j<=N;j++){
                int v = fs.nextInt();
                D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + v;
            }
        }

        StringBuilder sb = new StringBuilder(M*8);
        for (int k=0;k<M;k++){
            int x1=fs.nextInt(), y1=fs.nextInt(), x2=fs.nextInt(), y2=fs.nextInt();
            sb.append(D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]).append('\n');
        }
        System.out.print(sb.toString());
    }
}
