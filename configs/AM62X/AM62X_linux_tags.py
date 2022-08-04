# Device Family name
fam_name = 'AM62X'

# Project name and HTML title
sdk_product = 'null' #todo: remove after the new structure is used for all device families

project = u'Processor SDK Linux for AM62x'
html_title = 'Processor SDK AM62x Documentation'

# The master toctree document.
master_doc = 'devices/AM62X/index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

# AM62x RTOS docs are not in this project, rather referenced externally,
# so exclude 'rtos' folder along with others.
exclude_patterns = ['android', 'example_code', 'files', 'rtos', 'devices/AM335X', 'devices/AM437X', 'devices/AM64X', 'devices/AM65X', 'devices/J7', 'devices/J7200', 'devices/J721S2', 'devices/J784S4', 'devices/DRA821A']

# OS for the build. Sphinx uses source/{sdk_os} when looking for doc inputs
sdk_os = 'linux'


