"""
=== Password Generator + Strength Checker ===

Features:
  - User parameters se password generate karo
  - Generated password ki strength check karo
  - Result display karo

---- Structure ----

Functions:
  - get_parameters()      → user se length, numbers, special chars lo
  - generate_password()   → parameters ke basis pe password banao
  - check_strength()      → password strength check karo (weak/medium/strong)
  - display_result()      → password aur strength formatted print karo
  - main()                → while loop + menu

---- Topics Covered ----
  - Functions       → har operation alag function
  - Strings         → password build karna, character check
  - Sets            → character pool banana
  - Loops           → password characters pick karna
  - Conditionals    → strength check logic
  - Error handling  → invalid length input
  - import          → random, string modules

---- Menu ----
  1) Generate Password
  2) Exit

---- Flow ----
  main() → user choice → get_parameters() → generate_password() 
         → check_strength() → display_result() → repeat

---- Strength Rules ----
  Weak   → length < 8  ya sirf letters
  Medium → length 8-12, numbers ya special chars mein se ek
  Strong → length > 12, numbers aur special chars dono

---- Validation Rules ----
  Length     → number hona chahiye, minimum 4
  Parameters → kam se kam ek character type selected hona chahiye
"""