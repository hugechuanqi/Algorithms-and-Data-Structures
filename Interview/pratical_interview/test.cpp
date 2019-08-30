#include<iostream>
#include <algorithm>
using namespace std; 
int SearchMaxLengthSequence(string s1, string s2)
{
	int length1 = s1.length();
	int length2 = s2.length();
	int** matrix = new int*[length1 + 1];
	for (size_t i = 0; i < length1 + 1; i++)
	{
		matrix[i] = new int[length2 + 1]();
	}

	for (size_t i = 1; i <= length1; i++)
	{
		for (size_t j = 1; j <= length2; j++)
		{
			if (s1[i - 1] == s2[j - 1])
			{
				matrix[i][j] = matrix[i - 1][j - 1] + 1;
			}
			else
			{
				matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j]);
			}
		}
	}

	int commomLength = matrix[length1][length2];//最大子序列的长度
	string commomStr = "";//保存逆序的子序列
	//回溯部分
	while (length1 != 0)
	{
		if (matrix[length1][length2] == matrix[length1 - 1][length2])
		{
			length1--;
			continue;
		}
		if (matrix[length1][length2] == matrix[length1][length2 - 1])
		{
			length2--;
			continue;
		}
		if (matrix[length1][length2] == matrix[length1 - 1][length2 - 1] + 1)
		{
			commomStr += s1[length1 - 1];
			length1--;
			length2--;
		}
	}
	reverse(commomStr.begin(), commomStr.end());
	return commomLength;
}
int main(){
	int n;
	while(cin>>n){
		string s1,s2;
		while(n--){
			char c;
			cin>>c;
			s1+=c;
		}
		n=s1.size();
		while(n--){
			char c;
			cin>>c;
			s2+=c;
		}
		cout<<s1.size() - SearchMaxLengthSequence(s1,s2)<<endl;
	}
	return 0;
}
