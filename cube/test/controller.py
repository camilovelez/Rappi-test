from django.http import JsonResponse


UPDATE_COMMAND='UPDATE'
QUERY_COMMAND='QUERY'

def operate_cube(request):
    STDIN = request.POST['input'].split() #split string into a list
    T=int(STDIN[0])
    i=1
    error=''
    STDOUT=list()
    for t in range(T):
        inputs_list=list()
        N=int(STDIN[i])
        cube=[[[0 for z in range(N)] for y in range(N)] for x in range(N)]
        M=int(STDIN[i+1])
        i+=2
        for m in range(M):
            if(STDIN[i]==UPDATE_COMMAND):
                x,y,z,W=int(STDIN[i+1]),int(STDIN[i+2]),int(STDIN[i+3]),int(STDIN[i+4])
                if(max(x,y,z)<=N):
                    inputs_list.append([x,y,z,W])
                    cube[x-1][y-1][z-1]=W
                    i+=5
                else:
                    error='At least of one your inputs is bigger than the size of the cube'
                    return JsonResponse(error, safe=False)
                
            elif(STDIN[i]==QUERY_COMMAND):
                x1,y1,z1=int(STDIN[i+1]),int(STDIN[i+2]),int(STDIN[i+3])
                x2,y2,z2=int(STDIN[i+4]),int(STDIN[i+5]),int(STDIN[i+6])
                if(max(x2,y2,z2)<=N):
                    STDOUT.append(query_cube(inputs_list,x1, y1, z1,x2,y2,z2))
                    ''' STDOUT.append(query_cube(cube,x1, y1, z1,x2,y2,z2)) '''
                    i+=7
                else:
                    error='At least of one your inputs is bigger than the size of the cube'
                    return JsonResponse(error, safe=False)
                
                
            else:
                error='Please check your input structure, at least one operation row seems to be out of the standard for such rows'
                return JsonResponse(error, safe=False)

    return JsonResponse(STDOUT, safe=False)

def query_cube(inputs_list,x1, y1, z1,x2,y2,z2):
    query_sum=0
    for inp in inputs_list:
        if (inp[0]<=x2 and inp[0]>=x1 and inp[1]<=y2 and inp[1]>=y1 and inp[2]<=z2 and inp[2]>=z1):
            query_sum+=inp[3]
    return query_sum

''' def query_cube(cube,x1, y1, z1,x2,y2,z2):
    query_sum=0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            for k in range(y1-1,y2):
                query_sum+=cube[i][j][k]
    return query_sum '''