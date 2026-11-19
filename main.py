print("=== STUDYLOG ===")

theme = input("¿Qué estudiaste hoy?")

try:
    minutes = int(input("¿Cuántos minutos estudiaste?"))
except ValueError:
    print("Error: Please enter a valid integer.")
else:    
    if minutes >0:
        print("Valid study time")
        print("\n--- SUMMARY ---")
        print(f"Studied topic {theme}")
        print(f"Study time: {minutes}")
        print("Completed!") 
    else:
        print("Invalid study time")
    


