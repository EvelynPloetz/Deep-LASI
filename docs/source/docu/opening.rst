.. |br| raw:: html

   <br />

-----------------------------------------------

Starting Deep-LASI
~~~~~~~~~~~~~~~~~
To evaluate your experimental data with *Deep-LASI*, please open the program from the MATLAB command window by typing in :code:`>> DeepLASI`. It will open the core-program responsible for data import, trace extraction, as well as and manual selection and sorting. After a couple of seconds, the Start-GUI of the program will open as shown in :numref:`open-program`.

.. figure:: ./../figures/documents/Fig_2_Tracer_FirstPage.png
   :width: 650
   :alt: Open Deep-LASI
   :align: center
   :name: open-program

   The Main-GUI of *Deep-LASI* has six sub-windows for data processing and analysis.

*Deep-LASI* shows one empty Main-GUI together with six integrated sub-windows for analyzing the data and one menubar for handling the data reading, the settings of the program, the simulation of single-molecule data and training of (new) neural networks.

Menu Bar
~~~~~~~~~~~~~~~~~
Basic functionalities of *Deep-LASI* such as data handling, program settings, or the training of new neural networks for data analysis are controlled via the *Menu Bar*. It has the following five drop-down menus

..  csv-table:: Menu Bar Entries
   :widths: 15, 200

   *File*,   "Functions for loading, mapping, processing, saving, importing and exporting data"
   *Settings*,"Access to Camera Settings"
   *View*,   "Appearance of the GUI, Graphs and Data representation"
   *Tools*,  "Programs for accessing/simulating single-molecule data, and training Neural Networks"
   *Help*,   "Direct link to the Documentation in case of problems"
   *Reset*,  "Restart of *Deep-LASI* and clearance of all variable of the program"


**Dropdown Menu File.** |br|
The dropdown menu *File* (:numref:`file-menu`) controls all steps, starting from loading the experimental data, over mapping and background correction, to trace extraction and saving of traces. Moreover, it facilitates data import and export in different formats, as described in the :ref:`data-format` section. The dropdown menu hosts seven sub-routines:

#. The sub-routines in **Mapping** are used to match the corresponding image pixels between up to four different cameras. They allow the user to generate, save and reload maps containing the transformation matrices between the channels. A description of how to map the detection channels is given below in the :ref:`mapping` section.

#. **Load Image Data** facilitates the read-in of data files per detection channels. The data needs to be read in consecutively, starting with Channel 1 being the most 'blue'-shifted detection channel and Channel 4 being the most 'red'-shifted detection channel. Data loading is possible for a single file per channel, but also for multiple files at once. Please make sure: (1) that the numbers of loaded files per detection channel match and (2) that the files have consecutive numbering so that corresponding movies are loaded.

#. Using the **Load Traces/State** routine, previously extracted and potentially already evaluated traces can be reloaded into *Deep-LASI*.

#. The **Add Traces/State** routine allows the addition of further extracted traces to already loaded traces. This function is especially useful for merging trajectories from various measurements. Please note that only traces with identical experimental settings (e.g., number of frames, exposure time, or laser excitation) can be merged.

#. **Save Traces/State** to save desired changes on traces, for example, if you have already carried out all analysis steps.

#. The **Import** function allows loading data sets from other single-molecule measurements (as described in the :ref:`data-format` section above). The imported traces are only loaded and not further modified by *Deep-LASI*.

#. **Export** allows for transferring extracted traces to a former analysis software used by the hosting group and to save and export traces and enables the saving of single trajectories in graphic formats.

#. **Quit** terminates the program.

.. figure:: ./../figures/documents/Fig_3_Open_Mapping_Menu.png
   :width: 300
   :alt: Open mapping menu
   :align: center
   :name: file-menu

   *Deep-LASI* file menu

**Dropdown Menu Settings.** |br|
The dropdown menu *Settings* (:numref:`settings-menu`) opens a sub-window for entering the camera hardware settings chosen in the experimental setup. The routine asks for the EM Gain factor, the camera baseline in dark counts, and the number of photons per camera count for each camera. With this, *Deep-LASI* can convert/display the determined intensity instead of arbitrary units in Counts per second, i.e., in Hertz.

.. figure:: ./../figures/documents/Fig_4_Dropdown_Settings.png
   :width: 650
   :alt: Open settings menu
   :align: center
   :name: settings-menu

   *Deep-LASI* settings menu

**Dropdown Menu View.** |br|
The third dropdown menu *View* controls the appearance and settings of the graphical interfaces on the different GUI sub-windows of *Deep-LASI*. |br|
The sub-tab *Colormap* changes the color palette in 3D plots, e.g., on the Trace GUI surface (which shows small zoomed-in areas of 24x24 pixels) or the Extraction GUI surface (which shows the average projection of localized molecules). In both cases, localized molecules are highlighted. The default colormap is *jet*, which can be exchanged by other standard color maps from MATLAB. |br|
The *Plot Units* sub-tab controls the y-axis of the intensity and FRET panels for individual single-molecule trajectories. Checking/unchecking the different sub-tabs immediately updates the graphical interface and the way how a single-molecule trace is displayed. The sub-tab **Plot Units** provides the following seven different settings for displaying intensities and FRET trajectories:

..  csv-table:: Plot Units Entries
   :widths: 15, 200

   *Photons (Cam. calibrated)*,   "Intensity is shown as the absolute number of photons"
   *Mean across Particle Mask*,  "Intensity is shown as mean intensity within the detection mask"
   *QY/Det. Eff (gamma)*,         "Intensity after gamma correction"
   *Spectral crosstalk (beta)*,   "Intensity after correction against spectral crosstalk"
   *Direct Excitation (alpha)*,   "Intensity after correction against direct excitation"
   *Raw Trace (no BG subtr.)*,    "Intensity without background correction"
   *Corrected FRET*,              "Display of accurate FRET instead of apparent FRET"

.. tip:: @ Simon, what precisely is plotted, i.e. which axis is changed and how ??

#.  The first sub-tab, **Photons(Cam.calibrated)**, converts the intensity axis into the absolute number of photons being detected by the individual cameras during a particular excitation cycle. It updates the intensity axis of extracted single-molecule traces on the *Traces GUI$ window.
#.  The second sub-tab, **Mean Across Particle Mask**, shows the mean emission intensity of the particle within the detection mask after trace extraction on the y-axis of the single-molecule traces on the *Traces GUI$ window.
#.  The next three sub-tabs serve to correct and show the intensity after correction against direct excitation (**Direct Excitation (alpha)**), spectral crosstalk (**Spectral crosstalk (beta)**) or QY and detection sensitivity (**QY/Det. Eff (gamma)**), respectively. Without determining the correction factors, *Deep-LASI* provides identical plots for the corrected and uncorrected intensities.
#.  The penultimate sub-tab, **Raw Trace (no BG subtr.)**, activates the display of uncorrected, raw intensity traces, i.e., without background subtraction.
#.  If the last option, **Corrected FRET**, is selected, *Deep-LASI* shows Accurate FRET efficiencies for each single-molecule trajectory in case the FRET correction factors have already been determined. Otherwise, the displayed FRET values between Accurate and Apparent FRET are identical.

**Dropdown Menu Tools.** |br|
The fourth dropdown menu *Tools* opens the subpanels for simulating single-molecule traces and training of neural networks. A detailed description of its functionalities, workflow, and usage is given in the :doc:`sim` Chapter.

**Dropdown Menu Help.** |br|
In the case of problems or errors, help can be found in the dropdown menu *Help*, which provides a direct link opening this Online documentation of *Deep-LASI*.

**Dropdown Menu Reset.** |br|
When finishing the analysis of one data set, a change to a new data set can create errors, in particular, if they differ with respect to laser alternation, imaging modalities, or the number of emitters. In this case, please reload the program via the *Reset* button. DeepLASI will reset all temporal variables in the background, refresh the graphical interface and restart the program.