glowfi.sh python quick analytics demo instructions
-----------

Here we will use sample bank marketing data set (with survey answers as string, int, and float features) to train a glowfi.sh predictive model to determine whether a prospective client is likely ("yes") or not ("no") to buy a new service. Then we will ask glowfi.sh to predict whether clients that are new are likely to adopt this service and compare those to actual recorded survey results for accuracy.

More info on the bank marketing data set is [here](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).

We assume Python 2.x and pip are installed already. If not, the folowing links below give 1 line install instructions for both: 
[Install for Python on Windows](https://www.python.org/downloads/windows/), [Install for PIP on Windows](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows), and [Install for *nix](https://pip.pypa.io/en/latest/installing.html).

**Steps for glowfi.sh Python Analytics Demo**

*1. Download [bank_profile_train.json](https://raw.githubusercontent.com/glowfishAPI/glowfish-py/master/quick_analytics_demo/bank_profile_train.json) and [bank_profile_predict.json](https://raw.githubusercontent.com/glowfishAPI/glowfish-py/master/quick_analytics_demo/bank_profile_predict.json). (right-click on the links to download)*

*2. Install latest glowfish from PyPI:*

    pip install glowfi.sh --upgrade

*3. Startup python interactive shell (in the same directory as downloaded json files):*

    python

*4. To train the glowfi.sh model with 37000+ client "yes"/"no" responses, enter the following lines:*

    import json
    import glowfish.glowfish as glowfish
    glower = glowfish.Glower("<auth key>","<auth secret key>")
    glower.reset_model = "true"  #Specifies new learning model
    train_data = json.load(open('bank_profile_train.json'))
    train_return = glower.train(train_data['data_set'],train_data['response'])
    print train_return
    
Note: The "auth key" and "auth secret key" are located at the top of your app page in [your glowfi.sh app admin panel](https://api.glowfi.sh/admin/app/). If you do not have access to glowfi.sh yet, please [request access here](https://glowfi.sh/beta/).

*5. You should see the following print out:*

    {u'status': {u'status': u'SUCCESS', u'code': u'200.0', u'codeMessage': u'Api completed successfully'}, u'result':         
    {u'metrics': {u'rows': 37062, u'time': u'0.67 sec'}, u'model_status': u'created_new', u'solver': u'classifier'}}

*6. Now run glowfi.sh prediction request to get estimated "yes"/"no" prediction for 4000+ new clients:*

    glower.accuracy = "true"    #Specifies to return accuracy calculations since we provide known responses as well
    predict_data = json.load(open('bank_profile_predict.json'))
    predict_return = glower.predict(predict_data['data_set'],predict_data['response'])
    print predict_return['status'], predict_return["result"]["metrics"], predict_return["result"]["accuracy_data"]

*7. You should see the following (meta) information:*

    {u'status': u'SUCCESS', u'code': u'200.0', u'codeMessage': u'Api completed successfully'} {u'rows': 4118, u'time': u'1.12 sec'} {u'recall': [0.88, 0.64], u'f1_scores': [0.91, 0.5], u'precision': [0.95, 0.41], u'class_names': [u'no', u'yes'], u'Composite_Accuracy': 0.86}

*8. To see the actual predictions:*

    print predict_return["result"]["predictions"]["class_predictions"]

*9. The prediction output will take this form:*

    [<prediction1>,<prediction2>,...<predictionN>]

For full info on the structure of predict's json output, please see [the prediction api doc](http://glowfish.readme.io/v1.0/docs/predict).

The 'predictions.class_predictions' key shows the estimated responses for the 4000+ clients passed to glowfi.sh from  'bank_profile_predict.json'. The 'composite_accuracy' key gives the weighted mean of class f1 scores for all estimations compared to actual user responses in 'bank_profile_predict.json' (86% in this case).

