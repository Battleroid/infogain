# infogain

Entropy is calculated for the decision attribute (ex: 'class' in sample.csv) and the conditional entropy is calculated for each column against that decision attribute. Then the result of the conditional entropy is subtracted from the decision's entropy which gives use the Gain for that column.
