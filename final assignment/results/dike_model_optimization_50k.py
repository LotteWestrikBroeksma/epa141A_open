#ignore warnings
import warnings
warnings.filterwarnings('ignore')
# Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle

# EMA
import ema_workbench
from ema_workbench import (  Scenario, MultiprocessingEvaluator, ScalarOutcome, ema_logging)
from ema_workbench import  Policy,Scenario
from ema_workbench import save_results, load_results
from ema_workbench.em_framework.optimization import EpsilonProgress

# Model
from new_problem_formulation import new_get_model_for_problem_formulation

if _name_ == "_main_":
    ema_logging.log_to_stderr(ema_logging.INFO)

    #------------------------- Set Model Parameters
    problem_formulation = 2
    model, steps = new_get_model_for_problem_formulation(problem_formulation)

    uncertainties = model.uncertainties
    levers = model.levers
    outcomes = model.outcomes

    #------------------------- Reference Scenario
    ref_val = {'Bmax': 175,
               'Brate': 1.5,
               'pfail': 0.5,
                'discount rate': 3.5,
                'ID flood wave shape': 4}

    ref_dict = {}
    # < ref_dict >
    # reference scenario updated for all dike rings
    for key in model.uncertainties:
        name_split = key.name.split('_')
        if len(name_split) == 1:
            if key.name in ref_val.keys():
                ref_dict.update({key.name: ref_val[key.name]})
        else:
            ref_dict.update({key.name: ref_val[name_split[1]]})


    #------------------------- Optimization Parameters
    ref_scenario = Scenario('reference', **ref_dict)

    convergence_metrics = [EpsilonProgress()]
    #Set number of functional evaluations
    nfe = 50000


    #------------------------- Run Optimization
    ema_logging.log_to_stderr(ema_logging.INFO)

    #Set number of processes to available cores
    with MultiprocessingEvaluator(model) as evaluator:
        results, convergence = evaluator.optimize(nfe=nfe,
                                                searchover='levers',
                                                epsilons=[0.01]*len(model.outcomes),
                                                convergence=convergence_metrics,
                                                reference=ref_scenario
                                                )

    ## Plotting something I guess
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True)
    fig, ax1 = plt.subplots(ncols=1)
    ax1.plot(convergence.epsilon_progress)
    ax1.set_xlabel("nr. of generations")
    ax1.set_ylabel(r"$\epsilon$ progress")
    sns.despine()
    plt.show()

    # Save the results DataFrame using pandas
    results.to_pickle('../data/opt_pf2_50k_e001_step1.pkl')

    # Save the convergence object using pickle
    with open('../data/convergence__pf2_50k_e001_step1.pkl', 'wb') as f:
        pickle.dump(convergence, f)


    #Save Results
    results.to_csv('../data/optimization__pf2_50k_e001_step1.csv'.format(problem_formulation,nfe))