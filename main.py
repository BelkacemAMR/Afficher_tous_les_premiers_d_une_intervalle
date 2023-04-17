def is_prime(num):
    """Fonction pour vérifier si un nombre est premier."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(x, y):
    """Fonction pour afficher les nombres premiers dans l'intervalle [x, y]."""
    print(f"Nombres premiers dans l'intervalle [{x}, {y}] :")
    for num in range(x, y + 1):
        if is_prime(num):
            print(num)


