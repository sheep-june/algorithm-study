import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        char[] dna = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        int[] need = new int[4];
        for (int i = 0; i < 4; i++) need[i] = Integer.parseInt(st.nextToken());

        int[] map = new int[128];
        Arrays.fill(map, -1);
        map['A'] = 0; map['C'] = 1; map['G'] = 2; map['T'] = 3;

        int[] cnt = new int[4];
        int met = 0;                   
        for (int i = 0; i < 4; i++)    
            if (need[i] == 0) met++;

        for (int i = 0; i < p; i++) {
            int idx = map[dna[i]];
            if (idx >= 0) {
                cnt[idx]++;
                if (cnt[idx] == need[idx]) met++;
            }
        }

        int answer = (met == 4) ? 1 : 0;

        for (int i = p; i < s; i++) {
            int inIdx = map[dna[i]];
            if (inIdx >= 0) {
                cnt[inIdx]++;
                if (cnt[inIdx] == need[inIdx]) met++;
            }

            int outIdx = map[dna[i - p]];
            if (outIdx >= 0) {
                if (cnt[outIdx] == need[outIdx]) met--; 
                cnt[outIdx]--;
            }

            if (met == 4) answer++;
        }

        System.out.print(answer);
    }
}
