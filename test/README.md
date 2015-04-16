glowfi.sh python wrapper demo instructions
-----------

Here we will use sample user-movie rating data to train a glowfi.sh recommendation model (using 0-5 ratings) and then ask glowfi.sh to predict the movie ratings for 20 new users and compare those to actual recorded ratings for accuracy.

More info on the MovieLens data set is [here](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt).

We assume Python 2.x and pip are installed already. If not, the folowing links below give 1 line install instructions for both: 
[Install for Python on Windows](https://www.python.org/downloads/windows/) and 
[Install for PIP on Windows](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows).

**Steps for glowfi.sh Python Demo**

*1. install glowfish from PyPi:*

    pip install glowfish

*2. startup python interactive shell (in the same directory as movie_rating_train.json):*

    python

*3. To train the glowfi.sh model, enter the following lines:*

    import json
    import glowfish.glowfish as glowfish
    glower = glowfish.Glower(<auth key>,<auth secret key>)
    train_data = json.load(open('movie_rating_train.json'))
    train_return = glower.filter_train(train_data['data_set']['userid'],train_data['data_set']['productid'],
        train_data['data_set']['rating'])
    print train_return

*4. You should see the following print out:*

    {u'status': {u'status': u'SUCCESS', u'code': u'200.0', u'codeMessage': u'Api completed successfully'},
    u'result': {u'metrics': {u'rows': 80000, u'time': u'2.62 sec'}, u'model_status': u'updated_existing'}}

*5. Now run glowfi.sh prediction file to get estimated rating for 20 new users:*

    predict_data = json.load(open('movie_rating_prediction.json'))
    predict_return = glower.filter_predict(predict_data['data_set']['userid'],predict_data['data_set']['productid'],
        predict_data['data_set']['rating'])
    print predict_return

*6 You should see the following return from glowfi.sh "print predict_train":*

    {u'status': {u'status': u'SUCCESS', u'code': u'200.0', u'codeMessage': u'Api completed successfully'},
    u'result': {u'metrics': {u'rows': 20, u'time': u'0.55 sec'},
    u'predictions': {u'rmse_best': 1.1372652398974326, u'mae_best': 0.94, u'predictions': [4.115536580593806, 
        3.0373570509411114, 3.01191464889828, 3.4511459029840914, 3.163741539386915, 3.4648457452920924, 3.5163270846791916,
        4.022362015581322, 3.5763795626559816, 3.4838059087502207, 3.837655505048551, 3.3454290113185876, 2.883796523224529,
        4.035645217486952, 2.5771215401952916, 4.08059468678164, 3.1688319000154226, 3.2668625899622885, 3.9314662744373345,
        2.4121369232352645],
    u'mae_mean_rating': 1.11, u'rmse_mean_rating': 1.3655721804330099}}}

The "predictions"["predictions"] key shows the estimated ratings for the 20 userids passed to glowfi.sh from  'movie_rating_prediction.json'. The "predictions"["mae_best"] key gives the error of our estimated ratings compared to actual user ratings in 'movie_rating_prediction.json' (0.94 Stars out of 5 stars).
