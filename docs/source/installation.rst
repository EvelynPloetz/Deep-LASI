.. |br| raw:: html

   <br />
############
Installation
############

.. _installation:

DeepLASI is a MATLAB program that uses deep learning for automated data analysis from Python libraries.
In order to use the automated data analysis with the pretrained deep neural networks make sure you installed the required software packages below.
We recommend running DeepLASI with a MATLAB license and only use the compiled version if no license is available.
The source code is more frequently updated than the standalone version and certain features like generating new training data sets and training new models are not supported in the standalone version.
Download or clone the source code from the `Repository <https://gitlab.com/simon71/deeplasi>`_. In MATLAB, change your current folder to the installation directory and start DeepLASI via right-click on DeepLASI.m and Run or by typing `DeepLASI` into the MATLAB command window.

********************
System compatibility
********************

DeepLASI is compatible with Windows and Mac OS. It has been extensively tested for Mac OS systems. For ARM Macs using the M1 or M2 chips, please install MATLAB 2023b, which is the only version natively available for ARM Macs.
DeepLASI has not been installed on a Linux systems so far. If you encounter any problem, please
get in touch with us via the *Issue forum*.

*******************
MATLAB installation
*******************

If you have access to a MATLAB license, please download and install MATLAB at https://de.mathworks.com/products/matlab.html.
For ARM Macs (M1/M2), we strongly recommend installing MATLAB 2023b, which is natively available for ARM Macs.
For downloading MATLAB directly from MathWorks, you require an account. After signing in, link the account with your licence number (Step 1). In the next step you can download the MATLAB version associated with your licence (Step 2). Save the licence on your PC/Mac and download MATLAB. The licence file will be required during the local installation process.

.. figure:: ./../figures/installation/matlab_download.png
   :width: 500
   :alt: Matlab Download
   :align: center
   :name: matlab_download

   Selection steps for downloading MATLAB from MathWorks.

.. note::

   DeepLASI is tested for MATLAB version between R2019a and R2023b. Please make sure you install a compatible version of Python that can be handeled by MATLAB (`View compatiblity https://de.mathworks.com/support/requirements/python-compatibility.html`_), otherwise DeepLASI will only provide basic functionalities and will not be able call Python-based libraries for Automated data analysis.

If you plan to use the compiled standalone version of DeepLASI, please download and install MATLAB Runtime R2022b for your system at https://de.mathworks.com/products/compiler/matlab-runtime.html

The earliest MATLAB version required is R2019a.

The latest MATLAB version DeepLASI is tested on is R2023b.

*********************
DeepLASI installation
*********************

The open source version of DeepLASI requires a valid licence for MATLAB (2019a or newer). Some features of thae program require further access to tool boxes (Curve fitting, image processing, optimization, statistics, machine learning, and parallel computing) to work.

You can obtain and update DeepLASI either by download from *GitLab*, using the command line through *Git*, or by using the MATLAB *Git* integration.

**Download and update DeepLASI from the repository**

#. Download the open source version of DeepLASI from the `Repository <https://gitlab.com/simon71/deeplasi>`_.
#. Save the files in the MATLAB folder.
#. Start MATLAB and navigate to the DeepLASI folder.
#. Type :code:`DeepLASI` into the MATLAB command line to start the program.
#. Download the newest version and overwrite your former files for updating.


**Download and update DeepLASI using Git**

#. Install *Git* on your computer.
    * MacOS has *Git* pre-installed. Try to tun *git* from the terminal. If the command fails, you can download *Git* from https://git-scm.com/ .
    * For Windows, download and install *Git* from https://git-for-windows.github.io/ .
#. Clone the repository of *DeepLASI* to create a local copy in the folder *DeepLASI*.
    * For cloning a first copy, type in your terminal: |br| :code:`git clone https://gitlab.com/simon71/deeplasi.git DeepLASI`.
    * For updating, simply type :code:`!git pull` to obtain the latest version and changes.

**Download and update DeepLASI using the MATLAB Git Integration**

#. Create a folder for DeepLASI.
#. Start MATLAB and navigate to the DeepLASI folder.
#. Right click the 'Current Folder' panel in MATLAB and select 'Source Control' and 'Manage Files...'.
#. Set the 'Source control integration' to 'Git' and enter for the 'Repository path'
   https://gitlab.com/simon71/deeplasi .
#. Click 'Retrieve' to download the files automatically.
#. For updating *DeepLASI* from the Repository, simply type :code:`!git pull` into the MATLAB command line while your inside the target-folder :code:`DeepLASI`.

For the deep learning features, please follow the detailed instructions below.

Deep learning features for Mac
==============================

.. image:: ./../figures/logos/mac.png
   :width: 50
   :alt: Mac OS Logo

To run DeepLASI on Mac OS, installing Mambaforge (Conda) is highly recommended, as it allows a straightforward installation of python packages and creation of a separate environment for DeepLASI. The following software packages are required:

#. Python 3.7-3.10 (https://www.python.org/downloads/)
   * `Direct Download Python 3.10 <https://www.python.org/ftp/python/3.10.0/python-3.10.0post2-macos11.pkg>`_
   * `Direct Download Python 3.9 <https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg>`_
   * `Direct Download Python 3.8 <https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg>`_
   * `Direct Download Python 3.7 <https://www.python.org/ftp/python/3.7.0/python-3.7.0-macosx10.9.pkg>`_
#. Xcode (https://apps.apple.com/us/app/xcode/id497799835?mt=12)
#. TensorFlow 2.8.0 (Python package, https://www.tensorflow.org)

If you do not have Conda installed, open your terminal app and enter the following:

   .. code-block:: python
   
      curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
      bash Mambaforge-$(uname)-$(uname -m).sh

or download and install mambaforge directly from github: https://github.com/conda-forge/miniforge
If you downloaded the installer, you should run the following commands for the next steps to work:

.. code-block:: python
      source "${HOME}/conda/etc/profile.d/conda.sh"
      source "${HOME}/conda/etc/profile.d/mamba.sh"

In case you have issues with the installation, please visit https://github.com/conda-forge/miniforge for alternatives and detailed documentation.

Python installation on Mac
--------------------------

Check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version.
It is strongly recommended to create a new Python environment using Mambaforge (Conda).
Create a new environment with a specific python version and activate it. Type in your terminal:

.. code-block:: python
   
      conda create -n 'your_environment_name' python==3.10
      conda activate your_environment_name

If you do not want to install Conda, please download and install Python version 3.7-3.10 manually via the python website (listed above) and proceed to TensorFlow installation using 'pip' instead of 'conda'.

Workaround for ARM Macs (M1/M2) and MATLAB Versions below 2023b
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since all MATLAB versions below version 2023b are not natively available for ARM Macs, MATLAB and all dependencies have to be installed and executed via the rosetta environment. While this is done automatically for MATLAB, it must be done manually for Python.
First, install mambaforge (see above for details) and create a new environment (here: rosetta) by typing the following commands with the MATLAB compatible Python version (here: 3.10):

   .. code-block:: python
   
      CONDA_SUBDIR=osx-64 conda create -n rosetta python=3.10
      conda activate rosetta
      conda config --env --set subdir osx-64
      
If you close your terminal during the installation process or want to install additional packages, reactivate your environment first:

   .. code-block:: python

      conda activate rosetta

TensorFlow installation
-----------------------

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
Install TensorFlow by opening the Terminal app, activate your environment created by conda and install tensorflow in that environment:

   .. code-block:: python

      conda activate your_environment_name
      conda install tensorflow==2.8.0

Start MATLAB and link MATLAB to the python version in you conda environment. Find the correct python path by typing in your activated conda environment:

   .. code-block:: python

      which python

The path should look something like '/Users/your_name/mambaforge/envs/your_environment/bin/python'
Copy the path, open MATLAB and type in your MATLAB command window:

   .. code-block:: python

      pyversion '/Users/your_name/mambaforge/envs/your_environment/bin/python'

You can check the successfully installation and integration into MATLAB by entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use DeepLASI and its neural networks.

Packages for simulations and training
-------------------------------------

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib==3.5.2
      pip install numpy==1.23.1
      pip install scikit-learn==1.1.1
      pip install tqdm==4.64.0
      pip install mlxtend==0.20.0
      pip install pomegranate==0.14.8

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.

Checking for correct integration into MATLAB
--------------------------------------------

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


Deep learning features on Windows
=================================

.. image:: ./../figures/logos/windows.png
   :width: 50
   :alt: Windows Logo

To run DeepLASI on your local windows computer please follow the 
installation process in the following order:
To run DeepLASI on Windows, the following software packages are required:

#. Python 3.7-3.10 (https://www.python.org/downloads/)
   * `Direct Download Python 3.10 <https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe>`_
   * `Direct Download Python 3.9 <https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe>`_
   * `Direct Download Python 3.8 <https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe>`_
   * `Direct Download Python 3.7 <https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe>`_
#. Microsoft Visual C++ (https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
#. TensorFlow 2.8.0 (Python package, https://www.tensorflow.org)


Python installation and integration into MATLAB (Windows)
---------------------------------------------------------

Please check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version and install Python with version 3.7-3.10.

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


TensorFlow Installation
-----------------------

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the windows command prompt by pressing Win + R to open the Run box, then type "cmd" and hit Enter to open it or pressing Win + X (or right-click the Start button) and choose Command Prompt from the menu.
Next, enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successful installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use DeepLASI and its neural networks.

Packages for simulations and training
-------------------------------------

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib==3.5.2
      pip install numpy==1.23.1
      pip install scikit-learn==1.1.1
      pip install tqdm==4.64.0
      pip install mlxtend==0.20.0
      pip install pomegranate==0.14.8

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.


Common installation issues
--------------------------

If you run into errors while importing tensorflow, your protobuf package may need to be downgraded and/or your h5py package is incompatible.

Installing a compatible version of protobuf
""""""""""

Please open your windows command prompt by pressing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install protobuf==3.20.*

After successfull installation, restart your MATLAB session.

Installing the latest version of h5py
""""""""""

Please open your windows command prompt by pressing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install h5py --force-reinstall

After successfull installation, restart your MATLAB session.

Common issue with installing python packages on Windows
""""""""""

You may run into errors regarding access rights when installing packages with pip. If your access is denied please make the installation of the Python package a user install by adding the --user option:

   .. code-block:: python
   
      pip install name_of_python_package --user


Hidden Markov Model features
=============================================

DeepLASI comes with in-built HMM capabilities originally written by Kevin Murphy. You also have the option to use the python package *pomegranate*. So far, three-color FRET HMM is only available using the *pomegranate* package.
For both Windows and Mac systems, install *pomegranate* in your environment by typing the following into the Command Prompt/Terminal:

   .. code-block:: python
   
      pip install pomegranate==0.14.8
