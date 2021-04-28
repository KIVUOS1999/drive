#include<stdio.h>
#include<time.h>
# define V 6

int issafe(int graph[V][V], int r, int c, int*color)
{
	int i;
    for(i=0;i<V;i++)
        if(graph[r][i] && c == color[i])
            return 0;
        return 1;
}

int graphcoloringuntil(int graph[V][V], int m, int r, int*color)
{
	int i,c;
    if(r==V)
        return 1;
    
    for(c = 1;c<=m;c++)
    {
        if(issafe(graph, r, c, color))
        {
            color[r] = c;

            if(graphcoloringuntil(graph, m,r+1, color)==1)  
                return 1;
            color[r] = 0; 
        }
    }
    return 0;
}

int graphcoloring(int graph[V][V], int m)
{
    int color[V],i;
    for(i=0;i<V;i++)
        color[i] = 0;
    
    if (graphcoloringuntil(graph, m, 0, color) == 0) 
    { 
      printf("Solution does not exist"); 
      return 0; 
    } 

    printf("Solution Exists:"
            " Following are the assigned colors \n"); 
    for (i = 0; i < V; i++) 
      printf(" %d-%d ", i+1,color[i]); 
    printf("\n"); 
    return 1;
}

int main()
{
    int graph[V][V] = {
        {0, 1, 0, 0,0,1}, 
        {1, 0, 1, 0,0,1}, 
        {0, 1, 0, 1,1,0}, 
        {0, 0, 1, 0,1,0},
        {0,0,1,1,0,1},
        {1,1,0,0,1,0}
    }; 
    int m = 3; 
    graphcoloring(graph,m);
    return 0;
}
