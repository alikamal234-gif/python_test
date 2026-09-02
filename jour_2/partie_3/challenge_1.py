text_1 = "Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable. This form of analysis estimates the"
text_2 = "Logistic regression is a supervised machine learning algorithm widely used for binary classification tasks, such as identifying whether an email is spam or not and diagnosing diseases by assessing the presence or absence of specific conditions based on patient test results. This approach utilizes the logistic"

mots_commun = list(set(text_1.lower().split()) & set(text_2.lower().split()))
resultat = [ x for x in mots_commun if len(x) >= 3]
print(resultat)
