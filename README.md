# infogain

Entropy is calculated for the decision attribute (ex: 'class' in sample.csv) and the conditional entropy is calculated for each column against that decision attribute. Then the result of the conditional entropy is subtracted from the decision's entropy which gives use the Gain for that column.

## Sample

Using `sample.csv` for our sample data we get:

```
Parent (class):	0.918295834054
Gains:
age 	0.125814583694
income 	0.918295834054
```

The values of age are 1:~0.333, 2:0, 3:~0.45914. Income is just 0.

## References

* http://christianherta.de/lehre/dataScience/machineLearning/decision-trees.php
* http://homes.cs.washington.edu/~shapiro/EE596/notes/InfoGain.pdf
* http://www.math.unipd.it/~aiolli/corsi/0708/IR/Lez12.pdf
* http://stackoverflow.com/questions/1859554/what-is-entropy-and-information-gain
* http://www.saedsayad.com/decision_tree.htm
