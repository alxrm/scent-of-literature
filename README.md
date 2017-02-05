# Scent of literature
Russian literature sentiment analysis in terms of very small dataset

## It uses
* _Pandas_ to read the input data
* _Sklearn_ for the classification work

## Usage

Just run this in terminal:

```
./eval.py
```

### Variables

* `is_test_run` is the boolean, which defines whether it should just show report about the performance by testing itself on a training dataset or perform a real prediction on a `test_file`
* `train_file` is the path to the training dataset, which should contain text and labels (right now columns are `1` and `2`, because of the structure of the default `train.tsv` file)
* `test_file` is the path to the file you want to perform prediction on, it should contain only a single column with text you want to analyze(by default it searches for 0-th column because of the `data.txt` structure)

### Under the hood

To perform the classification it uses [SGD](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html) classifier(also here is [wiki](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)) with [hinge](https://en.wikipedia.org/wiki/Hinge_loss) as a loss function, aka [SVM](https://en.wikipedia.org/wiki/Support_vector_machine), which shows the best results in sentiment analysis afaik, but has more tuning options than [LinearSVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html) 

_Note_: the model's hyperparameters are chosen by sklearn's [GridSearchCV](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) (more on this [here](https://en.wikipedia.org/wiki/Hyperparameter_optimization)) and those are tuned to match the best [F1 score](https://en.wikipedia.org/wiki/F1_score)
