.. |br| raw:: html

   <br />

Installation
=====

.. _installation:

DeepLASI is a MATLAB program that uses deep learning for automated data analysis from Python libraries.
In order to use the automated data analysis with the pretrained deep neural networks make sure you installed the required software packages below.
We recommend running DeepLASI with a MATLAB license and only use the compiled version if no license is available.
The source code is more frequently updated than the standalone version and certain features like generating new training data sets and training new models are not supported in the standalone version.

System compatibility
------------

DeepLasi is compatible with Windows and Mac OS. It has been extensively tested for Mac OS x86 systems. For new Macs using the M1 or M2 CPUs, please follow the instructions in the 'Installation on ARM Macs (M1/M2)'.
DeepLASI has not been installed on a Linux systems so far. If you encounter any problem, please
get in touch with us via the *Issue forum*.

MATLAB Installation
--------

If you have access to a MATLAB license, please download and install MATLAB at https://de.mathworks.com/products/matlab.html.

For downloading MATLAB directly from MathWorks, you require an account. After signing in, link the account with your licence number (Step 1). In the next step you can download the MATLAB version associated with your licence (Step 2). Save the licence on your PC/Mac and download MATLAB. Deep-LASI is tested for MATLAB version between R2019a and R2022b. The licence file will be required during the local installation process.

.. note::

   Please make sure you install a compatible version of Python 3.7-3.10 that can be handeled by MATLAB, otherwise Deep-LASI will only provide basic functionalities and will not be able call Python-based libraries for Automated data analysis.

.. image:: ./../figures/installation/matlab_download.png
   :width: 300
   :alt: Matlab Download

If you plan to use the compiled standalone version of Deep-LASI, please download and install MATLAB Runtime R2022b for your system at https://de.mathworks.com/products/compiler/matlab-runtime.html

The earliest MATLAB version required is R2019a.

The latest MATLAB version DeepLASI is tested on is R2022b.

Installation on Mac
------------

Requirements for Mac
^^^^^^^^^^^^^^^^^^^^

.. image:: ./../figures/logos/mac.png
   :width: 50
   :alt: Mac OS Logo

To run Deep-LASI on Mac OS, the following software packages are required:

* Python 3.7-3.10 (https://www.python.org/downloads/)
* Xcode (https://apps.apple.com/us/app/xcode/id497799835?mt=12)
* TensorFlow 2.8.0 (Python package)


Python installation on Intel Macs
^^^^^^^^^^^^^^^^^^^^

Please install Python version 3.7-3.10 at https://www.python.org/downloads/ and check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version. If you have Conda installed, you can also create a new python environment with the specified Python version.

Python installation on ARM Macs (M1/M2)
^^^^^^^^^^^^^^^^^^^^

Since a native MATLAB version for ARM Macs is still in development, MATLAB and all dependencies have to be installed and executed via the rosetta environment. While this is done automatically for all MATLAB versions, it must be done manually for Python. First, download and install Conda by typing the following commands in your Terminal app:

   .. code-block:: python
   
      curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
      bash Mambaforge-$(uname)-$(uname -m).sh
      
or download and install from the Miniconda website: https://docs.conda.io/en/latest/miniconda.html

Next, create a new environment (here: rosetta) by typing the following commands with the MATLAB compatible Python version (here: 3.9):

   .. code-block:: python
   
      CONDA_SUBDIR=osx-64 conda create -n rosetta python=3.9
      conda activate rosetta
      conda config --env --set subdir osx-64
      
Finally, install all needed Python packages using the conda command instead of pip, e.g.:

   .. code-block:: python
   
      conda install tensorflow==2.8.0
      
If you close your terminal during the installation process or want to install additional packages, reactivate your environment first:

   .. code-block:: python

      conda activate rosetta

TensorFlow
^^^^^^^^^^^^^^^^^^^^

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the Terminal app (Path: /System/Applications/Utilities/Terminal.app) and enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successfully installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.

Packages for simulations and training new neural network models
^^^^^^^^^^^^^^^^^^^^

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib==3.5.2
      pip install numpy==1.23.1
      pip install sklearn==1.1.1
      pip install tqdm==4.64.0
      pip install mlxtend==0.20.0

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.


Checking for correct integration into MATLAB
^^^^^^^^^^^^^^^^^^^^

After installation you can check the MATLAB integration by entering the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
Example output for Python 3.9:

   .. code-block:: python
   
      version: '3.9'
      executable: 'path/to/python/executable/python3'
      library: 'path/to/python/library/3.9/lib/libpython3.9.dylib'
      home: 'path/to/python/environment'
      isloaded: 0
   
If no version or path information is shown or an incompatible Python version is loaded (e.g. due to multiple Python versions installed on your computer), link Python directly by entering the path to your Python executable in your MATLAB Command Window:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'


Installation on Windows
------------

Requirements for Windows
^^^^^^^^^^^^^^^^^^^^

.. image:: ./../figures/logos/windows.png
   :width: 50
   :alt: Windows Logo

To run Deep-LASI on your local windows computer please follow the 
installation process in the following order:
To run Deep-LASI on Windows, the following software packages are required:

* Python 3.7-3.10 (https://www.python.org/downloads/)
* Microsoft Visual C++ (https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
* TensorFlow 2.8.0 (Python package)


Python installation and integration into MATLAB (Windows)
^^^^^^^^^^^^^^^^^^^^

Please install Python with version 3.7-3.10 at https://www.python.org/downloads/ and check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version.

   .. note::
   
      When installing Python, check the box "Add Python 3.X to Path", choose "Customize installation", 
      click next and check the box "Install for all Users". This will change the installation path to "C:\ProgramFiles\PythonXX",
      which is necessary for MATLAB to automatically find the Python executable.
   
After installation you can check the MATLAB integration by entering the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
If no version or path information is shown or you did not install Python for all users, link Python directly by providing the path to your Python executable:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'

Installation of deep learning features on Windows
^^^^^^^^^^

TensorFlow
""""""""""

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the windows command prompt by pressing Win + R to open the Run box, then type "cmd" and hit Enter to open it or pressing Win + X (or right-click the Start button) and choose Command Prompt from the menu.
Next, enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successful installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.

Packages for simulations and training new neural network models
""""""""""

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib==3.5.2
      pip install numpy==1.23.1
      pip install sklearn==1.1.1
      pip install tqdm==4.64.0
      pip install mlxtend==0.20.0

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.


Common issues with deep learning features on Windows
^^^^^^^^^^

If you run into errors while trying to use neural networks, your protobuf package might need to be downgraded and/or your h5py package is incompatible.

Installing a compatible version of protobuf
""""""""""

Please open your windows command prompt by pressing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install protobuf==3.20.*
      
Installing the latest version of h5py
""""""""""

Please open your windows command prompt by pressing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install h5py --force-reinstall


Common issues with installing python packages on Windows
""""""""""

You may run into errors regarding access rights when installing packages with pip. If your access is denied please make the installation of the Python package a user install by adding the --user option:

   .. code-block:: python
   
      pip install name_of_python_package --user


Pomegranate installation for hidden Markov models
--------

For both Windows and Mac systems, install the pomegranate package by typing the following into the Command Prompt/Terminal:

   .. code-block:: python
   
      pip install pomegranate==0.14.8

Installing Deep-LASI
------------
The program can be downloaded from the `Repository <https://gitlab.com/simon71/deeplasi>`_ on *Gitlab*.

This *GitLab* repository contains:

* *source*: the open-source version of *Deep-LASI*
* *standalone versions*: the compiled versions for Windows and Mac
* *demos*: Some example data that users can use to try out *Deep-LASI*'s functionalities.

Installing the stand-alone version of *Deep-LASI*
~~~~~~~~~~~~~~~

#. Install the MATLAB Runtime as described above.
#. Download the compiled version of *Deep-LASI* for your Operating System (MacOS or Windows) from the `Repository <https://gitlab.com/simon71/deeplasicompiled>`_
#. Unpack the files.
#. Run the *.exe*-file (Windows) or *.app*-file (MacOS) to start the program

Installing and updating the open-source version of *Deep-LASI*
~~~~~~~~~~~~~~~

The open source version of *Deep-LASI* requires a valid licence for MATLAB (2019a or newer). Some features of the program require further access to tool boxes (Curve fitting, image processing, optimization, statistics, machine learning, and parallel computing) to work.

You can obtain and update *Deep-LASI* either by download from *Gitlab*, using the command line through *Git*, or by using the MATLAB *Git* integration.

**Download and update *Deep-LASI* from the repository**

#. Download the open source version of *Deep-LASI* from the `Repository <https://gitlab.com/simon71/deeplasi>`_
#. Save the files in the MATLAB folder
#. Start MATLAB and navigate to the *Deep-LASI* folder
#. Type :code:`DeepLASI` into the MATLAB command line to start the program.
#. Download the newest version and overwrite your former files for updating.


**Download and update *Deep-LASI* using *Git* **

#. Install *Git* on your computer.
    * MacOS has *Git* pre-installed. Try to tun *git* from the terminal. If the command fails, you can download *Git* from https://git-scm.com/ .
    * For Windows, download and install *Git* from https://git-for-windows.github.io/ .
#. Clone the repository of *Deep-LASI* to create a local copy in the folder *DeepLASI*
    * For cloning a first copy, type in your terminal: |br| :code:`git clone https://gitlab.com/simon71/deeplasi.git DeepLASI`
    * For updating, simply type :code:`!git pull` to obtain the latest version and changes.

**Download and update *Deep-LASI* using the *MATLAB Git Integration* **

#. Create a folder for *Deep-LASI*
#. Start MATLAB and navigate to the *Deep-LASI* folder
#. Right click the 'Current Folder' panel in MATLAB and select 'Source Control' and 'Manage Files...'.
#. Set the 'Source control integration' to 'Git' and enter for the 'Repository path'
   https://gitlab.com/simon71/deeplasi
#. Click 'Retrieve' to download the files automatically.
#. For updating *Deep-LASI* from the Repository, simply type :code:`!git pull` into the MATLAB command line.
