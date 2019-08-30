#include<bits/stdc++.h>
  
using namespace std;
     
int main(){
    vector<int> map={1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45};
    vector<int> to_match(6);
    int num=0;
   while(cin>>to_match[num]){
        num++;
       if(num==6){
            num=0;
            int first=0;
            for(first=0;first<map.size()-5;first++){
                if(map[first]==to_match[0])
                    break;
            }
            int next=first;
            int m=0;
            bool re=true;
            while((next<first+6) && (next<map.size())){
                re=true;
                if(map[next]==to_match[m]){
                    next++;
                    m++;
                }
                else{
                    re=false;
                    cout<<"0"<<endl;
                    break;
                }
            }
            if(re)
                cout<<"1"<<endl;
       }
    
   }
    return 1;
}