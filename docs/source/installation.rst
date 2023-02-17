Installation
=====

.. _installation:

Deep-LASI is a MATLAB program that uses deep learning for automated data analysis from Python libraries.
In order to use the automated data analysis with the pretrained deep neural networks make sure you installed the required software packages below.

System compatibility
------------

Deep-Lasi is compatible with Windows and Mac OS. It has been extensively tested for Mac OS x86 systems. For new Macs using the M1 or M2 CPUs, the deep learning features are not available until MathWorks releases a native MATLAB version. Deep-LASI can still be used using Parallels on M1/M2 Macs.
Deep-LASI has not been installed on a Linux systems so far. If you encounter any problem, please
get in touch with us via the *Issue forum*.

MATLAB Installation
--------

If you have access to a MATLAB license, please install MATLAB, which can be found at https://de.mathworks.com/products/matlab.html.

If you plan to use the compiled version of Deep-LASI, please install MATLAB Runtime R2022b for your system, which can be found athttps://de.mathworks.com/products/compiler/matlab-runtime.html

The latest MATLAB version Deep-LASI is tested on is R2022b.

Installation on Mac
------------

Requirements for Mac
~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../figures/logos/mac.png
   :width: 50
   :alt: Mac OS Logo

To run Deep-LASI on Mac OS, the following software packages are required:

* Python 3.7-3.10 (https://www.python.org/downloads/)
* Xcode (https://apps.apple.com/us/app/xcode/id497799835?mt=12)
* TensorFlow 2.8.0 (Python package)


Python installation and integration into MATLAB (Mac OS)
~~~~~~~~~~~~~~~~~~~~~~
Please install Python with version 3.7-3.10 at https://www.python.org/downloads/ and check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version.
After installation you can check the MATLAB integration by entering the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
If no version or path information is shown, link Python directy by providing the path to your Python executable:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'

Installing Python packages on Mac OS
~~~~~~~~~~~~~~~~~~~~~~
Next, the TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the Terminal app (Path: /System/Applications/Utilities/Terminal.app) and enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successfull installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.
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
~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~

Please install Python with version 3.7-3.10 at https://www.python.org/downloads/ and check https://de.mathworks.com/support/requirements/python-compatibility.html for the compatibility with your MATLAB version.
**Important: When installing Python, check the box "Add Python 3.X to Path", choose "Customize installation", klick next and check the box "Install for all Users". This will change the installation path to "C:\ProgramFiles\PythonXX", which is neccessary for MATLAB to automatically find the Python executable.**
After installation you can check the MATLAB integration by entering the following command into the MATLAB Command Window:

   .. code-block:: python
      
      pyversion
      
If no version or path information is shown, link Python directy by providing the path to your Python executable:

   .. code-block:: python
   
      pyversion 'your/path/to/python/python.exe'

Installing Python packages on Windows
~~~~~~~~~
The TensorFlow package needs to be installed for the Python environment integrated into MATLAB.
The easiest way to install TensorFlow is to open the windows command prompt by presssing Win + R to open the Run box, then type "cmd" and hit Enter to open it or pressing Win + X (or right-click the Start button) and choose Command Prompt from the menu. 
Next, enter the following command:

   .. code-block:: python
   
      pip install tensorflow==2.8.0

You can check the successfull installation and integration into MATLAB by restarting MATLAB and entering the following command into the MATLAB Command Window, which returns TensorFlow as a Python module:

   .. code-block:: python
   
      py.importlib.import_module("tensorflow")

You are now ready to use Deep-LASI.
If you are interested in generating simulated data and/or re-training the neural network models, additional Python packages are required and installed by entering the following commands into the terminal application:

   .. code-block:: python
   
      pip install matplotlib
      pip install numpy
      pip install sklearn
      pip install tqdm
      pip install mlxtend

If you encounter any problem during the installation procedure, please
get in touch with us via the *Issue forum*.


Common issues with deep learning features
--------

If you run into errors while loading the neural netork models your protobuf package might need to be downgraded. Please open your windows command prompt by presssing Win + R or terminal app on Mac and enter:

   .. code-block:: python
   
      pip install protobuf==3.20.*
      
      
