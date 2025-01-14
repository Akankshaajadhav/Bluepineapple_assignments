#include<stdio.h>
#include<string.h>

char* keys[10];
int value[10];
int currentSize=0;

int showIndex(char word[]){
    for(int i=0;i<currentSize;i++){
        if(strcmp(keys[i], word) == 0){
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

void print(){
    for(int i=0;i<currentSize;i++){
        printf("%s:%d\n",keys[i],value[i]);
    }
}

void main(){
    char para[500];
    printf("Enter paragraph : ");
    fgets(para,sizeof(para),stdin); // to consider spaces in input
    para[strcspn(para,"\n")]=0; // to remove newline character

    char* splitby=" .,!?"; //can add more punctuations to split
    char* word=strtok(para,splitby); // tokenize paragraph into first word as per split by mentioned above

    while (word!=NULL)
    {
        Insert(word,1);
        word=strtok(NULL,splitby); // NULL means it will remove previous token and operate strtok on remaining paragraph 
    }

    printf("\nWord Frequencies:\n");
    print();
    
}





