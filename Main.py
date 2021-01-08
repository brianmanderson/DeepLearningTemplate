__author__ = 'Brian M Anderson'
# Created on 9/28/2020

'''
All of the top part will be in PreProcessingTools
'''

'''
Load the DICOM and masks, register based on the exported registration matrix, export as nifti
'''
write_nifti = False
nifti_export_path = 5#r'H:\Deeplearning_Recurrence_Work\Nifti_Exports'
dicom_path = 5 # path to dicom images
if write_nifti:
    from PreProcessingTools.Dicom_to_Nifti import dicom_to_nifi
    dicom_to_nifi(nifti_path=nifti_export_path, dicom_path=dicom_path)

Contour_names = ['Retro_GTV', 'Retro_GTV_Recurred', 'Liver']
write_records = False
if write_records:
    from PreProcessingTools.Nifti_to_tfrecords import nifti_to_records
    nifti_to_records(nifti_path=nifti_export_path)


print("All finished here, now move on to MainDeepLearning.py!")
