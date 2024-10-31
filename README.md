# Hedgehog Engine Model Export & Convert

The **Hedgehog Engine Model Export & Convert** addon for Blender allows users to export 3D models to FBX format and convert them into Hedgehog Engine model files (.model) using the ModelConverter executable. This addon streamlines the process of preparing models for use in games developed with the Hedgehog Engine, making it easier for modders to integrate custom models into their projects.

## Features

- **FBX Export**: Export selected objects from Blender to FBX format with a scale of 1.00, ensuring that the model's dimensions are preserved correctly.
- **Conversion to Hedgehog Model**: Utilize the ModelConverter executable to convert exported FBX files into the appropriate format for Hedgehog Engine games.
- **Multiple Game Formats**: Easily convert models for various Hedgehog Engine games, including:
  - Sonic Unleashed
  - Sonic Generations
  - Sonic Lost World
  - Sonic Forces
  - Sonic Frontiers
- **User-Friendly Interface**: The addon provides an intuitive panel in Blender’s UI for easy access to export and conversion functionalities.
- **Configurable Executable Path**: Set the path to the ModelConverter executable directly within the addon’s preferences.

## Installation

To install the Hedgehog Engine Model Export & Convert addon, follow these steps:

1. **Download the Addon**:
   - Go to the [repository](https://github.com/Wunaa/hedgehog-model-export) and download the `.py` file directly.

2. **Download ModelConverter**:
   - Download the base ModelConverter from the [ModelConverter releases page](https://github.com/blueskythlikesclouds/ModelConverter/releases/tag/v1.0.2).
   - Extract the downloaded files to a convenient location.

3. **Install the Addon in Blender**:
   - Open Blender.
   - Go to `Edit > Preferences > Add-ons`.
   - Click the `Install...` button at the top right.
   - Select the downloaded `.py` file from your system.

4. **Enable the Addon**:
   - In the Add-ons panel, search for "Hedgehog Engine Model Export & Convert".
   - Check the box to enable the addon.

5. **Configure Preferences**:
   - Still in the Add-ons panel, find the "Hedgehog Engine Model Export & Convert" entry and click the arrow to expand its settings.
   - Specify the path to the `ModelConverter.exe` executable.

## Usage

1. **Prepare Your Model**:
   - Select the object(s) you want to export in Blender's 3D Viewport.

2. **Access the Addon Panel**:
   - Open the right-side toolbar (N-panel) in the 3D Viewport and navigate to the `Export Tools` tab.

3. **Set Export Parameters**:
   - Specify the FBX export folder location where the exported FBX file will be saved.
   - Enter the desired output model name (without the file extension).

4. **Export and Convert**:
   - Click the appropriate button for the game format you wish to convert your model for:
     - **Export & Convert for Unleashed**
     - **Export & Convert for Generations**
     - **Export & Convert for Lost World**
     - **Export & Convert for Forces**
     - **Export & Convert for Frontiers**

## Requirements

- **Blender Version**: This addon is compatible with Blender 2.80 and later.
- **ModelConverter**: Ensure you have the ModelConverter executable that works with Hedgehog Engine.

## Troubleshooting

- **Invalid Paths**: Ensure that the specified FBX folder path exists and is writable. Double-check the path to `ModelConverter.exe`.
- **Error Messages**: If you encounter errors during the conversion process, check the console for detailed error messages. These can provide insight into what went wrong.

---

Thank you for using the Hedgehog Engine Model Export & Convert addon! Happy modeling!
