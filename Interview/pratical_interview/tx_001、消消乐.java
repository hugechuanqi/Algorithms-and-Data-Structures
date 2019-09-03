import java.util.Scanner;

public class tx {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
    int bx = sc.nextInt();
    int ys = sc.nextInt();
    int[] bx1 = new int[bx];
    int[] ys1 = new int[ys];

    for(int i=0;i<bx;i++) {
    bx1[i] = sc.nextInt();
    }
    for(int i=0;i<ys;i++) {
    ys1[i] = sc.nextInt();
    }

    int bx_j=0 , bx_o=0 , ys_j=0 , ys_o=0;
    
    for(int i=0;i<bx;i++) {
    if(bx1[i]%2==0) {
    bx_o++;
    }else {
    bx_j++;
    }
    }
    for(int i=0;i<ys;i++) {
    if(ys1[i]%2==0) {
    ys_o++;
    }else {
    ys_j++;
    }
    }
    int result = Math.min(bx_o, ys_j)+Math.min(bx_j, ys_o);
    System.out.println(result);
}
}