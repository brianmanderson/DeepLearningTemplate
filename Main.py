__author__ = 'Brian M Anderson'
# Created on 9/28/2020
import os


'''
All of the top part will be in PreProcessingTools
'''

"""
First, identify the rois present in the scan
"""
dicom_path = r'H:\Deeplearning_Recurrence_Work\Dicom_Exports'
identify_rois = False
if identify_rois:
    from PreProcessingTools.Identify_Rois import identify_rois_in_path
    reader, rois = identify_rois_in_path(path=dicom_path)
    Contour_Names = ['liver']
    associations = {'liver_bma_program_4': 'liver'}
    reader.set_contour_names_and_associations(Contour_Names=Contour_Names, associations=associations)
    reader.which_indexes_lack_all_rois()  # Check and see if there are indexes that lack the rois

"""
Next, write the images and masks to nifti files
"""
Contour_Names = ['liver']
associations = {'liver_bma_program_4': 'liver'}
"""
Check what indexes don't have all of the rois
"""
write_nifti_files = False
nifti_path = r'H:\Nifti_exports'
description = 'Test'
excel_path = os.path.join('.', 'Patient_Distribution.xlsx')
if write_nifti_files:
    from PreProcessingTools.Dicom_to_Nifti import dicom_to_nifi
    dicom_to_nifi(nifti_path=nifti_path, dicom_path=dicom_path, Contour_Names=Contour_Names, associations=associations,
                  excel_file=os.path.join('.', 'Patient_Distribution.xlsx'), description=description)

'''
Ensure that all contours are within the liver contour, as sometimes they're drawn to extend past it
'''

Contour_names = ['liver']
write_records = False
if write_records:
    from Local_Recurrence_Work.Outcome_Analysis.PreProcessingTools.Nifti_to_tfrecords import nifti_to_records, os
    # nifti_to_records(nifti_path=os.path.join(nifti_export_path, 'Train'))
    nifti_to_records(nifti_path=os.path.join(nifti_export_path, 'Validation'))
    nifti_to_records(nifti_path=os.path.join(nifti_export_path, 'Test'))

print("All finished here, now move on to MainDeepLearning.py!")
