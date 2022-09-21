# ROCIDSTEST
A test of applicants DS / ML &amp; Ops Skills
=======
<p align="center"><a href="https://github.com/RociFi" target="blank"><img src="https://avatars.githubusercontent.com/u/86011685?s=200&v=4" width="80" alt="RociFi's Logo" /></a></p>
<h1 align="center">RociFi</h1>
<p align="center">Follow us on Twitter! <b>https://twitter.com/rocifi</b> 💜</p>
<p align="center">Take home test to <b>join us</b> 💜</p>

# The Mission

Your mission, should you choose to accept it, is to demonstrate your ability to work with lending data, build a model, and serve it using an API framework. Your task is to use the provided data (more info at the bottom) to design a model capable of ranking borrowers by the chance they are fraudulent.  

Your model should then be served through the small [FastAPI](https://fastapi.tiangolo.com/) file provided. 

## Before you pick a model

You will deal with Defi Lending Transactions data. We suggest you take a look and explore them. Since those are real data, they are noisy and sparse, and there may be duplicated data.

## Predict next month outgoing given the past 6 months of transactions

Set up a prediction function that takes an address, a list of transactions recorded on the address, and outputs a score for the chance that this address is fraud.

Outgoing is defined as the sum of all transactions with `< 0` amount over a certain time-period. So to get the monthly outgoing, you can sum the negative transactions over monthly periods.

As a bonus challange, come up with a way to filter out some borrowers before passing them to your probabilistic model. Show what you learned from the data that drove your decision. 

> **Tip 1.** It might make more sense to define a month as a 30 day period rather than the month itself since the snapshots can be taken at any point during the month and not necessarily at the end. 

# Delivery

To achieve your mission, you'll have to deliver:

- A documented `Python` (3.x) code (please specify what `Python` version you've used)
- A working API serving your prediction model based on `FastAPI`
- Notebooks and/or plots to support your decision process
- A `README.md` describing your approach
- A `requirements.txt` with the minimal set of dependencies necessary to run your api
- A `requirements-eda.txt` with all dependencies necessary to run your api and all additional notebooks or files that you may provide

You can basically make whatever choice you see fit, but we do expect you to justify all the decisions that you make.


**What's important for us**
We expect you to provide a critical discussion of the strength and weaknesses of your approach, and to elaborate on possible ways to improve your work.

- You must provide us with the necessary information to create a working environment to run your code.
- Your API must be able to run and respond to requests without error.
- It is very important that you guide us through your thought process, that you motivate your choices, and that you discuss the strengths and weaknesses of your approach and possible ways to improve your predictions. 

**What's not (so) important for us**

- You can use whatever other external software libraries you think are appropriate: pandas/numpy/scikit-learn are encouraged!
- The preprocessing/algorithms/loss functions and the split between train/validation/test set are yours to decide.
- You do not necessarily have to use all the data if you feel like some of it is irrelevant or not useful. 

# The Weapons we provide you

In the `data` folder, you will find a `csv` file containing anonymized data from real ETH addresses

- The `anonmyized_lending_df_bz2.pickle` contains row-by-row data and anonmyized features for real ETH addresses in a pandas dataframe.

**Tip** The dataframe was pickled and compressed using bz2 compression, and pandas 1.3.4. To load the file, use pd.read_pickle('anonmyized_lending_df_bz2.pickle', compression='bz2')

# FastAPI 101

Provided with this repo is also a `main.py` file with a minimal [FastAPI](https://fastapi.tiangolo.com/) app template. Once you have installed the `requirements.txt` in your `Python` environment you will be able to run the main file by simply calling
`uvicorn main:app` inside your directory. This should start the local server and you should be able to see the automatically generated API docs at `http://127.0.0.1:8000/docs`.

In order to serve your model in the API, move your preprocessing to a function which you can call any input on. You do not have to worry about validating the inputs, FastAPI will do this for you! You can then move your predict functionality to the `predict` function in the `main.py` and return the predicted amount.

You can test your API using the `test_main.py` file, just make sure you are running the server by calling `uvicorn main:app` in another terminal window.

If you use `pandas`, you can convert the `transactions` of type `List[Transaction]` passed to the API to a `pd.DataFrame` by calling:

```python
import pandas as pd

df = pd.DataFrame(map(dict, transactions))
```

This is because the objects passed to the API are using `pydantic`'s `BaseModel` class which allows easy conversion from object to dictionary through the default `.dict()` implementation.

If you wish to learn more about how to use `FastAPI`:

- [Official FastAPI Docs](https://fastapi.tiangolo.com/)
- [Official pydantic Docs](https://pydantic-docs.helpmanual.io/)
- [Medium Post: How to Deploy a Machine Learning Model](https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-dc51200fe8cf)
