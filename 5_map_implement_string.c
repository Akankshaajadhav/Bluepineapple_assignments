#include<stdio.h>
#include<string.h>

char* keys[10];
int value[10];
int currentSize=0;

int showIndex(char word[]){
    for(int i=0;i<currentSize;i++){
        if(strcmp(keys[i],word)==0){
            return i;
        }
    }
    return -1;
}

void Insert(char word[],int data){
    
    int index=showIndex(word);
    if(index==-1){
        keys[currentSize]=word;
        value[currentSize]=data;
        currentSize++;
    }
    else
        value[index]+=data;
}

int showValue(char word[]){
    int index=showIndex(word);
    if(index==-1){
        return -1;
    }
    else
        return value[index];
}

void print(){
    for(int i=0;i<currentSize;i++){
        printf("%s:%d\n",keys[i],value[i]);
    }
}

void main(){
    Insert("one",1);
    Insert("two",2);
    Insert("Three",3);
    printf("Map is : \n");
    print();
    printf("value of key two is %d",showValue("two"));
}


