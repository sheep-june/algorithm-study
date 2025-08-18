import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);

        int n = Integer.parseInt(br.readLine());

        int[] A = new int[n];
        int[] ans = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) A[i] = Integer.parseInt(st.nextToken());

        int[] stack = new int[n];
        int top = -1;

        stack[++top] = 0; 
        for (int i = 1; i < n; i++) {
            while (top >= 0 && A[stack[top]] < A[i]) {
                ans[stack[top--]] = A[i];
            }
            stack[++top] = i;
        }
        while (top >= 0) ans[stack[top--]] = -1;

        StringBuilder sb = new StringBuilder(n * 3);
        for (int i = 0; i < n; i++) {
            sb.append(ans[i]).append(' ');
        }
        sb.append('\n');

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out), 1 << 16);
        bw.write(sb.toString());
        bw.flush();
    }
}
