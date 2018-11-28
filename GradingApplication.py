#A Program to grade three exam scores and print out its Average (35 is the Pass mark)
maths = int(input("Enter your math exam score here: "))
chemistry = int(input("Enter your chemistry exam score here: "))
physics = int(input("Enter your physics exam score here: "))

if maths >= 35 and chemistry >= 35 and physics >= 35 and maths <= 100 and chemistry <= 100 and physics <= 100:

    Average = (maths + chemistry + physics)/3

    if Average >= 35 and Average <= 59:
        print("Grade C")
    elif Average >= 60 and  Average <= 69:
        print("Grade B")
    elif Average > 69 and Average <= 100:
        print("Grade A")

    print("Your final Average is:- ", Average)

elif maths < 35 and chemistry < 35 and physics < 35:
        print("You have failed the three exams!")

elif maths < 35 and not chemistry < 35 and not physics < 35:
    print("You have failed the maths exams")

elif not maths < 35 and chemistry < 35 and not physics < 35:
    print("You have failed the chemistry exams")

elif not maths < 35 and not chemistry < 35 and physics < 35:
    print("You have failed the physics exams")

elif maths < 35 and chemistry < 35 and not physics < 35:
    print("You have failed the maths and chemistry exams")

elif not maths < 35 and chemistry < 35 and physics < 35:
    print("You have failed the chemistry and physics exams")

elif maths < 35 and not chemistry < 35 and physics < 35:
    print("You have failed the maths and physics exams")

else:

    print("Incorrect! Your Score can't be above 100!")





