#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "header.h"
#include "structheader.h"
void doingSubscription()
{
    char lastLine[1024],details[20][80],valid[10];
    int id,oldID,check,year=2020;
    FILE *f;
    f=fopen("subscription.txt","r");
    if (f==NULL)
        printf("Could not open file.");
    while (!feof(f))
        fgets(lastLine,1024,f);
    fclose(f);

    split(details, lastLine, "\t");
    oldID = atoi(details[0]);
    id = oldID + 1;
    printf ("\nEnter age of Subscriber: ");
    if((scanf ("%d",&subs[id].age))!=1){
        scanf("%*s");
        printf ("INVAIID INPUT\n");
        doingSubscription();
    }
    if (subs[id].age ==0){
        printf ("\nMore than 15 days ? YES/NO\n");
        fflush(stdin);
        gets(valid);
        if (strcmp(valid,"No")==0 || strcmp(valid,"NO")==0 || strcmp(valid,"no")==0){
            printf("\n-- Available Insurance Plan Subscription --\nDoes not eligible to any plan\nReturning to Main Menu\n\n");
            mainMenu();
        }
    }
    if (subs[id].age >=0 && subs[id].age <= 20){
        do {
            printf ("\n-- Available Insurance Plan Subscription --\n1. Plan 120\n2. Plan 150\n3. Plan 200");
            printf ("\nPlease select your plan:");
            if(check =(scanf("%d",&subs[id].plan))!=1){
                scanf("%*s");
            }
            if (subs[id].plan >3 || subs[id].plan <1)
                printf("\nINVALID INPUT\nPlease enter again ");
        }while (subs[id].plan<=0 || subs[id].plan>= 4 || check ==1);
    }
    else if (subs[id].age >= 21 && subs[id].age <= 40){
        do{
        printf ("\n-- Available Insurance Plan Subscription --\n1. Plan 150\n2. Plan 200");
        printf ("\nPlease select your plan:");
        if(check =(scanf("%d",&subs[id].plan))!=1){
            scanf("%*s");
        }
        if (subs[id].plan >2 || subs[id].plan <1)
            printf("\nINVALID INPUT\nPlease enter again ");
        }while (subs[id].plan<=0 || subs[id].plan>= 3 || check ==1);
    }
    else if (subs[id].age >= 41 && subs[id].age <= 54){
        do{
        printf ("\n-- Available Insurance Plan Subscription --\n1. Plan 200");
        printf ("\nPlease select your plan:");
        if(check =(scanf("%d",&subs[id].plan))!=1){
            scanf("%*s");
        }
        if (subs[id].plan >1 || subs[id].plan <1)
            printf("\nINVALID INPUT\nPlease enter again \n");
        }while (subs[id].plan !=1 || check ==1 );
    }
    else {
        printf ("\n-- Available Insurance Plan Subscription --\nDoes not eligible to any plan\nReturning to Main Menu\n\n");
        mainMenu();
    }
    do{
        printf ("1. Annual package\n2. Lifetime package\nPlease select your plan:");
        if(check =(scanf("%d",&subs[id].plan2))!=1){
            scanf("%*s");
        }
        if (subs[id].plan2 >2 || subs[id].plan2 <1 )
            printf("\nINVALID INPUT\nPlease enter again \n");
    }while (subs[id].plan2<=0 || subs[id].plan2>= 3 || check ==1);
    printf ("\nEnter the following detail of subscriber\nName: ");
    fflush(stdin);
    gets (subs[id].name);
    printf ("Contact number: ");
    gets (subs[id].contact);
    printf ("Address: ");
    gets (subs[id].address);
    printf ("Health history: ");
    gets (subs[id].history);
    printf ("\n-- Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%d\nSubscription ID :S%03d",subs[id].name,subs[id].contact,subs[id].address,subs[id].history,subs[id].age,id);
    if (subs[id].age >= 21 && subs[id].age <= 40){
        subs[id].plan = subs[id].plan + 1;
    }
    else if (subs[id].age >=41 && subs[id].age <=54){
        subs[id].plan = subs[id].plan + 2;
    }
    else{
        subs[id].plan = subs[id].plan;
    }
    if (subs[id].plan == 1 && subs[id].plan2 ==1){
        subs[id].claim = 120000;
        subs[id].roomFee1 =120;
        subs[id].roomFee2 =250;
        printf ("\nBENIFI AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM120 \nICU : RM250");
    }
    else if (subs[id].plan == 1 && subs[id].plan2 == 2){
        subs[id].claim = 600000;
        subs[id].roomFee1 =120;
        subs[id].roomFee2 =250;
        printf ("\nBENIFIT AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM120 \nICU : RM250");
    }
    else if (subs[id].plan == 2 && subs[id].plan2 == 1){
        subs[id].claim = 150000;
        subs[id].roomFee1 =150;
        subs[id].roomFee2 =400;
        printf ("\nBENIFIT AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM150 \nICU : RM400");
    }
    else if (subs[id].plan == 2 && subs[id].plan2 == 2){
        subs[id].claim = 750000;
        subs[id].roomFee1 =120;
        subs[id].roomFee2 =400;
        printf ("\nBENIFIT AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM150 \nICU : RM400");
    }
    else if (subs[id].plan == 3 && subs[id].plan2 == 1){
        subs[id].claim = 200000;
        subs[id].roomFee1 =200;
        subs[id].roomFee2 =700;
        printf ("\nBENIFIT AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM200 \nICU : RM700");
    }
    else{
        subs[id].claim = 1000000;
        subs[id].roomFee1 =200;
        subs[id].roomFee2 =700;
        printf ("\nBENIFIT AVAILABLE\nMaxinum room charges claim limit per day : \nNormal ward : RM200 \nICU : RM700");
    }

    f = fopen("subscription.txt","a");
    if (f == NULL)
        printf ("Could not create .txt file");
    else{
        fprintf(f,"%d\t%s\t%s\t%s\t%s",id,subs[id].name,subs[id].contact,subs[id].address,subs[id].history);
        fprintf(f,"\t%d\t%d\t%d\t%d\t%d",subs[id].age,subs[id].plan,subs[id].plan2,subs[id].claim,subs[id].claim);
        fprintf(f,"\t%d\t%d\t%d\n",year,subs[id].roomFee1,subs[id].roomFee2);
    }
    fclose(f);
    printf("\nRecord successfully\n\n");
    mainMenu();
}
