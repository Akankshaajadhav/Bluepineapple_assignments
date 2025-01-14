#include<stdio.h>
#include<string.h>

struct book{
    int id;
    char name[100];
    char author[30];
    int price;
};

int count=0;
struct book arrbook[100];

void Addbook(){
    struct book new;
    new.id=count+1;

    printf("Enter book name : ");
    getchar();
    fgets(new.name,sizeof(new.name),stdin);
    new.name[strcspn(new.name, "\n")] = 0;
    printf("Enter author name : ");
    fgets(new.author,sizeof(new.author),stdin);
    new.author[strcspn(new.author, "\n")] = 0;
    printf("Enter book price : ");
    scanf("%d",&new.price);

    count++;
    arrbook[count]=new;
}

void Deletebook(){
    if(count==0){
        printf("There are no books to delete\n");
    }

    else{
        int id,j=0;
        printf("Enter id of the book to delete: ");
        scanf("%d",&id);
        for(int i=1;i<=count;i++){
            if(arrbook[i].id==id){
                j=i;
                break;
            }
        }

        for(int i=j;i<=count;i++){
            arrbook[i]=arrbook[i+1];
        }
    count--;
    printf("book deleted successfully\n");
    }
}

void Searchbook(){
    char name[100];
    printf("Enter the title of the book to search: ");
    getchar(); 
    fgets(name,sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0;

    int flag=0;
    for (int i = 1; i <= count; i++) {
        if (strcmp(arrbook[i].name, name) == 0) {
            printf("Book Found: ID: %d, Title: %s, Author: %s, Price: %d\n",
                   arrbook[i].id, arrbook[i].name, arrbook[i].author, arrbook[i].price);
                   flag=1;
            break;
        }
    }

    if(flag==0){
        printf("Book not found\n");
    }

}

void Viewbook(){
    if(count==0){
        printf("No books are added\n");
        return;
    }

    else{
        int i=1;
        printf("Book list is : \n");
        for(i;i<=count;i++){
            printf("Book %d : id(%d)-%s by %s (price- %d)\n",i,arrbook[i].id, arrbook[i].name, arrbook[i].author, arrbook[i].price);
        }
        printf("\n");
    }
}

int main(){
    int choose;
    while(1){
        printf("This is Book Management System. \n");
        printf("1.Add book\n 2.Delete book\n 3.Search book\n 4.View all books\n 5.Exit\n");
        printf("Choose your option : ");
        scanf("%d",&choose);

        switch (choose)
        {
        case 1:
            Addbook();
            break;
    
        case 2:
            Deletebook();
            break;

        case 3:
            Searchbook();
            break;

        case 4:
            Viewbook();
            break;

        case 5:
            return 0;
    
        default:
            break;
        }
    }
return 0;
}