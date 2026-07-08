package samsung01;

import java.util.Scanner;
import java.util.HashMap;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            String S = sc.next();

            // 접두 상태 (pA, pC) 하나를 long 키로 인코딩
            long span = 2L * N + 1;                 // 각 값의 범위 [-N, N] -> [0, 2N]
            HashMap<Long, Integer> map = new HashMap<>();

            int pA = 0, pC = 0;                      // pA = (#A-#T) 누적, pC = (#C-#G) 누적
            map.put(encode(pA, pC, N, span), 1);     // 첫 글자 이전의 접두 상태

            long answer = 0;                         // 최악의 경우 int를 넘을 수 있어 long
            for (int k = 0; k < N; k++) {
                switch (S.charAt(k)) {
                    case 'A': pA++; break;
                    case 'T': pA--; break;
                    case 'C': pC++; break;
                    case 'G': pC--; break;
                }
                long key = encode(pA, pC, N, span);
                int seen = map.getOrDefault(key, 0); // 같은 상태였던 과거 접두 개수
                answer += seen;                      // = 그 지점부터 여기까지가 균형 구간
                map.put(key, seen + 1);
            }

            System.out.println(answer);
        }
    }

    private static long encode(int pA, int pC, int N, long span) {
        return (long) (pA + N) * span + (pC + N);
    }
}