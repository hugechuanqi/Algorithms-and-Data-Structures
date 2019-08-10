#include<iostream>
#include<stdio.h>
#include<mutex>
#include<vector>
#include<cmath>
#include<string>
using namespace std;
struct database
{
    int a;
    string b;
    int c;
    bool d;
};

int search_data( vector<struct database> db , int delta , int x)
{
    int i = 0 , j;
    int len = db.size();
    int cnt = 0;
    for(i = 0 ; i<len-1 ; i++)
    {
        for(j = i+1 ; j<len ; j++)
        {
            if( db[i].c == x && db[j].c != x && (db[i].a - db[j].a <=delta) && (db[i].a - db[j].a >=-delta)&& db[i].b == db[j].b && db[i].d != db[j].d)
                cnt++;
        }
    }
    for(i = len-1 ; i>0 ; i--)
    {
        for(j = i-1 ; j>=0 ; j--)
        {
            if( db[i].c == x && db[j].c != x && (db[i].a - db[j].a <=delta) && (db[i].a - db[j].a >=-delta)&& db[i].b == db[j].b && db[i].d != db[j].d)
                cnt++;
        }
    }
    return cnt;
}

int main()
{
    int n , m ;
    cin>>n>>m;
    int i = 0;
    vector<struct database> vec;
    while(i<n)
    {
        struct database temp;
        string s;
        cin>>temp.a>>temp.b>>temp.c>>s;
        if(s == "True")
            temp.d = true;
        if(s == "False")
            temp.d = false;
        vec.push_back(temp);
        i++;
    }
    i = 0;
    int delta , x;
    while(i<m)
    {
        cin>>delta>>x;
        int temp = search_data(vec , delta , x);
        cout<<temp<<endl;
        i++;
    }

    return 0;
}


// 5 2
// 1 hello 1 True
// 2 hello 2 False
// 3 world 3 True
// 4 hello 4 False
// 5 hello 2 True
// 2 2
// 1 3