#include<stdio.h>
#include<string.h>

int main(){
    char phrase[20];
    int sum = 0;
    printf("Enter a string : ");
    scanf("%s",phrase);

    for(int i=0; phrase[i]!='\0'; i++){
        if (phrase[i] == 'P'){
            sum += 10;
        }
        else if (48 <= phrase[i] && phrase[i] <= 57){
            sum += (phrase[i] - '0');
        }
    }
    printf("Sum = %d\n",sum);
}