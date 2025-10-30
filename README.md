# Interval-vocabulary-learning
Interval vocabulary learning

This project is aimed at automating an interval approach to learning anything (for example, vocabulary in different languages or answers to questions). The main difference from the card-based approach is the possibility of using an infinite number of combinations (that is, not only pairs of values, but also triples/fours and so on). For example, it is convenient for learning the vocabulary of the Chinese language, since in addition to repeating the hieroglyph-translation pairs, you can add pinyin. The code uses the term 'word' to denote values, but it can be any combination of strings.

A .csv file is used as the data source, which must be filled in for your task (template in file_template.csv). Columns:

original_index - the number in order (index) for each combination

first_column, second_column, third_column <...> - rename them to suit your task (for example, 'word' and 'translation'). There are must be at least two columns with data, and as unlimited as possible (during combinations repetitions, the source column will be randomly selected from the specified ones, for the rest it is necessary to enter the corresponding value - this is how this program works)

status - when initially filling in, specify 1

updated - the date when the combination was added in the DD.MM.YYYY format.

When starting from the command line, specify the full path to the file .csv with data, a list of column names to repeat (separated by a space) and a limit of words/values to repeat (0 - if you need to repeat everything, or limit the number of combinations to repeat). When repeating, information is provided about how many combinations are left to repeat, which are correct or incorrect, and statistics at the end on the number of correct and incorrect answers.

How interval repetition works - about statuses. Each combination is given one of 10 statuses in the process of repeating them, each of which means how long ago you repeated it. If the answer is correct, the status of a particular combination increases by one until it reaches 10, which means that the combination has been learned. If the answer is incorrect, it is set to 1, which means that the combination must be learned again. Status values:

1 - a new word (repeat on this/the next day)

2 - repeat two days later

3 - repeat after a week

4 - repeat after two weeks

5 - repeat after a month

6 - repeat after two months

7 - repeat after three months

8 - repeat after six months 

9 - repeat after a year

10 - learned

After each repetition, the file .csv is overwritten, updating the status values of the combination, depending on your correct/incorrect answers. After the overwrittening, you can also add additional recordings by simply adding new combinations to the end of the file, or you can also manually make changes to existing recordings if you need to fix something.
