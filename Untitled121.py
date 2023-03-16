#!/usr/bin/env python
# coding: utf-8

# # question 01
What are the three measures of central tendency?
The three measures of central tendency are:

Mean: The mean is the sum of all the data values divided by the total number of data values in the dataset. It is also known as the arithmetic mean or the average.

Median: The median is the middle value in an ordered list of data values. It is the value that separates the lower 50% of the data from the upper 50% of the data.

Mode: The mode is the most frequent value in a dataset. It is the value that occurs most often in the dataset. If two or more values occur with equal frequency, then the dataset is said to be bimodal or multimodal.
# # question 02
Q2. What is the difference between the mean, median, and mode? How are they used to measure the
central tendency of a dataset?
Mean, median, and mode are measures of central tendency used to describe the typical value or the center of a dataset. The main differences between these measures are:

Mean: The mean is the sum of all the data values divided by the total number of data values in the dataset. It represents the average value of the dataset. The mean is sensitive to extreme values or outliers, which can skew the mean in one direction or another. The mean is a commonly used measure of central tendency because it takes into account all the data values in the dataset.

Median: The median is the middle value in an ordered list of data values. It represents the value that separates the lower 50% of the data from the upper 50% of the data. The median is a robust measure of central tendency that is less sensitive to extreme values or outliers than the mean. The median is often used to describe the typical value or the center of the data distribution, particularly when the data is skewed.

Mode: The mode is the most frequent value in a dataset. It represents the value that occurs most often in the dataset. If two or more values occur with equal frequency, then the dataset is said to be bimodal or multimodal. The mode is useful for describing the most common value or category in a dataset, particularly for nominal or categorical data.

The choice of measure of central tendency depends on the nature of the data and the research question. The mean is useful when the data is normally distributed or symmetrically distributed. The median is useful when the data is skewed or when there are outliers. The mode is useful for describing the most common value or category in a dataset, particularly for nominal or categorical data.

In summary, mean, median, and mode are important measures of central tendency used to describe the typical value or the center of a dataset. Depending on the nature of the data and the research question, different measures may be more appropriate for summarizing and describing the dataset.
# # question 03
Measure the three measures of central tendency for the given height data:
[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
To calculate the measures of central tendency for the given height data, we can use the following formulas:

Mean:

$$\overline{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

where $\overline{x}$ is the mean, $x_i$ is the $i$-th value in the dataset, and $n$ is the total number of values in the dataset.

Median:

If the dataset has an odd number of values, the median is the middle value when the values are ordered from smallest to largest. If the dataset has an even number of values, the median is the average of the two middle values.

Mode:

The mode is the most frequent value in the dataset.

Using these formulas, we can calculate the measures of central tendency for the given height data:

Mean:

$$\overline{x} = \frac{178 + 177 + 176 + 177 + 178.2 + 178 + 175 + 179 + 180 + 175 + 178.9 + 176.2 + 177 + 172.5 + 178 + 176.5}{16} = 176.90625$$

Therefore, the mean height is approximately 176.91 cm.

Median:

First, we need to order the values from smallest to largest:

[172.5, 175, 175, 176, 176.2, 176.5, 177, 177, 178, 178, 178, 178.2, 178.9, 179, 180]

The dataset has an even number of values, so the median is the average of the two middle values:

$$\text{median} = \frac{177+178}{2} = 177.5$$

Therefore, the median height is 177.5 cm.

Mode:

There are two values that occur most frequently in the dataset: 177 and 178. Therefore, the dataset is bimodal.

Therefore, the mode of the height data is 177 and 178 cm.
# # question 04
Q4. Find the standard deviation for the given data:
[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
To find the standard deviation for the given data, we can use the following formula:

$$\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \overline{x})^2}{n-1}}$$

where $\sigma$ is the standard deviation, $x_i$ is the $i$-th value in the dataset, $\overline{x}$ is the mean of the dataset, and $n$ is the total number of values in the dataset.

First, we need to calculate the mean of the dataset:

$$\overline{x} = \frac{178 + 177 + 176 + 177 + 178.2 + 178 + 175 + 179 + 180 + 175 + 178.9 + 176.2 + 177 + 172.5 + 178 + 176.5}{16} = 176.90625$$

Next, we can calculate the sum of the squared differences between each value and the mean:

$$(178-176.90625)^2 + (177-176.90625)^2 + \cdots + (176.5-176.90625)^2 = 100.6953125$$

Then, we can divide this sum by $n-1$ (which is 15, since there are 16 values in the dataset):

$$\frac{100.6953125}{15} = 6.7130208$$

Finally, we can take the square root of this result to get the standard deviation:

$$\sigma = \sqrt{6.7130208} \approx 2.5909$$

Therefore, the standard deviation of the given data is approximately 2.59 cm.
# # question 05
How are measures of dispersion such as range, variance, and standard deviation used to describe
the spread of a dataset? Provide an example.
Measures of dispersion such as range, variance, and standard deviation are used to describe the spread of a dataset by quantifying how much the individual data points deviate from the central tendency of the data.

Range: Range is a simple measure of dispersion that indicates the difference between the highest and lowest values in the dataset. It is useful for quickly getting an idea of how spread out the data is. However, it can be affected by outliers and doesn't take into account the distribution of the data. For example, if we have a dataset of ages of students in a classroom ranging from 16 to 18 years old, the range would be 2 years.

Variance: Variance is a measure of how much the data points deviate from the mean. It is calculated by squaring the differences between each data point and the mean, summing these values, and dividing by the total number of data points. A higher variance indicates that the data points are more spread out from the mean. However, variance is measured in squared units and can be difficult to interpret. For example, if we have a dataset of test scores ranging from 70 to 90 and the variance is calculated to be 36, this means that the average squared difference between each score and the mean is 36.

Standard deviation: Standard deviation is a measure of how much the data points deviate from the mean, similar to variance. However, standard deviation is the square root of variance and is measured in the same units as the data. It is useful because it provides a standardized measure of the spread of the data, making it easier to interpret and compare across datasets. A higher standard deviation indicates that the data points are more spread out from the mean. For example, if we have a dataset of weights of apples ranging from 100 to 120 grams and the standard deviation is calculated to be 3, this means that the majority of the apples weigh between 97 and 103 grams (one standard deviation from the mean).

In summary, measures of dispersion are used to provide information about the spread of data and how much the individual data points deviate from the central tendency. They are important for understanding the variability and distribution of data, and for making comparisons between different datasets.

# # question 06
Q6. What is a Venn diagram?
A Venn diagram is a graphical representation of the relationships between different sets of data. It consists of overlapping circles or other shapes, with each circle representing a set and the overlap between circles representing the intersection of those sets. Venn diagrams are commonly used in mathematics and statistics to illustrate set theory concepts, such as union, intersection, and complement.

Venn diagrams are useful for visualizing the relationships between sets and determining the number of elements in each set or subset. They can also be used to compare and contrast different groups or categories, such as the characteristics of two different products or the preferences of different demographic groups.

For example, consider a Venn diagram showing the relationship between three sets: A, B, and C. If A represents all apples, B represents all bananas, and C represents all oranges, the overlap between A and B represents apples that are also bananas, the overlap between B and C represents bananas that are also oranges, and the overlap between A and C represents apples that are also oranges. The center of the Venn diagram, where all three circles overlap, represents items that belong to all three sets, in this case, fruits that are apples, bananas, and oranges.
# # question 07
Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
(i) A B
(ii) A ⋃ B
(i) A B refers to the set of elements that are common to both A and B. In this case, the common elements are 2 and 6, so A B = {2, 6}.

(ii) A ⋃ B refers to the set of elements that belong to either A or B, or both. The union of A and B is {0, 2, 3, 4, 5, 6, 7, 8, 10}.
# # question 08
What do you understand about skewness in data?
In statistics, skewness is a measure of the asymmetry of a probability distribution or a dataset. A dataset or probability distribution is said to be skewed if it is not symmetric, that is, if it has more values on one side of the center than the other side.

There are two types of skewness: positive and negative. Positive skewness occurs when the tail of the distribution extends to the right and the peak of the distribution is towards the left. Negative skewness occurs when the tail of the distribution extends to the left and the peak of the distribution is towards the right.

Skewness can be measured using the skewness coefficient or skewness index, which is a statistical measure of the degree of asymmetry of a dataset. The skewness coefficient can be positive, negative or zero, depending on the direction and degree of skewness.

Skewness is important in data analysis because it affects the interpretation of certain statistical measures such as the mean, median, and mode. When a dataset is skewed, the mean is affected by the outliers on the skewed side of the distribution, while the median is less affected by outliers and provides a better measure of central tendency. Understanding skewness can help in selecting the appropriate statistical measures and methods for analyzing and interpreting the data.




# # question 09
If a data is right skewed then what will be the position of median with respect to mean?
If a dataset is right-skewed, then the mean will be greater than the median. This is because the skewness is caused by a few very high values in the dataset, which pull the mean towards the right or higher end of the distribution. The median, on the other hand, is less affected by extreme values and is a better measure of central tendency for skewed datasets. Therefore, the median will be closer to the center of the dataset, which is usually towards the left or lower end of the distribution in a right-skewed dataset.
# # question 10
Explain the difference between covariance and correlation. How are these measures used in
statistical analysis?
Covariance and correlation are both measures of the relationship between two variables in a dataset, but they differ in the way they are calculated and interpreted.

Covariance is a measure of how two variables vary together. It measures the degree to which two variables change in relation to each other. A positive covariance indicates that two variables tend to move in the same direction, while a negative covariance indicates that they tend to move in opposite directions. However, the magnitude of the covariance is not standardized and depends on the scale of the variables. Therefore, it is difficult to compare covariances between datasets with different scales.

Correlation, on the other hand, is a standardized measure of the relationship between two variables. It measures the degree to which two variables are linearly related. Correlation ranges from -1 to 1, where a correlation of 1 indicates a perfect positive linear relationship, a correlation of -1 indicates a perfect negative linear relationship, and a correlation of 0 indicates no linear relationship. Correlation is a more useful measure than covariance because it can be compared between datasets with different scales.

Both covariance and correlation are used in statistical analysis to understand the relationship between two variables. For example, they can be used to determine whether there is a relationship between a person's age and their income, or between a student's study time and their exam score. Covariance and correlation can help identify trends, patterns, and associations in the data, which can be useful for making predictions and making decisions based on the data.
# # question 11
What is the formula for calculating the sample mean? Provide an example calculation for a
dataset.
The formula for calculating the sample mean is:

Sample Mean = (Sum of all values in the sample) / (Number of values in the sample)

Here's an example calculation:

Suppose we have a dataset of 5 test scores: 85, 90, 92, 88, and 95. We want to find the sample mean.

Sample Mean = (85 + 90 + 92 + 88 + 95) / 5

Sample Mean = 450 / 5

Sample Mean = 90

Therefore, the sample mean of this dataset is 90.
# # question 12
For a normal distribution data what is the relationship between its measure of central tendency?
For a normal distribution, the mean, median, and mode are all equal. In other words, they have the same value and are located at the center of the distribution. This is because the normal distribution is symmetric, with data points evenly distributed around the mean. Therefore, the three measures of central tendency coincide and provide the same information about the location of the center of the distribution.
# # question 13
How is covariance different from correlation?
Covariance and correlation are both measures of the relationship between two variables, but they differ in their interpretation and scaling.

Covariance is a measure of how much two variables vary together. It is calculated by taking the average of the product of the deviations of each variable from its mean. Covariance can take on any value, positive or negative, and its magnitude indicates the strength of the relationship between the variables. However, the scale of the covariance depends on the units of the variables, which makes it difficult to compare covariances across different data sets.

Correlation, on the other hand, is a standardized measure of the relationship between two variables. It is calculated by dividing the covariance of the variables by the product of their standard deviations. Correlation takes on values between -1 and 1, with a correlation of 1 indicating a perfect positive relationship, a correlation of -1 indicating a perfect negative relationship, and a correlation of 0 indicating no relationship between the variables. Correlation is unitless and can be compared across different data sets.

In summary, covariance measures the strength and direction of the relationship between two variables, while correlation measures the strength and direction of the relationship in a standardized way that is independent of the units of the variables.
# # question 14
How do outliers affect measures of central tendency and dispersion? Provide an example.
Outliers can have a significant impact on measures of central tendency and dispersion.

Measures of central tendency, such as the mean and median, are affected by outliers because they are based on the values of all the data points. If an outlier is very large or very small compared to the other values, it can pull the mean in its direction, making it no longer representative of the typical value. The median is less sensitive to outliers, as it is the value that separates the upper and lower halves of the data set, but extreme outliers can still affect it.

Measures of dispersion, such as the range, interquartile range, and standard deviation, can also be affected by outliers. Outliers can increase the range, making it appear that the data set is more spread out than it actually is. The interquartile range is less affected by outliers, as it only considers the middle 50% of the data, but extreme outliers can still have an impact. The standard deviation is highly affected by outliers, as it takes into account the distance between each data point and the mean.

For example, suppose we have the following data set representing the ages of a group of people: 20, 22, 25, 27, 28, 30, 35, 37, 40, 42, 45, 50, 55, 60, 65. The mean age is 37, the median age is 37, the range is 45, and the standard deviation is 16.2. If we add an outlier of 100 to the data set, the mean age becomes 44.6, the median age remains 37, the range becomes 80, and the standard deviation increases to 31.6. This shows how the outlier can greatly affect the mean and standard deviation, while having little effect on the median and range.