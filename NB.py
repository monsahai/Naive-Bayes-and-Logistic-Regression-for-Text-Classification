import os
import re
import math


if __name__ == "__main__":
    ham_dict = dict()
    spam_dict = dict()
    count_ham = 0
    count_spam = 0
    vocab = set()
    vocab_dict=dict()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    with os.scandir('C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_train/train/ham') as ham_folder:
            for ham_files in ham_folder:
                file1 = open(ham_files, 'r')
                lines = file1.readlines()
                for line in lines:
                    line = line.strip()
                    line = line.lower()
                    words = line.split(" ")
                    for word in words:
                        if (regex.search(word) == None):
                            if word in ham_dict:
                                ham_dict[word] = ham_dict[word]+1
                            else:
                                ham_dict[word] = 1
                            vocab.add(word)
                file1.close()
    ham_length = len(ham_dict)

    with os.scandir('C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_train/train/spam') as spam_folder:
            for spam_files in spam_folder:
                file2 = open(spam_files, 'r', encoding='latin-1')
                lines2 = file2.readlines()
                for line2 in lines2:
                    line2 = line2.strip()
                    line2 = line2.lower()
                    words2 = line2.split(" ")
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

    #Test the ham files from test folder and check if it's a spam or ham and record accuracy:
    with os.scandir(
            'C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_test/test/ham') as ham_folder_test:
        for ham_files_test in ham_folder_test:
            num_files_ham+=1
            nb_ham = math.log(340 / (123 + 340))
            nb_spam = math.log(123 / (123 + 340))
            file3 = open(ham_files_test, 'r')
            lines = file3.readlines()
            for line in lines:
                line = line.strip()
                line = line.lower()
                words = line.split(" ")
                c_word_ham=0
                c_word_spam=0
                for word in words:
                    p_ham=0
                    p_spam=0
                    if (regex.search(word) == None):
                        if word in ham_dict:
                            c_word_ham = ham_dict.get('word')
                        if word in spam_dict:
                            c_word_spam = spam_dict.get('word')
                        p_ham = math.log((c_word_ham + 1)/(ham_length + vocab_length))
                        p_spam = math.log((c_word_spam + 1) /(spam_length + vocab_length))
                    nb_ham = nb_ham+p_ham
                    nb_spam = nb_spam + p_spam
            if(nb_ham<nb_spam):
                error_ham+=1
            file3.close()
        error_ham_total= error_ham / num_files_ham
        print("Error in ham test folder:")
        print(error_ham_total*100)
        error_ham_total_acc = (num_files_ham - error_ham) / num_files_ham
        print("Accuracy in ham test folder:")
        print(error_ham_total_acc*100)

    error_spam = 0
    nb_ham=0
    nb_spam=0
    num_files_spam=0

    # Test the spam files from test folder and check if it's a spam or ham and record accuracy:
    with os.scandir(
            'C:/Users/monik/Documents/Docs_monika/UTD/Sem2/ML/Assignments/Assignement_3/assignment3_test/test/spam') as spam_folder_test:
        for spam_files_test in spam_folder_test:
            nb_ham = math.log(340 / (123 + 340))
            nb_spam = math.log(123 / (123 + 340))
            num_files_spam+=1
            counter = []
            file4 = open(spam_files_test, 'r')
            lines = file4.readlines()
            for line in lines:
                line = line.strip()
                line = line.lower()
                words = line.split(" ")
                counter.append(words)
                c_word_ham = 0
                c_word_spam = 0
                for word in words:
                    p_ham=0
                    p_spam=0
                    if word not in counter:
                        if (regex.search(word) == None):
                            if word in ham_dict:
                                c_word_ham = ham_dict.get('word')
                            if word in spam_dict:
                                c_word_spam = spam_dict.get('word')
                            p_ham = math.log((c_word_ham + 1) / (ham_length + vocab_length))
                            p_spam = math.log((c_word_spam + 1) / (spam_length + vocab_length))
                    nb_ham = nb_ham + p_ham
                    nb_spam = nb_spam + p_spam
            if (nb_ham > nb_spam):
                error_spam += 1
            file4.close()

        error_spam_total = error_spam / num_files_spam
        print("Error in spam test folder:")
        print(error_spam_total*100)
        error_spam_total_acc = (num_files_spam - error_spam) / num_files_spam
        print("Accuracy in spam test folder:")
        print(error_spam_total_acc*100)
        print("Overall Accuracy")
        accuracy = (num_files_spam - error_spam + num_files_ham - error_ham)/(num_files_ham + num_files_spam)
        print(accuracy*100)

