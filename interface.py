"""
Create an interface for user feedback during BCI data collection and training
The interface provides sample feedback to users based on their experience
    level and anxiety levels.
Additionally, the interface provides sample descriptions for LDA, SVM, and
    random forests. 
"""
from random import *

def main():
    done = False
    while not done:
        opts = ["Data Collection User Feedback",
                "Classifiaction Algorithm Explanations", "Quit"]
        choice = menu(opts)
        if choice == 1:
            user_feedback()
        if choice == 2:
            classification_explanation()
        if choice == 3:
            done = True

def menu(opts):
    #print the menu options
    for i in range(len(opts)):
        print("%d. %s" % (i+1, opts[i]))

    print("\nEnter integer corresponding to your choice ")
    #ask the user for their choice
    print()
    choice = input("your choice --> ")
    valid = False
    while(not valid):
        if choice not in ['1', '2', '3'] :
            print("please enter a positive integer...")
            print()
            choice = input("your choice --> ")
        else:
            valid = True
    return int(choice)

def user_feedback():
    """
    Determine whether user is advanced or novice
    Determine anxiety level of user
        Incorporate game-like feature into feedback
    """
    # Determine experience level and anxiety level of the user
    experience = input("Do you have experience with brain-computer interfaces? \
    Yes (Enter 1) or No (Enter 0):  ")
    anxiety = input("Are you feeling anxious? Yes (Enter 1) or No (Enter 0):  ")

    experience = int(experience)
    anxiety = int(anxiety)

    # For the purpose of the interface, we will randomly generate good signal
    # quality (1) and bad signal quality (0)
    # For future use, import your own function for signal quality
    signal_quality = randrange(0,2)
    print(signal_quality)


    #Feedback for User
    if experience == 1 and anxiety == 1:
        print("\nWe understand you are an experienced user with some feelings of \
        anxiety. \n")

        # More honest negative feedback, but still some positivity
        # for feelings of anxiety

        #Strong signal quality
        if signal_quality == 1:
            print("Your signal looked great. Keep doing what you're doing")

        #Poor signal quality
        if signal_quality == 0:
            print("Your signal wasn't quite right. Good try and keep going.")

    elif experience == 1 and anxiety == 0:
        print("\nWe understand you are an experienced user with no feelings of anxiety. \n")

        # Provide very honest feedback with a slight negative bias

        #Strong signal quality
        if signal_quality == 1:
            print("Good job, your signal is strong but can always be improved. Keep focusing on the task at hand.")

        #Poor signal quality
        if signal_quality == 0:
            print("Your signal wasn't clear. Try changing up your strategy.")

    elif experience == 0 and anxiety == 1:
        print("\nWe understand you are an inexperienced user with some feelings of anxiety. \n")

        # Incorporate positive feedback (only feedback when user does well)

        #Strong signal quality
        if signal_quality == 1:
            print("Your signal looked great, fantastic job! Keep doing what you're doing.")

        #Poor signal quality
        if signal_quality == 0:
            print("Good try. We think you will improve with practice.")


    elif experience == 0 and anxiety == 0:
        print("\nWe understand you are an inexperienced user with no feelings of anxiety. \n")

        # More honest negative feedback, but still some positivity
        # for inexperienced user

        #Strong signal quality
        if signal_quality == 1:
            print("Your signal looked great. Keep doing what you're doing.")

        #Poor signal quality
        if signal_quality == 0:
            print("Your signal wasn't quite right. Good try and keep going.")

    print("\n\n")


def classification_explanation():
    """
    Provide explanation of LDA, SVM, and Random Forest
    These are example classification method explanations because these are the
        classification methods we implemented in classification.py
    """
    print("\nWhich classifier did you use in your data analysis? \n")
    classification_methods = ["Linear Discriminant Analysis (LDA)",
        "Support Vector Machine (SVM)","Random Forest"]
    choice = menu(classification_methods)

    # LDA
    if choice == 1:
        description = """
        Linear Discriminant Analysis (LDA) is a common tool used within Machine
        learning to take an input that has multiple dimensions and classify
        this input into different groups of less dimensions. The most common use
        of LDA is within supervised classification problems. LDA can be used to
        model the differences between multiple classes by mapping features from
        a higher dimension to a lower dimension. The criteria for creating new
        axes in LDA is to maximize the distance between means of the two classes
        and minimize the variation within each class. Common applications of LDA
        include facial recognition and medical disease classification.
        """

    #SVM
    elif choice == 2:
        description = """
        Support Vector Machine (SVM) is a supervised machine learning algorithm
        which is used for classification of 2-or-higher dimensional data.
        SVM plots N-dimensional data and creates a hyperplane to classify the
        data into 2 groups. If the data needs to be classified into more than 2
        groups, then the algorithm creates a binary classifier for each class of
        the data. When the data is non-linearly separable, Kernalized SVM is used.
        The pros of SVM are that it performs well on a range of datasets and is
        versatile for high and low dimensional data while the cons are its
        efficiency and difficulty in interpreting why a classification decision
        was made.
        """

    # Random Forest
    elif choice == 3:
        description = """
        Random Forest uses results from a combination of decision trees to
        classify signals. Decision trees can be though about in a similar manner
        to a flow chart. This flow chart uses various characteristics of the
        input to determine which classifier the signal falls under. In order
        to classify the output based on the decision trees, random forest uses
        the majority voting classifier. Voting classifier is a machine learning
        model which uses a variety (ensemble) of models to predict a
        classification based on the highest probability classification
        specified by the models.
        """

    print(description)

main()

