import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String str= sc.next();
        String[] str1 = str.split(";");
        int cnt= Integer.valueOf(str1[1]);
        String[] str2 = str1[0].split(",");
          int n=str2.length;

        int [] arr=new int[n];
        for (int i = 0; i <n ; i++) {
          arr[i]= Integer.valueOf(str2[i]);
        }


        // System.out.println(set);
        TreeSet<Integer> set1=new TreeSet<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer t1, Integer t2) {
                return t2-t1 ;
            }
        });
        TreeSet<Integer> set2=new TreeSet<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer t1, Integer t2) {
                return t2-t1 ;
            }
        });

        
        for (int i = 0; i <n ; i++) {
           if(arr[i]%2==0){
               set1.add(arr[i]);
           }
           else{
               set2.add(arr[i]);
           }
        }

        Iterator<Integer> iterator1 = set1.iterator();
        Iterator<Integer> iterator2 = set2.iterator();
        int cnt1=cnt;
        while (cnt1>0){
                if(iterator1.hasNext()){
                    if(cnt1==1){
                        System.out.print(iterator1.next());
                    }
                    else
                        System.out.print(iterator1.next()+",");
                }
                else{
                    if(iterator2.hasNext()){
                        if(cnt1==1){
                            System.out.print(iterator2.next());
                        }
                        else{
                            System.out.print(iterator2.next()+",");
                        }

                    }
                }
       cnt1--;
   }


    }
}