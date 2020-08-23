# Naive Bayes and Logistic Regression for Text Classification
 Naive Bayes and Logistic Regression for Text Classification(Spam/Ham)
Implemented and evaluated Naive Bayes and Logistic Regression for text classification. Used Python to implement the algorithms.

a. Downloaded the spam/ham (ham is not spam) dataset available on the elearning. 
  The data set is divided into two sets: training set and test set. 
  The dataset was used in the Metsis et al. paper [1]. 
  Each set has two directories: spam and ham. All files in the spam folders are spam messages and all files in the ham folder are legitimate (non spam) messages.

b. Implemented the multinomial Naive Bayes algorithm for text classification described here: http://nlp.stanford.edu/IR-book/pdf/13bayes.pdf.
    Note that the algorithm uses add-one Laplace smoothing. Did calculations in log-scale to avoid underflow. 
    Used the algorithm to learn from the training set and report accuracy on the test set.
 
c. Implemented the MCAP Logistic Regression algorithm with L2 regularization. Tried different values of λ. Used the algorithm to learn from the training set and reported accuracy on the test set for different values of λ. 
    Used gradient ascent for learning the weights. Did not run the gradient ascent until convergence; had put a hard limit on the number of iterations.

d. Improved the Naive Bayes and Logistic Regression algorithms by throwing away (i.e., filtering out) stop words such as \the" \of" and \for" from all the documents.
    A list of stop words can be found here: https://www.ranks.nl/stopwords. 
    Reported accuracy for both Naïve Bayes and Logistic Regression for this filtered set.