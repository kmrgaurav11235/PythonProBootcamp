enemies = 1

def increase_enemies():
    # enemies += 1 # Gives error -- UnboundLocalError: local variable 'enemies' referenced before assignment
    # enemies = 2 # This doesn't modifies the global "enemies" variables. It creates an entirely
    # different local variable "enemies".
    global enemies # This explicitly says that we have a global variable called "enemies" that is defined 
    # somewhere outside. That is the "enemies" that we want to use.
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}") 

# Global Constants: You define these once and never change them again.
# Naming convention: Use all caps for these
PI = 3.14159
URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

