import java.util.*;
class Main_ {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] arr=new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        int sum=0;
        int min1=0;
        int min2=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int num=arr[i][j];
                sum+=6*arr[i][j]-2*(num-1);
                if(i+1<n){
                    min1=Math.min(arr[i][j],arr[i+1][j]);
                    sum-=2*min1;
                }
                if(j+1<m){
                    min2=Math.min(arr[i][j],arr[i][j+1]);
                    sum-=2*min2;
                }
            }
        }
        System.out.println(sum);
    }
}