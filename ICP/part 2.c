#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"
#include "structheader.h"

void claimProcessing ()
{
    FILE *fp;
    FILE *fp1;
    FILE *fptemp;
    char details[20][80],StrLine[1024],display[30],display2[30];
    int claim,id,check=0,balanceAmount,minus=0,year,day,date,service,totalOtherFee=0,totalRoomFee,overload=0,CurrentIndex=1;
    time_t timep;
    struct tm *p;
    time (&timep);
    p=gmtime(&timep);
    printf("Enter Subscriber ID :");
    if((scanf("%d", &id))!=1){
        printf ("INVAIID INPUT\n");
        scanf("%*s");
        mainMenu();
    }
    printf("Enter Claimed year :");
    if((scanf("%d", &year))!=1){
        printf ("INVAIID INPUT\n");
        scanf("%*s");
        mainMenu();
    }
    fp=fopen("subscription.txt","r");
    while (!feof(fp))
    {
        if (CurrentIndex==id)
        {
            fgets(StrLine,1024,fp);
            check = 1;
            break;
        }
        fgets(StrLine,1024,fp);
        CurrentIndex++;
    }
    fclose(fp);
    split(details, StrLine, "\t");
    if (check == 0)
    {
        printf ("This ID does not exist.\nPlease enter again\n\n");
        mainMenu();
    }
    subs[id].age = atoi (details[5]);
    subs[id].plan = atoi (details[6]);
    subs[id].plan2 = atoi (details[7]);
    subs[id].oriClaim = atoi (details[8]);
    date = atoi(details[10]);
    if (subs[id].plan2 == 1){
        if (date != year){
            claim = subs[id].oriClaim;
        }
        else{
            claim = atoi(details[9]);
        }
    }
    else
        claim = atoi (details[9]);

    if (subs[id].plan == 1){
        strcpy (display,"Plan 120") ;
        subs[id].roomFee1 = atoi(details[11]);
    }
    else if (subs[id].plan == 2){
        strcpy (display,"Plan 150") ;
        subs[id].roomFee1 = atoi(details[11]);
    }
    else{
        strcpy (display,"Plan 200") ;
        subs[id].roomFee1 = atoi(details[11]);
    }
    if (subs[id].plan2 == 1)
        strcpy (display2,"Annual Package") ;
    else
        strcpy (display2,"Lifetime package") ;
    printf("\n-- Subscriber Detail --\nName :%s\nContact number :%s\nAddress :%s\nHealth history :%s\nAge :%d\nSubscription ID: S%03d\nSubscribed plan :%s (%s)\nBalance amount :%d",details[1],details[2],details[3],details[4],subs[id].age,id,display,display2,claim);
    printf("\n\nHow many days stay in hospital: ");
    scanf("%d",&day);
    printf("Types of room service\n1. Normal ward \n2. ICU\nPlease select your option :");
    scanf("%d",&service);
    if (service == 2 && subs[id].plan == 1){
        subs[id].roomFee1 = atoi(details[12]);
    }
    else if (service == 2 && subs[id].plan == 2){
        subs[id].roomFee1 = atoi(details[12]);
    }
    else if (service = 2 && subs[id].plan == 2){
        subs[id].roomFee1 = atoi(details[12]);
    }
    do {
        printf ("\n-- Other claimed method -- \n1. Hospital Supplies and Services\n2. Surgical Fees \n3. Other Fees\n4. Exit\nPlease select your option :");
        scanf ("%d",&check);
        if (check == 1 || check == 2|| check == 3 ){
            printf ("Insert the amount that subscriber has been claimed : ");
            scanf ("%d",&minus);
        }
        else if (check == 4){
            totalRoomFee = day * subs[id].roomFee1;
            totalOtherFee = totalOtherFee + minus;
            balanceAmount = claim - totalOtherFee - totalRoomFee;
            if (balanceAmount < 0){
                overload = abs(balanceAmount);
                balanceAmount = 0;
            }
            printf ("\n-- Subscriber Detail --\nName :%s\nContact number :%s\nAddress :%s\nHealth history :%s\nAge :%d\nSubscription ID: S%03d\nSubscribed plan :%s (%s)\nBefore claimed Balance amount : %d",details[1],details[2],details[3],details[4],subs[id].age,id,display,display2,claim);
            printf ("\nAfter claimed Balance amount: %d\nExtra payment : %d\n",balanceAmount,overload);
            printf("Recorded time : %02d:%02d:%02d\n",8+p->tm_hour,p->tm_min,p->tm_sec);
            fp1  = fopen("subscription.txt", "r");
            fptemp = fopen("replace.tmp", "w");
            if (fp1 == NULL || fptemp == NULL)
                {
                    printf("\nUnable to open file.\n");
                }
            CurrentIndex = 1;
            while ((fgets(StrLine,1024, fp1)) != NULL)
            {
                if (CurrentIndex==id){
                    fprintf(fptemp,"%d\t%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%s\t%s",id,details[1],details[2],details[3],details[4],subs[id].age,subs[id].plan,subs[id].plan2,subs[id].oriClaim,balanceAmount,year,details[11],details[12]);
                }
                else{
                    fputs(StrLine,fptemp);
                }
                CurrentIndex++;
            }
            fclose(fp1);
            fclose(fptemp);
            remove("subscription.txt");
            rename("replace.tmp","subscription.txt");
            mainMenu();
        }
        else {
            printf ("Invalid input\nPlease insert again");
            claimProcessing();
        }
    }while (check == 1 || check == 2 || check == 3);
}
