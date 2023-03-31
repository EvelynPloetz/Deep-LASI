.. |br| raw:: html

   <br />

-----------------------------------------------

Single-molecule data analysis using *Deep-LASI* is carried out in a fully automatic way. However, for new experimental systems, e.g., when studying a new protein system with unknown folding behavior, it is highly advisable to *not* go for an automatic analysis directly but to analyze the data manually and inspect the recorded traces by eye.

Hence, the following section gives an overview of how to use *Deep-LASI* manually to sort, categorize and prepare single-molecule data via the sub-GUI *Traces* (:numref:`trace_gui`) for later evaluation, e.g., by Hidden-Markov analysis, etc. Automatic data evaluation is described in a separate section on :ref:`auto-analysis`.

.. figure:: ./../figures/documents/Fig_18_Traces_Manual.png
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

.. figure:: ./../figures/documents/Fig_19_Trace_Surface.png
   :width: 700
   :alt: trace
   :align: center
   :name: trace_look

   Exemplary single-molecule traces for a (top) two-color and (bottom) three-color FRET measurement.

*Trace representation* |br|
Depending on the measurement type and amount of detection channels, up to three sub-panels will open up on the left side of the **Traces** GUI showing the intensity trajectories of a multi-labeled molecule in the upper panels. Their corresponding intensity projections are shown on the right side next to the trajectories. The panel on the bottom left shows the potential FRET signature for different dye pairs. Additionally, *Deep-LASI* shows small snippets in the column right next to the intensity traces showing the average movie projection in which multi-labeled molecules were found in the different detection channels including their corresponding area chosen for the background determination.

For a *two-color FRET experiment* (:numref:`trace_look`; top), the upper left
panel shows the time trace of both, the emission of the donor and acceptor after direction excitation (DD and AA), as well as the sensitized emission (DA), while the corresponding FRET traces is shown on the lower panel on the left. For a *single-color experiment*, the upper left panel in :numref:`trace_look` will show only one channel , while the corresponding panel for FRET traces will remain empty. Furthermore, *Deep-LASI* presents the total intensity given as the sum between the DD and DA channel as an additional dark grey/black trajectory. It should be a straight line after correcting against leakage, direct excitation, and detection sensitivity as described in the section :ref:`correction_factors`.

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
   "GI", "black :)"
   "RR", "dark red"
   "RI", " "
   "II", "black :)"

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

.. figure:: ./../figures/documents/Fig_20_Categories.png
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

.. figure:: ./../figures/documents/Fig_21_Selectors.png
   :width: 450
   :alt: Selector types
   :align: center
   :name: docu_selectors

   Activated selector types to manually mark areas in traces

When clicking with the mouse on the trace first, the mouse turns into an active cursor for a general selection of time windows, in which the FRET states and kinetics will be evaluated (:numref:`docu_selectors`; right), e.g., by HMM later on. Once the general selector is active, detection channel-specific selection is accessible by pressing the key 1, 2, or 3 on the keyboard, depending on how many detection channels are available. By pressing the same key again, the cursor will turn into a general selector again. Clicking into the **Traces** sub-GUI aside the trajectory will deactivate the selector tool.

To select specific areas in traces, one needs to click into a trace with the left button of the mouse, and drag the mouse to make the selected region shadowed, for example, from the beginning of a trace until a bleaching step. Correction or deselection of marked areas is achieved by clicking with the right button into the trace and deselecting the desired time window. Pressing the *empty space* key on the keyboard will reset all selections and permit restarting of the selection process all over.

The selection process depends on the bleaching behavior of fluorophores and the trace-inherent SNR and photochemical behavior, etc. Detection channel selection is required to determine trace-depending correction factors automatically. If a correction factor can be calculated for a trace, its value will be shown in the **FRET control** box in the lower right corner. We advise employing as many recorded traces for either of the analysis purposes (FRET evaluation or background correction factors analysis) to obtain significant statistics later on for determining absolute distances after full data correction. We advise marking the time windows with active fluorophores with channel-specific selectors first. A possible FRET evaluation should be selected lastly, as it is not always possible.

.. tip:: @Simon is the Selection process correctly described?

.. figure:: ./../figures/documents/Fig_22_Selectors_Traces.png
   :width: 800
   :alt: cursor example for a two color trace
   :align: center
   :name: example_cursor_trace

   Activated cursors for (A-B) channel-specific selection in the green channel (A), in the red channel (B), and for (C) choosing the time window by start and stop value in which the FRET states and kinetics shall be evaluated.

:numref:`docu_selectors` provides an example of the three selector types available to evaluate a 2c ALEX trace and the outcome of such an analysis. Using the green selector (:numref:`docu_selectors`; A), the time window was marked in which the green dye was active. The middle panel shows the time window in which the red fluorophore was active (:numref:`docu_selectors`; B). The general selector marks the time window for FRET evaluation. This time window is not extra visualized (:numref:`docu_selectors`; C). The FRET efficiency trace gets the selection until the first bleaching step, and this region will be added to the FRET histogram in the end.

..  _correction_factors:
Correction factors determination
~~~~~~~~~~~~~~~~~~~~
In real-world single-molecule FRET experiments, the intensity of the acceptor is biased by various sources. It needs to be corrected for direct excitation :math:`\alpha_{XY;DL}` of the acceptor dye *Y* during donor excitation *X* and spectral crosstalk :math:`\beta_{XY;DL}` from the donor molecule *X* into the acceptor channel *Y*. Furthermore, we need to correct for the differences in detection sensitivity :math:`\gamma_{XY;DL}` between the two fluorophores. We are aware that the nomenclature by *Deep-LASI*, at this stage, is not in line yet with the nomenclature recently introduced by a multi-laboratory benchmark study published by `Hellekamp et al., Nat. Meth (2018) <https://www.nature.com/articles/s41592-018-0085-0>`_. It will be adopted on the various sub-GUIs of *Deep-LASI* and throughout the software during the next release rounds. *Deep-LASI* denotes the correction factors currently as

.. list-table:: Correction factors employed by
   :widths: 35 50 250
   :header-rows: 1

   * - *Deep-LASI*
     - Hellekamp et al.
     - Description
   * - :math:`\alpha_{XY;DL}`
     - :math:`\delta_{XY}`
     - Direct excitation of the acceptor fluorophore *Y* during excitation with *X*
   * - :math:`\beta_{XY;DL}`
     - :math:`\alpha_{XY}`
     - Spectral crosstalk from the fluorophore *X* in the detector channel *Y*
   * - :math:`\gamma_{XY;DL}`
     - :math:`\gamma_{XY}`
     - Compensation for difference in detection sensitivities between Channels *X*

We denote the background-corrected intensities as :math:`I_{XY}` and the corrected intensity as :math:`I_{XY;corr}`, where *X* stands for the excitation source and *Y* for the detection channel.

*Trace-wise and global correction factors* |br|
Depending on when individual fluorophores photo-bleach, correction factors can be derived on a trace-to-trace basis. For most of the traces, however, only a subset of correction factors can be obtained for the individual trajectories. In these cases, *Deep-LASI* derives *global* correction factors, which are the *median* value of all trace-wise derived correction factors. The distribution of all three correction factors can be visualized on the **Histograms** GUI, and is described in the section :ref:`histograms` and below, respectively.

*Deep-LASI* uses bleaching steps in single-intensity trajectories to calculate trace-wise correction factors. These can be derived for traces containing bleaching steps, which were presorted and categorized as *B Bleach*, *G Bleach*, *R Bleach*, or *I Bleach*, respectively, depending on which fluorophore pairs were investigated. The correction factor for direct excitation of the acceptor during donor excitation can be derived for traces in which the donor bleached first or acceptor-only traces, via

.. math::
    \alpha_{XY;DL} = \left. \frac{\langle I_{XY}\rangle}{\langle I_{YY} \rangle} \right\vert_{\text{no donor}}

where :math:`\langle I_{XY}\rangle` and :math:`\langle I_{YY}\rangle` describes the mean acceptor intensity after donor or acceptor excitation, respectively.
Following the definition of leakage of the donor fluorescence into the acceptor channel according to

.. math::
    \beta_{XY;DL} = \left. \frac{\langle I_{XY}\rangle}{\langle I_{XX} \rangle} \right\vert_{\text{no acceptor}}

*Deep-LASI* determines :math:`\beta_{XY;DL}` from donor-only traces or at acceptor bleaching steps from the static intensity in the donor channel and acceptor channel after the bleaching. Here, :math:`\langle I_{XX}\rangle` refers to the mean donor intensity, and :math:`\langle I_{XY}\rangle` to the mean acceptor intensity after acceptor bleaching.

Lastly, the detection correction factor :math:`\gamma_{XY;DL}` is derived from traces categorized as **XY Gamma**, in which the acceptor *Y* is bleaching before the donor molecule *X*, Before determining :math:`\gamma_{XY;DL}`, the acceptor intensity :math:`I_{XY;corr}`is first corrected against direct excitation ad spectral crosstalk. Afterward, *Deep-LASI* derives the detection correction factor from the ratio of changes in the donor and acceptor emission before and after the photo-bleaching of the acceptor. The correction factor is calculated via

.. math::
    \gamma_{XY;DL} = \left. \frac{\langle \Delta I_{XY;corr}\rangle}{\langle \Delta I_{XX;corr} \rangle} \right\vert_{\text{A bleaches}}

with :math:`\langle \Delta I_{XX;corr}\rangle` and :math:`\langle \Delta I_{XY;corr}\rangle` being the intensity difference for the mean donor and acceptor emission after donor excitation before and after the acceptor photo-bleaches.

The correction factors calculated for each trace are shown in the **FRET control** box in the lower right corner (:numref:`categorization_table`; left). For each correction factor a pair *value 1 | value 2* is shown, which present the locally derived correction factors and the global correction factor. If a trace is not suitable for calculating any of the correction factors, of if the derived value is totally off, *Deep-LASI* permits to set a global correction factor. Clicking on the 'def.' box in the **FRET control** panel opens a sub-window (:numref:`categorization_table`; right). It provides an overview over the mean and mode value of all derived local correction factors including the number of traces, which underlies the statistics. By clicking on the 'use mean' or 'use mode' box, you can set the *global* correction factor for the trace. Otherwise, you can also set the correction factor value, by typing in its value in the **FRET control** panel.

.. figure:: ./../figures/documents/Fig_23_Trace_Correction_Factors.png
   :width: 800
   :alt: correction factor box
   :align: center
   :name: correction_factor_trace

   (Left) Trace-wise correction factors. (Right) After clicking on 'def.' in the **FRET control** panel, a sub-window opens showing the average *global* correction factors determined from other traces. By clicking on 'use mean' or 'use mode' the *global* correction factor values will be employed instead of the locally derived ones.

As shown in the right panel of :numref:`correction_factor_trace`, in this data set predominantly correction factors against leakage and detection sensitivity were obtained. This is mostly the case, when only the trajectories of co-localizing molecules have been extracted, as described in the :ref:`extraction_doc` section. To obtain a higher statistics for the correction factor against direction excitation in this case, it is advisable to also extract acceptor-only traces.

Once all correction factor are determined, every trace is corrected using the local, trace-wise correction factors, when available and suitable. Otherwise, the global correction factor is used. In three-color experiments, the corrected FRET efficiency for :math:`E_{YR}` is calculated first since it is required for subsequent corrections. Upon yellow excitation, the same approach is used as for two-color FRET experiments

.. math::
   \begin{eqnarray}
    I_{YY;corr} & = & I_{YY} \\
    I_{YR;corr} & = & I_{YR} - \alpha_{YR} I_{YY} - \delta_{YR} I_{RR}
   \end{eqnarray}

The corrected FRET efficiency is then given by the ratio of both corrected intensities

.. math::
    E_{YR} = \frac{I_{YR;corr}}{\gamma_{YR}I_{YY;corr} + I_{YR;corr}}

For the BY FRET pair, the fully corrected intensities after blue excitation read as

.. math::
   \begin{eqnarray}
    I_{BB;corr} & = & I_{BB} \\
    I_{BY;corr} & = & I_{BY} - \alpha_{BY} I_{BB} - \delta_{BY} I_{YY}
   \end{eqnarray}

The accurate BY FRET efficiency follows equation 5.5 with an additional term which takes into account the reduction in brightness of the yellow dye due to the FRET process between the YR pair

.. math::
    E_{BY} = \frac{I_{BY;corr}}{\gamma_{BY}I_{BB;corr}(1-E_{YR}) + I_{BY;corr}}

The intensity of the red fluorophore after blue excitation needs to be corrected against direct excitation, contributions of both the blue and yellow dye due to crosstalk into the red channel and due to cascading of FRET from the blue dye over the yellow dye into the red channel

.. math::
    I_{BR,corr} = I_{BR} - \delta_{BR} I_{RR} - \alpha_{BR} I_{BB} - \alpha_{YR}(I_{BY} - \alpha_{BY} I_{BB}) - \delta_{BY} E_{YR} (1-E_{YR})^{-1} I_{YY}

The accurate FRET efficiency of the BR FRET pair is then given by

.. math::
    E_{BR} = \frac{I_{BR;corr} - E_{YR}(\gamma_{YR}I_{BY,corr} + I_{BR,corr})}{\gamma_{BR}I_{BB;corr} + I_{BR;corr} - E_{YR}(\gamma_{BR}I_{BB,corr} + \gamma_{YR}I_{BY,corr} + I_{BR,corr})}


..  _hmm_fret:
Kinetics analysis by HMM
~~~~~~~~~~~~~~~~~~~~
Once all traces are categorized and time windows for the trace-wise data evaluation are selected, *Deep-LASI* provides two different ways to evaluate traces. For 2c FRET traces, state-of-the-art Hidden-Markov-Modeling can be used for manual analysis of the  underlying states and kinetics, as laid out in detail in the chapter on :ref:`hmm`. Additionally, HMM-AI can be automatically used on the preselected traces. This strategy is in particular required for 3cFRET traces, which cannot be evaluated with the current MATLAB and Python packages.

For an 2c HMM analysis, we first need to set the input parameters in the **HMM Input parameters** tab on the top row of the *HMM*-Gui (:numref:`hmm_fret_settings`). The procedure starts by specifying the HMM software package (as marked in blue in the very left list at the bottom) by clicking on (1) the MATLAB-based HMM package by Kevin Murphy (which works without Python-libraries) or (2) the Python-library *Pomegranate*. Next, the number of iterations per trace, and the analysis mode: (1) local or (2) global HMM analysis need to be set. The Default Convergence Threshold ist 1e-4.
Consecutively, specify the number of observations per hidden state and the number of hidden states. Depending on the number of hidden states, the number of input fields in the tabs on the right will change. The initial emission parameters and transition probabilities can be set (1) randomly, (2) evenly distributed or (3) manually. Depending on the selection, the values in the two tabs aside the Settings list will update. In the case of a *manual input*, please type in your envisioned values in both input windows. Lastly, choose the group of selected molecules that you wish to analyse and start the HMM analysis.

.. figure:: ./../figures/documents/Fig_24_HMM_Settings.png
   :width: 800
   :alt: HMM input parameters
   :align: center
   :name: hmm_fret_settings

   HMM Input parameters serve (1) for choosing the correct HMM package for global or local analysis, (2) for setting the initiation parameters, and (3) specifying the number of states and transition probabilities to analyse smFRET traces.

While *Deep-LASI* is running the HMM analysis, a green progress bar is shown on the bottom right of the GUI and the number of evaluated traces are displayed on the bottom left. Depending on the chosen input parameter, this process can last hours, in particular if a *global* HMM evaluation has been selected. Once *Deep-LASI* finished the process, the result tabs are updated (:numref:`hmm_fret_results`).

.. figure:: ./../figures/documents/Fig_25_HMM_Results.png
   :width: 800
   :alt: Local HMM results
   :align: center
   :name: hmm_fret_results

   HMM Results for a local analysis are summarized by showing (1) the FRET distribution, (2) the observed transitions via TDP and (3) the dwell-time per states via a dwell-time decay analysis. Local fitting results per single-molecule trace are shown on the bottom of the GUI.

*Local HMM* |br|
*Deep-LASI* summarizes the outcome of the analysis in the upper row of the *HMM Results* tab by 3 plots. It shows the state-wise histogram of all evaluated traces (:numref:`hmm_fret_results`). Next to it, the transition-density plot (TDP) is plotted summarizing all transitions being found in the evaluated traces. After selecting specific populations in the TDP with the mouse by dragging and positioning a white ellipse around it, *Deep-LASI* updates the dwell-time plot on the right and shows the distribution of residence times of single molecule being found in one state before transiting conformational into another one. If no selection was made, it shows the dwell-time distribution over all states together. The dwell-time, FRET values and selected events are summarized on average on the lower half of the dwell-time graph.

Results for individual single-molecule traces are shown on the bottom of the *HMM*-GUI. On the left side of :numref:`hmm_fret_results`, the overlay between single FRET traces and obtained Viterbi paths is depicted. The trace-wise values for the transition probability matrix and the emission parameters are specified next to it on the right.

*Global HMM* |br|
*Deep-LASI* further allow for a global analysis of the selected traces (:numref:`hmm_fret_results_global`). In this case, the number of iterations is not set per trace, but total rounds of training steps. Similar to *Local HMM*, *Deep-LASI* updates the results tables, however, it displays the transition probability matrix and emission parameters globally - and shows them on the top left corner of the **HMM results** tab, the results per single trace (on the bottom right corner) are not provided.

.. figure:: ./../figures/documents/Fig_26_HMM_Results_global.png
   :width: 800
   :alt: Global HMM results
   :align: center
   :name: hmm_fret_results_global

   For global analysis approaches, HMM Results are summarized by specifying the global transition probability matrix and emission properties besides the (1) FRET distribution, (2) TDP and (3) dwell-time analysis. Local fitting results per single-molecule trace are not provided.

..  _histograms:
Histogram Analysis
~~~~~~~~~~~~~~~~~~~~
Once all traces are analysed by *Deep-LASI* you can summarize the results by plotting the distributions of the different parameters. *Deep-LASI* provides distributions including fitting results on a trace-wise and frame-wise basis for

* apparent FRET
* accurate FRET (+/- denoising)
* Distances
* Stoichiometry
* the Correction factors :math:`\alpha_{XY;DL}`, :math:`\beta_{XY;DL}` and :math:`\gamma_{XY;DL}`
* Donor intensity
* Bleaching times.

