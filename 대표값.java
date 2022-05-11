import java.util.*;

public class 대표값 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int add = 0;
		int mini = 0;
		int N = sc.nextInt();
		int[] a = new int[N];
		int[] c = new int[N];
		if(5 <= N && N <= 100) {
			for(int i = 0;i<a.length;i++) {
				a[i] = sc.nextInt();
				add = a[i] + add;
			}
			if(a.length == N) {
				add = (add+5)/10*10;
				add = (add/a.length);
				for(int i = 0;i<a.length;i++) {
					c[i] = Math.abs(add-a[i]);
				}
				for(int i = 0;i<c.length;i++) {
					if(c[i] < c[mini]) {
						mini = i;
					}
					else if(c[i] == c[mini]) {
						if(a[i] > a[mini]) {
							mini = i;
						}
						else if(a[i] == a[mini]) {
							if (i < mini) {
								mini = i;
							}
						}
					}
				}
			}
			
		}
		System.out.printf("%d %d", add, mini+1);	
	}
}