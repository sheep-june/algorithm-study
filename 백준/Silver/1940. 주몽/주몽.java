import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader buff = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(buff.readLine());
        int M = Integer.parseInt(buff.readLine());
        int[] A = new int[N];
        StringTokenizer strtn = new StringTokenizer(buff.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(strtn.nextToken());
        }
        Arrays.sort(A);
        int count = 0;
        int i=0;
        int j = N-1;
        while(i<j){
            if(A[i]+A[j]<M)i++;
            else if(A[i]+A[j]>M)j--;
            else{
                count++;
                i++;
                j--;
            }
        }
        System.out.println(count);
    }
}