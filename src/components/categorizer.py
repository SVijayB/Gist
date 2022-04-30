# Use this module to define the category the article belongs to.

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import re


def categorize(text):
    dataset = pd.read_csv("dataset/BBC News Train.csv")
    target_category = dataset["Category"].unique()
    dataset["CategoryId"] = dataset["Category"].factorize()[0]
    category = (
        dataset[["Category", "CategoryId"]].drop_duplicates().sort_values("CategoryId")
    )

    x = np.array(dataset.iloc[:, 0].values)
    y = np.array(dataset.CategoryId.values)
    cv = CountVectorizer(max_features=5000)
    x = cv.fit_transform(dataset.Text).toarray()
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=0, shuffle=True
    )
    classifier = RandomForestClassifier(
        n_estimators=100, criterion="entropy", random_state=0
    ).fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    y_pred1 = cv.transform([text])
    yy = classifier.predict(y_pred1)
    result = ""
    if yy == [0]:
        result = "Business News"
    elif yy == [1]:
        result = "Tech News"
    elif yy == [2]:
        result = "Politics News"
    elif yy == [3]:
        result = "Sports News"
    elif yy == [1]:
        result = "Entertainment News"
    print(result)


categorize(
    """A 24-year-old woman has sustained serious burn injuries after her stalker allegedly threw acid on her on Thursday night. The accused had been following her for years even after the victim had rejected his proposals to marry her. On Thursday, after the final rejection, he came prepared to teach her a lesson.
According to the police, a day before the accused had warned the victim of dire consequences if she didn't adhere to his demands. Scared of the repercussions of his threat, on Thursday morning she left home for work with her father.
But at night, when she may have been leaving, she saw the man on the staircases of her office, where he asked her to marry him again. When she again refused, he threw the acid on her and fled. He is still on the run and a hunt has been launched to find him.
According to police, the incident happened near the Sunkadakatte area of West Bengaluru, at the finance company where she worked.
The accused has been identified as Nagesh, a 27-year-old man who works in a garment factory. The victim has sustained burns on the face, neck, hands and head. She was rushed to a hospital and her condition is said to be stable, police said."""
)
