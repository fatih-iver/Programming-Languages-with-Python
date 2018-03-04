# Memofibo

# Submit via the interpreter a definition for a memofibo procedure that uses a
# chart. You are going to want the Nth value of the chart to hold the Nth
# fibonacci number if you've already computed it and to be empty otherwise.

chart = {}

def memofibo(n):
    if n in chart:
        return chart[n]
    else:
        if n <= 2:
            fib = 1
            chart[n] = fib
            return fib
        else:
            fib = memofibo(n-1) + memofibo(n-2)
            chart[n] = fib
            return fib
    # Quiz
    
    
print (memofibo(100))


