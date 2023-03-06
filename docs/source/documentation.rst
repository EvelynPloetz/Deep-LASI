.. |br| raw:: html

   <br />

-----------------------------------------------

Documentation
=====

.. _documentation:

*Deep-LASI* comes with an interactive graphical user interface (GUI) to perform processing and analysis tasks during the data evaluation. This page serves for documenting its functionalities. *Deep-LASI* comes with six integrated GUI sub-windows for analyzing the data and one menubar for handling the data reading, the settings of the program, and simulating single-molecule data. The analysis-GUIs are dedicated to (1) opening and molecule identification, (2) mapping and trace extraction, (3) trace categorization, selection, trace correction/analysis, (4) SNR analysis of traces, (5) the summary of the results including FRET, States, correction factors and TDP plots, and (6) the classical HMM analysis via different software packages.

To start learning how to use *Deep-LASI*, we recommend, first, reading through the :doc:`starter` and :doc:`example` sections. 
A step-wise description of how to analyze different single-molecule data with *Deep-LASI* is given for selected showcases in the :doc:`example` in detail.

Overview
------------------
- :ref:`data-format`
- :ref:`opening`
- :ref:`mapping`
- :ref:`extraction_doc`
- :ref:`manual_analysis`
- :ref:`man-categorization`
- :ref:`man-selection`
- :ref:`hmm`
- :ref:`histograms`
- :ref:`statistics`
- :ref:`auto-analysis`

--------------------------------------------------------------------
.. Contains section on Data requirements ..

..  _data-format:
Data requirements
-------------------
.. include:: docu/data.rst

--------------------------------------------------------------------
.. Contains section on Processing single molecule data ..

..  _opening:
Processing Single-Molecule Data
-------------
.. include:: docu/opening.rst

--------------------------------------------------------
.. Contains section on Manual Data analysis on Traces GUI ..

..  _manual_analysis:
Manual data analysis
-------------

Intensity Traces
~~~~~~~~~~~~~~~~~~~~

After the extraction step which might take a while depending on the amount of data loaded, the resulting traces will open on the next tab called **Traces** as shown on figure 18 for both two- and three-color measurements. You can see on the left side that 6100 two-color traces were extracted from the loaded data set.

.. figure:: ./../figures/documents/Fig_18_Trace.png
   :width: 700
   :alt: trace
   :align: center
   :name: trace look

   Exemplary traces for a two-color measurement on the left, and three-color on the right

On figure 18 on the left, you see the time trace of both donor and acceptor in the left upper panel. Because of illuminating the sample using ALEX mode, a lot of information are available on each trace. The gray plot is the total intensity on the donor channel which in theory is expected to have a stable value before a bleaching step. The green trace is the signal of donor after donor excitation, the red trace is the emission of acceptor after donor excitation (FRET), and the dark red is the emission of acceptor after acceptor excitation. You can choose which intensity trace be shown from the right box **Plot Layout** by checking or unchecking the corresponding boxes.

The lower panel in orange, is the time trace of FRET efficiency. You can also choose which efficiency trace to see. It especially comes handy in case of having more than one FRET pair like the case shown on the right part. In the middle column, the detected particle on each channel is shown inside the detection mask, and in addition to the trace information this can also help to decide if we have a single molecule or not. For example you should see one emitter in the middle and no particle sitting on the background ring, since it will falsify the background calculation.

For a three-color measurement, you will get an additional panel. As shown on figure 18 on the right, the top panel consists of all the intensities after the blue excitation in the blue channel. So the dark blue is the emission of the blue dye after blue excitation, the light blue is the emission of green dye after the blue excitation, and the purple trace is the emission of red dye after blue excitation. The rest of the panels are the same as described before.

With the **navigation** slider you can go through all traces, and with the **classification** part, you can manually categorize your traces into several categories based on your analysis needs, see an example on figure 19. All traces are by default in the **Uncategorized** section, by clicking on the plus sign you can add more categories, rename, and also assign keyboard letters to transfer them to a corresponding category by simply pressing the assigned key.

.. note:: You can not assign the letters **A**, **D**, or **E** to your categories. These are the keys that you can use to go to the previous trace (A), the next trace (D), and have the program select analysis region for you (E).

You can also delete an unwanted category with the trash can icon or uncheck the filter box to prevent them being visible. It is especially helpful for the trash category for example. When you assign a trace to a specific category, it will be automatically removed from the first **Uncategorized** one.

.. figure:: ./../figures/documents/Fig_19_Categories.png
   :width: 300
   :alt: categorization options
   :align: center
   :name: categorization table

   Navigation and categorization box

For selecting the desired region on each trace for further analysis, you can drag the mouse to make the selected region shadowed, for example from the beginning of a trace until a bleaching step. By clicking on the trace region, the mouse turns to an active cursor for a general selection for example when all the dyes are active. *Deep-LASI* will use the first bleaching step to calculate the correction factors. If you want to select channel specific regions, press the numbers 1,2,… to indicate the channel with the same order you loaded the images, and then you can select the region by the cursor special to each channel like the example on figure 20 for the red channel as the second one. For other channels the cursor shows the other corresponding letters like B, G, and I.

.. figure:: ./../figures/documents/Fig_20_Cursor_Activating.png
   :width: 400
   :alt: cursor example with two color trace
   :align: center
   :name: example of activated cursor

   Activated cursor specific for red channel for regio selection

The next photo shows an example of region selection for both green and red channels. Here the FRET efficiency trace gets the selection until the first bleaching step, and this region will be added to the FRET histogram in the end.

The correction factors calculated from each trace are in the **FRET control** box on the lower right corner. If a trace is not suitable for calculating the correction factors, then the median value of the whole data set would be applied on that.

.. figure:: ./../figures/documents/Fig_21_Correction_Factor_Table.png
   :width: 450
   :alt: correction factor box
   :align: center
   :name: correction factor box

   Correction factors based on the selected region on a trace

After having all the traces categorized, you can move on to the **Histograms** tab (figure 22), choose the category you want which are the same as you defined (figure 23), and get information about your data as histograms already fitted. Information such as the total signal, background level, count-rate, signal to noise ratio, and bleaching time, figure 24. The fitting results are provided in a table on the right side.

.. figure:: ./../figures/documents/Fig_22_Histogram_Tab.png
   :width: 300
   :alt: histogram tab
   :align: center
   :name: histogram tab

   Histogram tab

.. figure:: ./../figures/documents/Fig_23_Histogram_Tab_Categories.png
   :width: 300
   :alt: same categories in histogram tab
   :align: center
   :name: same categories in histogram tab

   Categories shown on *Histogram* tab

.. figure:: ./../figures/documents/Fig_24_Measurement_Histograms.png
   :width: 450
   :alt: histograms showing measurement details
   :align: center
   :name: histograms showing measurement details

   Histograms showing measurement details

Then you can move on to the **FRET** tab, and again choose the desired category by clicking on the plus sign beside the list.

.. figure:: ./../figures/documents/Fig_25_FRET_Tab.png
   :width: 300
   :alt: FRET tab
   :align: center
   :name: FRET tab

   FRET tab on the GUI

.. figure:: ./../figures/documents/Fig_26_FRET_Tab_Categories.png
   :width: 500
   :alt: FRET tab categories
   :align: center
   :name: choosing categories on FRET tab

   Choosing desired category(ies) on *FRET* tab

After choosing the category, you can select from the **Plot Mode** which plot to get. In the example shown on figure 26, you get the histogram of apparent FRET efficiency, like the one in figure 27.

.. figure:: ./../figures/documents/Fig_27_Result_Histogram.png
   :width: 400
   :alt: apparent FRET histogram
   :align: center
   :name: apparent FRET histogram

   An exemplary histogram of apparent FRET efficiency with two populations

There are options in **Display Settings** (see figure 28) to make the frame-wise and/or molecule-wise plot visible, normalize them, and also to fit them by choosing the best fitting method. If sometimes fitting seems so wrong, you can manually insert some values based on what you roughly see on the plot, fix them and fit again. By playing around the fitting gets better, then you can uncheck the fixing boxes and let the program find the best fitting values. You can also change the color of your plot(s) by clicking on the colored rectangle and choose a desired color.

.. figure:: ./../figures/documents/Fig_28_Fitting_Histogram.png
   :width: 500
   :alt: display settings
   :align: center
   :name: result display settings

   Display settings for the resulting plots

On the HMM tab, you can again select a category and run the HMM on it. This option works for two-color measurements at the moment. There are some other options for analysis the kinetics of a three-color measurement which will come shortly in the following parts.

.. figure:: ./../figures/documents/Fig_29_HMM_Tab.png
   :width: 300
   :alt: HMM tab
   :align: center
   :name: HMM tab

   HMM tab on the software GUI

.. figure:: ./../figures/documents/Fig_30_HMM_Starting.png
   :width: 450
   :alt: starting HMM
   :align: center
   :name: running HMM

   Starting HMM analysis on data

..  _automatic_analysis:
Automated Analysis by Deep Learning
-------------

In case you want to save time and not go through all the analysis steps manually which might take days and even weeks especially for categorizing, you can use the automated analysis provided in the **Deep Learning** tab, Figure 31. This is an additional program using pre-trained deep neural networks incorporated into *Deep-LASI*.

.. figure:: ./../figures/documents/Fig_31_TracesTab.png
   :width: 400
   :alt: Deep learning tab
   :align: center
   :name: Deep learning tab

   The automated analysis tab, **Deep Learning**

The simplest way to get your final results is to click on **Magic Button** (figure 32) and the program will do all the steps of categorization, correction, and dynamics analysis for you! All neural network models are chosen automatically dependent on the number of channels in your data set. The first step is the categorization of all traces. Note, that only dynamic traces reaching the confidence threshold (editable the deep learning tab) will be included in the category 'Dynamic (filtered)' and further analyzed. The **Magic Button** carries out a series of analysis steps which you can also perform individually via the Buttons in the deep learning tab, namely:

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

After trace classification, auto calculation of all available correction factors is performed. Figure 33 shows the histograms of the extracted direct excitation, crosstalk and gamma factors with the corresponding median, mean, and mode values. Gamma factors are calculated 3-fold for median, mean and mode values of direct excitation and crosstalk to show you the influence of these globally used correction factors on the gamma factor. The total number of traces and frames used for the calculation of each correction factor is displayed above the histograms.

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

After trace classification and correction, the number of states classifier will predict the most probable number of states for each trace. The corresponding confidence values will be shown in a pop up histogram.

.. figure:: ./../figures/documents/Fig_34_number_of_states_confidence.png
   :width: 300
   :alt: state number
   :align: center
   :name: state number

   Number of states confidence for each trace

The predictions of the number of states classifier are used for model selection of the state transition classifier, which subsequently sort all frames in the dynamic traces into state occupancy. Figures 35 and 36 show a histogram of state-wise FRET efficiency and trace-wise state confidence, respectively.

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

After all neural network predictions are completed, the program asks you to choose the number of bins, the confidence threshold and the number of states categories to include in the TDP (Transition Density Plot).

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

By clicking on **Select ROI**, you can choose a cluster and obtain dynamic information about it. The mean values of dwell time, initial and final FRET, and the number of transitions appear on the rext box to the right. The live fit panel below fits the selected dwell times with an exponential. By choosing the **Fit Selection**, **Fit Upper Triangle** or **Fit Lower Triangle** you can fit the dwell times using the Curve Fitting Toolbox™ from MATLAB (not available in compiled programs!). **Plot Dwell times** will plot the dwell times of the selected transitions in a histogram. **Plot FRET** and **Plot corr. FRET** show you the histogrammed apparent and corrected FRET efficiency of the selection, respectively. In case of 3-color FRET data, the FRET efficiencies of all other dye pairs are shown as well.

Magic button is the fully automated step. You may also intend to take separate and different analysis steps without the magic button. For that, you first need to load a neural network from the same table of **Trace Tools**, figure 41. First choose the closest option to your measurement from the drop-down menu on the right, and then click on **Load Neural Network**. Then with the options provided you can do the necessary analysis on your data and get the results within a couple of minutes. Note that to do the autocorrect, you should first click on **Categorize** and then click on **Autocorrect**. After having the categories made by the software, you always have the option of going through the traces, make any changes, and save the current status of the data set.
