# RociFi Labs DS test

A test of applicants DS / ML &amp; Ops Skills
=======
<p align="center"><a href="https://github.com/RociFi" target="blank"><img src="https://avatars.githubusercontent.com/u/86011685?s=200&v=4" width="80" alt="RociFi's Logo" /></a></p>

# The Mission

Your mission, should you choose to accept it, is to demonstrate your ability to work with blockchain data, build a model, and serve it using an API framework. Your task is to use the provided data (more info at the bottom) to design a model capable of ranking borrowers by the chance they are fraudulent.  

Your model should then be served through the small [FastAPI](https://fastapi.tiangolo.com/) file provided. 

## Before you pick a model

You will deal with anonymized ETH Transactions data. We suggest you take a look and explore them. You may need to clean the data. We expect you to perform an EDA on the dataset.

## Predict if an address is Fraudulent

You will build a model that takes a list of transactions recorded for the address, and outputs a score for the chance that this address is fraud. You should connect this to your API built using FastAPI, so that if an address referenced by it is contained in the historical database, a Fraud Score is returned. To do this you will create a pipeline then integrate it with the `MyModel` interface in `model.py` 

The scaling for the Fraud Score is up to you, for example, you could return a Fraud score from 1-100. Please explain the scaling for your fraud score.

As a bonus challenge, come up with a way to filter out some addresses before training the model on them, are certain addresses outliers? Show what you learned from the data that drove your decision.  necessarily at the end. 

> **Tip** The index in the data frame are anonymized addresses, and the "to" column are where the transaction is going to. F0-F31 are anonymized features. We have also included anonymized transaction id's if that may be helpful. "Fraud" is a {0,1} variable where "1" means Fraud and "0" means non-Fraud.

# Delivery

To achieve your mission, you'll have to deliver:

- A well-documented `Python` (3.x) code (please specify what `Python` version you've used)
- A `Jupyter Notebook` showing an EDA performed on data provided
- A `Jupyter Notebook` showing how you came up with your model, this should be well documented, make use of markdown's!
- A working API serving your prediction model based on `FastAPI`
- Notebooks and/or plots to support your decision process
- A `README.md` describing how to test your code
- A `requirements.txt` with the minimal set of dependencies necessary to run your api
- A `requirements-eda.txt` with all dependencies necessary to run your api and all additional notebooks or files that you may provide

We expect you to implement all sections of code where implementation is requested in the comments. Additionally, we expect you to justify all the decisions that you make.


**What's important for us**  
We expect you to provide a critical discussion of the strength and weaknesses of your approach, and to elaborate on possible ways to improve your work.

- You must provide us with the necessary information to create a working environment to run your code.
- You must provide code that runs test cases on your API, along with clear documentation on how to run the test cases on our end.     
- Your API must be able to run and respond to requests without error.
- It is very important that you guide us through your thought process, that you motivate your choices, and that you discuss the strengths and weaknesses of your approach and possible ways to improve your predictions. 

**What's not (so) important for us**

- You can use whatever other external software libraries you think are appropriate: pandas/numpy/scikit-learn are encouraged!
- The preprocessing/algorithms/loss functions and the split between train/validation/test set are yours to decide.
- You do not necessarily have to use all the data if you feel like some of it is irrelevant or not useful. 

# The Weapons we provide you

In the `data` folder, you will find a `csv` file containing anonymized data from real ETH addresses

- The `anonmyized_lending_df_bz2.pickle` contains row-by-row data and anonymized features for real ETH addresses in a pandas data frame. The final column "fraud" takes a value of "0" if an address not is fraudulent, and a value of "1" if it is fraudulent.

**Tip** The data frame was pickled and compressed using bz2 compression, and pandas 1.3.4. To load the file, use pd.read_pickle('anonmyized_lending_df_bz2.pickle', compression='bz2')

# FastAPI 101

Provided with this repo is also a `main.py` file with minimal FastAPI implementation. You must implement the methods outlined in this module to build your API.

To test your API, you can run `uvicorn main:app --reload` inside your directory. This should start the local server and you should be able to see the automatically generated API docs at `http://127.0.0.1:8000/docs`. Navigating here is a useful way to test your API.

If you wish to learn more about how to use `FastAPI`:
- [Official FastAPI Docs](https://fastapi.tiangolo.com/)

# When you are finished
Please upload a tarball of your repo to the google drive subfolder that was provided to you in your invite email

# If you find any bugs
This test may not be perfect. If there are bugs that make it impossible to implement any code provided as prescribed, feel free to fix this code. Be sure to describe what bugs there were, and what you had to do to fix them. 

Additionally, if anything about this README is not clear, please feel free to email us any questions you have.

