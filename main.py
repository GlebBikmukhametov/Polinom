import random
def solve(coefficients):
    EPS=10**(-6)
    def palinom(x):
        summa=coefficients[0]*x+coefficients[1]
        for i in range(2,n):
            summa=summa*x+coefficients[i]
        return summa
    def binary_search(x1,y1,x2,y2):
        if (y1<y2):
            for j in range(300):
                x=(x1+x2)/2
                if palinom(x)<0:
                    x1=x
                else:
                    x2=x
            if (abs(palinom(x)<EPS)):
                return x
        for j in range(300):
            x = (x1 + x2) / 2
            if palinom(x) < 0:
                x2 = x
            else:
                x1 = x
        if (abs(palinom(x) < EPS)):
            return x

    n=len(coefficients)
    if (coefficients[0]==0):
        return "РЅРµРєРѕСЂСЂРµРєС‚РЅС‹Рµ РєРѕСЌС„С„РёС†РёРµРЅС‚С‹"
    if (n==2):
        return [-coefficients[1] / coefficients[0]]
    if (n==3):
        a=coefficients[0]
        b=coefficients[1]
        c=coefficients[2]
        D=b*b-4*a*c
        if (D<0):
            return []
        if (D==0):
            return [-b/(2*a), -b/(2*a)]
        return [(-b+D**0.5)/(2*a), (-b-D**0.5)/(2*a)]
    roots=[]
    coefficients_derivative =[]
    for i in range(n-1):
        coefficients_derivative.append(coefficients[i]*(n-i-1))
    extremums = solve(coefficients_derivative)
    extremums.sort()
    interesting_points = [-10**5]
    for elem in extremums:
        interesting_points.append(elem)
    interesting_points.append(10**5)
    i=0
    while(i<(len(interesting_points)-1)):
        x1=interesting_points[i]
        x2=interesting_points[i+1]
        y1=palinom(x1)
        y2=palinom(x2)
        if (abs(y1)<EPS):
            roots.append(x1)
            i+=1
            continue
        if (abs(y2)<EPS):
            roots.append(x2)
            i+=1
            continue
        if (y1*y2<=0):
            roots.append(binary_search(x1,y1,x2,y2))
        i+=1
    return roots

n=int(input())
coefficients= []
for i in range(n+1):
    a=int(input())
    coefficients.append(a*10)
roots=solve(coefficients)
roots.sort()
for root in roots:
    print(root)
