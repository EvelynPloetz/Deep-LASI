.. |br| raw:: html

   <br />

-----------------------------------------------

..  _auto-analysis:
Automatic smFRET Analysis
~~~~~~~~~~~~~

In case you want to save time and not go through all the analysis steps manually which might take days and even weeks especially for categorizing, you can use the automated analysis provided in the **Deep Learning** tab (:numref:`magic button`). This is an additional program using pre-trained deep neural networks incorporated into *Deep-LASI*.

The simplest way to get your final results is to click on **Magic Button** (:numref:`magic button`) and the program will do all the steps of categorization, correction, and dynamics analysis for you! All neural network models are chosen automatically depending on the number of channels in your data set. The first step is the categorization of all traces. Note, that only dynamic traces reaching the confidence threshold (editable in the deep learning tab) will be included in the category 'Dynamic (filtered)' and further analyzed. The **Magic Button** carries out a series of analysis steps which you can also perform individually via the Buttons in the deep learning tab, namely:

#. **Categorize Traces** (Sort all frames and traces into categories, e.g. 'Dynamic', 'Static', 'Bleached')
#. **Autocorrect** (Extract all correction factors and calculate the corrected intensities/FRET)
#. **Number of States** (Predict the number of observed states in all traces in the category 'Dynamic (filtered)', which depends on your set confidence level)
#. **State Transitions** (Predict state transitions using the model which corresponds to the predicted number of states at step 3)
#. **Transition Density Plot** (Generate TDP based on the predicted state transitions)

For the prediction of state transitions you have more freedom if you call the function separately. For example, you can run the prediction on fully corrected data, choose a specific model in case you have prior knowledge about the system or feed all frames into the state classifier without prior categorization of the trace classifier. Check the 'Global' checkbox if you want to feed all traces classified as dynamic into the number of states classifier and/or the state transition classifier at once. The global option will concatenate all dynamic frames, hence it will lead to a different prediction than the standard local approach. Due to the sensitivity of the number of states classifier and the normalization procedure of each input trace, the global output of the number of states is biased towards the maximum number of states. It is therefore recommended to use the Global feature only for small data sets or only for the state transition classifier.

.. figure:: ./../figures/documents/Fig_32_DeepLearning_Tab.png
   :width: 300
   :alt: magic button
   :align: center
   :name: magic button

   Deep Learning Tab with Magic Button

After trace classification, auto calculation of all available correction factors is performed. :numref:`gamma factor` shows the histograms of the extracted direct excitation, crosstalk and gamma factors with the corresponding median, mean, and mode values. Gamma factors are calculated 3-fold for median, mean and mode values of direct excitation and crosstalk to show you the influence of these globally used correction factors on the gamma factor. The total number of traces and frames used for the calculation of each correction factor is displayed above the histograms.

.. figure:: ./../figures/documents/Fig_33_ct_dir_autocalc.png
   :width: 300
   :alt: ct dir factors
   :align: center
   :name: de and ct correction factors

.. figure:: ./../figures/documents/Fig_33_gamma_autocalc.png
   :width: 300
   :alt: gamma factors
   :align: center
   :name: gamma factor

   Correction factors histograms

After trace classification and correction, the number of states classifier will predict the most probable number of states for each trace. The corresponding confidence values will be shown in a pop up histogram like :numref:`state number`.

.. figure:: ./../figures/documents/Fig_34_number_of_states_confidence.png
   :width: 300
   :alt: state number
   :align: center
   :name: state number

   Number of states confidence for each trace

The predictions of the number of states classifier are used for model selection of the state transition classifier, which subsequently sort all frames in the dynamic traces into state occupancy. :numref:`state prediction confidence` and :numref:`Statewise mean FRET histogram` show a histogram of trace-wise state confidence and state-wise FRET efficiency respectively.

.. figure:: ./../figures/documents/Fig_35_state_transition_confidence.png
   :width: 300
   :alt: state prediction confidence
   :align: center
   :name: state prediction confidence

   State transition confidence

.. figure:: ./../figures/documents/Fig_36_statewise_mean_FRET_histogram.png
   :width: 300
   :alt: state-wise mean FRET
   :align: center
   :name: Statewise mean FRET histogram

   Statewise mean FRET histogram

After all neural network predictions are completed, the program asks you to choose the number of bins, the confidence threshold and the number of states categories to include in the TDP (Transition Density Plot), as shown on :numref:`TDP input`.

.. figure:: ./../figures/documents/Fig_37_DL_TDP_input.png
   :width: 300
   :alt: TDP input
   :align: center
   :name: TDP input

   TDP input parameters

.. figure:: ./../figures/documents/Fig_38_TDP_LiveFit_Panel.png
   :width: 300
   :alt: TDP
   :align: center
   :name: TDP

   TDP with live fit panel

When the TDP is generated like the example shown on :numref:`TDP`, by clicking on **Select ROI**, you can choose a cluster and obtain dynamic information about it. The mean values of dwell time, initial and final FRET, and the number of transitions appear on the next box to the right. The live fit panel below fits the selected dwell times with an exponential function. By choosing the **Fit Selection**, **Fit Upper Triangle** or **Fit Lower Triangle** you can fit the dwell times using the Curve Fitting Toolbox™ from MATLAB (not available in compiled programs!). **Plot Dwell times** will plot the dwell times of the selected transitions in a histogram. **Plot FRET** and **Plot corr. FRET** show you the histogrammed apparent and corrected FRET efficiency of the selection, respectively. In case of 3-color FRET data, the FRET efficiencies of all other dye pairs are shown as well.

Magic button is the fully automated step. You may also intend to take automatic but still separate and different analysis steps without the magic button. That is why a couple buttons are provided on the same table of *Deep Learning* (:numref:`magic button`). For example, if you would only like to categorize your traces, you can click on the button *Categorize Traces*. Then with the options provided (:numref:`neural_models`) you can select the closest option to your measurement features. You can also leave it as the default option *Auto select* to have the Deep-LASI recognize the model. Then confirm it by clicking on *OK*, and after a short while, have all the traces categorized.

.. figure:: ./../figures/documents/neural_models.png
   :width: 250
   :alt: neural models
   :align: center
   :name: neural_models

   The options for selecting the closest neural model to the data under analysis 
   
You can also get information about the number of states within traces by clicking on *Number of States*. Then, the program will ask you to choose whether you want the raw traces or the corrected ones to be evaluated for that. Obviously, prior to choosing the *corrected traces* option, you should have the traces already corrected. In order to obtain the correction factors or corrected FRET efficiency, one can click on the button *Autocorrect*. Please note that to do the autocorrection, you should first click on *Categorize Traces* and then click on *Autocorrect*. The same is true for the button *State Transitions*. After categorization, you would first choose the correct model among the options, decide about the process being performed on raw or corrected traces, and have the program informing you about the number of transitions in the category *Dynamic (filtered)*. After having the categories made by the software, you always have the freedom of going through the traces, make any changes, and save the current status of the data set.
