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

.. tip:: @Pooyeh/Simon: Please add missing colors

For a *three-color measurement*, an additional panel displays the trajectories of the detected emitters after excitation with the third laser. As shown in :numref:`trace_look` on the bottom for 3c FRET with BGR laser alternation, the top panel shows three intensities trajectories for the three detection channels after blue excitation, i.e., the emission of the blue dye after blue excitation (BB) in dark blue, the emission of green dye after the blue excitation (BG) in cyan, and the emission of red dye after blue excitation (BR) in magenta. The lower panel shows the emission after green and red excitation. Similar to the two-color case, the color of the different channels will vary depending on which detection channels have been chosen during data extraction. *Deep-LASI* chooses the above-mentioned color schemes.

You can choose which intensity trace shall be displayed by checking or unchecking channels in the **Plot Layout** tab in the right lower corner of the GUI. This holds also true for the FRET efficiency signature (which is displayed in the lower panel) or when selecting different regions in the traces, as described in :ref:`man-selection`. Deselecting FRET channels can become especially handy in the case of having more than one FRET pair per molecule. The **Reset Plot** button restores the default trace representation.

*Trace analysis* |br|
The right part of the **Traces** GUi serves for data handling. |br|
In the *Navigation* tab, you can switch between traces via the slider.
It displays the currently shown trajectory and the total number of extracted traces. For the 2c-ALEX example, 6100 traces were retrieved from the loaded data set (:numref:`trace_look`; top). |br|

The *Classification* tab serves for the manual categorization of traces.
All traces are 'by default' in the **Uncategorized** group. By clicking on the plus sign, you can add more categories. You can rename the new group according to your analysis procedure and further assign keyboard letters via the dropdown menu. The assignment of letters allows for transferring/assigning single traces to the corresponding category by simply pressing the chosen letter on the keyboard when using the keyboard during the manual sorting procedure. An example of possible sorting categories based on your analysis needs is given
in :numref:`categorization_table`. The **Create Boolean Category** button creates an additional group to the *Navigation Tab* according to your selection criteria and adds the corresponding traces, which fulfill the condition to the group.
You can also delete an unwanted category by clicking on the trash-can icon. Unchecking the filter box hides traces that are already sorted, for example, when clicking through extracted trajectories. It is especially helpful for the trash category, for example. When you assign a trace to a specific category, it will be automatically removed from the first **Uncategorized** one and added to at least one other group.

.. figure:: ./../figures/documents/Fig_19_Categories.png
   :width: 300
   :alt: categorization options
   :align: center
   :name: categorization_table

   Navigation and categorization box

.. note:: You can not assign the letters **A**, **D**, or **E** to your categories. These are the keys for going to the previous trace (A) or the following trace (D). Pressing (E), triggers *Deep-LASI* to automatically find bleaching steps in traces, assign them to the corresponding bleaching group, and select the analysis region, as laid out in the section about :ref:`correction_factors`.

The next frame on the GUI comprises two sub-tabs, the *Plot Layout* tab, and the *Trace tools* tab. The first one allows for hiding or displaying specific emission channels for selected excitation sources, as well as their corresponding FRET signatures, as described above. The *Trace tools* tab serves for carrying out automated trace sorting, classification, and analysis, which will be described in :ref:`auto-analysis`.

The *FRET controls* tab displays and controls the FRET correction factors for direct excitation, leakage, and detection sensitivity. Its functionality will be described in the section about :ref:`correction_factors`.

..  _man-categorization:
Trace categorization
~~~~~~~~~~~~~~~~~~~~
The categorization of traces depends on the actual single-molecule experiment. In the following, we describe important steps for the analysis of a dual-color FRET experiment with alternating laser excitation as an example. Experienced users can certainly carry out different steps of the categorization and selection process in parallel, i.e., on a single-trace basis.

#. To fast categorize a large number of molecules, we advise first sorting out all unwanted molecules. Create two groups, for example, called *Trash* and *Further analysis* first. Depending on whether you want to go through the list of traces using a mouse or the keyboard, assign two separate letters on the keyboard to the two groups. Now go through all traces and sort out unwanted and useful ones traces. You can switch forward to the consecutive trace by typing **D** and go backward to the former trace, which is not categorized yet, by typing **A**. Once a trace is added to a group, it will not appear any longer in the **Uncategorized** group.

#. We additionally advise ensuring that you only keep the single-molecule events. For this, please inspect the middle column on the GUI showing the detected particle in each channel. Make sure that only one molecule is shown inside the detection mask in each channel while no emitter is detected inside the 'background mask'. Otherwise, exclude the trajectory since the false background calculation will lead to miscalculated FRET correction factors and, hence, FRET efficiencies.

#. Sort between *Static* and *Dynamic* molecules. Create categories for dynamic or static traces and add each trajectory to one of the two groups. By this step, you can select afterward which traces shall be analyzed by HMM, for example.

#. Select regions of the trajectories (as described in the following paragraph :ref:`man-selection`), which will be evaluated later by kinetics or histogram analysis. Traces with manually selected regions will be automatically added to the **Manual Selection** category.

#. Mark regions of the trajectories (as described in the following paragraph :ref:`man-selection`) in which fluorophores bleach. *Deep-LASI* will add the traces automatically to the following groups: **G Bleach**, **R Bleach**, **GR Alpha**, **GR Beta**, and **GR Gamma**.

..  _man-selection:
Trace selection
~~~~~~~~~~~~~~~~~~~~
For selecting regions in traces, either for further analysis or correction factor determination, *Deep-LASI* uses the mouse as the active tool for marking different areas. *Deep-LASI* has two different types of selectors: firstly, it allows for choosing specific time windows according to the detection channel (:numref:`docu_selectors`; left), which is required to derive trace-wise correction factors, and secondly, it provides one selector mode (:numref:`docu_selectors`; right), which marks the starting and stopping time points, in between which the kinetics and FRET states shall be evaluated.

.. figure:: ./../figures/documents/Fig_20_Selectors.png
   :width: 450
   :alt: Selector types
   :align: center
   :name: docu_selectors

   Activated selector types to manually marks areas in traces

When clicking with the mouse on the trace first, the mouse turns into an active cursor for a general selection of time windows, in which the FRET states and kinetics will be evaluated (:numref:`docu_selectors`; right), e.g., by HMM later on. Once the general selector is active, detection channel-specific selection is accessible by pressing the number 1, 2, or 3 on the keyboard, depending on how many detection channels are available. By pressing the same number again, the cursor will turn into a general selector again. Clicking into the **Traces** sub-GUI aside the trajectory will deactivate the selector tool.

To select specific areas in traces, one needs to click into a trace with the left button of the mouse, and drag the mouse to make the selected region shadowed, for example, from the beginning of a trace until a bleaching step. Correction or deselection of marked areas is achieved by clicking with the right button into the trace and deselecting the desired time window. Pressing the *empty space* key on the keyboard will reset all selections and permit restarting of the selection process all over.

The selection process depends on the bleaching behavior of fluorophores and the trace-inherent SNR and photochemical behavior, etc. Detection channel selection is required to determine trace-depending correction factors automatically. If a correction factor can be calculated for a trace, its value will be shown in the **FRET control** box in the lower right corner. We advise employing as many recorded traces for either of the analysis purposes (FRET evaluation or background correction factors analysis) to obtain significant statistics later on for determining absolute distances after full data correction. We advise marking the time windows with active fluorophores with channel-specific selectors first. A possible FRET evaluation should be selected lastly, as it is not always possible.

.. tip:: @Simon is the Selection process correctly described?

.. figure:: ./../figures/documents/Fig_21_Selectors_Traces.png
   :width: 800
   :alt: cursor example for a two color trace
   :align: center
   :name: example_cursor_trace

   Activated cursors for (A-B) channel-specific selection in the green channel (A), in the red channel (B) and for (C) choosing the time window by start and stop value in which the FRET states and kinetics shall be evaluated.

:numref:`docu_selectors` provides an example of the three selector types available to evaluate a 2c ALEX trace and the outcome of such an analysis. Using the green selector (:numref:`docu_selectors`; A) the time window was marked in which, the green dye was active. The middle panel shows the time window, in which the red fluorophore was active (:numref:`docu_selectors`; B). The general selector marks the time window for FRET evaluation. This time window is not extra visualized (:numref:`docu_selectors`; C). The FRET efficiency trace gets the selection until the first bleaching step, and this region will be added to the FRET histogram in the end.

..  _correction_factors:
Correction factors determination
~~~~~~~~~~~~~~~~~~~~
In realworld single-molecule FRET experiments, the intensity of the acceptor is biased from various sources. It needs to be corrected for direct excitation :math:`\alpha_{XY;DL}` of the acceptor dye *Y* during donor excitation *X*, and spectral crosstalk :math:`\beta_{XY;DL}` from the donor molecule *X* into the acceptor channel *Y*. Further more, we need to correct for the differences in detection sensitivity :math:`\gamma_{XY}` between the two fluorophores. We are aware that the nomenclature by *Deep-LASI* at this stage, is not in line yet with the nomenclature recently introduced by a multi-laboratory benchmark study published by `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_. It will be adopted on the various GUIs of *Deep-LASI* and through-out the software during the next release. *Deep-LASI* denotes the correction factors currently as

..  list-table:: Correction factors
   :widths: 50, 50, 200
   :header-row: 1

    * - Correction factor employed by *Deep-LASI*
      - Correction factor employed by Hellekamp et al.
      - Description
    * - :math:`\alpha_{XY;DL}`
      - :math:`\delta_{XY}`
      - Direct excitation of the acceptor fluorophore *Y* during excitation with *X*
    * - :math:`\beta_{XY;DL}`
      - :math:`\alpha_{XY}`
      - Spectral crosstalk from the fluorophore *X* in the detector channel *Y*
    * - :math:`\gamma_{XY}`
      - Compensation for difference in detection sensitivities between Channels *X* and *Y*

We denote the background-corrected intensities as :math:`I_{XY}` and the corrected intensity as :math:`I_{XY;corr}`, where *X* stands for the excitation source and *Y* for the detection channel.

*Trace-wise and global correction factors*
Depending on when individual fluorophores photo-bleach, correction factors can be derived on a trace-to-trace basis. For most of the traces, however only a subset of correction factors can be obtained for the individual trajectories. In these cases, *Deep-LASI* derives *global* correction factors, which are the *median* value of the corresponding distribution of trace-wise derived correction factors.

*Deep-LASI* uses bleaching steps in single intensity trajectories to calculate possible correction factors on a trace-to-trace basis. Using traces that were presorted and categorized as **B Bleach**, **G Bleach**, **R Bleach** or **I Bleach**, trace-wise correction factors for direct excitation and spectral crosstalk between two channels can be determined.

Following the definition of leakage of the donor fluorescence into the acceptor channel according to
.. :math::
    \beta_{XY;DL} = \left \frac{\langle I_{XY}\rangle}{\langle I_{XX} \rangle} \right\rvert_{no acceptor}

**Deep-LASI** determines :math:`\beta_{XY;DL}` for acceptor bleaching steps from the static intensity in the donor channel before and after the bleaching. Here, :math:`\langle I_{XX}\rangle` refers to the mean donor intensity and :math:`\langle I_{XY}\rangle` to the mean acceptor intensity after acceptor bleaching.

If you want to select channel specific regions, press the numbers 1,2,… to indicate the channel with the same order you loaded the images, and then you can select the region by the cursor special to each channel like the example on figure 20 for the red channel as the second one. For other channels the cursor shows the other corresponding letters like B, G, and I.


.. :math::
    \beta_{XY;DL} = \frac{\langle E    \rangle}{1 - XXX}



The correction factors calculated from each trace are in the **FRET control** box on the lower right corner. If a trace is not suitable for calculating the correction factors, then the median value of the whole data set would be applied on that.

.. figure:: ./../figures/documents/Fig_21_Correction_Factor_Table.png
   :width: 450
   :alt: correction factor box
   :align: center
   :name: correction factor box

   Correction factors based on the selected region on a trace



.. math::
   \frac{ \sum_{t=0}^{N}f(t,k) }{N}



..  _hmm:
Kinetics analysis by HMM
~~~~~~~~~~~~~~~~~~~~

..  _histograms:
Histogram Analysis
~~~~~~~~~~~~~~~~~~~~

