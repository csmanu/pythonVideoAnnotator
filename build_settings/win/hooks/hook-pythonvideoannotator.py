from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# pyforms import app settings.py dinamically so we need to inform pyinstaller

hiddenimports = [
	'pythonvideoannotator.settings',
	'pythonvideoannotator_models_gui.settings',
	'pythonvideoannotator.resources',
] \
+ collect_submodules('pythonvideoannotator_module_contoursimages') \
+ collect_submodules('pythonvideoannotator_module_tracking') \
+ collect_submodules('pythonvideoannotator_module_timeline') \
+ collect_submodules('pythonvideoannotator_module_patheditor') \
+ collect_submodules('pythonvideoannotator_module_backgroundfinder') \
+ collect_submodules('pythonvideoannotator_module_virtualobjectgenerator') \
+ collect_submodules('mcv_api') \
+ collect_submodules('mcv_gui') \
+ collect_submodules('geometry_designer') \


datas = [ ('pythonvideoannotator\\resources', 'pythonvideoannotator\\resources'),]