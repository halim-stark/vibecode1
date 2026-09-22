#include <stdio.h>
#include <stdbool.h>

//this is a comment

/*hello
 guys*/

int main(){
    int age = 0;
    char curency = '$';
    char name[30] = "";
    float money = 99;

    //getchar();
    printf("What is your name? : ");
    fgets(name, sizeof(name), stdin);

    printf("How old are you? : ");
    scanf(" %d", &age);

    printf("Hi my name is %s, I am %d years old, Now I have %c%f in my bank account\n", name, age,curency,money);
    printf("%s",name);
    printf("%d",age);


    return 0;
}