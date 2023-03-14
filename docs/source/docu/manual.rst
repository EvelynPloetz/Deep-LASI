.. |br| raw:: html

   <br />

-----------------------------------------------

..  _loading_doc:
Loading
~~~~~~~~~~~~~
Having extracted all traces, or in the case you wish to re-evaluate data, load the data into the soft ware. <to be continued>

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
