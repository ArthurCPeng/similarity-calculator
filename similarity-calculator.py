#Calculates the Dice coefficient and Jaccard coefficient (Intersection over Union) for two segmentation files
#By default, a value of '0' is considered to be 'no label' and is not included in calculations.
#The two masks must be of the same size and shape or an error will be raised. 


import os
import numpy as np
import nibabel
import sys

#Directory of the two masks to compare
mask1_dir = ''  
mask2_dir = ''

mask1 = nibabel.load(mask1_dir)
mask2 = nibabel.load(mask2_dir)

mask1 = np.array(mask1.get_data())
mask2 = np.array(mask2.get_data())

unique1, counts1 = np.unique(mask1, return_counts=True)
unique2, counts2 = np.unique(mask2, return_counts=True)


sum_counts1 = 0
sum_counts2 = 0
for count1 in counts1[1:]:
    sum_counts1 += count1
for count2 in counts2[1:]:
    sum_counts2 += count2


freq = 500 #Determines the frequency by which progress is reported. 

counts_intersect = 0 #The number of pixels/voxels with the same label in both segmentations.
counts_union = 0 #The number of pixels/voxels with a non-zero label in either segmentation. 
counts_dict = {}


for i in range(mask1.shape[0]):
    for j in range(mask1.shape[1]):
        for k in range(mask1.shape[2]):
            if k + mask1.shape[2] * j + mask1.shape[1] * mask1.shape[2] * i % freq == freq - 1:
                print((k + mask1.shape[2] * j + mask1.shape[1] * mask1.shape[2] * i) / (mask1.shape[0] * mask1.shape[1] * mask1.shape[2]))
            if mask1[i,j,k] == mask2[i,j,k] and mask1[i,j,k] != 0:
                counts_intersect += 1
                counts_union += 1
                label = mask1[i,j,k]
                
                if label in counts_dict.keys():
                    counts_dict[label] = counts_dict[label] + 1
                else:
                    counts_dict[label] = 1
                    
            if mask1[i,j,k] + mask2[i,j,k] != 0 and mask1[i,j,k] != mask2[i,j,k]:
                counts_union += 1

dice = (2 * counts_intersect) / (sum_counts1+sum_counts2)
jaccard = counts_intersect / counts_union

print("Dice coefficient is: {}".format(dice))
print("Jaccard coefficient is: {}".format(jaccard))
print("Intersection labels: {}".format(counts_dict))
