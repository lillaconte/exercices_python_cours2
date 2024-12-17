import time
#jai regardé cette video pour m'aider https://www.youtube.com/watch?v=nYDKH9fvlBY
#mais je crois que je ne comprends pas pourquoi on utilise args et kwargs
def chronometre(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func (*args, **kwargs)
        end = time.time()
        print(f"Temps mesuré par chronometre (en secondes) : {end - start:.6f} secondes")
        return result 
    return wrapper

@chronometre
def grosse_multiplication(multiplicateur):
    multiplicande = 1000000000000000*9999
    resultat = 0
    for i in range(1,multiplicateur):
        resultat += (multiplicande * multiplicateur *i)
    return  resultat

print(grosse_multiplication(56897*2))