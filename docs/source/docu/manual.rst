.. |br| raw:: html

   <br />

-----------------------------------------------

Single-molecule data analysis using *Deep-LASI* is carried out in an fully automatic way. However, for new experimental systems, e.g., when studying a new protein system with unknown folding behavior, it is highly advisable, to *not* go for an automatic analysis directly but to analyse the data manually and to inspect the recorded traces by eye.

Hence, the following section gives an overview on how to use *Deep-LASI* manually to sort, categorize and prepare single-molecule data via the sub-GUI *Traces* (:numref:`trace_gui`) for later evaluation, e.g. by Hidden-Markov analysis, etc. Automatic data evaluation is described in the separate section :ref:`auto-analysis`

.. figure:: ./../figures/documents/Traces_Manual.png
   :width: 650
   :alt: Trace Deep-LASI
   :align: center
   :name: trace_gui

   The sub-GUI **Traces** of *Deep-LASI* serves for data processing and pre-analysis and serves as starting point for automatic data analysis.

..  _loading_doc:
Loading
~~~~~~~~~~~~~
Starting point of any data evaluation is the loading process from 'freshly' extracted traces, or traces that shall be re-evaluated. Please load traces via :code:`> File > Load Traces`. When you recorded multiple datasets with deviating starting frame during alternating laser excitation, please first extract traces for each single movies and then load the extracted traces file-wise via reading the traces of the first file via :code:`> File > Load Traces`. and adding traces from the other files afterwards via :code:`> File > Add Traces`.

.. - :ref:`manual_analysis`
.. - :ref:`man-categorization`
.. - :ref:`man-selection`
.. - :ref:`correction_factors`

Traces GUI
~~~~~~~~~~~~~~~~~~~~
After data loading, traces will open/show up on the sub-GUI called **Traces** as shown in :numref:`trace_look` for example for two- or three-color FRET measurements with alternating laser excitation. You can switch between traces via the slider on the right upper side of the tab, showing the number of the shown trajectory and the total retracted traces. For the 2c-ALEX example, 6100 traces were extracted from the loaded data set.

.. figure:: ./../figures/documents/Fig_18_Trace.png
   :width: 700
   :alt: trace
   :align: center
   :name: trace_look

   Exemplary single-molecule traces for a (top) two-color and (bottom) three-color FRET measurement.

Depending on the measurement type and amount of detection channels, up to three sub-panels will open up on the left side of the **Traces** GUI showing the intensity trajectories of a multi-labeled molecule in the upper panels. Their corresponding intensity projections are shown on the right side next to the trajectories. The panel on the bottom left shows the potential FRET signature for different dye-pairs. Additionally, *Deep-LASI* shows small snipets in the column right next to the intensity traces showing the average movie projection in which multi-labeled molecules were found in the different detection channels including their corresponding area chosen for the background determination.

For two-color FRET experiments (:numref:`trace_look`; top), the upper left
panel shows the time trace of both, donor and acceptor after direction excitation, as well the sensitized emission. Further more, *Deep-LASI* presents the total intensity given as the sum between the DD and DA channel as an additional dark grey/black trajectory. It should be a straight line after correcting against leakage, direct excitation and detection sensitivity as described in section XXX.

Depending on the selected laser excitation scheme during the extraction process, *Deep-LASI* will present multi-color FRET data in different color-schemes, which are (of course) completely identical:

..  csv-table:: Color representation
   :header: "Detection Channel", "BG", "GR", "RI"
   :widths: 15, 200

  "donor emission after donor excitation (DD)",      "Blue",         "Green",   "Red"
  "acceptor emission after donor excitation (DA)",   "Light Green",  "Red",     "XXX"
  "acceptor emission after acceptor excitation (AA)","Green"         "Dark red","XXX"

You can choose which intensity trace shall be displayed by checking or unchecking channels in the box **Plot Layout** on the right lower corner of the GUI.


The lower panel in orange, is the time trace of FRET efficiency. You can also choose which efficiency trace to see. It especially comes handy in case of having more than one FRET pair like the case shown on the right part. In the middle column, the detected particle on each channel is shown inside the detection mask, and in addition to the trace information this can also help to decide if we have a single molecule or not. For example you should see one emitter in the middle and no particle sitting on the background ring, since it will falsify the background calculation.

The top panel shows the observed emission after donor excitation or the most blue-shifted excitation, respectively. In case of a three color experiment, the middle panel shows the observed emission in the detection channels after intermediate laser excitation. Direct e

In case of a 2c FRET experiment with ALEX(





..  _manual_analysis:
Trace selection
~~~~~~~~~~~~~~~~~~~~


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


..  _correction_factors:
Correction factors determination
~~~~~~~~~~~~~~~~~~~~