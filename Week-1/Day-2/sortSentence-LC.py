class Solution:
    def sortSentence(self, s: str) -> str:
        """ sort the sentence with prefix """
        sentence = s.split(" ")
        new_sentence: str = ""
        length: int = len(sentence)
        for index in range(length):
            for j in range(length - 1 - index):
                curr = sentence[j]
                nextw = sentence[j + 1]
                if int(curr[-1]) > int(nextw[-1]):
                    sentence[j], sentence[j + 1], = sentence[j + 1], sentence[j]
        for index in range(length):
            word_len = len(sentence[index]) - 1
            if index < length - 1:
                new_sentence += sentence[index][0:word_len] + " "
            else:
                new_sentence += sentence[index][0:word_len]
        return new_sentence
                
                