coeff correl type =
SWITCH(TRUE,
        [coeff corr]=-1                          ,"Perfect negative correlation",
        [coeff corr]>-1   &&  [coeff corr]<=-0.8 ,"Very strong negative correlation",
        [coeff corr]>-0.8 &&  [coeff corr]<=-0.6 ,"Strong negative correlation",
        [coeff corr]>-0.6 &&  [coeff corr]<=-0.4 ,"Moderate negative correlation",
        [coeff corr]>-0.4 &&  [coeff corr]<=-0.2 ,"Weak negative correlation",
        [coeff corr]>-0.2 &&  [coeff corr]<0     ,"Very weak negative correlation",
        [coeff corr]=0                           ,"No correlation",
        [coeff corr]>0    &&  [coeff corr]<0.2   ,"Very weak positive correlation",
        [coeff corr]>=0.2 &&  [coeff corr]<0.4   ,"Weak positive correlation",
        [coeff corr]>=0.4 &&  [coeff corr]<0.6   ,"Moderate positive correlation",
        [coeff corr]>=0.6 &&  [coeff corr]<0.8   ,"Strong positive correlation",
        [coeff corr]>=0.8 &&  [coeff corr]<1     ,"Very strong positive correlation",
        [coeff corr]=1                           ,"Perfect positive correlation"
)