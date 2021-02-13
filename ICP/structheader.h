#ifndef STRUCTHEADER_H_INCLUDED
#define STRUCTHEADER_H_INCLUDED

struct subscription{
    char name[40],contact[15],address[1024],history[1024];
    int age,plan,plan2,roomFee1,roomFee2,claim,oriClaim;
} subs[1000];

#endif // STRUCTHEADER_H_INCLUDED
