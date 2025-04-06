#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d,e,f,g,h,i;
    string s,x,y;
    getline(cin,s);
    a=stoi(s);
    for(i=1;i<=a;++i){
        getline(cin,s);
        printf("Command #%d: ",i);
        b=s.find('\"',1)+2;
        x=s.substr(b);
        s=s.substr(0,b);
        if(x[0]=='C'){
            b=x.find('\"',5);
            x=x.substr(5,b-5);
            b=s.find(x);
            if(b!=-1){
                s.erase(b,x.size());
            }
        }
        else if(x[0]=='A'){
            b=x.find('\"',8);
            x=x.substr(8,b-8);
            s.insert(s.size()-2,x);
        }
        else if(x[0]=='I'){
            b=x.find('\"');
            c=stoi(x.substr(7,b-1));
            d=x.find('\"',b+1);
            x=x.substr(b+1,d-1-b);
            s.insert(c,x);
        }
        else{
            b=x.find('\"',9);
            y=x.substr(9,b-9);
            //cout<<y<<endl;
            c=s.find(y);
            if(c!=-1){
                d=b+3;
                b=x.find('\"',b+3);
                x=x.substr(d,b-d);
                s.erase(c,y.size());
                s.insert(c,x);
                //cout<<y<<endl;
            }
        }
        for(char ch:s){
            putchar_unlocked(ch);
        }
        //cout<<s/*+"||"+x*/;
        putchar_unlocked(10);
    }
    return 0;
}
// https://judge.hkoi.org/submission/1351229/details?sharing=ZIxCckbfB9NU9EUk78yYlpvvLqE
// 評測結果
// 子任務	測試	結果	執行時間	記憶體	分數
// 1	1	正確	0.000 s	1.422 MB	100.000
// 1	2	正確	0.000 s	1.422 MB	100.000
// 1	3	正確	0.000 s	1.422 MB	100.000
// 1	4	正確	0.000 s	1.422 MB	100.000
// 1	5	正確	0.000 s	1.418 MB	100.000
// 1	6	正確	0.000 s	1.418 MB	100.000
// 1	7	正確	0.000 s	1.418 MB	100.000
// 1	8	正確	0.022 s	1.418 MB	100.000
// 2025-03-01 20:17:44
