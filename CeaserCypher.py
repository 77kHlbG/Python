#!/usr/bin/python -tt
import sys

# Define a main() function
def main():
 
  rotation=1

  # Get cyphertext from user
  cyphertext = input('Enter cyphertext: ')
  
  plaintext = cyphertext
  cyphertext = cyphertext.upper()
  
  print('\n')
  print('Performing Rotation Cypher...')
  
  # Repeats for all 25 possible rotations
  for rotation in range ( 1 , 26 ):

    # Rotates each character in cyphertext string
    for i in range( len( cyphertext ) ):
    
      # Use to skip non-alphabetic characters 
      if ord( cyphertext[i] ) + rotation >= 91:
        
        # Add 6 to skip non-alphabetic characters between Upper and Lower case 
        plaintext = plaintext[:i] + chr( ord( cyphertext[i] ) + rotation + 6 ).upper()
    
      # Increment character by rotation value    
      else:
    
        plaintext = plaintext[:i] + chr( ord( cyphertext[i] )+ rotation ).upper()
    
    # Print plaintext from each rotation
    print( 'ROT-' + str( rotation ) + ":" , plaintext )
    rotation = rotation + 1
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
