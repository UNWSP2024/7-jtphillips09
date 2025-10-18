# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)  

# --- Added code starts here ---
import math

def distance(coord1, coord2):
    """Return the distance between two 3D coordinates."""
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main():
    print("Enter two 3D coordinates (x, y, z).")

    try:
        # Get first coordinate
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        coord1 = (x1, y1, z1)

        # Get second coordinate
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        coord2 = (x2, y2, z2)

        # Call the distance function
        dist = distance(coord1, coord2)

        # Display the distance
        print(f"\nThe distance between {coord1} and {coord2} is {dist:.4f}")

    except ValueError:
        print("\nError: Please enter valid numeric values for coordinates.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# --- Added code ends here ---

# Call the main function.
if __name__ == '__main__':
    main()
