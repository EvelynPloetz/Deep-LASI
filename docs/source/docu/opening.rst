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

Main-GUI
~~~~~~~~~~~~~~~~~
Data-analysis with *Deep-LASI* involves consecutive working steps (:numref:`main-workflow`), which are accommodated in six different sub-GUIs. The Starting-GUI incorporates single molecule data at different levels. First of all, it reads movies from emCCD or sCMOS cameras, as usually acquired using a wide-field total internal reflection fluorescence (TIRF) microscope and maps corresponding pixels between camera onto each other (see section on  :ref:`mapping`). Next, it extracts the intensity information of single and co-localizing molecules depending on the excitation scheme and assay and saves the extracted traces afterwards, as described in more details in section :ref:`extraction_doc`. For already recorded intensity time traces from confocal microscopy and localization microscopy, *Deep-LASI* imports the trajectories as formerly saved without additional correction. Equally, already extracted traces can be loaded into *Deep-LASI* for further data analysis.

.. figure:: ./../figures/documents/Fig_5_Main_GUIs-Flow.png
   :width: 800
   :alt: Main GUIs
   :align: center
   :name: main-workflow

   Workflow summarizing the generic data formats used by *Deep-LASI*, as well as supported data formats for trace import.

The main data handling is carried out on the *Traces* GUI (:numref:`main-workflow`). Here, you can choose between manual or automated data analysis. Conventional data analysis, includes sorting, categorization and trace preparation (as described in section :ref:`manual_analysis`) before handing over the preselected traces for Hidden-Markov modeling on the *HMM* GUI followed by dwelltime analysis and TDPs. The Sub-Window *Histograms* allows for summarizing the analyzed data via histograms with respect to, e.g., frame-, molecule-, and state-wise histograms, or the global FRET correction factors (:numref:`main-workflow`). The sub-window *Statistics* on selected molecule groups with respect to, e.g., average brightness, background, SNR etc. |br|
The automated data analysis is carried out on the *Traces* GUI, which includes and automated selection, sorting, and categoriziation process prior to an automated kinetics analysis based on deep-learning. The data is afterwards automatically summarized by state-of-the-art dwell-time analysis and TDPs.


..  _mapping:
Mapping
~~~~~~~~~~~~~~~~~
Before loading data into *Deep-LASI*, one need to consider the experimental requirements. In the case, single-color data has been acquired, the data can directly be loaded into the software and single-channel traces can be extracted, as described in :ref:`extraction_doc`. In the case, that more than one detection channel has been employed, we need to know where the emission of labeled molecules are detected on the different field-of-views (FOV) of the camera, i.e., which pixels on one channel correspond to a pixels on the other (:numref:`gui_mapping`).

.. figure:: ./../figures/documents/Fig_6_Main_GUI_Mapping.png
   :width: 500
   :alt: Mapping
   :align: center
   :name: gui_mapping

   Mapping between multiple detection channels copes with translation, rotation, and magnification.

For mapping the different channels onto each other, an

If mapping is required between two or more cameras, go to **Mapping** from the menu under file. Then choose ‘Create New Map’ and the ‘First Channel’. You can see the path on figure 3.

.. figure:: ./../figures/documents/Fig_3_Mapping_Menu.png
   :width: 600
   :alt: Open mapping menu
   :align: center
   :name: mapping menu

   Mapping menu

Now the program will ask you to choose a file which could be an image or a series of images as a video file usually taken from a calibration pattern like a zero-mode waveguide. After choosing the file, the image gets open together with some adjusting options, like figure 4.

.. figure:: ./../figures/documents/Fig_4_Map_Image_Uploading.png
   :width: 450
   :alt: map uploading
   :align: center
   :name: mapping image uploading

   Uploading first mapping image

On the window opened for the user, you can use the **Channel Layout** to take the desired field of view. You can take the whole area or select a specific region with the buttons provided for that. There are also the options of rotating or flipping the image, so that all images from various cameras show the same pattern. Then click on OK. The image will be open on the mapping tab, figure 5.

.. figure:: ./../figures/documents/Fig_5_Map_Image_Detecting.png
   :width: 400
   :alt: map detection
   :align: center
   :name: mapping image detection

   Mapping image loaded to *Deep-LASI*

With the threshold bar, make sure that enough points are circled and detected by the program. Then continue opening images from other detectors with the same procedure, as shown on images 6 and 7.

.. figure:: ./../figures/documents/Fig_6_Map_Second_Channel.png
   :width: 300
   :alt: second map image
   :align: center
   :name: opening second mapping image

   Opening the second mapping image

.. figure:: ./../figures/documents/Fig_7_Map_Second_Uploading.png
   :width: 400
   :alt: second map uploading
   :align: center
   :name: second map uploading

   Adjusting the image for the second mapping image

After opening the mapping images from all the cameras, select which channel you prefer to be the reference channel, like figure 8. In most cases, the first channel is taken as the reference one unless you have a special mapping plan.

.. figure:: ./../figures/documents/Fig_8_Mapping_Starting.png
   :width: 450
   :alt: start mapping
   :align: center
   :name: start mapping

   Performing the mapping step

Then click on **Start Mapping**. The mapping process goes quit fast and gives the mapping result as before and after images like figure 9. It is recommended to check the quality of mapping. In some cases you might have to take new images for this step if the image quality you uploaded was not acceptable which is a rare event!

.. figure:: ./../figures/documents/Fig_9_Map_Before_After.png
   :width: 350
   :alt: check mapping
   :align: center
   :name: before and after mapping

   Mapping result showing the channels overlay before and after mapping

After mapping, the extraction tab opens showing a detection mask created like the one shown on the top right part of figure 10. This mask is used to calculate the emission intensity of the particle inside the central circle, and also the background within the outer ring. The user has the freedom to change the mask settings when needed. You have the option of saving the created map or loading a previous map from the same mapping menu.

.. figure:: ./../figures/documents/Fig_10_Map_Saving.png
   :width: 400
   :alt: created mask
   :align: center
   :name: created mask after mapping

   The mask created after mapping with adjustment options

..  _extraction_doc:
Loading the data
~~~~~~~~~~~~~

Now you can open the data files from file menu and **Load Image Data** similar to opening the mapping images like shown on figure 11. The order of channels should be the same as mapping order.

.. figure:: ./../figures/documents/Fig_11_Data_Loading.png
   :width: 300
   :alt: loading first channel
   :align: center
   :name: loading first channel data

   The menu for loading image data

*Deep-LASI* asks you to choose the data files, and you can open all the files from each channel at a time. After a short time, the following window (figure 12) will open to take the measurement parameters. The first box is for the sum of exposure time and frame transfer. For example in case of measuring with the exposure time of 50 ms, and the frame transfer of 2.2 ms, we can enter 52.2.

.. figure:: ./../figures/documents/Fig_12_Measurement_Parameters.png
   :width: 400
   :alt: inserting measurement parameters
   :align: center
   :name: measurement parameters

   The window for specifying measurement parameters and excitation scheme

The second box is to get the ALEX sequence used for illuminating the sample. Different combinations of two or three laser excitation can be entered here. Note that for the IR laser, you should only enter the letter ‘I’. The letter ‘G’ works for lasers in green or yellow region. Then you put the slider on the corresponding channel, for example, on the image shown here on the left or right position depending on reading data from first or second channel. It gets three divisions in case of a three-channel experiment.

Then choose which frames you want to load on the program by using the **Load frame range**. Also depending on the experiment, you can choose the range of desired frames for detecting the particles and extracting their intensity traces. *Deep-LASI* takes all the frames by default and you can change them as you wish.

The option of choosing the dye does nothing at the moment, but a library of various dyes could be added to the program so that dye specific information help us with a more complete analysis.

As the last step here, click on the corresponding channel color from the four options provided. Now *Deep-LASI* opens the first data file from the range that you selected, like figure 13.

.. figure:: ./../figures/documents/Fig_13_Detecting_Particles.png
   :width: 400
   :alt: first channel detection
   :align: center
   :name: particles detection

   Particle detection for the first channel data

The sliders below the image are to adjust the display contrast, and detection threshold so that one gets more particles detected. The detected particles are inside a triangle within the image, and the number of them is shown in the box next to the image on the top right position.

Continue opening the data images for the next channel(s) from the same menu, as shown on figure 14.

.. figure:: ./../figures/documents/Fig_14_Data_Loading_Second_Channel.png
   :width: 300
   :alt: loading second channel
   :align: center
   :name: menu for loading second channel

   Loading data from the second detector

Each time you load image files, the pop-up window appears asking you about the channel color to extract the data in the correct order.

.. figure:: ./../figures/documents/Fig_15_Measurement_Parameters_Second_Chan.png
   :width: 300
   :alt: inserting second measurement parameters
   :align: center
   :name: change parameters for the next detector

   Updating measurement parameters for the next channel

The example figures show a two-color measurement. As shown on figure 15, we put the slider on the second half to indicate the second channel (the same procedure works for the third channel by putting the slider to the most right position.), and also click on the R to indicate the acceptor channel (red in this case). After a short time the first frame of the second channel overlays on the image from the first one.

.. figure:: ./../figures/documents/Fig_16_Detecting_Colocal.png
   :width: 400
   :alt: detection of co-localization
   :align: center
   :name: finding co-localization

   Detection of particles and their co-localization

The color of triangles show the detected emitters on each corresponding channel and the circles show the co-localized particles. All the numbers are also reported in the small box on the top.

You can decide which particles you want to analyze using the options in the right box **Trace Selection** and then click on **Extract Traces**. In the example shown on figure 17 only the co-localized particles are considered to study their FRET.

.. figure:: ./../figures/documents/Fig_17_Extracting_Start.png
   :width: 450
   :alt: start extraction
   :align: center
   :name: performing the extraction

   Starting the extraction of intensity traces
