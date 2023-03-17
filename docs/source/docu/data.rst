.. |br| raw:: html

   <br />

-----------------------------------------------

Data handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Deep-LASI* incorporates single molecule data at different levels. First of all, it reads movies from emCCD or sCMOS cameras, as usually acquired using a wide-field total internal reflection fluorescence (TIRF) microscope. Consecutively, it extracts the intensity information of single and co-localizing molecules depending on the excitation scheme and assay and saves the extracted traces afterward. For already recorded intensity time traces from confocal microscopy and localization microscopy, *Deep-LASI* imports the trajectories as formerly saved without additional correction. :numref:`data-flow` summarizes the data handling.

.. figure:: ./../figures/documents/Fig_1_Data_Handling.png
   :width: 800
   :alt: Data Handling
   :align: center
   :name: data-flow

   Workflow summarizing the generic data formats used by *Deep-LASI*, as well as supported data formats for trace import.

-----------------------------------------------

Supported Data Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Deep-LASI* was developed to handle movie files containing single-molecule data. Nevertheless, it can also import recorded data from other sources (see below). We are happy to support further standard image formats to make *Deep-LASI* compatible with other systems and software packages. For more specialized / home-built setups and data formats, we recommend first reading the :ref:`custom-file` section before getting in touch with us in the Forum and/or via ...

**TIFF, Tagged Image File Format (.tif)**

*Deep-LASI* accepts movie files in the Tagged Image File Format (*.tif*). These files can contain stacks of wide-field/TIRF images with
one or multiple detection channels for different laser excitation schemes. Choose this file format if you want to load raw data from, e.g., emCCD cameras.

**PicoQuant universal file format (.ptu)**

*Deep-LASI* can handle confocal data obtained by scanning laser microscopy in 'Pick-n-destroy' mode. Single time traces saved in the PicoQuant universal file format (*.ptu*) can be read consecutively. So far only single-channel read-in is supported and tested on .PTU files recorded using HydraHarp Software V3.0.

**Hierarchical Data Format 5 (.hdf5)**

To analyze data files from localization microscopy extracted and generated with `Picasso <https://picassosr.readthedocs.io/en/latest/index.html>`_, we extended *Deep-LASI* also to read in the binary file format Photon-HDF5 (*.hdf5*) as described on `http://photon-hdf5.github.io <http://photon-hdf5.github.io>`_. For every localization event the raw photon stream is loaded while missing localizations default to 0 intensity.

..  _custom-files:
**Custom file formats**

The vast number of different commercial and custom-built microscope setups makes it fairly impossible to host all data and file formats that could be analyzed in *Deep-LASI*. We, therefore, designed a spot in the file type selection for a custom read-in routine. These routines are saved in the *import folder* and must be a MATLAB file (*.m*) with a specific structure which can be found in all other import functions.

-----------------------------------------------

Saved File Formats
~~~~~~~~~~~~~~~~~~~~~~~
For data import and storage, *Deep-LASI* saves and handles three further file types:

..  csv-table:: Data Types
   :header: "Format", "Data Types"
   :widths: 15, 200

   *.mat,   "File containing the extracted or imported traces"
   *.tdat,  "File containing the mapping information and saved data sets"
   *.npz,   "File containing simulated traces"

Files ending with *.mat* contain extracted or already imported traces. Mat-Files are the standard format by *Deep-LASI* using the MATLAB Data format.
How to access and, or read, this data externally is described in more detail in :ref:`data-structure`.

Files ending with *.tdat are generated after mapping different detection channels. They contain information about how camera images between different channels refer to each other, i.e., about potential translational and rotational offsets, as well as differences in magnification. :ref:`mapping` files are generated before trace extraction, usually via a separate movie showing a calibration pattern or multi-labeled particles, and used for matching single-molecule co-localizations between different channels.

Files ending with *.npz refer to simulated single-molecule traces as described in the :doc:`sim` page. They are read in directly for trace analysis.

-----------------------------------------------

..  _data-structure:
Data structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Most data in *Deep-LASI* is stored as global variables in the background to allow easy access. They are saved in the *transportable* structure *T*, which can be extracted at any point of the analysis to the workspace by typing :code:`>> global T` in the command line of MATLAB. The most important variables are:

..  csv-table:: Data format
   :header: "Variable", "Content and format"
   :widths: 15, 200

   T.Channel,        "Container for all the information for each camera"
   T.Channel.Traces, "All intensity and FRET traces sorted according to the excitation cycle"
   T.ALEXsequence,   "Excitation color for each frame"
   T.FrameTime,      "Exposure time including frame transfer"
   T.HMM,            "Container for all parameters and results obtained from Hidden Markov models"
   T.NeuralNetwork,  "Container for all loaded neural networks and prediction results"


.. ..  _profile:
.. User-specific settings
.. ~~~~~~~~~~~~~~~~~
.. *Deep-LASI* uses profiles to allow the users to work efficiently with data from different setups, configurations, assays or simply analysis folders.
.. It stores user-specific settings locally in the same MATLAB folder as *settings.mat* and *user_default_setting.mat*. *settings.mat* contains variables, on the path to the last working folder as well as camera specific settings. *user_default_setting.mat* contains a structure called *userdef* which comprises 34 fields with user specific variables when analyzing datasets

.. ..  csv-table:: Data format
..    :header: "Variable", "Value", "Content and format"
..    :widths: 15, 15, 200

..    userdef.alpha,     "0",     "Global value of the correction factor α"
..    userdef.beta,      "0",     "Global value of the correction factor β"
..    userdef.gamma,     "1",     "Global value of the correction factor γ"
..    userdef.seg,       "1001",  "Global value Number of Frames per movie - Length of trajectories"
..    userdef.frames,    "30",    ""
..    userdef.para_left, "1.5",   ""
..    userdef.para_right,"1.5",   ""
..    userdef.mode,      "1",     ""
..    userdef.orientation, "1",   "Startvalue - take full FOV for data extraction"
..    userdef.mapping_para,"1",   ""
..    userdef.mapping_para,"53",  "Exposure time (50 ms) + Frame transfer time (3 ms)"
..    userdef.gain,      "300",   ""
..    userdef.freq,      "10",    ""
..    userdef.peak_shift_tol,"4", ""
..    userdef.filename,  "C:\...",""
..    userdef.def,       "",      ""
..    userdef.path,      "C:\...",""
..    userdef.analysis,  "",      ""
..    userdef.startframe,"2",     "Value"
..    userdef.sigma,     "0.1",   "Initialisation value for the width σ in HMM"
..    userdef.states,    "3",     "Initialisation value for the number of states in HMM"
..    userdef.stepsize,  "40",    ""
..    userdef.mindwell,  "",      ""
..    userdef.iter,      "10000", "Number of chosen iterations in HMM"
..    userdef.hmm,       "",      ""
..    userdef.hmm_mode,  "2",     "Mode for HMM: 1 - global / 2 - local"
..    userdef.deviation, "0.3",   ""
..    userdef.temp_directory,"",  ""
..    userdef.autosave_interval, "", ""
..    userdef.hmm_refine,"0",     ""
..    userdef.hmm_stretch,"1",    ""
..    userdef.globalhmm, "1",     ""
..    userdef.thresh,    "1.0e-6",""
..    userdef.fix_sigma, "1",     ""
..    userdef.learn_mu,  "1",     ""

-----------------------------------------------

..  _import:
Data Import from OT and TRACY
~~~~~~~~~~~~~~~~~
This function is for internal use within the hosting group only.
*Deep-LASI* allows for importing FRET data obtained from `Multi-Color Orbital Tracking <https://onlinelibrary.wiley.com/doi/10.1002/smll.202204726>`_ measurements using the setup specific data format.

*TRACY* was the former software for the evaluation of 1c and 2c FRET traces. *Deep-LASI* allows for importing the formerly exported and evaluated traces, as well as exporting new data sets into the old format.
