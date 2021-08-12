# similarity-calculator
A program to calculate the similarity metrics (Dice coefficient, Jaccard coefficient) of two image segmentation files.  

## Note: 
- Segmentation files should be in .nii.gz format in order to be read by nibabel. 
- By default, a value of '0' is considered to be 'no label' and is not included in calculations. 
- The two segmentation files must be of the same size and shape or an error will be raised. 
