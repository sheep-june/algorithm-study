//import org.w3c.dom.Node;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        int[] seq = new int[N];
        for (int i = 0; i < N; i++) seq[i] = Integer.parseInt(br.readLine().trim());

        Deque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        int next = 1;
        for (int su : seq) {
            while (next <= su) {
                stack.push(next++);
                sb.append("+\n");
            }
            if (stack.isEmpty() || stack.peek() != su) {
                System.out.print("NO");
                return;
            }
            stack.pop();
            sb.append("-\n");
        }
        System.out.print(sb);
    }
}
