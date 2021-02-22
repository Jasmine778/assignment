#include <stdio.h>
#include "header.h"

int mainMenu ()
{
    int option;
    do {
        printf ("-- MAIN MENU --\n1. Insurance Plan Subcription\n2. Claim Processing\n3. Accounts Information\n4. Searching Functionalities\n5. Terminate program\nPlease select your option: ");
        if((scanf("%d", &option))!=1){
            printf ("INVAIID INPUT\n");
            scanf("%*s");
        }
        else{
            if (option == 1){
                doingSubscription();
            }
            else if (option == 2){
                claimProcessing();
            }
            else if (option == 3){
                accountsInformation();
            }
            else if (option == 4){
                menu();
            }
            else if (option == 5){
                printf ("Thank you for using this system");
                exit(0);
            }
            else{
                printf ("\nINVALID INPUT\nPlease enter again\n");
            }
        }
    }while (option >= 5 || option <= 0);
    return 0;
}

void menu()
{
    int check;
    do {
        printf ("Searching by using :\n1.ID or Name\n2.Plan\n3.Claim Limit Type \n4.Age\n5.Exit\nEnter your option: ");
        if((scanf("%d", &check))!=1){
            printf ("INVAIID INPUT\n");
            scanf("%*s");
            menu();
        }
        if (check == 1){
            searchingFunctionalities1();
        }
        else if (check == 2){
            searchingFunctionalities2();
        }
        else if (check == 3){
            searchingFunctionalities3();
        }
        else if (check == 4){
            searchingFunctionalities4();
        }
        else if (check == 5){
            mainMenu();
        }
        else{
            printf ("\nINVALID INPUT\nPlease enter again\n");
        }
    }while(check < 1 || check > 5);
}


