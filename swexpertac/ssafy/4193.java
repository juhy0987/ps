package ssafyTest;
/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.PriorityQueue;
/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		/*
		   아래의 메소드 호출은 앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
		   여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
		   이 코드를 프로그램의 처음 부분에 추가하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
		   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 메소드를 사용하셔도 좋습니다.
		   단, 채점을 위해 코드를 제출하실 때에는 반드시 이 메소드를 지우거나 주석 처리 하셔야 합니다.
		 */
		//System.setIn(new FileInputStream("res/input.txt"));

		/*
		   표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
		 */
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
			int R1, C1, R2, C2;
			int[][] field = new int[15][15];
			Boolean[][] visited = new Boolean[15][15];
			
			int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
			
			for(int i=0;i<N;i++)
			{
				for(int j=0;j<N;j++)
				{
					field[i][j] = sc.nextInt();
					visited[i][j] = false;
				}
			}
			
			R1 = sc.nextInt(); C1 = sc.nextInt();
			R2 = sc.nextInt(); C2 = sc.nextInt();
			
			PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[0]-b[0]);
			int depth = -1;
			int[] init = {0, R1, C1};
			q.add(init);
			while(!q.isEmpty())
			{
				int[] cur = q.poll();
				if(visited[cur[1]][cur[2]]) continue;
				visited[cur[1]][cur[2]] = true;
				
//				System.out.printf("%d %d, depth: %d\n", cur[1], cur[2], cur[0]);
				
				if(cur[1] == R2 && cur[2] == C2) {
					depth = cur[0];
					break;
				}
				
				int next_depth = cur[0]+1;
				for(int k=0;k<4;k++) {
					int[] next_value = {next_depth, cur[1] + dir[k][0], cur[2] + dir[k][1]};
					if(next_value[1] < 0 || next_value[1] >= N || next_value[2] < 0 || next_value[2] >= N)
						continue;
					if(visited[next_value[1]][next_value[2]])
						continue;
					if(field[next_value[1]][next_value[2]] == 1)
						continue;
					if(field[next_value[1]][next_value[2]] == 2) {
						int wait = 0;
						while ((cur[0]+wait) % 3 != 2) {
//							System.out.printf("%d\n", cur[0]+wait);
							wait += 1;
						}
						int[] tmp = {next_value[0]+wait, next_value[1], next_value[2]};
						q.add(tmp);
						continue;
					}
						
					q.add(next_value);
				}
			}
			
			System.out.printf("#%d %d\n", test_case, depth);
		}
	}
}