.. |br| raw:: html

   <br />

-----------------------------------------------

Single-molecule data analysis using *Deep-LASI* is carried out in a fully automatic way. However, for new experimental systems, e.g., when studying a new protein system with unknown folding behavior, it is highly advisable to *not* go for an automatic analysis directly but to analyze the data manually and inspect the recorded traces by eye.

Hence, the following section gives an overview of how to use *Deep-LASI* manually to sort, categorize and prepare single-molecule data via the sub-GUI *Traces* (:numref:`trace_gui`) for later evaluation, e.g., by Hidden-Markov analysis, etc. Automatic data evaluation is described in a separate section on :ref:`auto-analysis`.

.. figure:: ./../figures/documents/Traces_Manual.png
   :width: 650
   :alt: Trace Deep-LASI
   :align: center
   :name: trace_gui

   The sub-GUI **Traces** of *Deep-LASI* serves for data processing and pre-analysis and serves as starting point for automatic data analysis.

..  _loading_doc:
Loading
~~~~~~~~~~~~~
Starting point of any data evaluation is the loading process from 'freshly' extracted traces or traces that shall be re-evaluated. Please load traces via :code:`> File > Load Traces`. When you recorded multiple datasets with deviating starting frames during alternating laser excitation, please first extract traces for every single movie and then load the extracted traces file-wise via reading the traces of the first file via :code:`> File > Load Traces`. and adding traces from the other files afterward via :code:`> File > Add Traces`.

..  _manual_analysis:
Traces GUI
~~~~~~~~~~~~~~~~~~~~
After data loading, traces will open/show up on the sub-GUI called **Traces** as shown in :numref:`trace_look` for example for two- or three-color FRET measurements with alternating laser excitation. The GUI is split into two sections: the left part displays the single-molecule data, and the right part is dedicated to trace classification, preparation, sorting, data correction, and automated data analysis, as described later in this Chapter.

.. figure:: ./../figures/documents/Fig_18_Trace_Surface.png
   :width: 700
   :alt: trace
   :align: center
   :name: trace_look

   Exemplary single-molecule traces for a (top) two-color and (bottom) three-color FRET measurement.

*Trace representation* |br|
Depending on the measurement type and amount of detection channels, up to three sub-panels will open up on the left side of the **Traces** GUI showing the intensity trajectories of a multi-labeled molecule in the upper panels. Their corresponding intensity projections are shown on the right side next to the trajectories. The panel on the bottom left shows the potential FRET signature for different dye pairs. Additionally, *Deep-LASI* shows small snippets in the column right next to the intensity traces showing the average movie projection in which multi-labeled molecules were found in the different detection channels including their corresponding area chosen for the background determination.

For a *two-color FRET experiment* (:numref:`trace_look`; top), the upper left
panel shows the time trace of both, the emission of the donor and acceptor after direction excitation (DD and AA), as well as the sensitized emission (DA), while the corresponding FRET traces is shown on the lower panel on the left. Furthermore, *Deep-LASI* presents the total intensity given as the sum between the DD and DA channel as an additional dark grey/black trajectory. It should be a straight line after correcting against leakage, direct excitation, and detection sensitivity as described in the section :ref:`correction_factors`.

Depending on the selected laser excitation scheme during the extraction process, e.g., by choosing BG instead of GR, *Deep-LASI* will present dual- or triple-color FRET data in different color schemes but with (of course) identical intensity values. The chosen color schemes are summarized in the table below. The detection channel XY refers to the emission in the channel Y after excitation with color X, i.e., the acceptor emission in the red channel after blue excitation is abbreviated with BR:

..  csv-table:: Color representation
   :header: "Detection Channel", "Color"
   :widths: 50, 50

   "BB", "dark blue"
   "BG", "cyan"
   "BR", "magenta"
   "BI", " "
   "GG", "dark green"
   "GR", "orange"
   "GI", " "
   "RR", "dark red"
   "RI", " "
   "II", " "

.. top:: @Pooyeh/Simon: Please add missing colors

For a *three-color measurement*, an additional panel displays the trajectories of the detected emitters after excitation with a third laser. As shown in :numref:`trace_look` on the bottom for 3c FRET with BGR laser alternation, the top panel shows three intensities trajectories for the three detection channels after blue excitation, i.e., the emission of the blue dye after blue excitation (BB) in dark blue, the emission of green dye after the blue excitation (BG) in cyan, and the emission of red dye after blue excitation (BR) in fuchsia. The lower panel shows the emission after green and red excitation. Similar to the two-color case, the color of the different channels will vary depending on which detection channels have been chosen during data extraction. *Deep-LASI* chooses the above-mentioned color schemes.

You can choose which intensity trace shall be displayed by checking or unchecking channels in the **Plot Layout** tab in the right lower corner of the GUI. This holds also true for the FRET efficiency signature, which is displayed in the lower panel. Deselecting FRET channels can become especially handy in the case of having more than one FRET pair per molecule. The **Reset Plot** button restores the default trace representation.

*Trace analysis* |br|
The right part of the **Traces** GUi serves for data handling. |br|
In the *Navigation* tab, you can switch between traces via the slider.
It displays the currently shown trajectory and the total number of extracted traces. For the 2c-ALEX example, 6100 traces were retrieved from the loaded data set (:numref:`trace_look`; top). |br|

The *Classification* tab serves for the manual categorization of traces.
All traces are 'by default' in the **Uncategorized** group. By clicking on the plus-sign you can add more categories. You can rename the new group according to your analysis procedure and further assign keyboard letters via the dropdown menu. The assignment of letters allows for transferring/assigning single traces to the corresponding category by simply pressing the chosen letter on the keyboard when using the keyboard during the manual sorting procedure. An example of possible sorting categories based on your analysis needs is given
in :numref:`categorization_table`. The **Create Boolean Category** button adds an additional group to the *Navigation Tab* according to your selection criteria and will add the corresponding traces which fulfill the condition to the group.
You can also delete an unwanted category by clicking on the trash-can icon. Unchecking the filter box hides traces that are already sorted, for example when clicking through extracted trajectories. It is especially helpful for the trash category, for example. When you assign a trace to a specific category, it will be automatically removed from the first **Uncategorized** one and added to at least one other group.

.. figure:: ./../figures/documents/Fig_19_Categories.png
   :width: 300
   :alt: categorization options
   :align: center
   :name: categorization_table

   Navigation and categorization box

.. note:: You can not assign the letters **A**, **D**, or **E** to your categories. These are the keys used to go to the previous trace (A), or the next trace (D). Pressing (E), triggers *Deep-LASI* to automatically find bleaching steps in traces, assign them to the corresponding bleaching group, and select the analysis region, as laid out in the section about :ref:`correction_factors`.

The next frame on the GUI comprises two sub-tabs, the *Plot Layout* tab, and the *Trace tools* tab. The first one allows for hiding or displaying specific emission channels for selected excitation sources, as well as their corresponding FRET signatures, as described above. The *Trace tools* tab serves for carrying out automated trace sorting, classification, and analysis, which will be described in the section :ref:`auto-analysis`.

The *FRET controls* tab serves for controlling the FRET correction factors for direct excitation, leakage, and detection sensitivity. Its functionality will be described in the section about :ref:`correction_factors`.

..  _man-categorization:
Trace categorization
~~~~~~~~~~~~~~~~~~~~
The categorization of traces depends on the actual single-molecule experiment. In the following, we describe important steps for the analysis of a dual-color FRET experiment with alternating laser excitation as an example. Experienced users can certainly carry out different steps of the categorization and selection process in parallel, i.e., also on a single-trace basis.

#. To categorize a large number of molecules in a fast manner we advise first sorting out all unwanted molecules. Create two groups, for example, called *Trash* and *Further analysis* first. Depending on whether you want to go through the list of traces using a mouse or the keyboard, assign two separate letters on the keyboard to the two groups. Now go through all traces and sort out unwanted and useful ones traces. You can switch forward to the next trace by typing **D** and go backward to the former trace, which is not categorized yet, by typing **A**. Once a trace is already added to another group, it will no appear anylonger in the **Uncategorized** group.

#. We additionally advise ensuring that you only keep the single-molecule events. For this, please inspect the middle column on the GUI showing the detected particle in each channel. Make sure that only one molecule is shown inside the detection mask in each channel, while no emitter is detected inside the 'background mask'. Otherwise exclude the trajectory, since the false background calculation will lead to miscalculated FRET correction factors and hence FRET efficiencies.

#. Sort between *Static* and *Dynamic* molecules. Add categories for dynamic or static traces and add each trace to one of the two groups. By this step, you can select afterward, which traces shall be analyzed by HMM, for example.

#. Select regions of the trajectories (as described in the following paragraph :ref:`man-selection`) which will be evaluated later on by kinetics or histogram analysis. Traces with manually selected regions will be automatically added to the **Manual Selection** category.

#. Mark regions of the trajectories (as described in the following paragraph :ref:`man-selection`) in which fluorophores bleach. *Deep-LASI* will add the traces automatically to the following groups: **G Bleach**, **R Bleach**, *GR Alpha**, **GR Beta**, and **GR Gamma**.

..  _man-selection:
Trace selection
~~~~~~~~~~~~~~~~~~~~
For selecting desired regions in each trace for further analysis, you can drag the mouse to make the selected region shadowed, for example from the beginning of a trace until a bleaching step. By clicking on the trace region, the mouse turns to an active cursor for a general selection for example when all the dyes are active. *Deep-LASI* will use the first bleaching step to calculate the correction factors. If you want to select channel specific regions, press the numbers 1,2,… to indicate the channel with the same order you loaded the images, and then you can select the region by the cursor special to each channel like the example on figure 20 for the red channel as the second one. For other channels the cursor shows the other corresponding letters like B, G, and I.

.. figure:: ./../figures/documents/Fig_20_Cursor_Activating.png
   :width: 400
   :alt: cursor example with two color trace
   :align: center
   :name: example of activated cursor

   Activated cursor specific for red channel for region selection



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

..  _hmm:
Kinetics analysis by HMM
~~~~~~~~~~~~~~~~~~~~

..  _histograms:
Histogram Analysis
~~~~~~~~~~~~~~~~~~~~

