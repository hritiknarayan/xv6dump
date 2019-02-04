

#include <stdio.h> 
#include <stdlib.h> 
#include<time.h> 
#include<math.h>
  

int main(){ 
    int flag[100];
    int alreadygen[100];
    srand(time(0)); 
  
    int n;
    printf("Enter number of numbers required:");
    scanf("%d", &n);
  
    for(int i=0;i<100;i++){
    		flag[i]=0;
    		}
    		
    int j=0;
    int k;
    int randnum;
    int randdiv;
    int hashed;
    
    while(j<n){
    
    
    	k=rand()%(n+1);
    	
    
   	
    	
   	 if(flag[k]==0){
    
    	randdiv=(int)(pow(10,k+1)-pow(10,k)+1);
    	
    	hashed=(rand()*2654435761)%((int)pow(2,32));
    	randnum=pow(10,k)+hashed%randdiv-1;
    	
    	
    
    		if((alreadygen[k]!=randnum)&&(randnum>=0)){
    		
    			alreadygen[k]=randnum;
    			flag[k]=1;
    			printf("%d \n",randnum);
    			j++;
    
    
   		 }
   		 }
    
    
    
    
    
    
    }
  
 
    return 0; 
} 

