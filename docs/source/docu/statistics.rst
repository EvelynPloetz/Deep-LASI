.. |br| raw:: html

   <br />


Selected traces and categories
~~~~~~~~~~~~~~~~~~~~

<to be continued>


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
