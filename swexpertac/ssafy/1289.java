package day1;

import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int T = Integer.parseInt(s);
		for(int t = 1;t <= T;t++) {
			s = br.readLine();
			int pre = '0';
			int swap = 0;
			for(int i=0;i<s.length();i++) {
				int cur = s.charAt(i);
				if(pre != cur) {
					swap += 1;
					pre = cur;
				}
			}
			System.out.printf("#%d %d\n", t, swap);
		}
	}
}
