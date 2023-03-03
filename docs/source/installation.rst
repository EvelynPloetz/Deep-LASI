Installation
=====

.. _installation:

DeepLASI is a MATLAB program that uses deep learning for automated data analysis from Python libraries.
In order to use the automated data analysis with the pretrained deep neural networks make sure you installed the required software packages below.
We recommend running DeepLASI with a MATLAB license and only use the compiled version if no license is available.
The source code is more frequently updated than the standalone version and certain features like generating new training data sets and training new models are not supported in the standalone version.

System compatibility
------------

DeepLasi is compatible with Windows and Mac OS. It has been extensively tested for Mac OS x86 systems. For new Macs using the M1 or M2 CPUs, the deep learning features are not available until MathWorks releases a native MATLAB version. DeepLASI can still be used using Parallels on M1/M2 Macs.
DeepLASI has not been installed on a Linux systems so far. If you encounter any problem, please
get in touch with us via the *Issue forum*.

MATLAB Installation
--------

If you have access to a MATLAB license, please download and install MATLAB at https://de.mathworks.com/products/matlab.html.

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


Python installation and integration into MATLAB (Mac OS)
^^^^^^^^^^^^^^^^^^^^
Please install Python with version 3.7-3.10 at https://www.python.org/downloads/ and check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version.
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
   
If no version or path information is shown or an incompatible Python version is loaded (e.g. due to multiple Python versions installed on your computer), link Python directy by entering the path to your Python executable in your MATLAB Command Window:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'

Installing deep learning features on Mac OS
^^^^^^^^^^^^^^^^^^^^

**TensorFlow**

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the Terminal app (Path: /System/Applications/Utilities/Terminal.app) and enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successfull installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.

**Packages for simulations and training new neural network models**

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib
      pip install numpy
      pip install sklearn
      pip install tqdm
      pip install mlxtend

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.

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
      klick next and check the box "Install for all Users". This will change the installation path to "C:\ProgramFiles\PythonXX", 
      which is neccessary for MATLAB to automatically find the Python executable.
   
After installation you can check the MATLAB integration by entering the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
If no version or path information is shown or you did not install Python for all users, link Python directy by providing the path to your Python executable:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'

Installing deep learning features on Windows
^^^^^^^^^^

TensorFlow
""""""""""

For deep learning features, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the windows command prompt by presssing Win + R to open the Run box, then type "cmd" and hit Enter to open it or pressing Win + X (or right-click the Start button) and choose Command Prompt from the menu. 
Next, enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successfull installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.

Packages for simulations and training new neural network models
""""""""""

If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib
      pip install numpy
      pip install sklearn
      pip install tqdm
      pip install mlxtend

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.


Common issues with deep learning features on Windows
^^^^^^^^^^

If you run into errors while trying to use neural netorks, your protobuf package might need to be downgraded and/or your h5py package is incompatible. 

Installing a compatible version of protobuf
""""""""""

Please open your windows command prompt by presssing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install protobuf==3.20.*
      
Installing the latest version of h5py
""""""""""

Please open your windows command prompt by presssing Win + R or terminal app on Mac and enter:

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
   
      pip install pomegranate
