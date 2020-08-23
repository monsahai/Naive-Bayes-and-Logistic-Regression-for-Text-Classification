import os
import re
import math
import numpy as np
from scipy.special import expit
from nltk.corpus import stopwords
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def prob(k, d, w,vocab) -> int:
    m = 0
    sumi = 1
    for m in range(len(vocab)):
        sumi += d[k][m] * w[m]
    e = expit(sumi) / (1 + expit(sumi))
    return e

def test_files(vocab_dict) -> int:
    d1 = [[0 for i in range(len(vocab))] for i in range(478)]
    k=0
    count_ham=0
    count_spam=0
    with os.scandir(
            'C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_test/test/spam') as spam_folder_lg:
        for spam_files_lg in spam_folder_lg:
            sumi=1
            file6 = open(spam_files_lg, 'r')
            lines = file6.readlines()
            for line in lines:
                line = line.strip()
                line = line.lower()
                words = line.split(" ")
                words = [w for w in words if not w in stop_words]
                for word in words:
                    if (regex.search(word) == None):
                        if word in spam_dict_lg:
                            spam_dict_lg[word] = spam_dict_lg[word] + 1
                        else:
                            spam_dict_lg[word] = 1
            for word in spam_dict_lg:
                if (word in vocab_dict):
                    d1[k][vocab_dict[word]] += 1
            for m in range(len(vocab)):
                sumi += d1[k][m] * w[m]
            if (sumi>0):
                count_spam+=1
            else:
                count_ham+=1
            k += 1
            file6.close()
    return (count_spam/(count_spam+count_ham))


if __name__ == "__main__":
    ham_dict = dict()
    spam_dict = dict()
    count_ham = 0
    count_spam = 0
    vocab = set()
    vocab_dict=dict()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    stop_words = set(stopwords.words('english'))

    with os.scandir('C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_train/train/ham') as ham_folder:
            for ham_files in ham_folder:
                file1 = open(ham_files, 'r')
                lines = file1.readlines()
                for line in lines:
                    line = line.strip()
                    line = line.lower()
                    words = line.split(" ")
                    words= [w for w in words if not w in stop_words]
                    for word in words:
                        if (regex.search(word) == None):
                            if word in ham_dict:
                                ham_dict[word] = ham_dict[word]+1
                            else:
                                ham_dict[word] = 1
                            vocab.add(word)
                file1.close()
    ham_length = len(ham_dict)
    print(ham_length)

    with os.scandir('C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_train/train/spam') as spam_folder:
            for spam_files in spam_folder:
                #print(spam_files.name)
                file2 = open(spam_files, 'r', encoding='latin-1')
                lines2 = file2.readlines()
                for line2 in lines2:
                    line2 = line2.strip()
                    line2 = line2.lower()
                    words2 = line2.split(" ")
                    words = [w for w in words if not w in stop_words]
                    for word2 in words2:
                        if (regex.search(word2) == None):
                            if word2 in spam_dict:
                                spam_dict[word2] = spam_dict[word2]+1
                            else:
                                spam_dict[word2] = 1
                            vocab.add(word2)
                file2.close()
    spam_length = len(spam_dict)
    print(spam_length)
    vocab_length = len(vocab)
    print(vocab_length)
    nb_ham = math.log(340/(123+340))
    nb_spam = math.log(123/(123+340))
    error_ham = 0
    num_files_ham = 0
    vocab_dict=dict()

#Logistic Regression
    vocab1 = vocab
    sorted(vocab1)
    i=0
    spam_dict_lg=dict()
    d=[[0 for i in range(len(vocab))]for i in range(478)]
    w=[]
    k=0
    learning_rate= 0.1
    lamda = 0.001
    iteration = 100
    # for i in range(677):
    #     for j in range(len(vocab)):
    #         d.append(0)

    for word in vocab1:
        # vocab_dict.add(word)
        vocab_dict[word]=i
        w.append(1)
    with os.scandir(
            'C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_train/train/spam') as spam_folder_lg:
        for spam_files_lg in spam_folder_lg:
            # print(ham_files.name)
            file5 = open(spam_files_lg, encoding='latin-1')
            lines = file5.readlines()
            for line in lines:
                line = line.strip()
                line = line.lower()
                words = line.split(" ")
                words = [w for w in words if not w in stop_words]
                for word in words:
                    if (regex.search(word) == None):
                        if word in spam_dict_lg:
                            spam_dict_lg[word] = spam_dict_lg[word]+1
                        else:
                            spam_dict_lg[word] = 1
            for word in spam_dict_lg:
                if(word in vocab_dict):
                    d[k][vocab_dict[word]]+=1
            k += 1
        tempw=[]
        k=0
        file5.close()
        for it in range(iteration):
            for word in vocab:
                sumi1=0
                for p in range(478):
                    sumi1 = d[p][vocab_dict[word]] * (1 - prob( p, d, w, vocab))
                tempw.append(w[k] + learning_rate * sumi1 - learning_rate * lamda * w[k])
                k+=1
            w = np.array(tempw)
            print(w)
    count_accuracy = test_files(vocab_dict)
    print("Accuracy for test spam folder: ")
    print(count_accuracy)
















