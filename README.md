# infogain

Entropy is calculated for the decision attribute (ex: 'class' in sample.csv) and the conditional entropy is calculated for each column against that decision attribute. Then the result of the conditional entropy is subtracted from the decision's entropy which gives use the Gain for that column.

## References

* http://christianherta.de/lehre/dataScience/machineLearning/decision-trees.php
* http://homes.cs.washington.edu/~shapiro/EE596/notes/InfoGain.pdf
* http://www.math.unipd.it/~aiolli/corsi/0708/IR/Lez12.pdf
* http://stackoverflow.com/questions/1859554/what-is-entropy-and-information-gain
* http://www.saedsayad.com/decision_tree.htm
