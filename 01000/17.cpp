#include<bits/stdc++.h>
using namespace std;
int gets(){
    int a=0;
    char b=0;
    while(b<'0'||b>'9'){
        b=getchar_unlocked();
    }
    while(b>='0'&&b<='9'){
        a=a*10+(b-'0');
        b=getchar_unlocked();
    }
    return a;
}
string get(){
    string s="";
    char c=0;
    while(1){
        c=getchar_unlocked();
        if(c==EOF||c==10){
            break;
        }
        s+=c;
    }
    return s;
}
void put(int a){
    if(a>9){
        put(a/10);
    }
    putchar_unlocked(a%10+'0');
}
int main(){
    int a=gets(),b,c,d,e,f,g,h,i;
    string s,x,y;
    //getline(cin,s);
    //a=stoi(s);
    for(i=1;i<=a;++i){
        s=get();
        putchar_unlocked('C');
        putchar_unlocked('o');
        putchar_unlocked('m');
        putchar_unlocked('m');
        putchar_unlocked('a');
        putchar_unlocked('n');
        putchar_unlocked('d');
        putchar_unlocked(' ');
        putchar_unlocked('#');
        put(i);
        putchar_unlocked(':');
        putchar_unlocked(' ');
        //printf("Command #%d: ",i);
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
// https://judge.hkoi.org/submission/1351234/details?sharing=80eW9LvWAqFYQzlrhfsjW7CjOc
// 評測結果
// 子任務	測試	結果	執行時間	記憶體	分數
// 1	1	正確	0.000 s	1.418 MB	100.000
// 1	2	正確	0.000 s	1.418 MB	100.000
// 1	3	正確	0.000 s	1.426 MB	100.000
// 1	4	正確	0.000 s	1.426 MB	100.000
// 1	5	正確	0.000 s	1.422 MB	100.000
// 1	6	正確	0.000 s	1.418 MB	100.000
// 1	7	正確	0.000 s	1.426 MB	100.000
// 1	8	正確	0.005 s	1.422 MB	100.000
//   2025-03-01 20:22:25
