# README File

Created by:
Group Number 20

Emily Chatziandreou - 4934679
Lotte Westrik Broeksma - 5109477 
Maryvonne Marang - 5172470
Vera Vermeulen - 5127661


## Introduction

Welcome to our folder (epa141A_open) that contains all the details of our final assignment
of Model-Based Decision-Making. In this folder, you'll find 3 other folders and 
2 separate files. 


## README
The README file is the file you're reading at this exact moment. It tells 
the reader what the contents are of the other files that are included 
in the folder. If you're still interested in that information, continue reading. 


## Requirements
This file shows which packages and libraries need to be installed to run 
the simulation successfully.


## Data
The data folder contains 8 important result datafiles that you need 
to run the corresponding notebook analysis that are in the results folder. 

Here is a quick list of which file you need for which notebook:
- behaviour_run_10ksc_refpol.tar.gz for Final_Scenario_Discovery.ipynb
- policy_space_refsc_256pol.tar.gz for Open Exploration - Policy space.ipynb
- uncertainty_space_1024sc_refpol.tar.gz for Open Exploration - Uncertainty space.ipynb
- convergence__pf2_50k_e001_step1.pkl for Optimization analysis.ipynb
- convergence__pf2_100k_e001_step1.pkl for Optimization analysis.ipynb
- optimization__pf2_50k_e001_step1.csv for Optimization analysis.ipynb
- optimization__pf2_100k_e001_step1.csv for Optimization analysis.ipynb
- plausible_policies.csv for Robustness Assessment.ipynb

The behaviour_run_10ksc_refpol.tar.gz is the results that came from running 10.000 scenarios 
on the reference policy (where no policy levers are implemented) using the dike_model_simulation_behaviour.py file in the results 
folder. 

The policy_space_refsc_256pol.tar.gz is the results that came from running 265 different 
policies on the reference scenario using the dike_model_simulation_policy_space.py file 
in the results folder.

The uncertainty_space_1024sc_refpol.tar.gz is the results that came from running
1024 scenarios on the reference policy (where no policy levers are implemented) using the 
dike_model_simulation_uncertainty_space_1024.py file in the results folder. 

Both of the convergence pkl files are the graphs that respectively come from running either
dike_model_optimization_50k.py or dike_model_optimization_100k.py from the results 
folder (meaning either 50.000 or 100.000 functional evaluations and an ε - epsilon of 0.01).
The optimizations csv files store all policy outcome combinations that resulted out the 
the same optimization run.

At the end of the Optimization analysis.ipynb you save a csv with all plausible policies,
that you will use in the robustness assessment. 

The rest of the files in the data folder were already given for the final assignment.
We did not alter these files, so these can be discarded. 


## Report
This folder contains a written report that explain how and which analysis were used.
The results that came from the simulation are analysed, reflected on
and a conclusion is formulated.
Another file in the document is the political reflection file that reflects how our 
model functions in a political world. 


## Results
There is another directory inside the results folder, namely data. The data directory
contains all the results from the Scenario Discovery in csv files and the files 
experiments_rob.csv and outcomes_rob.csv. The experiments and outcomes file are the 
results from running the plausible_policies against the worst scenarios from the 
Scenario Discover.
The other files are the results of the worst case scenarios for the outcomes 
all deaths and damage. There are 2 overall files and also 5 files per outcome 
for the different locations. Lastly, there is also one merged_scenario_cleaned file, 
which includes all the critical scenarios for each location's death and damage outcomes.

The other files in the results directory were used to run either simulations or analysis, 
based on the simulation outcomes. The simulation files were all implemented using 
problem formulation 3. The simulations that were used to do an open exploration analysis
are run in the following order:
- dike_model_simulation_policy_space.py
- dike_model_simulation_uncertainty_space_1024.py
- dike_model_simulation_behaviour.py
The policy space was used to investigate the effects and interactions of the 
different combinations of levers on the outcomes. With this we could see how sensitive
the outcomes were to certain policies that were implemented. 
The uncertainty space was used to investigate the effects and interactions of the different
uncertainty parameters combinations on the outcomes. With this we could again see how 
sensitive the outcomes were, but now to the uncertain parameters.
Both of these simulations were sampled by the Sobol sampler. 
The behavior simulation was used to run a Scenario Discovery using Latin Hypercube Sampling, were you get all the scenarios
that are the worst for a certain outcome. 

These simulations provide result files that are in the data directory. With these results you
can run the following notebook analysis:
- Final_Scenario_Discovery.ipynb for the results of the dike_model_simulation_behaviour.py
- Open Exploration - Policy space.ipynb for the results of dike_model_simulation_policy_space.py
- Open Exploration - Uncertainty space.ipynb for the results of dike_model_simulation_uncertainty_space_1024.py

The policy space and uncertainty space are used to run a sensitivity analysis and feature 
scoring. The scenario discovery was used to get the worst case scenarios per outcome 
using Prim and also to do dimensional stacking to see if we have run enough scenarios to 
draw conclusions out of the results.

After the simulations, the dike_model_optimization_50k.py and dike_model_optimization_100k.py
were implemented. These optimization runs were used to conduct a directed search with policy constraints, derived from the political debates. 
For the optimization problem formulation 2 was run. The results of
these optimizations were then used in the Optimization analysis.ipynb. Out of this come
the most plausible policies that will then be used for the 
Final Robustness Assessment.ipynb, where the policies will be tested against the worst case
scenario's


## How to get started
To run the project code, follow these steps:
- Clone the repository to your local machine using this link:
https://github.com/LotteWestrikBroeksma/epa141A_open
- Install the necessary requirements. You can use pip to install the required Python
packages: pip install -r requirements.txt
