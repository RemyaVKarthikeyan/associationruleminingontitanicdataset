# associationruleminingontitanicdataset
Applying apriori algorithm on titanic dataset for extracting association rules that contains 'Survived' on the RHS of the rule

#Dependencies
Python 3.11.4.0
Jupyter Notebook

Before applying apriori algorithm, the dataset must be converted into a list using data_prepare() in ARutils package

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/38c1019d-0441-4e4a-a459-b619bb5c32e7)

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/cb057c26-fe86-4d12-b71e-f3d4dd4e18e6)


Make the rules with given minimum values of support and confidence values. Here min support = 0.02 and min confidence =0.2

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/9b097c06-f7dc-494f-ac7c-17c21c92fd23)

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/c344844f-9da7-4fea-9ed0-b7a6c48aff7c)


Extracting the rules and writing it to a dataframe called rules_df. From rules_df , the association rules containing 'Survived' in the RHS is shortlisted to Survived_rules_df.

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/fd3a2eae-d01f-41a9-b53f-aa1d8705b72a)

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/f8f87625-03c7-47a5-9b95-bcfef750e79d)


Plotting the association rules contained 'Survived' in the RHS with hover over feature.
X axis= Support values
Y axis = Confidence values
Color scale 'agsunset' is used and the intensity is vaied accordance to the value of Lift

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/00806399-7fa5-4c2b-9bdf-9042238c5736)

![image](https://github.com/RemyaVKarthikeyan/associationruleminingontitanicdataset/assets/145346713/0528967e-887c-4624-bbc0-e13cf9ef5ccd)

