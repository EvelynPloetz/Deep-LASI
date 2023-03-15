.. |br| raw:: html

   <br />

-----------------------------------------------

Single-molecule data analysis using *Deep-LASI* is carried out in an fully automatic way. However, for new experimental systems, e.g., when studying a new protein system with unknown folding behavior, it is highly advisable, to not directly go for an automatic analysis but to analyse the data step-wise by hand and inspect the recorded traces by eye.

The following section gives, therefore, an overview first on how to use *Deep-LASI* manually to sort, categorize and prepare single-molecule data using the sub-GUI *Traces* (:numref:`trace_gui`) for later evaluation, e.g. by Hidden-Markov analysis, etc. Automatic data evaluation is described in the separate section :ref:`auto-analysis`

.. figure:: ./../figures/documents/Traces_Manual.png
   :width: 650
   :alt: Trace Deep-LASI
   :align: center
   :name: trace_gui

   The sub-GUI **Traces** of *Deep-LASI* serves for data processing and pre-analysis and serves as starting point for automatic data analysis.

..  _loading_doc:
Loading
~~~~~~~~~~~~~
Starting point of any data evaluation is the loading process. Once you extracted all traces from a new single-molecule experiment, or in the case you wish to re-evaluate data, load the data into the software via :code:`> File > Load Traces`. In case you recorded multiple datasets with alternating laser excitation but deviating starting frame, please first extract the traces per single movies and load the extracted traces file-wise consecutively via :code:`> File > Add Traces`.

.. - :ref:`manual_analysis`
.. - :ref:`man-categorization`
.. - :ref:`man-selection`

Traces GUI
~~~~~~~~~~~~~~~~~~~~
After the extraction or loading step, the resulting traces will open/show up on the sub-GUI called **Traces** as shown in :numref:`trace_look` for example for two- or three-color FRET measurements.

.. figure:: ./../figures/documents/Fig_18_Trace.png
   :width: 700
   :alt: trace
   :align: center
   :name: trace_look

   Exemplary single-molecule traces for a (top) two-color and (bottom) three-color FRET measurement.


..  _manual_analysis:
Intensity Traces
~~~~~~~~~~~~~~~~~~~~



Depending on the measurement type and amount of detection channel, up to three sub-panels will open up showing the intensity

You can see on the left side that 6100 two-color traces were extracted from the loaded data set.

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

