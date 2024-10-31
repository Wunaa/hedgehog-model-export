bl_info = {
    "name": "Hedgehog Engine Model Export & Convert",
    "blender": (3, 6, 0),
    "category": "Export",
}

import bpy
import subprocess
import os

# Define properties for the ModelConverter executable path
class HedgehogModelConverterPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    model_converter_path: bpy.props.StringProperty(
        name="ModelConverter.exe Location",
        description="Specify the path to ModelConverter.exe",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "model_converter_path")

# Define properties for the folder location and output file name
bpy.types.Scene.model_export_folder = bpy.props.StringProperty(
    name="FBX Folder Location",
    description="Specify the folder to export FBX files",
    subtype='DIR_PATH'
)

bpy.types.Scene.output_model_name = bpy.props.StringProperty(
    name="Output Model Name",
    description="Specify the desired output file name for the .model file (without extension)"
)

# Define the operator to export the model to FBX and run ModelConverter
class ExportAndConvertOperator(bpy.types.Operator):
    bl_idname = "export_convert.hedgehog_model"
    bl_label = "Export and Convert to Hedgehog Model"
    
    format_option: bpy.props.StringProperty()

    def execute(self, context):
        folder_path = context.scene.model_export_folder
        converter_path = context.preferences.addons[__name__].preferences.model_converter_path
        output_name = context.scene.output_model_name

        # Verify paths and output name
        if not os.path.isdir(folder_path):
            self.report({'ERROR'}, "Invalid FBX folder path")
            return {'CANCELLED'}
        if not os.path.isfile(converter_path):
            self.report({'ERROR'}, "Invalid ModelConverter.exe path")
            return {'CANCELLED'}
        if not output_name:
            self.report({'ERROR'}, "Please specify an output file name")
            return {'CANCELLED'}
        
        # Export the active object to FBX with specified settings
        fbx_path = os.path.join(folder_path, "exported_model.fbx")
        bpy.ops.export_scene.fbx(
            filepath=fbx_path, 
            use_selection=True, 
            global_scale=1.00,  # Set scale to 1.00
            apply_unit_scale=True,  # Apply unit scale
            add_leaf_bones=False, 
            bake_anim=False,
            use_fbx_units=True  # Enable FBX units scale
        )
        
        # Define the destination path for the .model file
        model_path = os.path.join(folder_path, f"{output_name}.model")

        # Run the ModelConverter
        command = [converter_path, self.format_option, fbx_path, model_path]
        
        try:
            # Execute the command and capture any output or errors
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            if result.returncode != 0:
                self.report({'ERROR'}, f"ModelConverter failed: {result.stderr}")
                return {'CANCELLED'}
            else:
                self.report({'INFO'}, "Export and conversion completed successfully")
        
        except Exception as e:
            self.report({'ERROR'}, f"Failed to run ModelConverter: {e}")
            return {'CANCELLED'}
        
        return {'FINISHED'}

# Define the panel with folder input, executable path, output name, and export-convert buttons
class ModelExportConvertPanel(bpy.types.Panel):
    bl_label = "Hedgehog Engine Model Export & Convert"
    bl_idname = "VIEW3D_PT_model_export_convert_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Export Tools'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Folder and output name input fields
        layout.prop(scene, "model_export_folder")
        layout.prop(scene, "output_model_name")

        # Export and Convert buttons for each game format
        row = layout.row()
        row.operator("export_convert.hedgehog_model", text="Export & Convert for Unleashed").format_option = "--unleashed"
        row = layout.row()
        row.operator("export_convert.hedgehog_model", text="Export & Convert for Generations").format_option = "--gens"
        row = layout.row()
        row.operator("export_convert.hedgehog_model", text="Export & Convert for Lost World").format_option = "--lw"
        row = layout.row()
        row.operator("export_convert.hedgehog_model", text="Export & Convert for Forces").format_option = "--forces"
        row = layout.row()
        row.operator("export_convert.hedgehog_model", text="Export & Convert for Frontiers").format_option = "--frontiers"

# Register classes
def register():
    bpy.utils.register_class(HedgehogModelConverterPreferences)
    bpy.utils.register_class(ExportAndConvertOperator)
    bpy.utils.register_class(ModelExportConvertPanel)

def unregister():
    bpy.utils.unregister_class(HedgehogModelConverterPreferences)
    bpy.utils.unregister_class(ExportAndConvertOperator)
    bpy.utils.unregister_class(ModelExportConvertPanel)

if __name__ == "__main__":
    register()
