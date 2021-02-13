#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "header.h"
#include "structheader.h"

void searchingFunctionalities1()
{
    FILE * fp;
    char details[20][80],display[100],display2[100],StrLine[1024],idChar[100];
    int id=1,flag=0,claim,claimedAmount=0;
    printf("Enter Subscriber ID or Name: ");
    fflush(stdin);
    gets(idChar);
    fp=fopen("subscription.txt","r");
    while ((fgets(StrLine,1024,fp)) != NULL)
    {
        split(details,StrLine,"\t");
        if(strcmp(idChar,details[0])== 0){
            flag = 1;
            break;
        }
        else if (strcmp (idChar,details[1])== 0){
            flag = 1;
            break;
        }
        else
            flag = 0;
    }
    fclose(fp);
    if (flag == 0)
    {
        printf ("This ID haven't been recorded.\nPlease enter again\n\n");
        mainMenu();
    }
    subs[id].plan = atoi (details[6]);
    subs[id].plan2 = atoi (details[7]);
    subs[id].oriClaim = atoi (details[8]);
    claim = atoi(details[9]);
    if (subs[id].plan == 1){
        strcpy (display,"Plan 120") ;
    }
    else if (subs[id].plan == 2){
        strcpy (display,"Plan 150") ;
    }
    else{
        strcpy (display,"Plan 200") ;
    }
    if (subs[id].plan2 == 1){
        strcpy (display2,"Annual Package") ;
    }
    else{
        strcpy (display2,"Lifetime package") ;
    }
    claimedAmount = subs[id].oriClaim - claim;
    printf("\n\n-- Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%s\nSubscription ID :S%03d\nSubscribed plan :%s (%s)\nClaimed amount  :RM %d\nBalance amount  :RM %d (%s)\n",details[1],details[2],details[3],details[4],details[5],id,display,display2,claimedAmount,claim,details[10]);
    printf("Maxinum room charges claim limit per day : \nNormal ward : RM%s \nICU : RM%s\n\n",details[11],details[12]);
    mainMenu();
}

void searchingFunctionalities2()
{
    FILE * fp;
    char details[20][80],display[100],display2[100],StrLine[1024];
    int id,check,cnt=1,cnt2=1;

    printf("Choice:\n1.Plan 120\n2.Plan 150\n3.Plan 200\nEnter Selection of plan : ");
    scanf("%d",&check);
    fp=fopen("subscription.txt","r");
    while (!feof(fp))
    {
        fgets(StrLine,1024,fp);
        split (details,StrLine,"\t");
        id = atoi (details[0]);
        subs[id].plan = atoi(details[6]);
        if (id != cnt){
            break;
        }
        if (subs[id].plan == check){
            subs[id].plan2 = atoi(details[7]);
            if (subs[id].plan == 1){
                strcpy (display,"Plan 120") ;
            }
            else if (subs[id].plan == 2){
                strcpy (display,"Plan 150") ;
            }
            else{
                strcpy (display,"Plan 200") ;
            }
            if (subs[id].plan2 == 1){
                strcpy (display2,"Annual Package") ;
            }
            else{
                strcpy (display2,"Lifetime package") ;
            }
            printf("\n-- NO%d Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%s",cnt2,details[1],details[2],details[3],details[4],details[5]);
            printf ("\nSubscription ID :S%03d\nSubscribed plan :%s (%s)\nBalance amount  :RM %s\nRecorded year   :%s\n",id,display,display2,details[9],details[10]);
            printf ("Maxinum room charges claim limit per day : \nNormal ward : RM%d \nICU : RM%d\n\n",atoi(details[11]),atoi(details[12]));
            cnt2++;
        }
        cnt++;
    }
    fclose(fp);
    if (cnt2 == 1){
        printf ("NO SUBSCRIBER FOUND\n\n");
    }
    mainMenu();
}
void searchingFunctionalities3()
{
    FILE * fp;
    char details[20][80],display[100],display2[100],StrLine[1024];
    int id,check,cnt=1,cnt2=1;

    printf("Choice:\n1.Annual plan\n2.Lifetime plan\nEnter Selection of plan : ");
    scanf("%d",&check);
    fp=fopen("subscription.txt","r");
    while (!feof(fp))
    {
        fgets(StrLine,1024,fp);
        split (details,StrLine,"\t");
        id = atoi (details[0]);
        subs[id].plan2 = atoi(details[7]);
        if (id != cnt){
            break;
        }
        if (subs[id].plan2 == check){
            subs[id].plan = atoi(details[6]);
            if (subs[id].plan == 1){
                strcpy (display,"Plan 120") ;
            }
            else if (subs[id].plan == 2){
                strcpy (display,"Plan 150") ;
            }
            else{
                strcpy (display,"Plan 200") ;
            }
            if (subs[id].plan2 == 1){
                strcpy (display2,"Annual Package") ;
            }
            else{
                strcpy (display2,"Lifetime package") ;
            }
            printf("\n-- NO%d Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%s",cnt2,details[1],details[2],details[3],details[4],details[5]);
            printf ("\nSubscription ID :S%03d\nSubscribed plan :%s (%s)\nBalance amount  :RM %s\nRecorded year   :%s\n",id,display,display2,details[9],details[10]);
            printf ("Maxinum room charges claim limit per day : \nNormal ward : RM%d \nICU : RM%d\n\n",atoi(details[11]),atoi(details[12]));
            cnt2++;
        }
        cnt++;
    }
    fclose(fp);
    if (cnt2 == 1){
        printf ("NO SUBSCRIBER FOUND\n\n");
    }
    mainMenu();
}
void searchingFunctionalities4(){
    FILE * fp;
    char details[20][80],display[100],display2[100],StrLine[1024];
    int id,CurrentIndex=1,check,claim,cnt=1,cnt2=1,flag=0;

    printf("Enter age of Subscriber : ");
    scanf("%d",&check);
    fp=fopen("subscription.txt","r");
    while (!feof(fp))
    {
        fgets(StrLine,1024,fp);
        split (details,StrLine,"\t");
        id = atoi (details[0]);
        subs[id].age = atoi(details[5]);
        if (id != cnt){
            break;
        }
        if (subs[id].age == check){
            subs[id].plan = atoi(details[6]);
            subs[id].plan2 = atoi(details[7]);
            if (subs[id].plan == 1){
                strcpy (display,"Plan 120") ;
            }
            else if (subs[id].plan == 2){
                strcpy (display,"Plan 150") ;
            }
            else{
                strcpy (display,"Plan 200") ;
            }
            if (subs[id].plan2 == 1){
                strcpy (display2,"Annual Package") ;
            }
            else{
                strcpy (display2,"Lifetime package") ;
            }
            printf("\n-- NO%d Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history  :%s\nAge \t\t:%s",cnt2,details[1],details[2],details[3],details[4],details[5]);
            printf ("\nSubscription ID: S%03d\nSubscribed plan :%s (%s)\nBalance amount  :%s\nRecorded year   :%s\n",id,display,display2,details[9],details[10]);
            printf ("Maxinum room charges claim limit per day : \nNormal ward \t: RM%d \nICU \t\t: RM%d\n\n",atoi(details[11]),atoi(details[12]));
            cnt2++;
            flag = 0;
        }
        else
            flag = 1;
        cnt++;

    }
    fclose(fp);
    if (flag == 1){
        printf ("NO SUBSCRIBER FOUND\n\n");
    }
    mainMenu();
}
