x[0]=x0
tol=
i=0
while abs(x[i]-x[i+1])<tol:
        fx = df(x[i])
        dfx = ddf(x[i])
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton's method fails.")
        x[i + 1] = x[i] - fx / dfx
        i+=1