#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "header.h"
#include "structheader.h"
void accountsInformation()
{
    FILE * fp;
    char details[20][80],StrLine[1024],display[100],display2[100];
    int id,lifeClaimAmount,minus,cnt=0,lineCount=1,cnt3=0,claimedAmount=0,flag = 0;
    fp=fopen("subscription.txt","r");
    while ((fgets(StrLine,1024,fp))!= NULL)
    {
        split(details, StrLine, "\t");
        id = atoi (details[0]);
        subs[id].plan = atoi (details[6]);
        subs[id].plan2 = atoi(details[7]);
        subs[id].oriClaim = atoi(details[8]);
        subs[id].claim = atoi(details[9]);
        if (id != lineCount){
            printf ("no exist");
            mainMenu();
        }
        if (subs[id].plan2 == 2){
            if (subs[id].plan == 1){
                strcpy (display,"Plan 120") ;
            }
            else if (subs[id].plan == 2){
                strcpy (display,"Plan 150") ;
            }
            else{
                strcpy (display,"Plan 200") ;
            }
            strcpy (display2,"Lifetime Package") ;
            claimedAmount = subs[id].oriClaim - subs[id].claim;

            if (claimedAmount != 0){
                cnt3++;
                printf("\nSUBSCRIBER THAT CLAIMED AMOUNT IN LIFETIME CLAIM LIMIT\n\n-- NO%d Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%s\nSubscription ID :S%03d\nSubscribed plan :%s (%s)\nClaimed amount \t:RM %d\nBalance amount \t:RM %d (%s)\n",cnt3,details[1],details[2],details[3],details[4],details[5],id,display,display2,claimedAmount,subs[id].claim,details[10]);
                printf("Maxinum room charges claim limit per day : \nNormal ward : RM%s \nICU : RM%s\n",details[11],details[12]);
                minus = subs[id].oriClaim - subs[id].claim;
                lifeClaimAmount += minus;
            }
        lineCount++;
        }
        if (subs[id].plan2 == 1){
            if (subs[id].claim == 0 ){

                if (subs[id].plan == 1){
                    strcpy (display,"Plan 120") ;
                }
                else if (subs[id].plan == 2){
                    strcpy (display,"Plan 150") ;
                }
                else{
                    strcpy (display,"Plan 200") ;
                }
                strcpy (display2,"Annual Package") ;
                cnt = cnt+ 1;
                claimedAmount = subs[id].oriClaim - subs[id].claim;
                printf("\nSUBSCRIBER THAT CLAIMED AMOUNT IN Annual CLAIM LIMIT\n\n-- NO%d Subscriber Detail --\nName \t\t:%s\nContact number \t:%s\nAddress \t:%s\nHealth history \t:%s\nAge \t\t:%s\nSubscription ID :S%03d\nSubscribed plan :%s (%s)\nClaimed amount \t:RM %d\nBalance amount \t:RM %d (%s)\n",cnt,details[1],details[2],details[3],details[4],details[5],id,display,display2,claimedAmount,subs[id].claim,details[10]);
                printf("Maxinum room charges claim limit per day : \nNormal ward : RM%s \nICU : RM%s\n",details[11],details[12]);
            }
        lineCount++;
        }
    }
    fclose(fp);
    printf ("Total amount claimed by Lifetime Claim Limit subscribers : %d",lifeClaimAmount);
    printf ("\nTotal number of Annual Claim Limit subscribers who have exhausted all their eligible amount : %d\n\n",cnt);
   mainMenu();
}

