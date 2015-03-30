
glowfi.sh the Pythonic Way: Now with machine guns and rocket launchers.
-----------

**Installation**

    pip install glowfi.sh

**Setup**

    from glowfish import glowfish
    glower = glowfish.Glower('<GLOWFISH_SID>', '<GLOWFISH_AUTH_TOKEN>')

**Useage**

Get ready for some simple machine learning...

*Training*

    response = glower.train({ # the data set
	    'feature_name1': [1, 2, 3, 4, ...etc],
	    'feature_name2': [9, 4, 5, 6, ...etc]
    }, { # the response set
	    'class': [4, 3, 5, 6, ...etc]
    })

*Training using CSVs*

    response = glower.train_csv('./data_set.csv', './response.csv')

*Predict*
It's important to note that predicting will throw an error if you have not trained against a data set first.

    response = glower.predict({ # the data set
	    'feature_name1': [1, 2, 3, 4, ...etc],
	    'feature_name2': [9, 4, 5, 6, ...etc]
    })
    
*Predict using CSVs*

    response = glower.predict_csv('./data_set.csv')

*Clustering*

    response = glower.cluster({ # the data set
	    'feature_name1': [1, 2, 3, 4, ...etc],
	    'feature_name2': [9, 4, 5, 6, ...etc]
    })

*Clustering using CSVs*

    response = glower.cluster_csv('./data_set.csv')

*Feature Selection*

    response = glower.feature_select({ # the data set
	    'feature_name1': [1, 2, 3, 4, ...etc],
	    'feature_name2': [9, 4, 5, 6, ...etc]
    }, { # the response set
	    'class': [4, 3, 5, 6, ...etc]
    })
    
*Feature Selection using CSVs*

    response = glower.feature_select_csv('./data_set.csv', './response.csv')
    
*Filter Train*
    # userids, productids, then ratings
    response = glower.filter_train(userids=[1, 2, 3, 4, ...etc],productids=[1, 2, 3, 4, ...etc],ratings=[1, 2, 3, 4, ...etc])
    
*Filter Predict*
    # userids, productids, then ratings
    response = glower.filter_predict(userids=[1, 2, 3, 4, ...etc],productids=[1, 2, 3, 4, ...etc],ratings=[1, 2, 3, 4, ...etc])

**CSV File Format**

*Data Set*

    Feature 1, Feature 2, Feature 3,
    1, 2, 3,
    4, 5, 6,
    7, 8, 9

*Response Set*

    Response Key
    1
    2
    3

**Further Documentation**

Docs - http://glowfish.readme.io/  
Registration - http://glowfi.sh/
