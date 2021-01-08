__author__ = 'Brian M Anderson'
# Created on 1/8/2021
from Base_Deeplearning_Code.Dicom_RT_and_Images_to_Mask.src.DicomRTTool import DicomReaderWriter


def dicom_to_nifi(nifti_path, dicom_path):
    reader = DicomReaderWriter()
    reader.walk_through_folders(dicom_path)
    xxx = 1
    return None


if __name__ == '__main__':
    pass
