#include <stdio.h>/*header files*/
#include <string.h>

struct employee{
    char name[40],contact[15],department[1024];
} emp[100];
struct temp{
    char name[40],contact[15],department[1024];
} temp[100];

/*declare the functions*/
void search();
void assign();
void update();
void showList();
void split(char [][80], char * , char* );

/*system functions*/
int main ()
{
    int option;
    do
        { // looping
        printf ("-- MAIN MENU --\n1. Search employee telephone number \n2. Assign telephone numbers to new employees\n3. Update telephone number of the existing employees\n4. Produce a list of all employees and their telephone numbers department-wise.\nPlease select your option: ");
        if((scanf("%d", &option))!=1){ //avoid user insert alphabet
            printf ("INVAIID INPUT\nPlease enter again\n\n");
            scanf("%*s"); // asking user reenter
        }
        else{
            if (option == 1){
                search();
            }
            else if (option == 2){
                assign();
            }
            else if (option == 3){
                update();
            }
            else if (option == 4){
                showList();
            }
            else{
                printf ("\nINVALID INPUT\nPlease enter again\n\n");
            }
        }
    }while (option >= 4 || option <= 0);
    return 0;
}
void search()
{
    char details[20][80],nameOrTel[1024],StrLine[1024];
    int flag;
    FILE *fp;
    printf ("Enter employee name or id:");
    fflush(stdin);
    gets(nameOrTel);
    fp=fopen("tel.txt","r"); // read .txt file
    while ((fgets(StrLine,1024,fp)) != NULL) //read datalines
    {
        split(details,StrLine,"\t"); //split
        if(strcmp(nameOrTel,details[0])== 0){
            flag = 1;
            break;
        }
        else if (strcmp (nameOrTel,details[1])== 0){
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
        main();
    }
    printf ("\n--EMPLOYEE INFO--");
    printf ("\nName : %s",details[1]);
    printf ("\ncontact : %s",details[2]);
    printf ("\nDepartment : %s\n",details[3]);
    main();
}
void assign()
{
    int id=0,check;
    char filecontent[1024];
    FILE *f;
    f=fopen("tel.txt","r");
    if (f==NULL)
        printf("Could not open file.");
    while (!feof(f)){
        fgets(filecontent,1024,f);
        id = id + 1;
    }
    fclose(f);
    printf ("Enter the following detail of employee\nName:");
    fflush(stdin);
    gets (emp[id].name);
    printf ("Contact number: ");
    gets (emp[id].contact);
    printf ("Department: ");
    gets (emp[id].department);
    printf ("\n\n-- Employee Detail --\nName \t\t: %s\nID \t\t: %d\nContact number \t: %s\nDepartment \t: %s",emp[id].name,id,emp[id].contact,emp[id].department);
    f = fopen("tel.txt","a");
    if (f == NULL)
        printf ("Could not create .txt file"); // if file doesnt not exist
    else{
        fprintf(f,"%d\t%s\t%s\t%s\n",id,emp[id].name,emp[id].contact,emp[id].department); // add content to .txt file
    }
    fclose(f);
    printf("\nRECORD SUCCESSFULLY\n\n");
    main();
}
void update()
{
    char StrLine[1024];
    int id,CurrentIndex=1,check=0;
    FILE *fp;
    FILE *fp1;
    FILE *fptemp;
    printf("Enter employee ID :");
    if((scanf("%d", &id))!=1){ // avoid user enter alphabet
        printf ("INVAIID INPUT\n");
        scanf("%*s");
        main();
    }
    fp=fopen("tel.txt","r");
    while (!feof(fp)) // checking employee id exist or not
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
    if (check == 0)
    {
        printf ("This ID does not exist.\nPlease enter again\n\n");
        main();
    }

    printf ("Reenter the following detail of employee\nName:");
    fflush(stdin);
    gets (emp[id].name);
    printf ("Contact number: ");
    gets (emp[id].contact);
    printf ("Department: ");
    gets (emp[id].department);
    printf ("\n\n-- Employee Detail --\nName \t\t: %s\nID \t\t: %d\nContact number \t: %s\nDepartment \t: %s",emp[id].name,id,emp[id].contact,emp[id].department);
    fp1  = fopen("tel.txt", "r"); //original file
    fptemp = fopen("replace.tmp", "w"); //open temporary .txt file
    CurrentIndex = 1; // reset current index value
    while ((fgets(StrLine,1024, fp1)) != NULL)//read datalines when .txt file is not empty
    {
        if (CurrentIndex==id){//find the correct employee data
            fprintf(fptemp,"%d\t%s\t%s\t%s\n",id,emp[id].name,emp[id].contact,emp[id].department);
        }
        else{ // remain the other data
            fputs(StrLine,fptemp);
        }
        CurrentIndex++;
    }
    fclose(fp1);
    fclose(fptemp);
    remove("tel.txt");
    rename("replace.tmp","tel.txt");
    printf ("\nUPDATE SUCCESFULLY\n\n");
    main();
}
void showList()
{
    char details[20][80],StrLine[1024],depart[1024],depart2[1024]; //memory buffer
    int id=1,id2,CurrentIndex=0,check=0;
    FILE *fp;
    fp=fopen("tel.txt","r");
    while (!feof(fp)) // checking how many employee have in .txt file
    {
        fgets(StrLine,1024,fp);
        CurrentIndex++;
    }
    fclose(fp);

    fp=fopen("tel.txt","r");
    while ((fgets(StrLine,1024, fp)) != NULL)//read datalines
    {
        split(details, StrLine, "\t");
        strcpy (emp[id].name,details[1]);
        strcpy (emp[id].contact,details[2]);
        strcpy (emp[id].department,details[3]);

        id ++;
    }

    for (id=1;id<CurrentIndex;id++)
    {
        for (id2=id+1;id2<CurrentIndex;id2++)
        {
            strcpy (depart,emp[id].department);
            strcpy (depart2,emp[id2].department);
            if ((strcmp(depart,depart2))== 1)
            {
                strcpy (temp[id].name,emp[id].name);
                strcpy (temp[id].contact,emp[id].contact);
                strcpy (temp[id].department,emp[id].department);

                strcpy (emp[id].name,emp[id2].name);
                strcpy (emp[id].contact,emp[id2].contact);
                strcpy (emp[id].department,emp[id2].department);

                strcpy (emp[id2].name,temp[id].name);
                strcpy (emp[id2].contact,temp[id].contact);
                strcpy (emp[id2].department,temp[id].department);
            }
        }
    }
    fclose (fp);
    printf ("\n--EMPLOYEE LIST--");
    for (id=1;id<CurrentIndex;id++)
    {
        printf ("\n--NO%d--",id);
        printf ("\nEmployee name: %s",emp[id].name);
        printf ("\nEmployee contact: %s",emp[id].contact);
        printf ("\nEmployee department: %s",emp[id].department);
    }
}
void split(char details[][80], char* str, char* spl)
{
    int n = 0;
    char * storage = NULL;
    storage = strtok(str, spl);
    while(storage != NULL )
    {
        strcpy(details[n++], storage);
        storage = strtok(NULL, spl);
    }
}




