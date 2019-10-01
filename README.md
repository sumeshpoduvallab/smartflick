# smartflick

## Summary
Have you ever had to answer “What movie should I watch next?” question at least once when you came home from work? The need to build robust movie recommendation systems is extremely important given the huge demand for personalized content of modern consumers.
Popular streaming service like Netflix estimate the likelihood that you will watch a particular title in our catalog based on a number of factors including:
* your interactions with our service (such as your viewing history and how you rated other titles)
* other members with similar tastes and preferences on our service, and
* information about the titles, such as their genre, categories, actors, release year, etc.

SmartFlick should recommend movies to viewer based on their past likings. SmartFlick will find similar movies to a given movie and then recommend those similar movies to the viewer.

## Requirements
* SmartFlick will collect list of movies viewer liked recently.
* SmartFlick will recommend movies similar to viewers previous likings.
* [Nice to do] SmartFlick will recommend movies from all genres (equally distributed).

## Design Theory

Our objective is to build SmartFlick which is a content based recommendation engine. So, we need to find similar movies to a given movie and then recommend those similar movies to the user.
How can we find the similarity between 2 movies? We need vector representation of these movies. Now we can say that two vectors are similar if the distance (angular distance) between them is small. Further from the machine learning perspective, we can understand that the value of cos θ makes more sense to us rather than the value of theta. Based on the above we can find similarity between contents.
This is how we can achieve the above:
* Combine the values of columns keywords, cast, genres, director into single string.
* Feed these combines string to get the count matrix.
* Obtain the cosine similarity matrix from the count matrix
* Our next step is to get the title of the movie that the user currently likes.
* Then we will find the index of that movie. After that, we will access the row corresponding to this movie in the similarity matrix. Thus, we will get the similarity scores of all other movies from the current movie.
* Then we will enumerate through all the similarity scores of that movie to make a tuple of movie index and similarity score. This will convert a row of similarity scores 

## Tools

Our objective is to build SmartFlick which is a content based recommendation engine. So, we need to find similar movies to a given movie and then recommend those similar movies to the user.
How can we find the similarity between 2 movies? We need vector representation of these movies. Now we can say that two vectors are similar if the distance (angular distance) between them is small. Further from the machine learning perspective, we can understand that the value of cos θ makes more sense to us rather than the value of theta. Based on the above we can find similarity between contents.
In order to implement we will use Python, scikit-learn library, pandas, numpy.
* Scikit-learn library will help with
* * way to represent these texts as vectors
* * calculate cosine similarity for similarity matrix.
* Pandas will help with
* * read dataset csv

## Risk Retirement

* Training Constrains
I have to gather and prepare data, then train the algorithm. There are much more uncertainties.
* * Mitigation Plan : Starting early and solving the core/complex pieces at the beginning will help mitigate uncertainties. Also, early implementation allow more time to train the model or we could use GPU resources available through BU.

* Black box problem
I might able to understand how a single prediction was made, it is very difficult to understand how the whole model works.
* * Mitigation Plan : Adequate testing

* Data
Not having enough data and/or having bad data can bring enormous risk to any modeling process, but really comes into play with machine learning.

* * Mitigation Plan : For this project I could rely on the sample data found online.

* New to Machine Learning
Me being new to the machine learning world, I might not have full understanding of how I’m suppose to solve certain core problems, which could lead to incompletion or incorrect results.

* * Mitigation Plan : I’ll try to involve the instructors early and often to guide me to the right direction.

* Bias
As susceptible as any system to the “garbage in, garbage out” syndrome. In the case of self-learning systems, the type of “garbage” is biased data. Left unchecked, feeding biased data to self-learning systems can lead to unintended outcomes.
* * Mitigation Plan : I’ll try to eliminate the problematic data, by keeping only relevant data.

## HOW SUCCESS WILL BE ASSESSED

Using just one error metric can give us a limited view of how these systems work. We should always try to evaluate with different methods

* Traditional Metrics : For SmartFlick predictive models with algorithms that, generally, are looking to minimize the error of a function. Hence it is important to measure the prediction error they have comparing the expected results with the ones the model gives as an output.
* Root Mean Square Error (RMSE) is the standard deviation of the residuals (prediction errors). Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread out these residuals are.
* Mean Squared Error (MSE) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors; that is, the average squared difference between the estimated values and the actual value.
* Mean Absolute Error (MAE) is a measure of difference between two continuous variables. Assume X and Y are variables of paired observations that express the same phenomenon.



